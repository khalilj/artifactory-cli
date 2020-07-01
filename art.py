import click
from artcli.artifactory_adapter import ArtifactoryAdapter
from artcli.token_cache import TokenCache
from artcli.config import logging
import os

art_ad = ArtifactoryAdapter()
token_cache = TokenCache()

@click.group()
def cli():
    """Artifactory CLI"""
    pass

@cli.command()
@click.option('--user', help='Artifactory user', required=True)
@click.option('--passwd', help='Artifactory password', required=True)
@click.option('--endpoint', help='Artifactory api endpoint', required=True)
def auth(user, passwd, endpoint):
    """Authenticate using user/pass with Artifactory"""
    token = art_ad.auth(user, passwd, endpoint)
    if token == '':
        logging.error('Authentication failed!')
        return
    
    token_cache.save_token(token, endpoint)

@cli.command()
def ping():
    """Ping the Artifactory server"""
    token_data = token_cache.retrieve_token()
    art_ad.ping(token_data)

@cli.command()
def versions():
    """Prints the Artifactory server versions"""
    token_data = token_cache.retrieve_token()
    art_ad.versions(token_data)

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
    token_data = token_cache.retrieve_token()
    user_data = {'user_name': username,
                'passwd': passwd,
                'email': email}
    art_ad.user_create(token_data, user_data)

@user.command()
@click.option('--username', help='User name', required=True)
def delete(username):
    """Creates a user"""
    token_data = token_cache.retrieve_token()
    art_ad.user_delete(token_data, username)

@cli.group()
def storage():
    """Storage operations"""
    pass

@storage.command()
def info():
    """Print Storage information"""
    token_data = token_cache.retrieve_token()
    art_ad.storage_info(token_data)
