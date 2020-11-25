import scrapy
import calendar
import datetime
import re
from scrapy.spiders import CrawlSpider
from ..items import TravelItem


class TravelSpider(CrawlSpider):
    name = 'vietnamtourism.gov.vn'
    allowed_domains = ['vietnamtourism.gov.vn']

    def start_requests(self):
        start_urls = []
        for i in range(1, 28):
            start_urls.append('http://vietnamtourism.gov.vn/english/index.php/cat/62/{0}'.format(i))  # 2
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)
        tmp_data = {}
        data_resp = scrapy.Selector(response)

        data_list = data_resp.xpath("//div[@class='cat-block-inner-content']/div[@class='row']/div")

        # only get 20 item
        for data_item in data_list:
            item = TravelItem()
            link = data_item.xpath("//div[@class='block-item-title-wrapper']/a/@href").extract_first()
            item['origin_id'] = re.sub('[^\d]',"", link)
            item['link'] = link
            item['image'] = data_item.xpath("//div[@class='block-item-image-wrapper image-wrapper']/div/@data-src").extract_first()
            item['title'] = data_item.xpath("//div[@class='block-item-title-wrapper']/a/@title").extract_first()
            item['description'] = data_item.xpath("//div[@class='block-item-summary']/text()").extract_first()
            date = data_item.xpath("//div[@class='block-item-title-wrapper']/a/span/text()").extract_first()
            item['date'] = re.sub('[()]', "", date)
            # item['view'] = data_item.xpath("article/header[@class='entry-header']/div[@class='entry-meta']/span[@class='views']").extract_first()

            yield item
