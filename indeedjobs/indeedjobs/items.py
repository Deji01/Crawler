# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_space(value):
    return value.strip()


def clean_money(value):
    return value.replace('Â', '')


def complete_url(value):
    return 'https://uk.indeed.com' + value


class IndeedjobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_space), output_processor=TakeFirst())
    company = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_space), output_processor=TakeFirst())
    location = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_space), output_processor=TakeFirst())
    salary_range = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_space, clean_money), output_processor=TakeFirst())
    post_date = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_space), output_processor=TakeFirst())
    job_summary = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_space), output_processor=TakeFirst())
    job_link = scrapy.Field(input_processor=MapCompose(
        complete_url), output_processor=TakeFirst())
