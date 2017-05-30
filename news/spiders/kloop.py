# -*- coding: utf-8 -*-
from time import strftime
from base import BaseSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class KloopSpider(BaseSpider):
    name = 'kloop'

    allowed_domains = ['kloop.kg']
    start_urls = ['https://kloop.kg/']

    rules = (
        Rule(LinkExtractor(allow=('https://kloop.kg/blog/{0}/*'.format(strftime('%Y/%m/%d')))), callback="parse_articles", follow=True),
    )

    def extractTags(self, response):
        return response.xpath('//div[@class="td-post-source-tags"]/ul/li/a/text()').extract()