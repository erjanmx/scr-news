# -*- coding: utf-8 -*-
from time import strftime
from base import BaseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class KnewsSpider(BaseSpider):
    name = 'knews'

    allowed_domains = ['knews.kg']
    start_urls = ['http://knews.kg/']

    rules = (
        Rule(LinkExtractor(allow=('http://knews.kg/{0}/*'.format(strftime('%Y/%m')))), callback="parse_articles", follow=True),
    )

    def extractTags(self, response):
        return []