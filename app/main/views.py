from flask import render_template, request, redirect, url_for
from  ..requests import get_sources
from ..models import Source
from . import main

@main.route('/')
def index():
    business_news = get_sources('business')
    # entertainment = get_sources('entertainment')
    # health = get_sources('health')
    # technology = get_sources('technology')
    # science = get_sources('science')
    # general = get_sources('general')
    # sports = get_sources('sports')

    return render_template('index.html', business_news=business_news)
    