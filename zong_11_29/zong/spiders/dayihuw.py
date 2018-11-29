# -*- coding: utf-8 -*-
import scrapy
import win_unicode_console
win_unicode_console.enable()
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor


class DayinhuwSpider(CrawlSpider):
    name = 'dayinhuw'
    # allowed_domains = ['http://www.dayinhu.com/news/category/']
    start_urls = ['http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF/page/1']
    rules = (
            Rule(LinkExtractor(allow='http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF/page/1'),follow=True),
            Rule(LinkExtractor(allow='http://www.dayinhu.com/news/\d{6}.html',restrict_css='h1.entry-titl e a'),follow=False,callback='parse_item'),


    )


    def parse_item(self, response):
        sel = Selector(response)
        try:
            if sel.xpath("//header[@class='entry-header']/h1[@class='entry-title']/text()").extract_first():
                title = sel.xpath("//header[@class='entry-header']/h1[@class='entry-title']/text()").extract_first()
                print(title)
            else:
                raise Exception("没有标题")

            if sel.xpath("//footer[@class='entry-meta']/a[1]/time[@class='entry-date']/text()").extract_first():
                data_time = sel.xpath("//footer[@class='entry-meta']/a[1]/time[@class='entry-date']/text()").extract_first()
                print(data_time)
            else:
                raise Exception("没有时间")

            if sel.xpath("//div[@class='entry-content']/p/text()").extract():
                neirong = sel.xpath("//div[@class='entry-content']/p/text()").extract()
                print(neirong)
            else:
                neirong = "没有内容"
                print(neirong)

            if sel.xpath("//div[@class='entry-content']/p[1]/text()").extract():
                daodu = sel.xpath("//div[@class='entry-content']/p[1]/text()").extract()
                print(daodu)
            else:
                daodu = "没有导读"
                print(daodu)

            if sel.xpath("//p/img[@class='aligncenter size-full wp-image-1142']/@src").extract():
                img_url = sel.xpath("//p/img[@class='aligncenter size-full wp-image-1142']/@src").extract()
                print(img_url)
            else:
                img_url = "没有图片"
                print(img_url)

            if sel.xpath('//head/meta[@name="keywords"]/@content').extract_first():
                biaoqian = sel.xpath('//head/meta[@name="keywords"]/@content').extract_first()
                print(biaoqian)
            else:
                biaoqian = "没有标签"
                print(biaoqian)
        except:
            pass

        # print(response.url,'===========')
