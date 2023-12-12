#!/usr/bin/env python3

from apps.authentication.models import Users

from datetime import datetime

from esipy import EsiApp
from esipy import EsiClient
from esipy import EsiSecurity
from esipy.exceptions import APIException

from configparser import ConfigParser
# Config
config = ConfigParser()
config.read('apps/eve/config.py')

# EVE Online OAuth details
CLIENT_ID = config.get('esi', 'client_id')
CLIENT_SECRET = config.get('esi', 'secret')
REDIRECT_URI = 'http://localhost:5000/callback'  # This should match the one in your EVE Developer account
AUTH_URL = 'https://login.eveonline.com/v2/oauth/authorize'
TOKEN_URL = 'https://login.eveonline.com/v2/oauth/token'

# INIT ESIPY
esiapp = EsiApp().get_latest_swagger
esisecurity = EsiSecurity(
    redirect_uri=REDIRECT_URI,
    client_id=CLIENT_ID,
    secret_key=CLIENT_SECRET
)

class EveESI(char_id):

    def get_wallet(char_id):
        user = Users.query.filter_by(character_id=char_id)

        wallet = None
        op = esiapp.op['get_characters_character_id_wallet'](
            character_id=user.character_id
        )
        wallet = esiclient.request(op)
        return(wallet)