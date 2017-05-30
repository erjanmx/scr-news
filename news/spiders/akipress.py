# -*- coding: utf-8 -*-
import re
from base import BaseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class AkipressSpider(BaseSpider):
    name = 'akipress'

    allowed_domains = ['kg.akipress.org']
    start_urls = ['http://kg.akipress.org/']

    rules = (
        Rule(LinkExtractor(allow=('http://kg.akipress.org/news:[\d]+$')), callback="parse_articles", follow=True),
    )

    def extractTags(self, response):
        return [t[1:] for t in response.xpath('//div[@class="news_tag"]/a/text()').extract()]

    def extractTitle(self, response):
        return response.css('title::text').re(r'(.*) - Новости из Кыргызстана.*')
