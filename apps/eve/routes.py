# -*- encoding: utf-8 -*-

# TODO: update token on refresh https://github.com/Kyria/flask-esipy-example/blob/594c99f27ee433d75eaf73c3726c44811a151ed3/app.py#L233C28-L233C28



from apps.eve import blueprint
from flask import render_template, request, request, redirect, session, url_for, jsonify, g
from apps import db
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
import requests
import base64
import json
from apps.authentication.models import Users
from apps.eve.models import Characters
from apps.eve.login import VerifyCharacter



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

# TODO: use token generation for state
def generate_token():
    """Generates a non-guessable OAuth token"""
    chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    rand = random.SystemRandom()
    random_string = ''.join(rand.choice(chars) for _ in range(40))
    return hmac.new(
        config.SECRET_KEY.encode('utf-8'),
        random_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

@blueprint.route('/evelogin')
#@login_required
def login():
    state = generate_token
    """Start the OAuth process by redirecting to EVE Online SSO."""
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'login.eveonline.com',
    }
    scopes = [
        'esi-wallet.read_character_wallet.v1',
        'esi-skills.read_skills.v1',
        'esi-fittings.read_fittings.v1',
        'esi-fittings.write_fittings.v1'
    ]

    oauth_params = {
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'state': state,
#        'scope': 'esi-skills.read_skills.v1',  # Request the needed scope(s)
#        'scope': 'esi-wallet.read_character_wallet.v1',  # Request the needed scope(s) TODO: specify multiple scopes
        # This isn't doing multiple scopes.
        'scope': ' '.join(scopes)
    }
    login_url = requests.Request('GET', AUTH_URL, params=oauth_params, headers=headers).prepare().url
    return redirect(login_url)


@blueprint.route('/callback')
#@login_required
def callback():
    g.user = current_user.get_id()
    """Handle the callback from EVE Online SSO."""
    code = request.args.get('code')
    
    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'login.eveonline.com'
    }
    data = {
        'grant_type': 'authorization_code',
        'code': code
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    if response.status_code == 200:
        tokens = response.json()
        session['access_token'] = tokens['access_token']
        session['refresh_token'] = tokens.get('refresh_token')  # Might not be present depending on scopes
        id = current_user.get_id() # change to current user id
        at = tokens['access_token']
        rt = tokens.get('refresh_token')
        character = Characters(owner_id=id, access_token=at, refresh_token=rt)
        db.session.add(character)
        db.session.commit()
        db.session.close()
        VerifyCharacter.initial(at)
        # VerifyCharacter to do initial validation of character
        # VerifyCharacter.initial(access_token)
        #return "Authentication successful!"
        return redirect("/list")
    else:
        return f"Failed to get tokens. Status code: {response.status_code} - {response.text}"

@blueprint.route("/test")
@login_required
def test():
    characters = Characters.query.filter_by(id="1").first()
    data = str(characters.name)
    return(data)

    
@blueprint.route("/list")
@login_required
def list():
    toons = Characters.query.all()
    return render_template('home/list-toons.html', characters=toons)


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None