import click
from artcli.artifactory_adapter import ArtifactoryAdapter

art_ad = ArtifactoryAdapter("https://khalil.jfrog.io/artifactory/api")

@click.group()
def cli():
    """Artifactory CLI"""
    pass

@cli.command()
@click.option('--user', help='Artifactory user', required=True)
@click.option('--passwd', help='Artifactory password', required=True)
def auth(user, passwd):
    """Authenticate using user/pass with Artifactory"""
    print(art_ad.auth(user, passwd))

@cli.command()
def ping():
    """Ping the Artifactory server"""
    art_ad.ping()