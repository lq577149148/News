# -*- coding: utf-8 -*-
import scrapy,re,rules
import win_unicode_console
win_unicode_console.enable()
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
# from ..items import WurenjiItem

class WurenjiwSpider(CrawlSpider):
    name = 'wurenjiw'
    # allowed_domains = ['http://www.81uav.cn/uav-news/4.html']
    start_urls = ['http://www.81uav.cn/uav-news/4.html']
    rules = (
                Rule(LinkExtractor(allow='http://www.81uav.cn/uav-news/4_\d+.html'),follow=True),
                Rule(LinkExtractor(allow='http://www.81uav.cn/uav-news/\d{6}/\d{2}/\d+.html',restrict_css="div.news_left a"),callback='parse_item',follow=False),
             )
    # def start_requests(self):
    #     for i in range(1,10):
    #         url = 'http://www.81uav.cn/product/zhibaowurenji/0-0-0-'+str(i)+'-0.html'
    #         yield scrapy.Request(url=url,callback=self.parse)

    def parse_item(self, response):
        # item = WurenjiItem()
        print(response.url)
        sel = Selector(response)
        #详情页文章标题
        if sel.xpath('//h1/text()').extract_first():
            title = ''.join(sel.xpath('//h1/text()').extract_first())
            # print(type(title),'===')
            # print(title)
        else:
            title = "没有"
            print(title,response.url)
        # 详情页文章内容
        if sel.css("div.info::text").re("\d{4}-\d{2}-\d{2}")[0]:
            data_time = ''.join(sel.css("div.info::text").re("\d{4}-\d{2}-\d{2}"))
            # print(type(data_time),'****')
            print(data_time)

        else:
            data_time = "没有"
            print(data_time, response.url)
        # 详情页内容
        if sel.xpath("//div[@id='content']/div[@id='article']/p/text()").extract():
            neirong = ';'.join(sel.xpath("//div[@id='content']/div[@id='article']/p/text()").extract())
            # print(type(neirong),'-----')
            # print(neirong)
        else:
            neirong = "没有"
            print(neirong,response.url)
        # 详情页的图片url
        if sel.xpath("//div[@id='content']/div[@id='article']/p/img/@src").extract():
            img_url = ';'.join(sel.xpath("//div[@id='content']/div[@id='article']/p/img/@src").extract())
            # print(type(img_url),'+++')
            # print(img_url)
        else:
            img_url = "没有"
            print(img_url,response.url)
        # item['title'] = title
        # item['data_time'] = data_time
        # item['neirong'] = neirong
        # item['img_url'] = img_url
        # return item















        # print(self.rules,'=============================')
        # name = response.xpath("//div[@class='qc-body']/dl/ul/li/p/a/text()").extract()
        # print(name)
        # title = re.findall('<title>(.*?)</title>', response.text)
        # print(title)
        # link = response.xpath("//div/dl/ul/li/p/a/@href").extract()
        # for i in link:
        #     urls = i
        #     yield scrapy.Request(url=urls,callback=self.parse1)

    # def parse1(self ,response):
    #     title = re.findall('<title>(.*?)</title>',response.text)
    #     price = re.findall('<font>(.*?)</font>',response.text)
    #     print(title)
    #     print(price)
