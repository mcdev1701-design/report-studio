/**
 * Report Studio
 *
 * Główny plik JavaScript aplikacji.
 *
 * ETAP_01D
 * Frontend Bootstrap
 */

/**
 * Aktualnie zaznaczony obiekt.
 */
let selectedObjectId = null;

/**
 * Obiekty znajdujące się na canvasie.
 */
const canvasObjects = [];

console.log("Report Studio Frontend");

/**
 * Uruchamiane po pełnym załadowaniu dokumentu HTML.
 */
document.addEventListener(
    "DOMContentLoaded",
    () => {
// Pobranie informacji o aplikacji z backendu.
        loadApplicationInfo();
// Inicjalizacja panelu narzędzi.
        initializeToolbox();
// Inicjalizacja skrótów klawiaturowych.
        initializeKeyboardShortcuts();

    }
);
/**
 * Pobiera informacje o aplikacji z backendu.
 */
async function loadApplicationInfo() {

    try {

            console.log("Pobieranie informacji o aplikacji...");

            const response = await fetch(
                "/api/v1/info"
            );

            const data = await response.json();

            console.log(data);

            const backendInfoElement = 
                document.getElementById("backend-info");

            backendInfoElement.innerHTML = `
                <strong>Application:</strong> ${data.application}<br>
                <strong>Version:</strong> ${data.version}<br>
                <strong>Status:</strong> ${data.status}
            `;
    }
    catch (error) {
        console.error(error);
    }


}

/**
 * Obsługa wyboru narzędzia.
 */
function initializeToolbox() {

    const toolButtons =
        document.querySelectorAll(".tool-button");

    toolButtons.forEach(button => {

        button.addEventListener("click", () => {

            const selectedTool =
                button.dataset.tool;

            updatePropertyPanel(
                selectedTool
            );

            addCanvasObject(
                selectedTool
            );

        });

    });

}

/**
 * Aktualizacja PropertyPanel.
 */
function updatePropertyPanel(
    selectedTool
) {

    const propertyPanel =
        document.getElementById(
            "property-placeholder"
        );

    propertyPanel.innerHTML = `
        <strong>Selected Tool</strong>
        <br><br>
        ${selectedTool}
    `;
}

/**
 * Aktualizacja CanvasPanel.
 */
function updateCanvasPanel(
    selectedTool
) {

    const canvasPanel =
        document.getElementById(
            "canvas-placeholder"
        );

    canvasPanel.innerHTML = `
        <strong>Selected Tool</strong>
        <br><br>
        ${selectedTool}
    `;
}

/**
 * Dodanie obiektu do canvasa.
 */
function addCanvasObject(selectedTool) {

        canvasObjects.push({
        id: Date.now(),
        type: selectedTool
    });


    renderCanvas();

}

/**
 * Renderowanie obiektów canvas.
 */
function renderCanvas() {

    const canvasElement =
        document.getElementById(
            "canvas-placeholder"
        );

    let html = "";

    canvasObjects.forEach(object => {

        const selectedClass =
        object.id === selectedObjectId
            ? "canvas-object-selected"
            : "";
        html += `
            <div
                class="canvas-object ${selectedClass}"
                data-id="${object.id}">

                ${object.type} Object

            </div>
        `;

    });

    canvasElement.innerHTML = html;

    attachCanvasEvents();
}

/**
 * Obsługa zdarzeń dla obiektów canvas.
 */
function attachCanvasEvents() {

    const canvasObjectsElements =
        document.querySelectorAll(
            ".canvas-object"
        );

    canvasObjectsElements.forEach(element => {

        element.addEventListener(
            "click",
            () => {

                selectedObjectId =
                    Number(
                        element.dataset.id
                    );

                selectCanvasObject();

            }
        );

    });

}

/**
 * Wybór obiektu canvas i aktualizacja PropertyPanel.
 */
function selectCanvasObject() {

    const selectedObject =
        canvasObjects.find(
            object =>
                object.id === selectedObjectId
        );

    renderCanvas();
    
    updatePropertyPanelObject(
        selectedObject
    );

}

/**
 * Aktualizacja PropertyPanel dla wybranego obiektu.
 * @param {*} object 
 */
function updatePropertyPanelObject(
    object
) {

    const propertyPanel =
        document.getElementById(
            "property-placeholder"
        );

    propertyPanel.innerHTML = `
        <strong>Selected Object</strong>

        <br><br>

        Type: ${object.type}

        <br>

        ID: ${object.id}
    `;
}

/**
 * Obsługa skrótów klawiaturowych.
 */
function initializeKeyboardShortcuts() {

    document.addEventListener(
        "keydown",
        (event) => {

            if (event.key === "Delete") {

                deleteSelectedObject();

            }

        }
    );

}

/**
 * Usunięcie zaznaczonego obiektu.
 */
function deleteSelectedObject() {

    if (selectedObjectId === null) {

        return;

    }

    const objectIndex =
        canvasObjects.findIndex(
            object=>
                object.id === selectedObjectId
        );

    if (objectIndex === -1) {

        return;

    }

    canvasObjects.splice(
        objectIndex,
        1
    );

    selectedObjectId = null;

    renderCanvas();

    clearPropertyPanel();

}

function clearPropertyPanel() {

    const propertyPanel =
        document.getElementById(
            "property-placeholder"
        );

    propertyPanel.innerHTML =
       "Brak zaznaczonego obiektu";
}
