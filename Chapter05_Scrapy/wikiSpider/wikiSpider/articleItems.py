from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
'''it will output the usual Scrapy debugging data along with each article item as a Python dictionary'''

class ArticleSpider(CrawlSpider):
    name = 'articleItems'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [
        Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'), callback='parse_items', follow=True),
    ]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
        return article
'''Scrapy uses the Item objects to determine which pieces of information it should save from the pages 
it visits. This information can be saved by Scrapy in a variety of ways, such as CSV, JSON, or XML 
files, using the following commands:
    $ scrapy runspider articleItems.py -o articles.csv -t csv 
    $ scrapy runspider articleItems.py -o articles.json -t json 
    $ scrapy runspider articleItems.py -o articles.xml -t xml 
Each of these runs the scraper articleItems and writes the output in the specified format to the 
provided file. This file will be created if it does not exist already. 

The text variable is a list of strings rather than a single string. Each string in this list 
represents text inside a single HTML element, whereas the content inside <div id="mwcontent-text">,
from which you are collecting the text data, is composed of many child elements. Scrapy manages 
these more complex values well. In the CSV format, for example, it converts lists to strings and 
escapes all commas so that a list of text displays in a single CSV cell. In XML, each element of 
this list is preserved inside child value tags. In the JSON format, lists are preserved as lists.'''
