
from scrapy.item import Item, Field

class EtsyItem(Item):
    title = Field()
    link = Field()
