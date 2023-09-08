import scrapy  # type: ignore


class CarSpider(scrapy.Spider):
    name = "car"
    start_urls = ['https://example-car-site.com']

    def parse(self, response):
        # Extract data logic
        yield {
            'model': response.css('div.model::text').get(),
            # Add other fields similarity
        }
