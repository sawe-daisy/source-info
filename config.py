import os

class Config:
    News_source_url = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}