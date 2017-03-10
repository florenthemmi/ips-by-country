import json
import os

import scrapy


class CIDRSpider(scrapy.Spider):
    name = 'cidr'

    def start_requests(self):
        urls = ['http://www.subnet-calculator.com/cidr.php']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        cidr_max_subnets = {}

        for link in response.css('#cidr_max_subnets option'):
            cidr = int(link.css('::attr(value)').extract_first()) + 1
            max_subnets = link.css('::text').extract_first()

            cidr_max_subnets[max_subnets] = cidr

        print(json.dumps(cidr_max_subnets, indent=4))
