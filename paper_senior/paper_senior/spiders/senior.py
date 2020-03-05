# -*- coding: utf-8 -*-
import scrapy
from paper_senior.items import PaperSeniorItem
from scrapy.http import Request,FormRequest
import re
import requests
#36
class SeniorSpider(scrapy.Spider):
    name = 'senior'
    allowed_domains = ['http://d.zww.cn/gaozhong']
    start_urls = ['http://d.zww.cn/xiaoxue/']

    def parse(self, response):
        '''
        获取到 学科  年级
        '''
        subject_href = response.xpath("//dl[@class='classlist classlist2']//dt//span//a/@href").extract()[:-1]
        print('*************************************************',subject_href)
        for url in subject_href:
            yield scrapy.Request(
                url = 'http://d.zww.cn/' + url,
                dont_filter=True,
                callback=self.parse_page,
            )

    def parse_page(self,response):
        '''
        实现翻页
        '''
        page_re = '<script type="text/javascript">pagenav\((.*?),\".*?\"\);//PageCount in new.js</script>'
        page_list = re.findall(page_re,response.text)[0]
        print('+++++++++++++++++++++++++++++++++++++++++++++',page_list)
        for i in range(1,int(page_list)+1):
            yield scrapy.Request(
                url=response.url+'{}.htm'.format(i),
                dont_filter=True,
                callback=self.parse_reque,
            )

    def parse_reque(self,response):
        '''
        获取试卷名及详情链接
        '''
        paper_href = response.xpath("//div[@class='artlist']//li//a/@href").extract()
        print(paper_href)
        for href in paper_href:
            yield scrapy.Request(
                url='http://d.zww.cn/'+href+'#downfile',
                dont_filter=True,
                callback=self.parse_down,
            )

    def parse_down(self,response):
        '''
        试卷下载链接
        '''
        item = PaperSeniorItem()
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        }
        subject = response.xpath("//div[@class='curposition']//a/text()").extract()[1]
        grade = response.xpath("//div[@class='curposition']//a/text()").extract()[2]
        paper_name = response.xpath("//div[@class='col1']//h1/text()").extract()[0]
        down_one_re = '<script>down(.*?);</script>'
        down_one = re.findall(down_one_re,response.text)[0]
        if down_one == []:
            down_one= []
        down_two_re = '(?<=,")(.*?)(?=")'
        down_two = re.findall(down_two_re,down_one)[0].replace('\\\\','/')
        if down_two == []:
            down_two = []
        down = 'http://d.zww.cn/' + down_two
        item['subject'] = subject
        item['grade'] = grade
        item['paper_name'] = paper_name
        item['down'] = down
        r = requests.get(url=item['down'],headers = headers)
        r.encoding = 'gb2312'
        item['down_content'] = r
        yield item
