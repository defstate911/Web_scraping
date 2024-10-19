# import scrapy
#
#
# class DivannewparsSpider(scrapy.Spider):
#     name = "divannewpars"
#     allowed_domains = ["divan.ru"]
#     start_urls = ["https://www.divan.ru/category/divany-i-kreslap"]
#
#     def parse(self, response):
#         divans = response.css('div._Ud0k')
#         for divan in divans:
#             yield {
#                 'name': divan.css('div.lsooF span::text').get(),
#                 'price': divan.css('div.pY3d2 span::text').get(),
#                 'url': divan.css('a').attrib['href'],
#             }
import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    # Добавляем заголовки для имитации браузера
    custom_settings = {
        'ROBOTSTXT_OBEY': False,  # Игнорируем robots.txt
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }
    }

    def parse(self, response):
        # Проверьте актуальные селекторы в DevTools браузера
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                'url': divan.css('a').attrib['href'],
            }

