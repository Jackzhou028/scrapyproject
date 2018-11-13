# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import datetime
import re
import scrapy
from scrapy.loader import  ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst,Join
from settings import SQL_DATETIME_FORMAT,SQL_DATE_FORMAT
from w3lib.html import remove_tags



class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
def add_jobbole(value):
    return value+"-bobby"
def data_convert(value):
    try:
        create_data=datetime.datetime.strftime(value,"%Y/%m/%d").date()
    except Exception as e:
        create_data = datetime.datetime.now().date()
    return create_data


