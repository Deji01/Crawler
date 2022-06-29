import scrapy
from datetime import datetime

class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['www.indeed.com']
    start_urls = ['https://uk.indeed.com/jobs?q=graduate&l=London%2C%20Greater%20London&start=10&vjk=0fe9a7e476658f5c']

    def parse(self, response):
        cards = response.css("div.job_seen_beacon ")
        for card in cards:
            atag = card.css("h2.a")
            job_title = atag.css("::text").get()
            job_link = "https://uk.indeed.com" + atag.css("attr(href)").get()  
            today = datetime.today().strftime('%Y-%m-%d')
            company = card.css("span > companyName::text").get()
            company_location = card.css("div#companyLocation::text").get()
            job_summary = card.css("div > job-snippet::text").strip().replace('\n','')
            post_date = card.css("span > date::text").get().replace('Posted','')

        try:
            salary_range = card.css("div > attribute_snippet::text").get()
        except AttributeError:
            salary_range = ""

        record = {
            "job_title":job_title,
            "company":company,
            "company_location":company_location,
            "salary_range":salary_range,
            "post_date":post_date,
            "today":today,
            "job_link":job_link,
            "job_summary":job_summary,
        }
        yield record
