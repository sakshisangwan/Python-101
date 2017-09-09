from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def _init_(self, base_url, page_url):
        super._init_()
        self.base_url = base_url
        self.page_url = page_url
        self links = set()

    def hadle_starttag(self, tag, attrs):
        #print tag
        if tag == 'a':
            for (attribute,value) in attrs:
                if attribute == 'href':
                    url=parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
