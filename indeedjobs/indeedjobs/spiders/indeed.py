import scrapy
# from datetime import datetime
from indeedjobs.items import IndeedjobsItem
from scrapy.loader import ItemLoader
from .test import location


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['uk.indeed.com', 'indeed.com']
    start_urls = [
        'https://uk.indeed.com/jobs?q=graduate&l=Newcastle%20upon%20Tyne%2C%20Tyne%20and%20Wear&start=10&vjk=7b5c6d959ed70987',
        'https://uk.indeed.com/jobs?q=graduate&l=London%2C%20Greater%20London&start=10&vjk=0fe9a7e476658f5c',
        'https://uk.indeed.com/jobs?q=data&l=United+Kingdom&start=10'
    ]
    links = location()
    for link in links:
        start_urls.append(link)
    # today = datetime.today().strftime('%Y-%m-%d')

    def parse(self, response):
        for card in response.css("div.job_seen_beacon "):
            loader = ItemLoader(item=IndeedjobsItem(), selector=card)

            loader.add_css("job_title", "h2.jobTitle > a > span")

            loader.add_css("company", "span.companyName")

            loader.add_css("location", "div.companyLocation")

            loader.add_css("job_summary", "tr.underShelfFooter > td > div > div > ul > li ")

            loader.add_css("post_date", "span.date")

            loader.add_css("salary_range", "div.attribute_snippet")

            loader.add_css("job_link", "a.jcs-JobTitle::attr(href)")

            yield loader.load_item()

        next_page = response.css(
            "ul.pagination-list > li:nth-child(7) > a::attr(href)").get()
        next_url = response.urljoin(next_page)
        if next_page is not None:
            yield response.follow(url=next_url, callback=self.parse)
