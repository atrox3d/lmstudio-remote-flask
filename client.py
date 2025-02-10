import typer
import logging
import chat
import helpers


logger = logging.getLogger(__name__)
app = typer.Typer(add_completion=False)


@app.command()
def main(
    user_prompt   : str,
    system_prompt : str = '',
    temperature   : float = 0.7,
    max_tokens    : int = -1,
    stream        : bool = False,
    host          : str = chat.SERVER_IP,
    port          : int = chat.PORT,
    urlschema     : helpers.Url = typer.Option(helpers.Url.openai, help="Endpoint to connect to"),
    loglevel      : helpers.LogLevelsEnum = typer.Option(helpers.LogLevelsEnum.INFO, help="Logging level")
):
    logging.basicConfig(level=loglevel)
    
    chat.chat(
        user_prompt,
        system_prompt,
        temperature,
        max_tokens,
        stream,
        host,
        port,
        urlschema
    )


if __name__ == "__main__":
    app()
