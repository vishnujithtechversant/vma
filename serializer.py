import pickle
from base64 import b64encode, b64decode


def serialize(data):
    obj = pickle.dumps(data)
    return b64encode(obj).decode()

def deserialize(data):
    obj = b64decode(data.encode())
    return pickle.loads(obj)
