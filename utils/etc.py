from base64 import b64encode

def get_basic_auth_token(username, password):
    return "Basic " + b64encode(f"{username}:{password}".encode()).decode()