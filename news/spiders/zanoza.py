# -*- coding: utf-8 -*-
from .base import BaseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class ZanozaSpider(BaseSpider):
    name = 'zanoza'

    allowed_domains = ['kaktus.media']
    start_urls = ['https://kaktus.media/']

    rules = (
        Rule(LinkExtractor(allow=('https://kaktus.media/doc/*')), callback="parse_articles", follow=False),
    )

    def extractTags(self, response):
        return response.xpath('//div[@class="topic-tags"]/div/a/text()').extract()