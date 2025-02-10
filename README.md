# Remote LMS from Flask

This project provides a simple relay server and client for interacting with a Language Model Studio (LM Studio) using Flask and Typer. The relay server acts as an intermediary between the client and the LM Studio, forwarding chat requests and responses.

## Project Structure

- `relay_server.py`: Contains the relay server code that forwards chat requests to the LM Studio.
- `client.py`: Contains the client code that sends chat requests to the relay server, or to the remote LM stdio server

## Requirements

- Python 3.7+
- Flask
- Typer
- Requests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/remote-lms-from-flask.git
    cd remote-lms-from-flask
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Relay Server

1. Start the relay server:
    ```sh
    python relay_server.py run --host 0.0.0.0 --port 5000 --lms-ip <LM_STUDIO_IP>
    ```

### Using the Client

1. Send a chat request using the client:
    ```sh
    python client.py chat --user-prompt "Hello, how are you?" --system-prompt "You are a helpful assistant." --temperature 0.7 --max-tokens 100 --stream False --host <RELAY_SERVER_IP> --port 5000
    ```

## Configuration

- [relay_server.py](http://_vscodecontentref_/0):
  - [SERVER_IP](http://_vscodecontentref_/1): Default IP address of the LM Studio.
  - `LM_STUDIO_URL`: URL for the LM Studio API.

- [client.py](http://_vscodecontentref_/2):
  - [SERVER_IP](http://_vscodecontentref_/3): Default IP address of the relay server.
  - [PORT](http://_vscodecontentref_/4): Default port number of the relay server.
  - [MODEL](http://_vscodecontentref_/5): Model name used for chat completions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.