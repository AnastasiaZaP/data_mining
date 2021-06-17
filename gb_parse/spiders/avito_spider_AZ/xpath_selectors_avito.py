FLAT = {
    'selector': '//div[@data-marker="catalog-serp"]//a[@data-marker="item-title"]/@href',
    'callback': 'one_flat_parse'
}

FLAT_DATA = {
    'title': {"xpath": '//div[@class="title-info-main"]//span[@itemprop="name"]/text()'},
    'price': {"xpath": '//span[@itemprop="price"]/@content'},
    'address': {"xpath": '//span[@class="item-address__string"]/text()'},
    'metro': {"xpath": '//span[@class="item-address-georeferences-item__content"]/text()'},
    'parameters': {"xpath": '//div[@class="item-params"]//li[@class="item-params-list-item"]//text()'},
    'developer': {"xpath": '//a[@class="item-params-link js-nd-house-complex-link"]/@href'}
}
