import urllib.request,json
from .models import Source


api_key = None
base_url = None
article_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_URL']
    article_url = app.config['ARTICLES_URL']

def get_sources(category):
    get_sources_url = base_url.format(category, api_key)

    # import pdb; pdb.set_trace()
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_source_response = json.loads(get_sources_data)

        sources_list = None
        if get_source_response['sources']:
            rest_here = get_source_response['sources']
            sources_list = process_results(rest_here)

    return sources_list

def process_results(results):
    sources_list = []

    for item in results:
        id = item.get('id')
        description = item.get('description')
        url = item.get('url')
        category = item.get('category')

        new_item = Source(id, description, url, category)
        sources_list.append(new_item)
        
    return sources_list

def get_articles(domains):
    get_articles_url = article_url.format(domains, api_key)
    with urllib.request.urlopen(get_articles_url)as url:
        articles_details = url.read()
        article_response = json.loads(articles_details)
        articles_list = []
        if article_response:
            id = article_response('id')
            description = article_response('description')
            url =article_response('url')
            