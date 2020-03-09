import requests

from requests.exceptions import ConnectionError
from serializer import deserialize

SCHEMA_ROUTE = "/api/get-schema"

# TODO ssl
def get_metadata_from_parent(base_url):
    try:
        resp = requests.get(base_url + SCHEMA_ROUTE)
        schema = resp.json()
        return deserialize(schema["schema"])
    except ConnectionError:
        print("here")
        raise RuntimeError(f"Could not reach parent at {base_url}")
