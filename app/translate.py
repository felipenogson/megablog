import json
import requests
from flask_babel import _
from app import app

#borrar esto es por mientras
end_point = 'https://blog-translator.cognitiveservices.azure.com/sts/v1.0/issuetoken'
key = '5888b2991cca4fc5abcb71acb719f34a'
def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
        not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: The tranlsation server is not configured')
    auth = {'0cp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    headers = {'0cp-Apim-Subscription-Key' : app.config['MS_TRANSLATOR_KEY'],
            'Content-type' : 'aplication/json'}
    body = [{
        'text' : text
    }]
    path = '/translate?api-version=3.0'
    params = '&to={source_language}&to={dest_language}'
    constructed_url = end_point + path + params
    r = requests.post(constructed_url, headers=headers, json=body)
    return r.json()