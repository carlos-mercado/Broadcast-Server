# Broadcast-Server
Very simple Python websockets server that broadcasts client music information submitted from a html form.

## Files

### main.py

- **Description:**  
  The backend server script written in Python.
- **Functionality:**  
  - Starts a websockets server.
  - Handles client connections.
  - Broadcasts state changes to all connected clients.
  - Uses WebSockets for real-time communication.

### client.html

- **Description:**  
  The frontend client for connecting to the broadcast server.
- **Functionality:**  
  - Connects to the backend server.
  - Sends and receives broadcast messages.
  - Provides a simple UI for user interaction.

## Usage

1. **Start the server:**
   ```bash
   python main.py
   ```

2. **Open the client:**
   - Open `client.html` in your web browser.
   - *note* If opening the file from another device other than the device the server is running on, change localhost to the ip-address of the server device
   - Follow on-screen instructions to connect and interact.

## Requirements

- Python 3.x
- Any required Python packages (see comments or requirements.txt if available)
- A modern web browser

## Notes

- Ensure the backend server is running before opening the client.
- Adjust server/client URLs as needed for your environment.
