import scrapy


class DataItem(scrapy.Item):
    text = scrapy.Field()
    # def __init__(self):
    #     self.fields = []
