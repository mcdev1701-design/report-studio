"""
Debug Windows Pipe Source.

Tryby:

server
client
"""

import json
import sys
from pprint import pprint

import win32file
import win32pipe

from backend.app.services.datasources.windows_pipe_source import (
    WindowsPipeSource
)

PIPE_NAME = r"\\.\pipe\ReportStudio"


def run_server():
    """
    Uruchomienie serwera Pipe.
    Tworzy Named Pipe i oczekuje na klienta.
    Po połączeniu wysyła przykładowe dane w formacie JSON.
    """
    pipe = win32pipe.CreateNamedPipe(
        PIPE_NAME,
        win32pipe.PIPE_ACCESS_OUTBOUND,
        win32pipe.PIPE_TYPE_MESSAGE
        | win32pipe.PIPE_WAIT,
        1,
        65536,
        65536,
        0,
        None
    )

    print()
    print("Pipe utworzony:")
    print(PIPE_NAME)

    print()
    print("Oczekiwanie na klienta...")

    win32pipe.ConnectNamedPipe(
        pipe,
        None
    )

    payload = [
        {
            "id": 1,
            "name": "Produkt A",
            "price": 10.50
        },
        {
            "id": 2,
            "name": "Produkt B",
            "price": 25.90
        }
    ]

    data = json.dumps(payload)

    win32file.WriteFile(
        pipe,
        data.encode("utf-8")
    )

    print()
    print("Dane wysłane.")

    win32file.CloseHandle(pipe)

    print()
    print("Pipe zamknięty.")


def run_client():

    source = WindowsPipeSource(
        PIPE_NAME
    )

    source.connect()

    dataset = source.get_data()

    source.disconnect()

    print()
    print("=== DATASET ===")
    print()

    print(dataset)

    print()
    print("=== COLUMNS ===")
    print(dataset.columns)

    print()
    print("=== ROW COUNT ===")
    print(dataset.row_count)

    print()
    print("=== ROWS ===")
    pprint(dataset.rows)


if __name__ == "__main__":

    if len(sys.argv) != 2:

        print()
        print("Użycie:")
        print(
            "python -m tools.debug_windows_pipe_source "
            "[server|client]"
        )

        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "server":

        run_server()

    elif mode == "client":

        run_client()

    else:

        print()
        print("Dostępne tryby:")
        print("server")
        print("client")