# -*- coding: utf-8 -*-
from base import BaseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class ZanozaSpider(BaseSpider):
    name = 'zanoza'

    allowed_domains = ['zanoza.kg']
    start_urls = ['http://zanoza.kg/']

    rules = (
        Rule(LinkExtractor(allow=('http://zanoza.kg/doc/*')), callback="parse_articles", follow=True),
    )

    def extractTags(self, response):
        return response.xpath('//div[@class="topic-tags"]/div/a/text()').extract()