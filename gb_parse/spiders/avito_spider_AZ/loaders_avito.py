from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from .xpath_selectors_avito import FLAT_DATA
from .processors import to_type, concatenate_items

class AvitoLoader(ItemLoader):
    default_item_class = dict
    item_type_out = TakeFirst()
    url_out = TakeFirst()
    title_out = TakeFirst()
    price_in = MapCompose(to_type(float))
    price_out = TakeFirst()
    address_out = TakeFirst()
    author_site_out = TakeFirst()
    developer_out = TakeFirst()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get("response"):
            self.add_value("url", self.context["response"].url)
        self.add_value("item_type", "real_estate")
        for key, selector in FLAT_DATA.items():
            self.add_xpath(key, **selector)
