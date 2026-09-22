from fastapi import FastAPI

app = FastAPI(
    title="Report Studio",
    version="0.1.0"
)


@app.get("/")
def root():
    """
    Główny endpoint testowy.

    Cel:
    Sprawdzenie poprawności działania aplikacji.
    """

    return {
        "application": "Report Studio",
        "version": "0.1.0"
    }