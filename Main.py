import scrapy
from scrapy.crawler import CrawlerProcess
from BasicPythonScraper.spiders.m_spydr import MainSpiderGen

def main():
    #Get the Universal Product Code from the user
    UPC = input("Enter the products UPC:")
    Source = int(input("Enter what store to search\n1=Walmart\n2=Home_Depot\n:"))
    #Create and start the web spider
    spydr = MainSpiderGen(UPC, Source) 
    crawler = CrawlerProcess(settings=None)
    crawler.crawl(spydr)
    crawler.start(stop_after_crawl=True)
    
    #Print the results to consol
    with open("TempItemData.txt", "r") as f:
        print(f.read())
    
if __name__ == '__main__':
    main()
  