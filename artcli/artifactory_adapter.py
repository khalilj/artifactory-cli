import json
import requests

class ArtifactoryAdapter:
    base_url = "http://localhost:8081/artifactory/api"

    def __init__(self, base_url):
        self.base_url = base_url

    def auth(self, user, passwd):
        url = self.base_url + '/security/token'
        pay_load = {"username": user, "scope": "member-of-groups:readers"}
        r = requests.post(url, auth=(user, passwd), data=pay_load)
        return r.json()['access_token']
    
    def ping(self):
        url = self.base_url + '/system/ping'
        r = requests.get(url)
        print(r.text)