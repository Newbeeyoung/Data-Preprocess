import scrapy
from scrapy.http import Request
from scrapy.contrib.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from cv_camera.items import CvCameraItem
import os
from urllib.parse import quote


class CameraSpider(scrapy.Spider):
    name='camera'
    allowed_domains=['blog.csdn.net']
    search_term='nikon+dslr'
    url = 'https://www.google.com/search?q=' + quote(search_term) + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&tbs=none&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
    print (url)
    start_urls=[url]
    def parse(self, response):
        image=CvCameraItem()
        rel=response.xpath('//div[contains(@class,"rg_meta")]/text()').extract()
        print("*****Length:"+str(len(rel)))
        content=[]
        for i in range(len(rel)):
            s=rel[i]
            start_content = s.find('"ou"')
            end_content = s.find(',"ow"')
            content_raw = str(s[start_content + 6:end_content - 1])
            content.append(content_raw)
        image['image_urls'] =content
        yield image