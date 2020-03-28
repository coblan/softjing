from helpers.pcweb.shotcut import web_page_dc
from .models import Banner
from helpers.maintenance.update_static_timestamp import static_url

class SoftJingHome(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_label(self):
        return '竞嘉'
    
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
                {'editor':'com-top-block-ctn','title':'我们的服务','sub_title':'灵活多变,以人为本。',
                 'items':[
                    {'editor':'com-ti-caption','class':'wow zoomIn dh-1','css':'.dh-1{height:380px}',
                     'image_url':static_url('image/admin_sys2.jpg'),
                     'title':'管理系统','sub_title':'契合业务的管理系统是您的秘密武器!'},
                    {'editor':'com-ti-caption','class':'wow zoomIn dh-1',
                     'image_url':'http://h1.ioliu.cn/bing/OverwinteringMonarchs_ZH-CN0248511586_1920x1080.jpg',
                     'title':'公众号',
                     'sub_title':'移动互联网时代'},
                    {'editor':'com-ti-caption','class':'wow zoomIn dh-1',
                     'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                    {'editor':'com-ti-caption','class':'wow zoomIn dh-1',
                     'image_url':'http://h1.ioliu.cn/bing/RhinosOxpecker_ZH-CN6392794613_1920x1080.jpg','title':'xxx','sub_title':'犀牛'},
                   
                    ]},
                {'editor':'com-top-transparent-ctn','image_url':'http://h1.ioliu.cn/bing/NambungPinnacles_ZH-CN7198283991_1920x1080.jpg',
                 'title':'大千世界,近在眼前',
                 'subtitle':'互联网技术带来了第四次工业革命，带来了空前的变革,搭上这趟快车，您将拥有无限可能!'}, #'image_url':'http://h1.ioliu.cn/bing/BlueChip_ZH-CN7376022522_1920x1080.jpg'},
                
                {'editor':'com-top-block-ctn','title':'测试','items':[
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':static_url( 'image/admin_sys.jpg' ),
                     'title':'xxx','sub_title':'集成电路'} ,
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