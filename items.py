# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    avatar = scrapy.Field()#头像
    profile_link = scrapy.Field()#个人主页链接
    name = scrapy.Field()#昵称
    # gender = scrapy.Field()#性别
    age = scrapy.Field()#年龄
    content = scrapy.Field()#笑话内容
    content_link = scrapy.Field()#笑话页面链接
    up = scrapy.Field()#点赞数
    comment_num = scrapy.Field()#评论数
    pass


