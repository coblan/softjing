from helpers.pcweb.shotcut import web_page_dc
from .models import Banner

class SoftJingHome(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_context(self):
        banners = []
        for banner in Banner.objects.all():
            banners.append({
                'name':banner.pk,
                'label':banner.title,
                'editor':'com-swiper-image',
                'image_url':banner.cover,
            })
        
        return {
            'tops':[
                {'editor':'com-top-swiper-fade','items': banners
                 #[ 
                    #{'name':'1','label':'犀牛','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/RhinosOxpecker_ZH-CN6392794613_1920x1080.jpg'},
                    #{'name':'2','label':'鸟类','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg'},
                    #{'name':'3','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/OverwinteringMonarchs_ZH-CN0248511586_1920x1080.jpg'},
                    #{'name':'4','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/HairyHighlanders_ZH-CN5546635143_1920x1080.jpg'},
                #]
                 },
                {'editor':'com-top-block-ctn','title':'当前状态','sub_title':'网站正在开发中',
                 'items':[
                    {'editor':'com-ti-caption','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                    {'editor':'com-ti-caption','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/OverwinteringMonarchs_ZH-CN0248511586_1920x1080.jpg','sub_title':'测试鸟类,测试鸟类,测试鸟类,测试鸟类,'},
                    {'editor':'com-ti-caption','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                    {'editor':'com-ti-caption','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/StubenamAlberg_EN-AU7684816211_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                   
                    ]},
                {'editor':'com-top-transparent-ctn','image_url':'http://h1.ioliu.cn/bing/NambungPinnacles_ZH-CN7198283991_1920x1080.jpg'}, #'image_url':'http://h1.ioliu.cn/bing/BlueChip_ZH-CN7376022522_1920x1080.jpg'},
                
                {'editor':'com-top-block-ctn','title':'测试','items':[
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/BlueChip_ZH-CN7376022522_1920x1080.jpg','title':'xxx','sub_title':'集成电路'} ,
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/ZhangjiajieLandscape_EN-AU12445284069_1920x1080.jpg','sub_title':'张家界国家森林公园'} ,
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'} ,
                ]}
                #{'editor':'com-slide-win','images':[
                    #{'url':'xxx'},
                    #{'url':'bbb'},
                #]}
            ]
        }

web_page_dc.update({
    'home':SoftJingHome
})