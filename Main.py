import scrapy
from scrapy.crawler import CrawlerProcess
from BasicPythonScraper.spiders.m_spydr import MainSpider

def main():
    UPC = input("Enter the products UPC:")
    spydr = MainSpider(UPC=UPC) 
    crawler = CrawlerProcess(settings=None)
    crawler.crawl(spydr)
    crawler.start()
    f = open("TempItemData.txt", "r")
    print(f.read())
    

if __name__ is '__main__':
    main()
