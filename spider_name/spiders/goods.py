from scrapy import Spider, Request
from spider_name.items import Item
from datetime import datetime, timezone


class GoodsSpider(Spider):
    """Класс, отвечающий за парсинг HTML страниц"""

    name = "goods"

    def start_requests(self):
        urls = [
            "https://alkoteka.com/catalog/slaboalkogolnye-napitki-2",
            "https://alkoteka.com/catalog/produkty-1/options-categories_sneki",
            "https://alkoteka.com/catalog/produkty-1/options-categories_konfety-v-korobkakh",
        ]
        return [Request(url=url, callback=self.parse_items) for url in urls]

    def parse_items(self, response):
        item = Item()

        item["timestamp"] = datetime.now(timezone.utc)
        item["RPC"] = response.css("div.rpc::text").get()
        item["url"] = response.url
        item["title"] = response.css("h1::text").get()
        item["marketing_tags"] = response.css("div.marketing_tags::text").get()
        item["brand"] = response.css("div.brand::text").get()
        item["section"] = response.css("div.section::text").get()
        item["price_data"] = self.get_price_data(response)
        item["stock"] = self.get_stock(response)
        item["assets"] = self.get_assets(response)
        item["metadata"] = self.get_metadata(response)
        item["variants"] = self.get_variants(response)

        yield item

    def get_price_data(self, response):
        """Оформление вложенной категории 'price_data'"""
        current_price = response.css("div.current_price::text").get()
        original_price = response.css("div.original_price::text").get()
        sale_tag = response.css("div.sale_tag::text").get()

        return {
            "current": current_price,
            "original": original_price,
            "sale_tag": sale_tag,
        }

    def get_stock(self, response):
        """Оформление вложенной категории 'stock'"""
        in_stock = True if response.css("div.in_stock::text").get() else None
        count = response.css("div.count::text").get()

        return {
            "in_stock": in_stock,
            "count": count,
        }

    def get_assets(self, response):
        """Оформление вложенной категории 'assets'"""
        main_image = response.css("div.image::attr(src)").get()
        set_images = response.css("div.images::attr(src)").getall()
        view360 = response.css("div.view360::attr(src)").get()
        video = response.css("div.video::attr(src)").get()

        return {
            "main_image": main_image,
            "set_images": set_images,
            "view360": view360,
            "video": video,
        }

    def get_metadata(self, response):
        """Оформление вложенной категории 'metadata'"""
        metadata = dict()
        metadata["__description"] = response.css("div.description::attr(src)").get()
        metadata["color"] = response.css("div.description::text").get()
        metadata["volume"] = response.css("div.volume::text").get()
        metadata["supplier"] = response.css("div.supplier::text").get()
        return metadata

    def get_variants(self, response):
        """Оформление вложенной категории 'variants'"""
        return response.css("div.variants::text").get()
