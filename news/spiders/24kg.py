# -*- coding: utf-8 -*-
from time import strftime
from .base import BaseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class TfSpider(BaseSpider):
    name = 'twentyfour'

    allowed_domains = ['24.kg']
    start_urls = ['https://24.kg/obschestvo/']

    rules = (
        Rule(LinkExtractor(allow=('https://24.kg/obschestvo/*')), callback="parse_articles", follow=False),
        # Rule(LinkExtractor(allow=('https://24.kg/*')), callback="parse_articles", follow=False),
    )

    def extractTags(self, response):
        return []

    def extractTitle(self, response):
        title = str(response.css('title::text').extract_first())
        pos = title.find(' » Общество')
        if pos > 0:
            title = title[:pos]

        return title
