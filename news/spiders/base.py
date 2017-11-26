# -*- coding: utf-8 -*-
import requests
from ..models.record import Record
from scrapy.spiders import CrawlSpider

class BaseSpider(CrawlSpider):
    response = None

    def parse_articles(self, response):
        self.response = response
        print(response)
        r = Record(source=self.name, title=self.extractTitle(response), url=self.extractUrl(response))
        r.description = self.extract_description()
        r.media_image = self.extract_media()
        r.content = self.extract_content()
        tags = self.extractTags(response)
        r.setTags(tags)

        if r.save():
            self.log('saved %s' % r.url)

    def extractUrl(self, response):
        return response.url

    def extractTitle(self, response):
        return response.css('title::text').extract_first()

    def extract_description(self):
        return self.response.xpath("//meta[@property='og:description']/@content").extract_first()

    def extract_media(self):
        return self.response.xpath("//meta[@property='og:image']/@content").extract_first()

    def extract_content(self):
        return self.response.body