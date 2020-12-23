import requests
import os
from dotenv import load_dotenv
import time
from pathlib import Path  # python3 only
from tok import BearerAuth


load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

tok = os.getenv("FORGE_TOKEN")
base = "https://forge.laravel.com"
headers = {
'Accept': 'application/json',
'Content-Type': 'application/json'}

get_servers = base + "/api/v1/servers"
site = "418015"

def create_site(domain, username):
    payload = {
        'domain': domain,
        'project_type': 'php',
        'directory': '/',
        'isolated': True,
        'username': username
    }
    response = requests.post(f'{get_servers}/{site}/sites', auth=BearerAuth(tok), headers=headers, json=payload)
    time.sleep(10)
    return response.json()

def create_db(name, user, password):
    payload = {
        'name': name,
        'user': user,
        'password': password
    }
    response = requests.post(f'{get_servers}/{site}/mysql', auth=BearerAuth(tok), headers=headers, json=payload)
    time.sleep(10)
    return response.json()

create_site("site", "user")
create_db("db_name", "db_username", "db_pass")