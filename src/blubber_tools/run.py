import click

from .manage.cli import hello
from .queries.cli import dashboard

@click.group()
def cli():
    """
    
    Blubber is the internal database interaction tool designed by Hubbub.

    This tool depends on connection to either the production Hubbub database
    or development replica of it. Make sure you have the following variables
    defined in your .env file:

        BLUBBER_DEBUG=0\n
        DATABASE_URL=<database-credentials-here>

    Contact Ade if you need help :)
    """
    click.echo("Welcome to Blubber Tools.")

cli.add_command(hello)
cli.add_command(dashboard)

if __name__ == '__main__':
    cli()