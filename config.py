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
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT' or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['pon.felipon@gmail.com']

    # Variable que configura los post por pagina
    # para pruebas se pone un numero bajo
    POSTS_PER_PAGE = 2
