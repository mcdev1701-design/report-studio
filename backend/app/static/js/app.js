/**
 * Report Studio
 *
 * Główny plik JavaScript aplikacji.
 *
 * ETAP_01D
 * Frontend Bootstrap
 */

console.log("Report Studio Frontend");

/**
 * Uruchamiane po pełnym załadowaniu dokumentu HTML.
 */
document.addEventListener("DOMContentLoaded", () => {

    console.log("DOM loaded");

    loadApplicationInfo();

});

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
