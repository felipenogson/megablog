import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Variables to configure the emal notification service
    # la mayoria de estas variables las encuentras en el archivo
    # .env para ser ejecutadas por pydotenv
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT' or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['pon.felipon@gmail.com']

    # Variable que configura los post por pagina
    # para pruebas se pone un numero bajo
    POSTS_PER_PAGE = 10 

    # Configuracion para whoosh el buscador de texto
    WHOOSHEE_DIR = os.path.join(basedir, 'whooshee')
    MAX_SEARCH_RESULTS = 50

    # Configuracion para babel i18n y l10n
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY') or None
    MS_TRANSLATOR_ENDPOINT = os.environ.get('MS_TRANSLATOR_ENDPOINT') or None

