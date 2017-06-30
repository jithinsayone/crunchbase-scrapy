import scrapy,os


class CrunchSpider(scrapy.Spider):
    name = "crunch"

    def start_requests(self):
        urls = [
            'https://www.crunchbase.com/app/search/companies',
            ]
        yield scrapy.Requests(urls[0])

    def parse(self, response):
        print response.body
