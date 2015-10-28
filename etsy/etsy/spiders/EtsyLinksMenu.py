import scrapy
from scrapy.selector import HtmlXPathSelector
from etsy.items import EtsyItem

class EtsyLinksMenuSpider(scrapy.Spider):
	name = "EtsyLinksMenu"
	allowed_domains = ["etsy.com"]
	start_urls = ["https://www.etsy.com/es/"]

	def parse(self, response):
		print '---> CEDENA <---'
		items = []
		for sel in response.xpath("//ul/li"):
			titles = sel.xpath('a/text()').extract()
			links = sel.xpath('a/@href').extract()
			
			first_title = ''
			first_link = ''

			if(len(titles) > 0):
				first_title = titles[0]
				first_title = first_title.replace('\n', '').strip()

			if(len(links) > 0):
				first_link = links[0]

			if first_title and first_link:
				if '?ref=catnav-' in first_link:
					item = EtsyItem()
					item['title'] = first_title
					item['link'] = first_link
					items.append(item)
		return items
