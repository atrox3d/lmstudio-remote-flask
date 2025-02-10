import typer
from flask import Flask, request
import requests

cli = typer.Typer(add_completion=False)
app = Flask(__name__)

SERVER_IP = 'localhost'
LM_STUDIO_URL = f"http://{SERVER_IP}:1234/v1/completions"


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    response = requests.post(LM_STUDIO_URL, json=data)
    return response.json()


@cli.command()
def run(
    host: str = '0.0.0.0', 
    port: int = 5000,
    lms_ip: str = SERVER_IP
):
    global SERVER_IP
    SERVER_IP = lms_ip
    
    app.run(
        host=host, 
        port=port,
        debug=True
    )


if __name__ == "__main__":
    cli()