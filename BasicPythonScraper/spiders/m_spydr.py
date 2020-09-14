import scrapy

def MainSpiderGen(upc, source):
    #Create and return a spider class usin the UPC and source site
    #test upc: 095385791568
    if(source==0):
        class MainSpider(scrapy.Spider):
            name = "mainCrawl"
            UPC = upc
            start_urls = ['https://brickseek.com/products/?search='+str(UPC)]
            
            def parse(self, response):
                #Retrive the HTML of the search page for the item, and follow the first item link
                new_Link = response.xpath('//*[@id="main"]/div[2]/div[1]/div/div/a/@href').extract()
                yield scrapy.Request(new_Link, callback=self.item_page_parse)
                
            def item_page_parse(self, response):
                #Retrive the items attributes from the items page
                ItemName = response.xpath('//*[@id="main"]/div/div[1]/div[2]/h2/text()').get()
                ItemMSRP = response.xpath('//*[@id="main"]/div/div[1]/div[2]/div[1]/div/div[2]/text()').get()
                ItemStores = {}
                i = 1
                while response.xpath('//*[@id="online-offers"]/div/a['+str(i)+']') != 'None':
                    name = response.xpath('//*[@id="online-offers"]/div/a['+str(i)+']/span[3]/text()').get()
                    ItemStores[name] = response.xpath('//*[@id="online-offers"]/div/a['+str(i)+']/span[1]/text()').get()
                    i+=1
                #Write data to a file
                with open('TempItemData.txt', 'w') as f:
                    f.write("Item Name: "+ItemName)
                    f.write("Item MSRP: "+ItemMSRP)
                    f.write("Availible Stores: ")
                    for x,y in ItemStores.items():
                        f.write(x+" with a price of : "+y)
    elif(source==1):
        class MainSpider(scrapy.Spider):
            name = "mainCrawl"
            UPC = upc
            start_urls = ['https://www.walmart.com/search/?query='+str(UPC)]
            
            def parse(self, response):
                #Retrive the HTML of the search page for the item, and follow the first item link
                new_Link = response.xpath('//*[@id="searchProductResult"]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/a/@href').extract()
                yield scrapy.Request(new_Link, callback=self.item_page_parse)
                
            def item_page_parse(self, response):
                #Retrive the items attributes from the items page
                ItemName = response.xpath('//*[@id="product-overview"]/div/div[3]/div/h1/text()').get()
                ItemMSRP = response.xpath('//*[@id="price"]/div/span[1]/span/span[2]/span[2]/text()').get()
                ItemMSRP = ItemMSRP+'.'
                ItemMSRP = ItemMSRP+response.xpath('//*[@id="price"]/div/span[1]/span/span[2]/span[4]/text()').get()
                ItemDetailsMain = response.xpath('//*[@id="accordion-card-content-accordion-card-features"]/div/div[1]/div/div/text()').get()
                i = 1
                ItemDetailsList = []
                while response.xpath('//*[@id="accordion-card-content-accordion-card-features"]/div/div[1]/div/div/ul/li['+str(i)+']') != []:
                    ItemDetailsList.append(response.xpath('//*[@id="product-overview"]/div/div/div[1]/div[2]/div/div/div/div/ul/li['+str(i)+']/span/text()').get())
                    i+=1
                
                #Write data to a file
                with open('TempItemData.txt', 'w') as f:
                    f.write("Item Name: "+ItemName)
                    f.write("\nItem MSRP: $"+ItemMSRP)
                    f.write("\nItemDetails: "+ItemDetailsMain)
                    for dis in ItemDetailsList:
                        f.write("\n# "+dis)
    elif(source==2):
        class MainSpider(scrapy.Spider):
            name = "mainCrawl"
            UPC = upc
            start_urls = ['https://www.homedepot.com/s/'+str(UPC)]
            
            def parse(self, response):
                #Search the site for the Upc and then parse the item page after it redirects you
                ItemName = response.xpath('//*[@id="root"]/div/div[4]/div/div/div[3]/div/div/div[1]/div/div/div[1]/span/h1/text()').get()
                ItemMSRP = response.xpath('//*[@id="standard-price"]/div/div/span[2]/text()').get()
                ItemMSRP = ItemMSRP+'.'
                ItemMSRP = ItemMSRP+response.xpath('//*[@id="standard-price"]/div/div/span[3]/text()').get()
                ItemDetailsMain = response.xpath('//*[@id="product-overview"]/div/div/div[1]/div[2]/div/div/div/text()').get()
                i = 1
                ItemDetailsList = []
                while response.xpath('//*[@id="product-overview"]/div/div/div[1]/div[2]/div/div/div/div/ul/li['+str(i)+']') != []:
                    ItemDetailsList.append(response.xpath('//*[@id="product-overview"]/div/div/div[1]/div[2]/div/div/div/div/ul/li['+str(i)+']/span/text()').get())
                    i+=1
                
                #Write data to a file
                with open('TempItemData.txt', 'w') as f:
                    f.write("Item Name: "+ItemName)
                    f.write("\nItem MSRP: $"+ItemMSRP)
                    f.write("\nItemDetails: "+ItemDetailsMain)
                    for dis in ItemDetailsList:
                        f.write("\n# "+dis)
    return MainSpider

    