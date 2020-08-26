import scrapy
import logging
from ..items import ProductItem #1
from scrapy.spiders import CrawlSpider
class CrawlerSpider(CrawlSpider):
    name = "thegioididong"
    allowed_domains = ["thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com/dtdd-samsung#i:1",
        "https://www.thegioididong.com/dtdd-oppo#i:1",
        "https://www.thegioididong.com/dtdd-xiaomi#i:1",
        "https://www.thegioididong.com/dtdd-vivo#i:1"
        "https://www.thegioididong.com/dtdd-vsmart#i:1",
        "https://www.thegioididong.com/dtdd-apple-iphone#i:1",

    ]

    def parse(self, response):

        products = response.css('.homeproduct li')

        for product in products:
            item = ProductItem()
            logging.info(product.css("a div.price::text"))
            item['product_image'] = product.css("a img::attr('data-original')").extract_first() if product.css("a img::attr('data-original')") else product.css("a img:first-child::attr('src')").extract_first()
            item['product_name'] = product.css("a h3::text").extract_first()
            item['product_price'] = product.css("a div.price strong::text").extract_first()
            item['product_price_old'] = product.css("a div.price span::text").extract_first()
            item['product_rating'] = product.css("a .ratingresult span::text").extract_first()
            item['product_promo'] = product.css("a .promo p::text").extract_first()
            item['product_info'] = ''.join(product.css("a .bginfo").extract()).strip()
            yield item