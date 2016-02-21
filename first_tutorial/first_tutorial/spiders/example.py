# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.cnn.com"]
    start_urls = (
        'http://www.www.cnn.com/',
    )

    def parse(self, response):
        pass
