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
        pages = response.css('div.listagem-box div.listagem-titulo_descr span.H-titulo a')

        for page in pages:
            yield response.follow(page, callback=self.parse_item)
            '''
            item = KabumItem()
            item['name'] = div.css('div.listagem-titulo_descr span.H-titulo a::text').extract_first()
            raw_price = div.css('div.listagem-precos div.listagem-preco::text').re(r'\d+\,\d+')
            if  len(raw_price) > 0:
                item['price'] = float(raw_price[0].replace(',','.'))
            else:
                item['price'] = 0.0
            item['category'] = response.url.split('/')[-1]
            yield item
            '''

        next_page_container = response.css('div.listagem-paginacao')[0].css('form table tr td')[6].css('a')
        if len(next_page_container) > 0:
            yield response.follow(next_page_container[0], callback=self.parse_sub)

    def parse_item(self, response):
        item = KabumItem()
            
        item['name'] = response.css('div#titulo_det h1.titulo_det::text').extract_first()

        raw_price = response.css('span.preco_desconto span span strong').re(r'\d*\.*\d+\,\d+')
        if len(raw_price) > 0:
            item['price'] = float(raw_price[0].replace('.','').replace(',','.'))
        else:
            item['price'] = 0.0

        item['category'] = response.css('h2.h2titcategoria::text').extract_first()

        yield item