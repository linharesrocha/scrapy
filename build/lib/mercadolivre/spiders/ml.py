import scrapy

search = input('Pesquisa:')

class MlSpider(scrapy.Spider):
    name = 'ml'
    start_urls = ['https://lista.mercadolivre.com.br/'+search]

    def parse(self, response):
        # lista dos produtos
        for produto in response.css('.andes-card--padding-default'):
            yield {
                'nome': produto.css('.ui-search-item__title::text').get(),
                'preco': produto.css('.ui-search-price--size-medium .ui-search-price__second-line .price-tag-fraction::text').get(),
                'preco-fracao':  produto.css('.ui-search-price--size-medium .ui-search-price__second-line .price-tag-cents::text').get(),
                'full': produto.css('.ui-search-item__group__element--shipping use::attr(href)').get(),
                'link-anuncio': produto.css('.ui-search-result__image a::attr(href)').get(),
            }