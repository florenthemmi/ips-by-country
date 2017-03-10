import os
import shutil
import urllib.request

import scrapy

from config import RAW_DIRECTORY


class IPSpider(scrapy.Spider):
    name = 'ip'

    def start_requests(self):
        urls = ['http://www.nirsoft.net/countryip/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        countries = {}

        for link in response.css('table[width="650"] a'):
            country_code = link.css('::attr(href)').extract_first().split('.')[0]
            country_name = link.css('::text').extract_first().encode('utf-8')
            filename = '{}.csv'.format(country_code)
            url = 'http://www.nirsoft.net/countryip/{}.csv'.format(country_code)

            countries[country_code] = country_name

            with urllib.request.urlopen(url) as response, open(os.path.join(RAW_DIRECTORY, filename), 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
