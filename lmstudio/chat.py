# @app.command()
import requests
import typer
import json
import logging

import lmstudio.helpers as helpers


logger = logging.getLogger(__name__)
SERVER_IP = 'localhost'
SERVER_IP = '192.168.1.10'
PORT = 1234
# LM_STUDIO_URL = f"http://{SERVER_IP}:1234/v1/completions"           # openAI, deprecated
# LM_STUDIO_URL = f"http://{SERVER_IP}:1234/api/v0/chat/completions"  # LM Studio (beta)
# LM_STUDIO_URL = f"http://{SERVER_IP}:1234/v1/chat/completions"      # openAI
MODEL = 'meta-llama-3.1-8b-instruct'


def chat(
    user_prompt   : str,
    system_prompt : str = '',
    temperature   : float = 0.7,
    max_tokens    : int = -1,
    stream        : bool = False,
    host          : str = SERVER_IP,
    port          : int = PORT,
    urlschema     : helpers.Url = typer.Option(helpers.Url.openai, help="Endpoint to connect to"),
):
    url = helpers.get_url(urlschema, host, port)
    headers = {"Content-Type": "application/json"}
    payload = helpers.get_payload(
        user_prompt,
        system_prompt, MODEL,
        temperature,
        max_tokens,
        stream
    )
    logger.debug(f'payload: {payload}')
    logger.info(f"Connecting to {url}")
    response = requests.post(url, json=payload, headers=headers, stream=stream)
    response.raise_for_status()

    if stream:
        print('streaming...')
        for chunk in response.iter_lines(decode_unicode=True):
            logger.debug(f"chunk: {chunk}")
            if (chunk := chunk.replace('data: ', '')) and chunk != '[DONE]':
                try:
                    delta = json.loads(chunk)['choices'][0]['delta']
                    if delta:
                        print(delta['content'], end='')
                except json.JSONDecodeError as e:
                    logger.error(f"Error: {e}")
                    logger.error(f'chunk: {chunk}')
                    continue
            else:
                continue
        print()
    else:
        print(response.json()['choices'][0]['message']['content'])