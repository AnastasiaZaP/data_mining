import scrapy
from .xpath_selectors_avito import FLAT
from .loaders_avito import AvitoLoader


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ["avito.ru"]
    start_urls = ['https://www.avito.ru/moskva/nedvizhimost']


    def parse(self, response):
        yield response.follow(
            response.xpath("//a[@data-category-id='24'][@title='Все квартиры']/@href").get(),
            callback=self.flats_parse)

    def flats_parse(self, response, paginate=True):
        for url in response.xpath(FLAT["selector"]):
            yield response.follow(url, getattr(self, FLAT["callback"]))
        for page_num in range(2, 101) if paginate else []:
            yield response.follow(f"?p={page_num}", callback=self.flats_parse, cb_kwargs={"paginate": False})

    def one_flat_parse(self, response):
        loader = AvitoLoader(response=response)
        yield loader.load_item()

