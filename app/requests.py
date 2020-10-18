import urllib.request,json
from .models import Source, Articles


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
    '''
    Method that gets the json response to our url request
    '''
    get_articles_url = articles_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(articles):
    articles_results = []
    for item in articles:
        id = item.get('id')
        author = item.get('author')
        urlToImage = item.get('urlToImage')
        url = item.get('url')

        if urlToImage:
            article_object = Articles(id, author,title,urlToImage,url)
            articles_results.append(article_object)
    return articles_results