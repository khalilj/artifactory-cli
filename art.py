import click
from artcli.artifactory_adapter import ArtifactoryAdapter
from artcli.token_cache import TokenCache
from artcli.config import logging

art_ad = ArtifactoryAdapter('https://khalil.jfrog.io/artifactory/api')
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
    if token == '':
        logging.error('Authentication failed!')
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

@cli.group()
def user():
    """User operations"""
    pass

@user.command()
@click.option('--username', help='User name', required=True)
@click.option('--passwd', help='User password', required=True)
@click.option('--email', help='User email', required=True)
def create(username, passwd, email):
    """Creates a user"""
    token = token_cache.retrieve_token()
    user_data = {'user_name': username,
                'passwd': passwd,
                'email': email}
    art_ad.user_create(token, user_data)

@user.command()
@click.option('--username', help='User name', required=True)
def delete(username):
    """Creates a user"""
    token = token_cache.retrieve_token()
    art_ad.user_delete(token, username)

@cli.group()
def storage():
    """Storage operations"""
    pass

@storage.command()
def info():
    """Print Storage information"""
    token = token_cache.retrieve_token()
    art_ad.storage_info(token)