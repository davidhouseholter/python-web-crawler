import time
import scrapy
from scrapy.crawler import CrawlerProcess

from server.spider.my_spider import MySpiderSpider

def start_spider(seed:str):
    
    print(seed)
    spiderProcess = CrawlerProcess()
    spiderProcess.crawl(MySpiderSpider)
    spiderProcess.start()
    #time.sleep(10)

    return False

