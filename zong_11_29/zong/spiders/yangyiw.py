# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
import win_unicode_console
win_unicode_console.enable()


class YangyiwSpider(scrapy.Spider):
    name = 'yangyiw'
    # allowed_domains = ['https://news.163.com/']
    # start_urls = ['http://temp.163.com/special/00804KVA/cm_guonei_03.js?callback=data_callback']
    #https://news.163.com/18/1126/19/E1IHK36M0001875N.html"
    #https://news.163.com/18/1126/19/E1IHG4NT0001875N.html"
    # rules = (
    #         Rule(LinkExtractor(allow=("http://temp.163.com/special/00804KVA/cm_guonei_03.js?callback=data_callback")),follow=True,callback='parse_item'),
    #         Rule(LinkExtractor(allow=("https://tech.163.com/\d{2}/\d{4}/\d{2}/\w{1}\d{1}\w{1}\d{2}\w{2}\d{6}\w{1}\d{2}.html")),follow=False)
    #
    # )

    def start_requests(self):
        url = "http://temp.163.com/special/00804KVA/cm_guonei_03.js?callback=data_callback"
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        link = re.findall('"docurl":"(.*?)"',response.text)
        for i in link:
            url = i
            print(i)
            yield scrapy.Request(url=url,callback=self.parse1)

    def parse1(self, response):
        #标题
        title = re.findall('<title>(.*?)</title>',response.text)
        print(title)
        #内容
        neirong = response.xpath("//div[@class='post_body']/div[@id='endText']/p/text()").extract()
        print(neirong)
        #时间
        data_time = response.xpath("//div[@id='epContentLeft']/div[@class='post_time_source']/text()").extract()
        print("时间",data_time)
        #来源
        laiyuan = response.xpath("//div[@class='post_time_source']/a[@id='ne_article_source']/text()").extract()
        print("来源：",laiyuan)
        #作者
        author = response.xpath("//div[@class='ep-source cDGray']/span[@class='ep-editor']/text()").extract()
        print("作者",author)
        #图片链接
        img_url = response.xpath("//div[@id='endText']/p[@class='f_center']/img/@src").extract()
        print("图片链接：",img_url)
        #关键字
        keyword = response.xpath('//meta[@name="keywords"]/@content').extract()
        print("关键字：",keyword)
        #导读
        # daodu = response.xpath('//meta[@name="description"/@content]').extract()
        # print("导读",daodu)


