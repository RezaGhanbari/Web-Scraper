# coding=utf-8
# writing a spider is specific to a web page.
# This won’t work on Group on or another website.
from scrapy.spider import BaseSpider

from scraper_app.items import LivingSocialDeal


class LivingSocialSpider(BaseSpider):
    """Spider for regularly updated livingsocial.com site, San Francisco Page"""
    name = "livingsocial"
    allowed_domains = ['livingsocial.com']
    