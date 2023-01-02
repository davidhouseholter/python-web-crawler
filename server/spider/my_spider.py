import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.shell import inspect_response
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import sys
from scrapy import signals
from pydispatch import dispatcher
# for chrome driver
from shutil import which

from server.spider.Items import DataItem

 
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless'] 
 
DOWNLOADER_MIDDLEWARES = {
     'scrapy_selenium.SeleniumMiddleware': 800
     }
class MySpiderSpider(CrawlSpider):
    name = 'quotes_spider'
    allowed_domains = ['lens.xyz']
    disallowed_urls = [
"https://docs.lens.xyz/docs/community-faq",
"https://docs.lens.xyz/docs/faq",
"https://docs.lens.xyz/docs/authentication-quickstart",
"https://docs.lens.xyz/docs/deployed-contract-addresses",
"https://docs.lens.xyz/docs/developer-quickstart",
"https://docs.lens.xyz/docs/querying-from-an-application",
"https://docs.lens.xyz/docs/api-links",
"https://docs.lens.xyz/docs/sdk-revenue",
"https://docs.lens.xyz/docs/use-notifications",
"https://docs.lens.xyz/docs/use-currencies",
"https://docs.lens.xyz/docs/sdk-misc",
"https://docs.lens.xyz/docs/use-feed",
"https://docs.lens.xyz/docs/use-unread-notification-count",
"https://docs.lens.xyz/docs/use-comments",
"https://docs.lens.xyz/docs/use-collected-publications",
"https://docs.lens.xyz/docs/use-create-post",
"https://docs.lens.xyz/docs/discovery",
"https://docs.lens.xyz/docs/use-publications",
"https://docs.lens.xyz/docs/sdk-publication",
"https://docs.lens.xyz/docs/use-profile-following",
"https://docs.lens.xyz/docs/use-active-profile",
"https://docs.lens.xyz/docs/use-mutual-followers"
"https://docs.lens.xyz/docs/use-profile",
"https://docs.lens.xyz/docs/sdk-profile",
"https://docs.lens.xyz/edit/metadata-publication-filters",
"https://docs.lens.xyz/edit/user",
"https://docs.lens.xyz/edit/reactions",
"https://docs.lens.xyz/edit/who-collected-publication",
"https://docs.lens.xyz/edit/publication-metadata-status",
"https://docs.lens.xyz/edit/proxy-action-gasless",
"https://docs.lens.xyz/edit/reactions",
"https://docs.lens.xyz/edit/add-reaction",
"https://docs.lens.xyz/edit/get-reaction",
"https://docs.lens.xyz/edit/profile-revenue",
"https://docs.lens.xyz/edit/who-reaction-publication",
"https://docs.lens.xyz/edit/reporting",
"https://docs.lens.xyz/edit/report-publication",
"https://docs.lens.xyz/edit/revenue",
"https://docs.lens.xyz/edit/quick-setup",
"https://docs.lens.xyz/edit/follow",
"https://docs.lens.xyz/edit/primer",
"https://docs.lens.xyz/edit/collect",
"https://docs.lens.xyz/edit/built-in-governance",
"https://docs.lens.xyz/edit/unpausing-the-protocol",
"https://docs.lens.xyz/docs/sdk-react-intro",
"https://docs.lens.xyz/edit/use-wallet-login",
"https://docs.lens.xyz/edit/use-wallet-logout",
"https://docs.lens.xyz/edit/use-profile",
"https://docs.lens.xyz/edit/lenshub",
"https://docs.lens.xyz/edit/creating-a-profile",
"https://docs.lens.xyz/edit/creating-publications",
"https://docs.lens.xyz/edit/following-a-profile",
"https://docs.lens.xyz/edit/collecting-publications",
"https://docs.lens.xyz/edit/approve-follow",
"https://docs.lens.xyz/docs/collecting-publications",
"https://docs.lens.xyz/docs/following-a-profile",
"https://docs.lens.xyz/docs/creating-publications",
"https://docs.lens.xyz/docs/creating-a-profile",
"https://docs.lens.xyz/docs/testing-a-module",
"https://docs.lens.xyz/docs/creating-a-module",
"https://docs.lens.xyz/docs/module-interfaces",
"https://docs.lens.xyz/edit/ifollowmodulesol",
"https://docs.lens.xyz/edit/icollectmodulesol",
"https://docs.lens.xyz/edit/events",
"https://docs.lens.xyz/edit/apollo-client",
"https://docs.lens.xyz/edit/urql",
"https://docs.lens.xyz/edit/explore-publications",
# "https://docs.lens.xyz/docs/what-database-do-we-use
# "https://docs.lens.xyz/docs/how-do-we-cache
# "https://docs.lens.xyz/docs/how-do-we-index
# "https://docs.lens.xyz/docs/why-our-own-indexer
# "https://docs.lens.xyz/docs/general-information
# "https://docs.lens.xyz/docs/e2ee-dms
# "https://docs.lens.xyz/docs/profile-feed
# "https://docs.lens.xyz/docs/user-timeline
# "https://docs.lens.xyz/docs/timeline
# "https://docs.lens.xyz/docs/search-profiles-and-publications
# "https://docs.lens.xyz/docs/search
# "https://docs.lens.xyz/docs/publication-revenue
# "https://docs.lens.xyz/docs/profile-follow-revenue
# "https://docs.lens.xyz/docs/profile-revenue
# "https://docs.lens.xyz/docs/revenue
# "https://docs.lens.xyz/docs/report-publication
# "https://docs.lens.xyz/docs/reporting
# "https://docs.lens.xyz/docs/who-reaction-publication
# "https://docs.lens.xyz/docs/get-reaction
# "https://docs.lens.xyz/docs/remove-reaction
# "https://docs.lens.xyz/docs/add-reaction
# "https://docs.lens.xyz/docs/reactions
# "https://docs.lens.xyz/docs/proxy-action-gasless
# "https://docs.lens.xyz/docs/user
# "https://docs.lens.xyz/docs/publication-metadata-status
# "https://docs.lens.xyz/docs/metadata-publication-filters
"https://docs.lens.xyz/edit/comment",]
    # start_urls = ['https://docs.lens.xyz/docs']
    start_urls = ['https://docs.lens.xyz/docs',
    'https://docs.lens.xyz/docs/what-is-lens',
    'https://docs.lens.xyz/docs/overview',
    'https://docs.lens.xyz/docs/developer-quickstart',
    'https://docs.lens.xyz/docs/profile',
    'https://docs.lens.xyz/docs/publication',
    'https://docs.lens.xyz/docs/comment',
    'https://docs.lens.xyz/docs/mirror',
    'https://docs.lens.xyz/docs/collect',
    'https://docs.lens.xyz/docs/follow',
    'https://docs.lens.xyz/docs/built-in-governance',
    'https://docs.lens.xyz/docs/multisig-governance',
    'https://docs.lens.xyz/docs/introduction'
    ]


    rules = [ 
        Rule( 
            LinkExtractor( 
                canonicalize=True, 
                unique=True 
            ), 
            follow=True, 
            callback="parse_page" 
        ) 
    ]   
 
    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        sys.stdout.close()

      # second param is instance of spder about to be closed.
    def start_requests(self):

        sys.stdout = open('textout.txt', 'w')
        url = 'https://docs.lens.xyz/docs'
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        #print(response.url)

        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response) 
        #print(links)
        for link in links: 
            is_allowed = False 
            for allowed_domain in self.allowed_domains: 
                if allowed_domain in link.url and link.url in self.start_urls: 
                    is_allowed = True 
                if is_allowed and  link.url in self.disallowed_urls:
                    is_allowed = False
            if is_allowed: 
                #print(link.url)
                yield scrapy.Request(link.url, callback=self.parse)
        #print(response.text)
        # with open("test.txt", "a") as myfile:
        #     myfile.write(response.text)
        #     myfile.write("\n----\n")
        #inspect_response(response, self)
        # content = response.xpath('string(//p)').extract()
        # yield content
        quote_item = DataItem.DataItem()
       
        for quote in response.css('div'):
            h1 = te = quote.css("h1::text").extract()
            h2 = te = quote.css("h2::text").extract()
            h3 = te = quote.css("h3::text").extract()

        #     quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            if len(h1) > 0:
                print(h1)
            # if len(h2) > 0:
            #     print(h2)
            #print(h2)
            #print(h3)
          
        for quote in response.css('p'):
            te = quote.css("p::text").extract()

            if len(te) > 0:
                print(te)
                
        yield quote_item
