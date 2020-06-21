from datetime import datetime
from wikiSpider.items import Article
from string import whitespace
'''to tie the settings.py file and the updated spider together by adding the pipeline.
'''

class WikispiderPipeline(object):
    '''The class WikispiderPipeline has a method process_item that takes in an Article
    object, parses the lastUpdated string into a Python datetime object, and cleans 
    and joins the text into a single string from a list of strings. process_item is 
    a mandatory method for every pipeline class. Scrapy uses this method to 
    asynchronously pass Items that are collected by the spider. The parsed Article 
    object that is returned here will be logged or printed by Scrapy if, for example,
    you are outputting items to JSON or CSV as was done in the previous section. You
    now have two choices when it comes to deciding where to do your data processing: 
    the parse_items method in the spider, or the process_items method in the pipeline.'''
    
    def process_item(self, article, spider):
        article['lastUpdated'] = article['lastUpdated'].replace('This page was last edited on', '')
        article['lastUpdated'] = article['lastUpdated'].strip()
        article['lastUpdated'] = datetime.strptime(article['lastUpdated'], '%d %B %Y, at %H:%M.')
        article['text'] = [line for line in article['text'] if line not in whitespace]
        article['text'] = ''.join(article['text'])
        return article
