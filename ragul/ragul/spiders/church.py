import scrapy
from ragul.items import InstItem


class ChurchSpider(scrapy.Spider):
    name = "church"
    allowed_domains = ["godsglory.church"]
    start_urls = ["https://godsglory.church/"]

    def parse(self, response):
        for link in response.css('.sidebar-block.typography a'):
            item = InstItem()
            item['username'] = link.css('::text').get()
            item['url'] = link.css('::attr(href)').get()
            yield item

