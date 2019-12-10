import scrapy
import logging
from ..items import ProductItem #1
from scrapy.spiders import CrawlSpider
class CrawlerSpider(CrawlSpider):
    name = "abc"
    allowed_domains = ["thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com/dtdd-samsung",
    ]

    def parse(self, response):

        products = response.css('.homeproduct li')

        for product in products:

            item = ProductItem()
            logging.info(product.css("a div.price::text"))
            item['product_image'] = product.css("a img::attr('src')").extract_first()
            item['product_name'] = product.css("a h3::text").extract_first()
            item['product_price'] = product.css("a div.price strong::text").extract_first()
            item['product_price_old'] = product.css("a img::attr('src')").extract_first()
            item['product_rating'] = product.css("a img::attr('src')").extract_first()
            item['product_promo'] = product.css("a img::attr('src')").extract_first()
            item['product_info'] = product.css("a img::attr('src')").extract_first()
            yield item