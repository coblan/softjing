from helpers.pcweb.shotcut import web_page_dc
from helpers.maintenance.update_static_timestamp import static_url

class ExamplePage(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_context(self):
        return {
            'tops':[
                {'editor':'com-top-image-top-pad',
                 'image_url':static_url('image/server-2160321_1280.webp'),
                 'class':'my-top-image',
                 'css':'.my-top-image .head{height:320px}.my-top-image .head img{height:370px}',
                 'inn_editor':'com-ctn-tab',
                 'inn_ctx':{
                     'tabs':[
                         {'label':'管理后台','icon':static_url('image/系统.png'),'icon_active':static_url('image/系统_active.png')},
                         {'label':'移动应用','icon':static_url('image/移动端.png'),'icon_active':static_url('image/移动端_active.png')},
                         {'label':'数据分析','icon':static_url('image/数据.png'),'icon_active':static_url('image/数据_active.png')},
                     ]
                 }
                 },
                
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
            ]
        }

web_page_dc.update({
    'example':ExamplePage,
})