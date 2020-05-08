from helpers.pcweb.shotcut import web_page_dc
from webmain.models import Banner
from helpers.maintenance.update_static_timestamp import static_url
from webmain.mobile_pages.home import get_service_html

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
                {'editor':'cus-our-service',**get_service_html()},
                
                #{'editor':'com-top-block-ctn','title':'我们的服务','sub_title':'灵活多变,以人为本。',
                 #'items':[
                    #{'editor':'com-ti-caption','class':'wow zoomIn dh-1','css':'.dh-1{height:380px}',
                     #'image_url':static_url('image/admin_sys2.jpg'),
                     #'title':'管理系统','sub_title':'契合业务的管理系统是您的秘密武器!'},
                    #{'editor':'com-ti-caption','class':'wow zoomIn dh-1',
                     #'image_url':static_url('image/admin_sys2.jpg'),
                     #'title':'公众号',
                     #'sub_title':'移动互联网时代'},
                    #{'editor':'com-ti-caption','class':'wow zoomIn dh-1',
                     #'image_url':static_url('image/admin_sys2.jpg'),
                     #'title':'开发中','sub_title':'开发中'},
                    #{'editor':'com-ti-caption','class':'wow zoomIn dh-1',
                     #'image_url':static_url('image/admin_sys2.jpg'),
                     #'title':'开发中','sub_title':'犀牛'},
                   
                    #]},
                {'editor':'com-top-transparent-ctn',
                 'image_url':static_url('image/desert-4791919_1280.jpg'),
                 'title':'大千世界,近在眼前',
                 'subtitle':'互联网技术带来了第四次工业革命，带来了空前的变革,搭上这趟快车，您将拥有无限可能!'}, #'image_url':'http://h1.ioliu.cn/bing/BlueChip_ZH-CN7376022522_1920x1080.jpg'},
                
                {'editor':'com-top-block-ctn','title':'我们的特点','items':[
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':static_url( 'image/admin_sys.jpg' ),
                     'title':'新技术高效率','sub_title':'python+django+vuejs模块化开发，速度惊人'} ,
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':static_url( 'image/collective-3300872_640.png' ),
                     'title':'模块化低成本',
                     'sub_title':'模块化开发，人力成本降低，费用大幅减少'} ,
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':static_url( 'image/owl-50267_640.jpg' ),
                     'title':'全站开发易维护',
                     'sub_title':'全栈开发，程序统一而连贯，极大提高程序的可维护性。使得项目长期维护成为可能。灵活多变。'} ,
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