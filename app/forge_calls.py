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
#tok = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijc1OWE4M2FiOTcwZTE4NTUwNGFhMjQwYzJlMDRmMmU2MDkwMDViZGFiM2E5NzczZGIzMjcwYzk2MDEyZTU3MjlhODBiNjAwZmZlMjI3ZjkxIn0.eyJhdWQiOiIxIiwianRpIjoiNzU5YTgzYWI5NzBlMTg1NTA0YWEyNDBjMmUwNGYyZTYwOTAwNWJkYWIzYTk3NzNkYjMyNzBjOTYwMTJlNTcyOWE4MGI2MDBmZmUyMjdmOTEiLCJpYXQiOjE1ODM5MTQ5NjQsIm5iZiI6MTU4MzkxNDk2NCwiZXhwIjoxODk5NDQ3NzY0LCJzdWIiOiIxMTQ2ODEiLCJzY29wZXMiOltdfQ.QfW_tcOvESIzrMSJixFwM7JgJINnZE73ukf9bzPuuDZ9LiWJiC8LUu-jy1WsALPZnoF_KMkh9qGjalz414JAA96nX_LoYQvo2SYu_HknGSt-dzGzmimAAU4Orb90pxn03dEUVyeZY-QkIrBKl4JrvgoHBF2_ztrvg8Q5FyS8j_934BMprZCwnAHxGD_E8NpRTUwhgHCAE5n5Zm0R0PZT1qLXYKxzDnd5M3xKcH_FC6k8uLSGrkaZ3EEkNoCxc_HPCflRf17HqesqOQVse7Fk9SKb87rjQRUQwBAzcGp2_3VtpeztwO8Pnyt6kcxOqY42LD6360MBiCuRjVeQnIfr7Tzo9WgNg8BIajhyLD9OFqLORgPZxXfRF-p4yz2MQp9eOZaRjPDn5ny8pqDwpg6jH2aFISVrSfPDPjNbRFZdIkkM4iyqGaWav3nTJj95wbelIveQPZotgQtlveFoJNro_26Bk9LauXMR1XJ4dkNvcH9etWxb_rgopSZD_wSXqCp9feLD9idyS4Yu744nLYlUaD4wrevwsZxawxPR7DUD72ABZL3DuqxFbT1dyMXtnzMt4f3kALrZmrhfRutxI9fIbOe3gyjYL27WN4M3KhuO6xArXvk8DjJIGIKgODcVc76j-f_bjmNgxtkohph3-qR_fjyvzqUv-gTYLknZlqXoALY"
base = "https://forge.laravel.com"
headers = {
'Accept': 'application/json',
'Content-Type': 'application/json'}

get_servers = base + "/api/v1/servers"

def create_site(domain, username, server):
    payload = {
        'domain': domain,
        'project_type': 'php',
        'directory': '/',
        'isolated': True,
        'username': username
    }
    response = requests.post(f'{get_servers}/{server}/sites', auth=BearerAuth(tok), headers=headers, json=payload)
    time.sleep(10)
    return response.json()

def create_db(name, user, password, server):
    payload = {
        'name': name,
        'user': user,
        'password': password
    }
    response = requests.post(f'{get_servers}/{server}/mysql', auth=BearerAuth(tok), headers=headers, json=payload)
    time.sleep(10)
    return response.json()

def list_sites(server):
    sites = []
    response = requests.get(f'{get_servers}/{server}/sites', auth=BearerAuth(tok), headers=headers).json()
    for i in response['sites']:
        sites.append(i['name'])
    return sites

def list_server_ids():
    servers = {}
    response = requests.get(f'{get_servers}', auth=BearerAuth(tok), headers=headers).json()
    for i in response['servers']:
        #print(i['name'], i['id'])
        servers.update({i['name']: i['id']})
    return servers