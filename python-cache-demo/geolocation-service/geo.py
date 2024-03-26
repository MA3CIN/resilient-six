import requests
import requests_cache
from requests_cache import CachedSession

from flask import Flask

infra_svc_endpoint_address = 'http://127.0.0.1:5000/'
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
   if (infra_svc_endpoint_address in session.cache.urls()):
      print("gotten from cache")
   else:
      print("gotten manually")
   return session.get(infra_svc_endpoint_address)


if __name__ == '__main__':
    app.run(port=6000)