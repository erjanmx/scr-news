# -*- coding: utf-8 -*-
from record import Record
from scrapy.spiders import CrawlSpider

class BaseSpider(CrawlSpider):

    def parse_articles(self, response):
        r = Record(source=self.name, title=self.extractTitle(response), url=self.extractUrl(response))

        tags = self.extractTags(response)
        r.setTags(tags)

        if r.save():
            self.log('saved %s' % r.url)
        
    def extractUrl(self, response):
        return response.url

    def extractTitle(self, response):
        return response.css('title::text').extract_first()

