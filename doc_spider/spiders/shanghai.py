# -*- coding: utf-8 -*-
import scrapy

from pprint import pprint
import cssselect
from scrapy import Request
from scrapy.http.response import Response
from scrapy.selector import Selector
from doc_spider.util.coding_conversion import gbk2utf8, gbk2unicode

class ShanghaiSpider(scrapy.Spider):
    name = 'shanghai'
    allowed_domains = ['www.shanghai.gov.cn']

    def start_requests(self):
        url = 'http://www.shanghai.gov.cn/nw2/nw2314/nw2319/nw12344/index.html'
        yield Request(url)

    def parse(self, response):
        body = gbk2unicode(response.body)
        sl = Selector(text=body).css('div#pageList ul.uli14.pageList li a')
        for s in sl:
            href = s.xpath('@href').extract_first()
            url = response.urljoin(href)
            title = s.xpath('@title').extract_first()
            meta = {'title': title}
            yield Request(url, callback=self.parse_announcement, meta=meta)
    
    def parse_announcement(self, response):
        body = gbk2unicode(response.body)
        print(response.meta['title'])
        
if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl shanghai'.split())