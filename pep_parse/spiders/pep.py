import re
import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.css('section#numerical-index table a[href]')
        for pep_link in all_pep:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        name_number = response.css('h1.page-title::text').get()
        date = {
            'number': name_number.split()[1],
            'name': re.split(r'PEP \d+...', name_number)[1],
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(date)
