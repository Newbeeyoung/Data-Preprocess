# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy import log
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class CvCameraPipeline(object):
    def process_item(self, item, spider):
        return item

# class MyImagesPipeline(ImagesPipeline):
#     #Name download version
#     def file_path(self, request, response=None, info=None):
#         #item=request.meta['item'] # Like this you can use all from item, not just url.
#         image_guid = request.url.split('/')[-1]
#         return 'full/%s' % (image_guid)
#
#     #Name thumbnail version
#     def thumb_path(self, request, thumb_id, response=None, info=None):
#         image_guid = thumb_id + response.url.split('/')[-1]
#         return 'thumbs/%s/%s.jpg' % (thumb_id, image_guid)
#
#     def get_media_requests(self, item, info):
#         #yield Request(item['images']) # Adding meta. Dunno how to put it in one line :-)
#         for image in item['image_urls']:
#             yield Request(image)

