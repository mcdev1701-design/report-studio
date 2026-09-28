/**
 * Report Studio
 *
 * Główny plik JavaScript aplikacji.
 *
 * ETAP_01D
 * Frontend Bootstrap
 */

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

        loadApplicationInfo();

        initializeToolbox();

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
function addCanvasObject(
    selectedTool
) {

    canvasObjects.push(selectedTool);

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

        html += `
            <div class="canvas-object">
                ${object} Object
            </div>
        `;

    });

    canvasElement.innerHTML = html;
}
