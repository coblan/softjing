from helpers.pcweb.shotcut import web_page_dc

class SoftJingHome(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_context(self):
        return {
            'tops':[
                {'editor':'com-top-swiper-fade','items':[
                    {'name':'1','label':'犀牛','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/RhinosOxpecker_ZH-CN6392794613_1920x1080.jpg'},
                    {'name':'2','label':'鸟类','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg'},
                    {'name':'3','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/OverwinteringMonarchs_ZH-CN0248511586_1920x1080.jpg'},
                    {'name':'4','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/HairyHighlanders_ZH-CN5546635143_1920x1080.jpg'},
                ]},
                {'editor':'com-top-block-ctn','title':'测试标题','items':[
                    {'editor':'com-ti-caption','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                    {'editor':'com-ti-caption','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/OverwinteringMonarchs_ZH-CN0248511586_1920x1080.jpg','sub_title':'测试鸟类,测试鸟类,测试鸟类,测试鸟类,'},
                    {'editor':'com-ti-caption','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                    {'editor':'com-ti-caption','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                   
                    ]},
                
                {'editor':'com-top-block-ctn','title':'测试','items':[
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'} 
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