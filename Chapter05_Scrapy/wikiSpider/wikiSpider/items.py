# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
'''To help organize all the information you’re collecting, you need to create an Article object. 
Replacing the default Item stub with a new Article class extending scrapy.Item'''

class Article(scrapy.Item):
    '''Defining three fields that will be collected from each page: a title, URL, and the date 
    the page was last edited. When collecting data for multiple page types, you should define 
    each separate type as its own class in items.py. If your items are large, or you start to 
    move more parsing functionality into your item objects, you may also wish to extract each 
    item into its own file.'''
    
    url = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    lastUpdated = scrapy.Field()

#Now go to the articleSpider.py file