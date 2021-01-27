# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):#必须继承于scrapy.Spider
    name = 'demo'               #当前爬虫的名字叫demo
    #allowed_domains = ['python123.io'] #只能爬取这个域名下的链接
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):#解析页面 self:面向对象类所属关系的标记 response:存储返回对象
        fname=response.url.split('/')[-1]
        with open(fname,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.'%fname)
