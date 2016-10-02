# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesinconcertItem(scrapy.Item):
    city = scrapy.Field()
    country = scrapy.Field()
    date = scrapy.Field()
    link = scrapy.Field()
    state = scrapy.Field()
    title = scrapy.Field()
