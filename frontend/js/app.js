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

    console.log("Pobieranie informacji o aplikacji...");

    const response = await fetch(
        "http://127.0.0.1:8000/api/v1/info"
    );

    const data = await response.json();

    console.log(data);

}