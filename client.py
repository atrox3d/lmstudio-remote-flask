import json
from operator import add
from flask.cli import F
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


    # stream = False  # disable streaming for now, returns a 500 error


    response = requests.post(url, json=data, headers=headers)
    print(f'response: {response}')

    response.raise_for_status()

    if stream:
        if response.status_code == 200:
            for chunk in response.iter_lines(decode_unicode=True):
                print(f'Chunk: {chunk}')
                if chunk and chunk.strip():
                    try:
                        # print(json.loads(chunk))
                        pass
                    except json.JSONDecodeError as e:
                        print(f"Failed to parse JSON: {e}")
                else:
                    break
        else:
            print(f"request failed with status code {response.status_code}")
    else:
    # print(json.dumps(response.json(), indent=4))
    # print(response.json()['choices'][0]['text'])
        print(response.json()['choices'][0]['message']['content'])

if __name__ == "__main__":
    app()
