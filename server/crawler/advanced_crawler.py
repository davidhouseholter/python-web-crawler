import scrapy
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class AdvancedCrawler(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ['lens.xyz']
    start_urls = ['https://docs.lens.xyz/docs']
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)

    def parse(self, response):
        self.driver.get(response.url)
        print(response)
        # while True:
        #     next = self.driver.find_element_by_xpath('//td[@class="pagn-next"]/a')

        #     try:
        #         next.click()

        #         # get the data and write it to scrapy items
        #     except:
        #         break

        self.driver.close()