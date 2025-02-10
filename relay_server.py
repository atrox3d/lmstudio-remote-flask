import typer                                     # Import the typer library
from flask import Flask, request                  # Import Flask and request
import requests                                  # Import the requests library

cli = typer.Typer(add_completion=False)          # Create a Typer instance, disabling auto-completion
app = Flask(__name__)                             # Create a Flask web application instance

SERVER_IP = 'localhost'                           # Define the default server IP address
LM_STUDIO_URL = f"http://{SERVER_IP}:1234/v1/completions"           # openAI, deprecated
LM_STUDIO_URL = f"http://{SERVER_IP}:1234/api/v0/chat/completions"  # LM Studio
LM_STUDIO_URL = f"http://{SERVER_IP}:1234/v1/chat/completions"           # openAI, deprecated


@app.route("/chat", methods=["POST"])             # Define a route for the /chat endpoint, accepting POST requests
def chat():                                      # Define the chat function to handle requests
    data = request.json                           # Extract JSON data from the incoming request
    response = requests.post(LM_STUDIO_URL, json=data)  # Send a POST request to LM Studio with the data
    return response.json()                        # Return the JSON response from LM Studio

@cli.command()                                   # Define a command for the command-line interface
def run(                                         # Define the run function to start the server
    host: str = '0.0.0.0',                       # Define the host address, defaulting to 0.0.0.0
    port: int = 5000,                             # Define the port number, defaulting to 5000
    lms_ip: str = SERVER_IP                       # Define the LM Studio IP address, defaulting to SERVER_IP
):                                               #
    global SERVER_IP                              # Access the global SERVER_IP variable
    SERVER_IP = lms_ip                            # Update the global SERVER_IP with the provided IP
    
    app.run(                                     # Start the Flask development server
        host=host,                                # Specify the host address
        port=port,                                # Specify the port number
        debug=True                                # Enable debug mode
    )                                               #

if __name__ == "__main__":                       # Check if the script is being run directly
    cli()                                         # Execute the command-line interface
