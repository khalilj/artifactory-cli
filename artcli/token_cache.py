import os
import json
from datetime import datetime

class TokenCache:
    local_cache_dir = os.environ['HOME'] + '/.arcli'
    local_cache_file = local_cache_dir + '/config'
    
    def save_token(self, token):
        if not os.path.exists(self.local_cache_dir):
            os.makedirs(self.local_cache_dir)
            os.chmod(self.local_cache_dir, 0o700)

        data = {"token": token, "creation_time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
        with open(self.local_cache_file, 'w') as outfile:
            json.dump(data, outfile)
        os.chmod(self.local_cache_file, 0o600)
    
    def retrieve_token(self):
        if not os.path.exists(local_cache_file):
            return ""
        
        with open(self.local_cache_file) as json_file:
            data = json.load(json_file)
            return data["token"]
