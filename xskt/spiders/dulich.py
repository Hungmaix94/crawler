import scrapy
import calendar
import datetime

from scrapy.spiders import CrawlSpider
from ..items import IvivuItem


class IvivuSpider(CrawlSpider):
    name = 'ivivu'
    allowed_domains = ['www.ivivu.com']

    def start_requests(self):
        start_urls = []
        for i in range(580, 851):
            start_urls.append('https://www.ivivu.com/blog/page/{0}'.format(i))  # 2
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        tmp_data = {}
        data_resp = scrapy.Selector(response)

        data_list = data_resp.xpath("//div[@class='archive-postlist']/div")

        for data_item in data_list:

            item = IvivuItem()
            item['title'] = data_item.xpath("article/header[@class='entry-header']/h2/a/text()").extract_first()
            item['image'] = data_item.xpath("article/header[@class='entry-header']/h2/a/@href").extract_first()
            item['description'] = data_item.xpath("article/div[@class='entry-excerpt']/p/text()").extract_first()
            item['date'] = data_item.xpath("article/header[@class='entry-header']/div[@class='entry-meta']/span[@class='date']/text()").extract_first()
            item['view'] = data_item.xpath("article/header[@class='entry-header']/div[@class='entry-meta']/span[@class='views']").extract_first()

            yield item
