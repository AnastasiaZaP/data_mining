import os
import dotenv
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from gb_parse.spiders.autoyoula_spider_AZ.autoyoula import AutoyoulaSpider
from gb_parse.spiders.hh_spider_AZ.hh import HHSpider
from gb_parse.spiders.avito_spider_AZ.avito import AvitoSpider
from gb_parse.spiders.instagram_spider_AZ.instagram import InstagramSpider
from gb_parse.spiders.fraud_parse.fraud import FraudSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule('gb_parse.settings')
    crawler_process = CrawlerProcess(settings=crawler_settings)
    #crawler_process.crawl(AutoyoulaSpider)
    #crawler_process.crawl(HHSpider)
    #crawler_process.crawl(AvitoSpider)
    #crawler_process.crawl(InstagramSpider, login=os.getenv("LOGIN"), password=os.getenv("PASSWORD"), tags=["python"])
    crawler_process.crawl(FraudSpider)
    crawler_process.start()