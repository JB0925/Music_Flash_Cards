"""command-line interface
"""

import typer


cli = Typer()


@cli.callback()
def callback(ctx: typer.Context):
    """"""
