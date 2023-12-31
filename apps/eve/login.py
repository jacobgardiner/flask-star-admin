#!/usr/bin/env python3

from configparser import ConfigParser
from apps.eve.models import Characters
from apps import db
import requests
import json

# Config
config = ConfigParser()
config.read('apps/eve/config.py')

# EVE Online OAuth details
CLIENT_ID = config.get('esi', 'client_id')
CLIENT_SECRET = config.get('esi', 'secret')
REDIRECT_URI = 'http://localhost:5000/callback'  # This should match the one in your EVE Developer account
AUTH_URL = 'https://login.eveonline.com/v2/oauth/authorize'
TOKEN_URL = 'https://login.eveonline.com/v2/oauth/token'

class EveLogin: 
    print(CLIENT_ID)

# Class to validate character. Input is access token
class VerifyCharacter():
    def initial(token):
        character = Characters.query.filter_by(access_token=token).first()

        # Check if initial has been done
        #if not character.name:
        #    print("THIS HAS BEEN DONE")
        print(character)

        url = "https://login.eveonline.com/oauth/verify"
        headers={"Authorization": "Bearer " + token}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            # Insert DB insert here. 
            json_response = response.json()
            character_id = json_response['CharacterID']
            character_name = json_response['CharacterName']
            token_expiry = json_response['ExpiresOn']
            scopes = json_response['Scopes']

            character = Characters.query.filter_by(access_token=token).first()
            character.name = character_name
            character.character_id = character_id
            character.scopes = scopes
            character.token_expiry = token_expiry
            rows_changed = Characters.query.filter_by(access_token=token).update(dict(
                name=character_name, 
                character_id=character_id, 
                token_expiry=token_expiry, 
                scopes=scopes
                ))
            db.session.commit()

            return(response.json())
        elif response.status_code == 401:
            return("401")
        else:
            return("HAH")

#        print(response_json)
#        return(response_json)