from urllib.request import urlopen
from 001-general import *
from 002-link_finder import LinkFinder

class Spider:

    #Class variables (shared between all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def _init_(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = project_name + "/queue.txt"
        Spider.crawled_file = project_name + "/crawled.txt"
        self.boot()
        self.crawl_page('first spider', Spider.base_url)

    @staticmethod
    def boot(self):
        create_project_directory(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url nit in Spider.crawled:
            print (thread_name + " crawling " + page_url)
            print ("Queue : " + str(len(Spider.queue)) + " | Crawled : " + str(len(Spider.crawled))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
