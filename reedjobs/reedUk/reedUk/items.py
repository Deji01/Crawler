# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class ReedukItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    def remove_space(value):
        return value.strip()

    def complete_url(value):
        return "https://www.reed.co.uk" + value

    def clean_money(value):
        return value.replace("\u00a3", "")

    def clean_summary(value):
        return value.replace("\u2019", "").replace("\u00a0", "")

    def clean_location(value):
        return value.replace("\r\n", "").strip()

    job_title = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space),
        output_processor=TakeFirst(),
    )

    company = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space),
        output_processor=TakeFirst(),
    )

    location = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space, clean_location),
        output_processor=TakeFirst(),
    )

    job_summary = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space, clean_summary),
        output_processor=TakeFirst(),
    )

    salary_range = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space, clean_money),
        output_processor=TakeFirst(),
    )

    post_date = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space),
        output_processor=TakeFirst(),
    )

    job_type = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space),
        output_processor=TakeFirst(),
    )

    remote = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space),
        output_processor=TakeFirst(),
    )

    url = scrapy.Field(
        input_processor=MapCompose(remove_tags, complete_url),
        output_processor=TakeFirst(),
    )
