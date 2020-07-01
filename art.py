import click
from artcli.artifactory_adapter import ArtifactoryAdapter
from artcli.token_cache import TokenCache
from artcli.config import logging

art_ad = ArtifactoryAdapter("https://khalil.jfrog.io/artifactory/api")
token_cache = TokenCache()

@click.group()
def cli():
    """Artifactory CLI"""
    pass

@cli.command()
@click.option('--user', help='Artifactory user', required=True)
@click.option('--passwd', help='Artifactory password', required=True)
def auth(user, passwd):
    """Authenticate using user/pass with Artifactory"""
    token = art_ad.auth(user, passwd)
    if token == "":
        logging.error("Authentication failed!")
        return
    
    token_cache.save_token(token)

@cli.command()
def ping():
    """Ping the Artifactory server"""
    art_ad.ping()

@cli.command()
def versions():
    """Prints the Artifactory server versions"""
    token = token_cache.retrieve_token()
    art_ad.versions(token)