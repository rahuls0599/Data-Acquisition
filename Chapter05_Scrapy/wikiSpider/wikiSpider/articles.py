from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    '''This new ArticleSpider extends the CrawlSpider class. Rather than providing a
    start_requests function, it provides a list of start_urls and allowed_domains.
    This tells the spider where to start crawling from and whether it should follow or
    ignore a link based on the domain.
    
    A list of rules is also provided. This provides further instructions on which links to
    follow or ignore (in this case, you are allowing all URLs with the regular expression (.*)
    
    Instead of just visiting article pages on Wikipedia, it’s free to roam to nonarticle 
    pages as well
    '''
    
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]
    '''This line provides a list of Scrapy Rule objects that define the rules that all links
    found are filtered through. When multiple rules are in place, each link is checked against
    the rules in order. The first rule that matches is the one that is used to determine how 
    the link is handled. If the link doesn’t match any rules, it is ignored. '''

    def parse_items(self, response):
        '''In addition to extracting the title and URL on each page, a couple of new items have
    been added. The text content of each page is extracted using an XPath selector. XPath
    is often used when retrieving text content including text in child tags (for example, an
    <a> tag inside a block of text). If you use the CSS selector to do this, all text within
    child tags will be ignored.

    The last updated date string is also parsed from the page footer and stored in the
    lastUpdated variable.'''
        
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated = lastUpdated.replace('This page was last edited on ', '')
        print('URL is: {}'.format(url))
        print('title is: {} '.format(title))
        print('text is: {}'.format(text))
        print('Last updated: {}'.format(lastUpdated))
