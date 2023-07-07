import scrapy


class PepParseItem(scrapy.Item):
    """Processes data received from the spider."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
