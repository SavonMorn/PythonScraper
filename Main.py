import scrapy
from scrapy.crawler import CrawlerProcess
from BasicPythonScraper.spiders.m_spydr import MainSpider

def main():
    #Get the Universal Product Code from the user
    UPC = input("Enter the products UPC:")
    #Create and start the web spider
    spydr = MainSpider(UPC=UPC) 
    crawler = CrawlerProcess(settings=None)
    crawler.crawl(spydr)
    crawler.start()
    #Print the results to consol
    f = open("TempItemData.txt", "r")
    print(f.read())
    

if __name__ is '__main__':
    main()
  