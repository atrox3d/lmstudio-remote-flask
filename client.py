import json
import requests
import typer

app = typer.Typer()

@app.command()
def chat(
    prompt: str,
    host: str = "localhost", 
    port: int = 5000
):
    url = f"http://{host}:{port}/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "meta-llama-3.1-8b-instruct",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.5,
        "top_p": 0.9,
        "n": 1,
        "stop": None    
    }

    response = requests.post(url, json=data, headers=headers)
    # print(response.json()['choices'][0]['text'])
    print(json.dumps(response.json(), indent=4))
if __name__ == "__main__":
    app()
