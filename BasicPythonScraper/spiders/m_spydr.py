import scrapy


class MainSpider(scrapy.Spider):
    name = "mainCrawl"
    UPC = 0
    start_urls = ['https://brickseek.com/products/?search='+str(UPC)]
    
    def parse(self, response):
        new_Link = response.xpath('//*[@id="main"]/div[2]/div[1]/div/div/a/@href').extract()
        yield scrapy.Request(new_Link, callback=self.item_page_parse)
        
    def item_page_parse(self, response):
        ItemName = response.xpath('//*[@id="main"]/div/div[1]/div[2]/h2//text()').extract()
        ItemMSRP = float(response.xpath('//*[@id="main"]/div/div[1]/div[2]/div[1]/div/div[2]//text()').extract())
        ItemStores = {}
        #Div for divs: '//*[@id="online-offers"]/div'
        #Div1 price: '//*[@id="online-offers"]/div/a[1]/span[1]'
        #Div1 name: '//*[@id="online-offers"]/div/a[1]/span[3]'
        #Div2 price: '//*[@id="online-offers"]/div/a[2]/span[1]'
        #Div2 name: '//*[@id="online-offers"]/div/a[2]/span[3]'

        with open('TempItemData.txt', 'wb') as f:
            f.write("Item Name: "+ItemName)
            f.write("Item MSRP: "+ItemMSRP)
            f.write("Availible Stores: ")
            for x,y in ItemStores.items():
                f.write(x+" with a price of : "+y)