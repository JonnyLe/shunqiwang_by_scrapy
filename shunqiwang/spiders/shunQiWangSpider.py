# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from shunqiwang.spiders import montageURL
from shunqiwang import items


class ShunqiwangspiderSpider(CrawlSpider):
    name = 'shunQiWangSpider'
    city_list = montageURL.montageUrl()
    restrict_xpath_zhen = ''
    allowed_domains = ['11467.com']
    # start_urls = ['http://11467.com/']
    def start_requests(self):
        for city in self.city_list:
            #http://shanwei.11467.com/
            url = 'http://'+city+'.11467.com/'
            print('开始爬取：',url)
            yield scrapy.Request(url=url,callback=self.parse_city_item)

    #只需要提取县级地名
    def parse_city_item(self,response):
        # print('页面内容',response.text)
        links_show = []
        # link = LinkExtractor(restrict_xpaths='//*[@id="il"]/div[1]/div/div/dl/dt/',tags='a',attrs='href')
        link = LinkExtractor(restrict_xpaths='//*[@id="il"]/div[1]/div/div/dl/dt/a',attrs='href')
        links = link.extract_links(response)
        # links:[Link(url='http://shaoguan.11467.com/wujiang/', text='武江区', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wujiang/xinhuajiedao/', text='新华', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wujiang/huiminjiedao/', text='惠民', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wujiang/xilianzhen/', text='西联镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wujiang/xihezhen/', text='西河镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wujiang/longguizhen/', text='龙归镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wujiang/jiangwanzhen/', text='江湾镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/zhenjiang/', text='浈江区', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/zhenjiang/donghejiedao/', text='东河', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/zhenjiang/chezhanjiedao/', text='车站', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/zhenjiang/tianluochongjiedao/', text='田螺冲', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/zhenjiang/taipingjiedao/', text='太平', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/zhenjiang/nanmenjiedao/', text='南门', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/zhenjiang/hepingjiedao/', text='和平', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/qujiang/', text='曲江区', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/qujiang/mabazhen/', text='马坝镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/qujiang/datangzhen/', text='大塘镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/qujiang/fengwanzhen/', text='枫湾镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/qujiang/xiaokengzhen/', text='小坑镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/qujiang/shaxizhen/', text='沙溪镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/qujiang/wushizhen/', text='乌石镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/shixing/', text='始兴县', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/shixing/taipingzhen/', text='太平镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/shixing/mashizhen/', text='马市镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/shixing/chengjiangzhen/', text='澄江镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/shixing/dungangzhen/', text='顿岗镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/shixing/luobazhen/', text='罗坝镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/shixing/siqianzhen/', text='司前镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/renhua/', text='仁化县', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/renhua/danxiajiedao/', text='丹霞', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/renhua/wenshaozhen/', text='闻韶镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/renhua/fuxizhen/', text='扶溪镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/renhua/changjiangzhen/', text='长江镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/renhua/chengkouzhen/', text='城口镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/renhua/hongshanzhen/', text='红山镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wengyuan/', text='翁源县', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wengyuan/longxianzhen/', text='龙仙镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wengyuan/bazizhen/', text='坝仔镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wengyuan/jiangweizhen/', text='江尾镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wengyuan/guanduzhen/', text='官渡镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wengyuan/zhoubeizhen/', text='周陂镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/wengyuan/wengchengzhen/', text='翁城镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/ruyuan/', text='乳源县', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/ruyuan/ruchengzhen/', text='乳城镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/ruyuan/yiliuzhen/', text='一六镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/ruyuan/guitouzhen/', text='桂头镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/ruyuan/luoyangzhen/', text='洛阳镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/ruyuan/dabuzhen/', text='大布镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/ruyuan/daqiaozhen/', text='大桥镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/xinfeng/', text='新丰县', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/xinfeng/fengchengjiedao/', text='丰城', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/xinfeng/huangcazhen/', text='黄礤镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/xinfeng/matouzhen/', text='马头镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/xinfeng/meikengzhen/', text='梅坑镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/xinfeng/shatianzhen/', text='沙田镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/xinfeng/yaotianzhen/', text='遥田镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/lechang/', text='乐昌市', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/lechang/lechengjiedao/', text='乐城', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/lechang/beixiangzhen/', text='北乡镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/lechang/jiufengzhen/', text='九峰镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/lechang/langtianzhen/', text='廊田镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/lechang/changlaizhen/', text='长来镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/lechang/meihuazhen/', text='梅花镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/nanxiong/', text='南雄市', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/nanxiong/xiongzhoujiedao/', text='雄州', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/nanxiong/wujingzhen/', text='乌迳镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/nanxiong/jiezhizhen/', text='界址镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/nanxiong/pingtianzhen/', text='坪田镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/nanxiong/huangkengzhen/', text='黄坑镇', fragment='', nofollow=False), Link(url='http://shaoguan.11467.com/nanxiong/dengfangzhen/', text='邓坊镇', fragment='', nofollow=False)]
        print('县页面链接：',links)
        for l in links:
            links_show.append(l.url)
            yield scrapy.Request(url=l.url,callback=self.parse_towns_items)
        print('所有县目标链接：',links_show)

    def parse_towns_items(self, response):
        links_show = []
        # link = LinkExtractor(restrict_xpaths='//*[@id="il"]/div[2]/div',tags=('dl','a'),attrs='href')
        link = LinkExtractor(restrict_xpaths='//*[@id="il"]/div[2]/div/dl/dd/a',attrs='href')
        links = link.extract_links(response)
        # 乡镇页面链接： [Link(url='http://foshan.11467.com/gaoming/hechengjiedao/', text='荷城', fragment='', nofollow=False),
        #          Link(url='http://foshan.11467.com/gaoming/yanghezhen/', text='杨和镇', fragment='', nofollow=False),
        #          Link(url='http://foshan.11467.com/gaoming/genghezhen/', text='更合镇', fragment='', nofollow=False),
        #          Link(url='http://foshan.11467.com/gaoming/mingchengzhen/', text='明城镇', fragment='', nofollow=False),
        #          Link(url='http://foshan.11467.com/gaoming/duichuanchachang/', text='对川茶场', fragment='',nofollow=False),
        #          Link(url='http://foshan.11467.com/gaoming/gaomingjianyu/', text='高明监狱', fragment='', nofollow=False),
        #          Link(url='http://foshan.11467.com/gaoming/yunyonglinchang/', text='云勇林场', fragment='', nofollow=False),
        #          Link(url='http://foshan.11467.com/gaoming/foshanjianyu/', text='佛山监狱', fragment='', nofollow=False)]
        print('乡镇页面链接：', links)
        #去重
        links = set(links)
        for l in links:
            links_show.append(l.url)
            yield scrapy.Request(url=l.url)
        print('所有乡镇目标链接：', links_show)

    rules = (
        # Rule(LinkExtractor(restrict_xpaths='//*[@id="il"]/div[3]/div/div', tags=('a'), attrs='href')),
        Rule(LinkExtractor(allow=r'http://[a-z]+.11467.com/[a-z]+/pn\d+')),
        # Rule(LinkExtractor(restrict_xpaths='//*[@id="il"]/div[3]/div/ul', tags=('a'), attrs='href'),callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=r'//www.11467.com/[a-z]+/co/\d+.htm'),callback='parse_item',follow=False)
    )
    def parse_item(self, response):
        print(response.text)
        item = items.ShunqiwangItem()
        item['company'] = ''.join(response.xpath('//*[@id="gongshang"]/div/table//tr/td[contains(text(),"法人名称")]/following::td[1]/text()').extract())
        # item['company'] = ''.join(response.xpath('//*[@id="logo"]/h1/text()').extract())
        item['company_tel'] = ''.join(response.xpath('//*[@id="contact"]/div/dl/dd[2]/text()').extract())
        item['company_phone_manager'] =''.join(response.xpath('//*[@id="contact"]/div/dl/dd[4]/text()').extract())
        item['company_address'] =''.join(response.xpath('//*[@id="contact"]/div/dl/dd[1]/text()').extract())
        # item['company_net'] =''.join(response.xpath('//*[@id="gongshang"]/div/table//tr[16]/td[2]/a/text()').extract())
        item['company_net'] = ''.join(response.xpath('//*[@id="gongshang"]/div/table//tr/td[contains(text(),"公司官网")]/following::td[1]/text()').extract())
        if item['company_net'] == '':
            item['company_net'] = ''.join(response.xpath('//*[@id="gongshang"]/div/table//tr/td[contains(text(),"商铺")]/following::td[1]/text()').extract())
        item['company_email'] = ''.join(response.xpath('//*[@id="contact"]/div/dl/dt[contains(text(),"电子邮件：")]/following::dd[1]/text()').extract())
        item['company_state'] = ''.join(response.xpath('//*[@id="gongshang"]/div/table//tr/td[contains(text(),"经营状态：")]/following::td[1]/text()').extract())
        if (item['company'] or item['company_phone_manager'] or item['company_address'] or item['company_email'] or item['company_state'] or item['company_net']) =="":
            # response.url
            print('处理未出阿道数据的情况')
            pass
        print('******************************************************************************')
        print(response.url)
        print(item)

        print('******************************************************************************')
        yield item