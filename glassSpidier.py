import numpy as np
import pandas as pd
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'ctg'
    start_urls = ['https://www.cleaningtheglass.com/stats/']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)
EOF
 scrapy runspider myspider.py