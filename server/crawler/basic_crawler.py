import logging
import requests
from requests.adapters import HTTPAdapter, Retry

from bs4 import BeautifulSoup
from .core import ApplicationError


import scrapy
from scrapy_selenium import SeleniumRequest
  
# for firefox
from shutil import which
 

class BasicCrawler(object):
    """A web crawler based on a seed url and the depth"""

    crawl_map = {}
    links_list = list()
    seed, depth = None, 0

    def __init__( self, seed, depth ): 
        self.crawl_map = {
            "seed": seed,
            "depth": depth,
            "contents": []
        }
        self.seed = self._validate_seed( seed )
        print('final')
        print(self.seed)
        self.depth = self._validate_depth( depth )

    def _validate_seed( self, seed ): 
        if not seed: 
            raise ApplicationError("seed must be a string.")
        print(seed)
        print(seed.index('https://'))
        return seed       
        # try: 
        #     if seed.index('http://') == 0 or seed.index('https://') == 0:
        #         print('in if')
        #         return seed
        # except ValueError:
        #     return "http://" + seed

        # return "http://" + seed

    def _validate_depth( self, depth ): 

        if depth is None: 
            raise ApplicationError("depth must be a number.")

        return int(depth)
        
    def start_crawl( self, seed=None, depth=None ): 
        seed = seed or self.seed
        depth = depth or self.depth

        self.crawl(seed, depth)
        return self.crawl_map

    def format_url( self, seed, url ):

        def base( u ):
            u = u.split('?')[0].rstrip('/')
            return u

        seed = base(seed)

        if url == "/":
            return seed
        elif url.startswith("http://") or url.startswith("https://"):
            return base(url)
        elif url.startswith("/"):
            return seed + url

    def start_requests(self):
        yield SeleniumRequest(
            url = self.seed,
            wait_time = 3,
            screenshot = True,
            callback = self.parse,
            dont_filter = True
        )
  
    def parse(self, response):
        print(response)
        # courses make list of all items that came in this xpath
        # this xpath is of cards containing courses details
        courses = response.xpath('//*[@id ="active-courses-content"]/div/div/div')
  
        # course is each course in the courses list
        for course in courses:
            # xpath of course name is added in the course path
            # text() will scrape text from h4 tag that contains course name
            course_name = course.xpath('.//a/div[2]/div/div[2]/h4/text()').get()
  
            # course_name is a string containing \n and extra spaces
            # these \n and extra spaces are removed
  
            course_name = course_name.split('\n')[1]
            course_name = course_name.strip()
  
              
            yield {
                'course Name':course_name
            }
    def crawl( self, seed, depth ):
        print("Crawling:  {seed} at {depth}".format(seed=seed, depth=depth))
        # session = requests.Session()
        # retry = Retry(connect=3, backoff_factor=0.5)
        # adapter = HTTPAdapter(max_retries=retry)
        # session.mount('http://', adapter)
        # session.mount('https://', adapter)
        
        # response = session.get(seed, timeout=20)
        # response = requests.get(seed)
        
        # with open('content.txt', 'w') as f:
        #     f.write(response.content)
        # soup = BeautifulSoup(response.content, "html.parser")
        # with open('soup.txt', 'w') as f:
        #     f.write(soup)
        # print(soup)
        # imgs = []
        # for img in soup.find_all('p', src=True):
        #     img_src = self.format_url(seed, img)

        #     if img_src and img_src not in imgs:
        #         imgs.append(img_src)

        # result = {
        #     'link': seed,
        #     'images': imgs
        # }
        # self.crawl_map["contents"].append(result)

        # if depth:
        #     for anchor in soup.find_all('a', href=True):
        #         sub_link = self.format_url(seed, anchor['href'])

        #         if sub_link and sub_link not in self.links_list and len(self.links_list) < 4:
        #             self.links_list.append(sub_link)
        #             self.crawl(sub_link, depth - 1)