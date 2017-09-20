from scrapy import Spider
from kabum.items import KabumItem

class KabumSpider(Spider):
    name = 'kabum'
    start_urls = ['https://www.kabum.com.br/']

    def parse(self, response):
        pages = response.css('div.texto_categoria p.bot-categoria a')

        for page in pages:
            yield response.follow(page, callback=self.parse_sub)

    def parse_sub(self, response):
        elements = response.css('div.listagem-box')

        for div in elements:
            item = KabumItem()

            item['name'] = div.css('div.listagem-titulo_descr span.H-titulo a::text').extract_first()
            item['price'] = div.css('div.listagem-precos div.listagem-preco::text').extract_first()
            item['category'] = response.url.split('/')[-1]

            yield item

        next_page_container = response.css('div.listagem-paginacao')[0].css('form table tr td')[6].css('a')
        if len(next_page_container) > 0:
            yield response.follow(next_page_container[0], callback=self.parse_sub)