# -*- coding: utf-8 -*-
import scrapy

# from scrapy.spiders import Request
# from scrapy.spiders import Spider
from qiubai.items import QiubaiItem
# import re
# import json
# import urllib


class Qiubai1Spider(scrapy.Spider):
    name = 'qiubai1'
    allowed_domains = ['www.qiushibaike.com']
    # host = ["http://www.qiushibaike.com"]
    start_urls = ['https://www.qiushibaike.com/text/',
                  'https://www.qiushibaike.com/',
                  'https://www.qiushibaike.com/hot/']
    # gender_strip_pattern = re.compile('articleGender|Icon')
    #
    def parse(self, response):
        item = QiubaiItem()

        item['name'] = response.xpath('//div[@class="author clearfix"]/a/h2/text()').extract()
        item['content'] = response.css("div.content span::text").extract()
        item['profile_link'] = response.xpath('//div[@class="author clearfix"]/a/@href').extract()
        item['avatar'] = response.xpath('//div[@class="author clearfix"]/a/img/@src').extract()
        item['age'] = response.xpath('//div[@class="author clearfix"]/div/text()').extract()
        item['content_link'] = response.xpath('//a[@class="contentHerf"]/@href').extract()
        item['up'] = response.xpath('//span[@class="stats-vote"]/i/text()').extract()
        item['comment_num'] = response.xpath('//span[@class="stats-comments"]/a/i/text()').extract()
        yield item


        # auther_div = content_div_list.xpath('./div[@class="author clearfix"')#用户信息框
        # # test_anonymous = auther_div.xpath('./a').extract()
        # # if test_anonymous:
        # item['profile_link'] = auther_div.xpath('./a/@href').extract_first()#用户个人主页链接
        # item['avatar'] = auther_div.xpath('./a[@rel]/img/@src').extract_first()
        # item['name'] = auther_div.xpath('.//h2/text()').extract()
        # # gender_text = auther_div.xpath('./div[contains(@class,"articleGender]/@class').extract_first()
        # # item['gender'] = self.gender_strip_pattern.sub(gender_text,'')
        # item['age'] = auther_div.xpath('./div[contains(@class,"articleGender]/text()').extract_first()
        # content_href_div = content_div_list.xpath('./a[@class="contentHerf"]')
        # item['content'] = content_href_div.xpath('./div[@class="conent"]/span/text()').extract_first()
        # item['content_link'] = content_href_div.xpath('./@href').extract_first()
        # stat_div = content_div_list.xpath('./div[@class="stats"]')
        # item['up'] = stat_div.xpath('./span[@class="stats-vote"]/i[@class="number"]/text()').extract_first()
        # comment_href = stat_div.xpath('./span[@class="stats-comments"]/a[@class="qiushi_comments"]')
        # item['comment_num'] = comment_href.xpath('./i[@class="number"]/text()').extract_first()

            # print(item)
        # next_page = content_left_div.xpath('./ul[@class="pagination"]/li[last()]/a/@href').extract_first()
        # if next_page:
        #     yield Request(next_page,callback=self.parse)
    #
    # def parse(self, response):
    #     # 实例化item
    #     item = QiubaiItem()
    #     #猎取数据
    #     biaotis = response.xpath("//div/h2/text()").extract()
    #     contents=response.css("div.content span::text").extract()
    #     item['biaoti'] = biaotis
    #     item['content']=contents
    #     yield item