# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XsktItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    xs_info = scrapy.Field()
    xs_data = scrapy.Field()


class ProductItem(scrapy.Item):
    product_image = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_price_old = scrapy.Field()
    product_rating = scrapy.Field()
    product_promo = scrapy.Field()
    product_info = scrapy.Field()
    product_discount = scrapy.Field()


class IvivuItem(scrapy.Item):

    # define the fields for your item here like:
     title = scrapy.Field()
     image = scrapy.Field()
     description = scrapy.Field()
     date = scrapy.Field()
     view = scrapy.Field()

class TravelItem(scrapy.Item):

    # define the fields for your item here like:
     origin_id = scrapy.Field()
     title = scrapy.Field()
     image = scrapy.Field()
     description = scrapy.Field()
     date = scrapy.Field()
     link = scrapy.Field()

