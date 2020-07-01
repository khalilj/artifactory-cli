import json
import requests
from artcli.config import logging

class ArtifactoryAdapter:
    def auth(self, user, passwd, endpoint):
        url = endpoint + '/security/token'
        payload = {"username": user, "scope": "member-of-groups:admins"}
        r = requests.post(url, auth=(user, passwd), data=payload)
        if r.status_code != 200:
            return ""

        return r.json()['access_token']
    
    def ping(self, token_data):
        url = token_data['endpoint'] + '/system/ping'
        r = requests.get(url)
        logging.info(r.text)

    def versions(self, token_data):
        url = token_data['endpoint'] + '/system/version'
        r = requests.get(url, headers=self.get_auth_header(token_data['token']))
        logging.info(r.text)
    
    def storage_info(self, token_data):
        url = token_data['endpoint'] + '/storageinfo'
        r = requests.get(url, headers=self.get_auth_header(token_data['token']))
        logging.info(r.text)
    
    def user_create(self, token_data, user_data):
        url = token_data['endpoint'] + '/security/users/' + user_data['user_name']
        payload = self.get_create_user_request(user_data)
        r = requests.put(url, json=payload, headers=self.get_auth_header(token_data['token']))

    def user_delete(self, token_data, user_name):
        url = token_data['endpoint'] + '/security/users/' + user_name
        r = requests.delete(url, headers=self.get_auth_header(token_data['token']))
        logging.info(r.text)

    def get_auth_header(self, token):
        return {'Authorization': 'Bearer ' + token}
    
    def get_create_user_request(self, user_data):
        return {
            "email" : user_data['email'],
            "password": user_data['passwd']
        }
