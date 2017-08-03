# -*- coding: utf-8 -*-
from .base import BaseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class KaktusSpider(BaseSpider):
    name = 'kaktus'

    allowed_domains = ['kaktus.media']
    start_urls = ['http://kaktus.media/']

    rules = (
        Rule(LinkExtractor(allow=('http://kaktus.media/doc/*')), callback="parse_articles", follow=False),
    )

    def extractTags(self, response):
        return response.xpath('//div[@class="topic-tags"]/div/a/text()').extract()