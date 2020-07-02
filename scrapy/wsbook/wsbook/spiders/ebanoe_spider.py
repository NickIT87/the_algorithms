import scrapy

class EbanoeSpider(scrapy.Spider):
    name = 'ebanoespider'
    start_urls = ['https://ebanoe.it/']

    def parse(self, response):
        yield print("PARSE")