import scrapy

class ArticleSpider(scrapy.Spider):
    name='article'

    def start_requests(self):
        urls = [
            "http://en.wikipedia.org/wiki/Python_%28programming_language%29",
            "https://en.wikipedia.org/wiki/Functional_programming",
            "https://en.wikipedia.org/wiki/Monty_Python"]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))

'''The name of this class (ArticleSpider) is different from the name of the directory
(wikiSpider), indicating that this class in particular is responsible for spidering
through only article pages, under the broader category of wikiSpider, which you may
later want to use to search for other page types.
For large sites with many types of content, you might have separate Scrapy items for
each type (blog posts, press releases, articles, etc.), each with different fields, but all
running under the same Scrapy project. The name of each spider must be unique
within the project.
The scraper goes to the three pages listed as the start_urls, gathers information, and
then terminates.
The spider in the isn’t much of a crawler, confined to scraping only the list of URLs it’s 
provided. It has no ability to seek new pages on its own. '''