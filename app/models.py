class Source:

    source_list = []

    def __init__(self, id, description, url, category):
        self.id = id
        self.description = description
        self.url = url
        self.category = category

class Articles:
    
    def __init__(self, id,author, title, urlToImage, url):
        self.id = id
        self.author = author
        self.title = title
        self.urlToImage= urlToImage
        self.url = url
        