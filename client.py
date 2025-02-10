import json
from typing import Literal
import requests
import typer
import logging

import helpers


logger = logging.getLogger(__name__)
app = typer.Typer(add_completion=False)

SERVER_IP = 'localhost'
SERVER_IP = '192.168.1.10'
PORT = 1234
# LM_STUDIO_URL = f"http://{SERVER_IP}:1234/v1/completions"           # openAI, deprecated
# LM_STUDIO_URL = f"http://{SERVER_IP}:1234/api/v0/chat/completions"  # LM Studio (beta)
# LM_STUDIO_URL = f"http://{SERVER_IP}:1234/v1/chat/completions"      # openAI
MODEL = 'meta-llama-3.1-8b-instruct'


@app.command()
def chat(
    user_prompt   : str,
    system_prompt : str = '',
    temperature   : float = 0.7,
    max_tokens    : int = -1,
    stream        : bool = False,
    host          : str = SERVER_IP, 
    port          : int = PORT,
    urlschema      : helpers.Url = typer.Option(helpers.Url.openai, help="Endpoint to connect to")
):
    # url = f"http://{host}:{port}/v1/chat/completions"
    url = helpers.get_url(urlschema, host, port)
    headers = {"Content-Type": "application/json"}
    data1 = helpers.get_payload(
        user_prompt, 
        system_prompt, MODEL, 
        temperature, 
        max_tokens, 
        stream
    )
    
    data = data1
    logger.info(f"Connecting to {url}")
    response = requests.post(url, json=data, headers=headers, stream=stream)
    response.raise_for_status()

    if stream:
        print('streaming...')
        for chunk in response.iter_lines(decode_unicode=True):
            if chunk.replace('data: ', ''):
                try:
                    delta = json.loads(chunk)['choices'][0]['delta']
                    if delta:
                        print(delta['content'], end='')
                except json.JSONDecodeError as e:
                    logger.error(f"Error: {e}")
                    continue
            else:
                continue
    else:
        print(response.json()['choices'][0]['message']['content'])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
