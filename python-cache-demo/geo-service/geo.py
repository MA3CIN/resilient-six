import requests
import requests_cache
import os
from requests_cache import CachedSession

from flask import Flask

INFRA_URL = os.getenv('INFRA_URI', 'http://127.0.0.1:3000/') 
DB_URL = os.getenv('DB_URL', 'http://127.0.0.1:3000/') 

# invalidate cache after 1 hour
session = CachedSession('infra_owners_cache', backend='sqlite', expire_after=3600)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_location_for_gate():
    returner_owners = get_owners()
    return(str(returner_owners.json()))

# get endpoint IF cache is empty. 
#invalidate cache if you have a serial number without a corresponding cached owner 
#with cache enabled
def get_owners():
   if (INFRA_URL in session.cache.urls()):
      print("gotten from cache")
   else:
      print("gotten manually")
   return session.get(INFRA_URL)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)