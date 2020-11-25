import scrapy
import calendar
import datetime
import re
from scrapy.spiders import CrawlSpider
from ..items import TravelItem


class TravelItemSpider(CrawlSpider):
    name = 'vietnamtourism-item'
    allowed_domains = ['vietnamtourism.gov.vn']

    def start_requests(self):
        start_urls = []
        for i in range(0, 28):
            file = open("../../vnat1json")
            start_urls = [url.strip() for url in file.readlines()]
            file.close()
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        tmp_data = {}
        data_resp = scrapy.Selector(response)

        data_list = data_resp.xpath("//div[@class='cat-block-inner-content']/div")

        for data_item in data_list:
            item = TravelItem()
            item['image'] = data_item.xpath("//div[@class='block-item-image-wrapper image-wrapper']/div/@data-src").extract_first()
            item['title'] = data_item.xpath("//div[@class='block-item-title-wrapper']/a/@title").extract_first()
            item['description'] = data_item.xpath("//div[@class='block-item-summary']/text()").extract_first()
            date = data_item.xpath("//div[@class='block-item-title-wrapper']/a/span/text()").extract_first()
            item['date'] = re.sub('[()]', "", date)
            # item['view'] = data_item.xpath("article/header[@class='entry-header']/div[@class='entry-meta']/span[@class='views']").extract_first()

            yield item
