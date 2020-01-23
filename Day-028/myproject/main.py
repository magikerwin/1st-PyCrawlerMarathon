import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTCrawler', urls_txt_path='./target_urls.txt', output_path='test.json')
    process.start()

	
if __name__ == '__main__':
    main()
