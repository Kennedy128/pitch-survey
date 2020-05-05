class Config:
    '''
    General configuration parent class
    '''
    
    SECRET_KEY = 'kenny'
    

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kennedymbithi12@gmail.com'
    MAIL_PASSWORD = 'Email12345!'



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kennedy:Kennedy128@localhost/pitching'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kennedy:Kennedy128@localhost/pitching_test'

    


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
