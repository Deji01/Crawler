# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class ReedukPipeline:
    def __init__(self):
        self.con = sqlite3.connect("reedjobs.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS reedjobs(
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT,
            company TEXT,
            location TEXT,
            job_summary TEXT,
            salary_range TEXT,
            post_date TEXT,
            job_type TEXT,
            remote TEXT,
            url TEXT)
            """
        )

    def process_item(self, item, spider):
        self.cur.execute(
            """INSERT OR IGNORE INTO PRODUCTS(?,?,?)""",
            (
                item["job_title"],
                item["company"],
                item["location"],
                item["job_summary"],
                item["salary_range"],
                item["post_date"],
                item["job_type"],
                item["remote"],
                item["url"],
            ),
        )
        self.con.commit()
        return item
