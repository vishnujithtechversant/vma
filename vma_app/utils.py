import urllib3
import requests
import configparser
from requests.exceptions import ConnectionError
from serializer import deserialize
import os

SCHEMA_ROUTE = "/api/get-schema"
## TODO get from config
config = configparser.ConfigParser()
print(os.environ.get("VMACONFIG"))
configfilename = os.environ.get("VMACONFIG")
config.read(configfilename)
print(config['parent']['client_cer'])
CLIENT_CERT = config['parent']['client_cer']

# for dev only
urllib3.disable_warnings()


def get_metadata_from_parent(base_url):
    try:
        resp = requests.get(base_url + SCHEMA_ROUTE, cert=CLIENT_CERT, verify=False)
        schema = resp.json()
        return deserialize(schema["schema"])
    except ConnectionError as e:
        raise RuntimeError(f"Could not reach parent at {base_url}")
