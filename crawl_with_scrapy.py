import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    
    start_urls = ['https://example.com']  # Replace with the URL of the website you want to scrape
    
    def parse(self, response):
        # Example: titles = response.css('h2.title::text').extract()
        # Example: prices = response.xpath('//div[@class="price"]//text()').extract()

if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()

