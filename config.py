class GeneralConfig(object):
    APP_NAME='ClinAPP'
    SECRET_KEY='notsecure'

class DevelopmentConfig(GeneralConfig):
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root@localhost/clinapp_db'
