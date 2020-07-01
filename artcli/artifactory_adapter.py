import json
import requests
from artcli.config import logging

class ArtifactoryAdapter:
    base_url = "http://localhost:8081/artifactory/api"

    def __init__(self, base_url):
        self.base_url = base_url

    def auth(self, user, passwd):
        url = self.base_url + '/security/token'
        pay_load = {"username": user, "scope": "member-of-groups:admins"}
        r = requests.post(url, auth=(user, passwd), data=pay_load)
        if r.status_code != 200:
            return ""

        return r.json()['access_token']
    
    def ping(self):
        url = self.base_url + '/system/ping'
        r = requests.get(url)
        logging.info(r.text)

    def versions(self, token):
        url = self.base_url + '/system/version'
        r = requests.get(url, headers=self.get_auth_header(token))
        logging.info(r.text)
    
    def storage_info(self, token):
        url = self.base_url + '/storageinfo'
        r = requests.get(url, headers=self.get_auth_header(token))
        logging.info(r.text)
    
    def user_create(self, token, user_data):
        url = self.base_url + '/security/users/' + user_data['user_name']
        payload = self.get_create_user_request(user_data)
        logging.info(payload)
        r = requests.put(url, data=payload, headers=self.get_auth_header(token))
        logging.info(r.text)

    def user_delete(self, token, user_name):
        url = self.base_url + '/security/users/' + user_name
        r = requests.delete(url, headers=self.get_auth_header(token))
        logging.info(r.text)

    def get_auth_header(self, token):
        return {'Authorization': 'Bearer ' + token}
    
    def get_create_user_request(self, user_data):
        return {
            "email" : user_data['email'],
            "password": user_data['passwd']
        }
