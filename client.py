import json
import requests
import typer

app = typer.Typer(add_completion=False)

SERVER_IP = '192.168.1.10'
SERVER_IP = 'localhost'

# LM_STUDIO_URL = f"http://{SERVER_IP}:1234/v1/completions"           # openAI, deprecated
LM_STUDIO_URL = f"http://{SERVER_IP}:1234/api/v0/chat/completions"  # LM Studio (beta)
LM_STUDIO_URL = f"http://{SERVER_IP}:1234/v1/chat/completions"      # openAI, deprecated


@app.command()
def chat(
    user_prompt: str,
    system_prompt: str = '',
    temperature: float = 0.7,
    max_tokens: int = -1,
    stream: bool = False,
    host: str = SERVER_IP, 
    port: int = 1234
):
    # stream = False  # disable streaming for now, returns a 500 error
    # print(f'ignore stream: {stream}')
    
    # url = f"http://{host}:{port}/chat"
    url = f"http://{host}:{port}/v1/chat/completions"
    print(f'URL: {url}')
    
    headers = {"Content-Type": "application/json"}
    data1 = {
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

    # data2 = {
        # "model": "meta-llama-3.1-8b-instruct",  # Replace with your model's identifier
        # "messages": [
            # {"role": "user", "content": "hello"}
        # ],
        # "stream": stream  # Enable streaming
    # }
    
    data = data1
    print(f'data: {data}')
    print(f'stream: {stream}')
    response = requests.post(url, json=data, headers=headers, stream=stream)
    response.raise_for_status()
    print(f'status code: {response.status_code}')

    if stream:
        print('streaming...')
        for chunk in response.iter_lines(decode_unicode=True):
            if chunk.strip().startswith('data: '):
                chunk = chunk.replace('data: ', '')
                # print(f'chunk: {chunk!r}')
                try:
                    delta = json.loads(chunk)['choices'][0]['delta']
                    if delta:
                        print(delta['content'], end='')
                except json.JSONDecodeError as e:
                    # print(f"Failed to parse JSON: {e}")
                    # print(f'chunk: {chunk!r}')
                    pass
            else:
                # print(f'no data {chunk!r}')
                continue
    else:
    # print(json.dumps(response.json(), indent=4))
    # print(response.json()['choices'][0]['text'])
        # print(response.text)
        print(response.json()['choices'][0]['message']['content'])

if __name__ == "__main__":
    app()
