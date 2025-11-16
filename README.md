# Broadcast-Server
Very simple Python websockets server that broadcasts client music information submitted from a html form.

## Files

### main.py

- **Description:**  
  The backend server script written in Python.
- **Functionality:**  
  - Starts a web server (likely using Flask, FastAPI, or similar).
  - Handles client connections.
  - Broadcasts messages to all connected clients.
  - May use WebSockets or HTTP endpoints for real-time communication.

### client.html

- **Description:**  
  The frontend client for connecting to the broadcast server.
- **Functionality:**  
  - Connects to the backend server (possibly via WebSocket or HTTP).
  - Sends and receives broadcast messages.
  - Provides a simple UI for user interaction.

## Usage

1. **Start the server:**
   ```bash
   python main.py
   ```

2. **Open the client:**
   - Open `client.html` in your web browser.
   - Follow on-screen instructions to connect and interact.

## Requirements

- Python 3.x
- Any required Python packages (see comments or requirements.txt if available)
- A modern web browser

## Notes

- Ensure the backend server is running before opening the client.
- Adjust server/client URLs as needed for your environment.
