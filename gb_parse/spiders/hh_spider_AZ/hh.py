import scrapy
from .xpath_selectors_hh import VACANCY, PAGINATION,  VACANCY_DATA, COMPANY, COMPANY_DATA
from .loaders_hh import VacancyLoader, CompanyLoader

class HHSpider(scrapy.Spider):
    name = 'hh'
    allowed_domains = ["hh.ru", "*.hh.ru"]
    start_urls = ['https://hh.ru/search/vacancy?resume=ae049b01ff088399bc0039ed1f46516174656f&from=resumelist']

    def _get_follow(self, response, selector_str, callback):
        for a_link in response.xpath(selector_str):
            yield response.follow(a_link, callback=callback)

    def parse(self, response):
        for item in (PAGINATION, VACANCY):
            yield from self._get_follow(response, item["selector"], getattr(self, item["callback"]))

    def vacancy_parse(self, response):
        loader = VacancyLoader(response=response)
        loader.add_value('url', response.url)
        for key, selector in VACANCY_DATA.items():
            loader.add_xpath(key, **selector)
            data = loader.load_item()
        yield response.follow(data["author"], callback=self.company_parse)
        yield data

    def company_parse(self, response):
        loader = CompanyLoader(response=response)
        loader.add_value('url', response.url)
        for key, selector in COMPANY_DATA.items():
            loader.add_xpath(key, **selector)
        yield loader.load_item()

