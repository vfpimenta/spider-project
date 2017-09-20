from scrapy import Spider
from kabum.items import KabumItem

class KabumSpider(Spider):
    name = 'kabum'
    start_urls = ['https://www.kabum.com.br/']

    def parse(self, response):
        for div in response.css('div.H-box'):
            item = KabumItem()

            item['name'] = div.css('div.padding-prime div.align-list div a span.H-titulo::text').extract_first()
            item['price'] = div.css('div.padding-prime div.preco_kabum div.H-preco::text').extract_first()

            yield item