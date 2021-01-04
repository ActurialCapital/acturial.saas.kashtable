import os
import os.path as op

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    DATABASE_FILE = 'db.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
#    SECRET_KEY = os.environ.get('SECRET_KEY')
#    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')    
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        
    FLASK_ADMIN_BOOTSTRAP = 'bootstrap3'
    FLASK_ADMIN_SWATCH = 'Slate' # https://bootswatch.com/
    
    FILE_PATH = op.join(op.dirname(__file__), 'files')
    
    BASIC_AUTH_USERNAME = 'alfie@example.com'
    BASIC_AUTH_PASSWORD = 'alfiephillips'
    