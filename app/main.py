# import requests
# import os
# import time
# from pathlib import Path  # python3 only
# from tok import BearerAuth
#from app.forge_calls import list_sites
from typing import Optional
from fastapi import FastAPI
from forge_calls import create_site, create_db, list_sites, list_server_ids
from generate_pass import *

app = FastAPI()

@app.post("/api/forge/devsite")
def create_dev_site(domain: str, server_id: int):
    user_name = ''.join(domain.split('.'))
    db_name = f'{user_name}_db'
    db_username = f'{user_name}_db_user'
    db_password = get_random_string(10)
    create_site(domain, user_name, server_id)
    create_db(db_name, db_username, db_password, server_id)
    return {'access': {'db': db_name, 'db_user': db_username, 'db_pass': db_password, 'username': user_name}}

@app.get("/api/forge/list_sites")
def list_server_sits(server_id: int):
    return list_sites(server_id)

@app.get("/api/forge/servers")
def list_servers():
    return list_server_ids()