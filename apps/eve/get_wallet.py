#!/usr/bin/env python3

from datetime import datetime
from configparser import ConfigParser
import requests
import json

from apps.authentication.models import Users
from apps.eve.models import Characters

# Config
config = ConfigParser()
config.read('apps/eve/config.py')

class EveESI():
    global esi_url
    esi_url = "https://esi.evetech.net/dev/characters/"

    def __init__(self):
        pass

    def get_wallet(char_id):
        c = Characters.query.filter_by(id=char_id).first()
        headers = {"authorization" : "Bearer " + c.access_token}
        data = requests.get(esi_url + str(c.character_id) + "/wallet", headers=headers)
        wallet = json.loads(data.text)
        return(wallet)
    
    def get_skills(char_id):
        c = Characters.query.filter_by(id=char_id).first()
        headers = {"authorization" : "Bearer " + c.access_token}
        data = requests.get(esi_url + str(c.character_id) + "/skills", headers=headers)
        print(data)
        skills = json.loads(data.text)
        return(skills)