import scrapy, re

class DmozSpider(scrapy.Spider):
    name = "title"
    allowed_domains = ["m.blog.daum.net"]
    start_urls = [
            "http://m.blog.daum.net/_blog/_m/articleList.do?blogid=04ZDV"
            ]
    
    def parse(self, response):
        filename = response.url.split("/")[-2]
        
#        titles = response.xpath('//ul/li/a/div[@class="has_img_wrap"]/span[@class="title"]').extract()
#        titles = response.xpath('//ul[@class="type1"]/li[@class="has_thumbnail"]/a/div[@class="has_img_wrap"]/span[@class="title"]/text()').extract()
        titles = response.xpath('//span[@class="title"]/text()').extract()
        

        print(titles)

        with open(filename, 'wb') as f:
            #f.write(response.body)
            for title in titles:
                title = re.sub("\t", "", title)
                title = re.sub("\r\n", "", title)
                title = re.sub("  ", "", title)
                title = title+"\n"
                print title
                f.write(title.encode("utf-8"))
            #f.write(titles)
