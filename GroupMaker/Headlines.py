# Chris Allulis
# Looks for headlines of the NYT

import scrapy

class headlineSpider(scrapy.Spider):
    name = "NYT"
    allowed_domains = ["http://www.nytimes.com/"]
    start_urls = ["http://www.nytimes.com/" ]

    def parse(self,response):
        filename = response.url.split("/"[-2])
        open(filename,'wb').write(response.body)


def main():
    scrapy crawl NYT

if __name__ == "__main__":
    main()

