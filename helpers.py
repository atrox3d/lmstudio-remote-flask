from enum import Enum


class Url(str, Enum):
    openai = 'openai'
    lmstudio = 'lmstudio'


URLS = {
    'openai': 'http://{server}:{port}/v1/chat/completions',
    'lmstudio' : 'http://{server}:{port}/api/v0/chat/completions'
}

def get_url(url: Url, server: str, port: int) -> str:
    return URLS[url.value].format(server=server, port=port)


def get_payload(
    user_prompt     : str, 
    system_prompt   : str   = '', 
    model           : str   = 'meta-llama-3.1-8b-instruct',
    temperature     : float = 0.7, 
    max_tokens      : int   = -1, 
    stream          : bool  = False
) -> dict:
    return {
        'model': model,
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
