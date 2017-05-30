# -*- coding: utf-8 -*-
from time import strftime
from base import BaseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class TfSpider(BaseSpider):
    name = 'twentyfour'

    allowed_domains = ['24.kg']
    start_urls = ['https://24.kg/obschestvo']

    rules = (
        Rule(LinkExtractor(allow=('https://24.kg/obschestvo/*')), callback="parse_articles", follow=True),
    )

    def extractTags(self, response):
        return []

    def extractTitle(self, response):
        return response.css('title::text').re(r'(.*) » Общество.*')
