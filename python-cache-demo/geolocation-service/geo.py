import requests
import requests_cache
from requests_cache import CachedSession

from flask import Flask

infra_svc_endpoint_address = 'http://127.0.0.1:5000/'
session = CachedSession('infra_owners_cache', backend='sqlite', expire_after=3600)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_location_for_gate():
    print("Getting owners:")
    returner_owners = get_owners()
    print(returner_owners)
    return(returner_owners)

# get endpoint IF cache is empty. 
#invalidate cache if you have a serial number without a corresponding cached owner 
# invalidate cache after 1 hour
#with cache enabled
def get_owners():
   if (session.cache.contains(infra_svc_endpoint_address)):
      print("gotten from cache")
      print(session.cache.get(infra_svc_endpoint_address))
      return session.cache.get(infra_svc_endpoint_address)
   else:
    response = requests.get(infra_svc_endpoint_address)
    print("gotten manually")
   return str(response.json())



if __name__ == '__main__':
    app.run(port=6000)