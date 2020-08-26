import scrapy
import calendar
import datetime

from scrapy.spiders import CrawlSpider
from ..items import IvivuItem

def get_total_date_month(year, month):
    now = datetime.datetime.now()
    total_date = calendar.monthrange(year, month)[1]

    if year == now.year and month == now.month and now.day < total_date:
        return now.day

    return total_date

class IvivuSpider(CrawlSpider):
    name = 'ivivu'
    allowed_domains = ['www.ivivu.com']

    start_urls = []

    for i in range(1, 851):
        start_urls.append('https://www.ivivu.com/blog/page/{0}'.format(i)) #2

    def parse(self, response):
        item = IvivuItem()
        tmp_data = {}
        data_resp = scrapy.Selector(response)

        data_list = data_resp.xpath("//div[@class='archive-postlist']/div[@class='one-half']")

        for data_item in  data_list:
            item['title'] = data_item.xpath("//article/header[@class='entry-header']/h2/a/text()").extract_first()
            item['image'] = data_item.xpath("//article/header[@class='entry-header']/h2/a/@href").extract_first()
            item['description'] = data_item.xpath("//article/div[@class='entry-excerpt']/p/text()").extract_first()
            item['date'] = data_item.xpath("//article/header[@class='entry-header']/div[@class='entry-meta']/span[@class='date']/text()").extract_first()
            item['view'] = data_item.xpath("//article/header[@class='entry-header']/div[@class='entry-meta']/span[@class='views']").extract_first()

        yield item
