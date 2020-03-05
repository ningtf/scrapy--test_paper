# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperSeniorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    subject = scrapy.Field()
    grade = scrapy.Field()
    paper_name = scrapy.Field()
    down = scrapy.Field()
    down_content = scrapy.Field()