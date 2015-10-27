from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from etsy.items import EtsyItem

class EtsyLinksMenuSpider(BaseSpider):
	name = "EtsyLinksMenu"
	allowed_domains = ["etsy.com"]
	start_urls = ["https://www.etsy.com/es/"]

	def parse(self, response):
		print '---> CEDENA <---'
		items = []
		for sel in response.xpath("//ul/li"):
			item = EtsyItem()
			item["title"] = sel.xpath('a/text()').extract()
			item["link"] = sel.xpath('a/@href').extract()

			tam_list = len(item['link'])
			if(tam_list >= 1):
				rel_url = item.get('link')[0]
				if "?ref=catnav-" in rel_url:
					items.append(item)
		return items