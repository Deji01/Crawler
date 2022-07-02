# from datetime import datetime
# import time
import scrapy
from reedUk.items import ReedukItem
from scrapy.loader import ItemLoader


class ReedSpider(scrapy.Spider):
    name = "reed"
    allowed_domains = ["www.reed.co.uk/jobs/"]
    start_urls = [
        "https://www.reed.co.uk/jobs/work-from-home-jobs?pageno=1/",
        "https://www.reed.co.uk/jobs/work-from-home-jobs?pageno=2&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/work-from-home-jobs?pageno=3&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/work-from-home-jobs?pageno=4&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/work-from-home-jobs?pageno=5&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/work-from-home-jobs?pageno=6&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/work-from-home-jobs?pageno=2&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/part-time?pageno=2&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/part-time?pageno=3&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/part-time?pageno=4&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/part-time?pageno=5&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/part-time?pageno=6&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/part-time?pageno=2&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/part-time?pageno=1&sortby=DisplayDate",
        "https://www.reed.co.uk/jobs/immediate-start-jobs?pageno=1",
        "https://www.reed.co.uk/jobs/graduate-jobs?pageno=2",
        "https://www.reed.co.uk/jobs/graduate-jobs",
        "https://www.reed.co.uk/jobs/graduate-jobs",
        "https://www.reed.co.uk/jobs/graduate-jobs?pageno=3",
        "https://www.reed.co.uk/jobs/graduate-jobs?pageno=4",
        "https://www.reed.co.uk/jobs/graduate-jobs?pageno=5",
        "https://www.reed.co.uk/jobs/graduate-jobs?pageno=6",
        "https://www.reed.co.uk/jobs/graduate-jobs?pageno=3",
    ]

    def parse(self, response):
        for article in response.css("section.results article"):

            loader = ItemLoader(item=ReedukItem(), selector=article)

            loader.add_css(
                "job_title",
                "header.job-result-heading > h3.job-result-heading__title > a",
            )

            loader.add_css("company", "div.job-result-heading__posted-by > a")

            loader.add_css(
                "location",
                "ul.job-metadata > li.job-metadata__item.job-metadata__item--location",
            )

            loader.add_css("job_summary", "p.job-result-description__details")

            loader.add_css(
                "salary_range",
                "ul.job-metadata > li.job-metadata__item.job-metadata__item--salary",
            )

            loader.add_css("post_date", "div.job-result-heading__posted-by")

            loader.add_css(
                "job_type",
                "ul.job-metadata > li.job-metadata__item.job-metadata__item--type",
            )

            loader.add_css(
                "remote",
                "ul.job-metadata > li.job-metadata__item.job-metadata__item--remote",
            )

            loader.add_css(
                "url",
                "article.job-result-card > a::attr(href)",
            )

            yield loader.load_item()

            # today = datetime.today().strftime("%Y-%m-%d")
