import scrapy  # type: ignore


class CarSpider(scrapy.Spider):
    name = "car"
    start_urls = ['https://example-car-site.com']

    def parse(self, response):
        cars = response.css('div.car-item') # Assuming each car is in a `car-item` div.
        for car in cars:
            yield {
                'model': car.css('span.model::text').get(),
                'year': car.css('span.year::text').get(),
                # Fetch other details similarly
            }
        # Handle pagination
        next_page = response.css('li.next a::attr(href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

