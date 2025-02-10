import json
from operator import add
import requests
import typer

app = typer.Typer(add_completion=False)

@app.command()
def chat(
    user_prompt: str,
    system_prompt: str = '',
    temperature: float = 0.7,
    max_tokens: int = -1,
    stream: bool = False,
    host: str = "localhost", 
    port: int = 5000
):
    url = f"http://{host}:{port}/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        'model': 'meta-llama-3.1-8b-instruct',
        'messages': [
            {
                'role': 'system', 
                'content': system_prompt
            },
            {
                'role': 'user', 
                'content': user_prompt
            }
        ],
        'temperature': temperature,
        'max_tokens': max_tokens,
        'stream': stream
    }

    {
        "model": "meta-llama-3.1-8b-instruct",
        "prompt": user_prompt,
        "max_tokens": 100,
        "temperature": 0.5,
        "top_p": 0.9,
        "n": 1,
        "stop": None    
    }

    response = requests.post(url, json=data, headers=headers)
    # print(json.dumps(response.json(), indent=4))
    # print(response.json()['choices'][0]['text'])
    print(response.json()['choices'][0]['message']['content'])
if __name__ == "__main__":
    app()
