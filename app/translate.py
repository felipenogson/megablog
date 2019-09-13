import json
import requests
from flask_babel import _
from app import app

#borrar esto es por mientras
def translate(text,  dest_language, source_language=None):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
        not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: The tranlsation server is not configured')

    headers = {'Ocp-Apim-Subscription-Key' : app.config['MS_TRANSLATOR_KEY'], 
        'Content-type' : 'application/json'}

    body = [{
        'text' : text
    }]
    
    end_point = app.config['MS_TRANSLATOR_ENDPOINT'] 
    path = '/translate?api-version=3.0'
    params = f'&to={dest_language}&from{source_language}'
    constructed_url = end_point + path + params
    print(constructed_url)
    print(headers)

    r = requests.post(constructed_url, headers=headers, json=body)
    return r
