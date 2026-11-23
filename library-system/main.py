import sys
import webbrowser
import threading
import uvicorn


def open_browser(url: str):
    """Open Swagger UI in default web browser once server starts."""
    webbrowser.open(url)


def main():
    host = "127.0.0.1"
    port = 8000
    docs_url = f"http://{host}:{port}/docs"

    print("\n" + "=" * 65)
    print("  📚 LIBRARY MANAGEMENT SYSTEM - FASTAPI APPLICATION")
    print("=" * 65)
    print(f"\n🚀 Starting Swagger UI server at: {docs_url}")
    print("📖 Opening Swagger documentation in your browser...")
    print("🛑 Press Ctrl+C in this terminal to stop the server.\n")

    # Open the browser automatically after 1.2 seconds when server binds
    threading.Timer(1.2, open_browser, args=[docs_url]).start()

    # Run the uvicorn ASGI server directly
    uvicorn.run("api:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
