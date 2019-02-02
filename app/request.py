from app import app
import urllib.request,json
from .models import articles
from .models import sources

# Getting api key
api_key = app.config['SOURCES_API_KEY']


Articles = articles.Articles
Sources = sources.Sources
