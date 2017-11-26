# -*- coding: utf-8 -*-
from time import strftime
from .base import BaseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class KnewsSpider(BaseSpider):
    name = 'knews'

    allowed_domains = ['knews.kg']
    start_urls = ['http://knews.kg/{0}/'.format(strftime('%Y/%m/%d'))]

    rules = (
        # Rule(LinkExtractor(allow=('http://knews.kg/{0}/*'.format(strftime('%Y/%m'))), deny=('http://knews.kg/{0}/'.format(strftime('%Y/%m/%d')))), callback="parse_articles", follow=False),
        Rule(LinkExtractor(allow=('http://knews.kg/{0}/*'.format(strftime('%Y/%m')))), callback="parse_articles", follow=False),
    )

    def extractTags(self, response):
        return []