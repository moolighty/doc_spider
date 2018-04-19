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
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Host': 'service.shanghai.gov.cn',
        'Referer': 'http://www.shanghai.gov.cn/nw2/nw2314/nw2319/nw12344/index.html',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': 'ASP.NET_SessionId=jebjcbwj1ewg5bkluq3a5j2s',
    }
    start_page = 1
    end_page = 1198;
    url = 'http://service.shanghai.gov.cn/pagemore/iframePagerIndex_12344_2_22.html?objtype=2&nodeid=12344&page={}&pagesize=22'

    def start_requests(self):
        for i in range(self.start_page, self.end_page + 1):
            url = self.url.format(i)
            yield Request(url, headers=self.headers)

    def parse(self, response):
        body = gbk2unicode(response.body)
        sl = Selector(text=body).css('ul.uli14.pageList li a')
        print(len(sl))
        for s in sl:
            href = s.xpath('@href').extract_first()
            url = response.urljoin(href)
            title = s.xpath('@title').extract_first()
            meta = {'title': title}
            yield Request(url, callback=self.parse_announcement, meta=meta)
    
    def parse_announcement(self, response):
        body = gbk2unicode(response.body)
        article = Selector(text=body).xpath('//*[@id="ivs_content"]').extract()
        print(article, response.url)
        
if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl shanghai'.split())