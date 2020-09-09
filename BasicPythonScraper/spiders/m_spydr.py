import scrapy

def MainSpiderGen(upc):
    #Create and return a spider class usin the UPC
    class MainSpider(scrapy.Spider):
        name = "mainCrawl"
        UPC = '095385791568'
        start_urls = ['https://brickseek.com/products/?search='+str(UPC)]
        
        def parse(self, response):
            #Retrive the HTML of the search page for the item, and follow the first item link
            new_Link = response.xpath('//*[@id="main"]/div[2]/div[1]/div/div/a/@href').extract()
            yield scrapy.Request(new_Link, callback=self.item_page_parse)
            
        def item_page_parse(self, response):
            #Retrive the items attributes from the items page
            ItemName = response.xpath('//*[@id="main"]/div/div[1]/div[2]/h2/text()').extract()
            ItemMSRP = float(response.xpath('//*[@id="main"]/div/div[1]/div[2]/div[1]/div/div[2]/text()').extract())
            ItemStores = {}
            i = 1
            while response.xpath('//*[@id="online-offers"]/div/a['+str(i)+']') != 'None':
                name = response.xpath('//*[@id="online-offers"]/div/a['+str(i)+']/span[3]/text()').extract()
                ItemStores[name] = response.xpath('//*[@id="online-offers"]/div/a['+str(i)+']/span[1]/text()').extract()
                i+=1
            #Write data to a file
            with open('TempItemData.txt', 'w') as f:
                f.write("Item Name: "+ItemName)
                f.write("Item MSRP: "+ItemMSRP)
                f.write("Availible Stores: ")
                for x,y in ItemStores.items():
                    f.write(x+" with a price of : "+y)
    return MainSpider
