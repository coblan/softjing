from helpers.pcweb.shotcut import web_page_dc
from helpers.maintenance.update_static_timestamp import static_url
from helpers.director.shortcut import ModelTable,director
from webmain.models import ExampleInfo

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
                         {'label':'综合系统','icon':static_url('image/综合数据.png'),'icon_active':static_url('image/综合数据_active.png'),
                          'editor':'com-example-info',
                          'director_name':'example-list',
                          'preset':'rt={kind:1}',
                          },
                         {'label':'管理系统',
                          'icon':static_url('image/系统.png'),'icon_active':static_url('image/系统_active.png'),
                          'editor':'com-example-info',
                          'director_name':'example-list',
                           'preset':'rt={kind:2}',},
                        {'label':'移动系统',
                          'icon':static_url('image/移动端.png'),'icon_active':static_url('image/移动端_active.png'),
                          'editor':'com-example-info',
                          'director_name':'example-list',
                           'preset':'rt={kind:3}',},
                         {'label':'数据分析','icon':static_url('image/数据.png'),'icon_active':static_url('image/数据_active.png')},
                     ]
                 }
                 },
                
                #{'editor':'com-top-block-ctn','title':'测试标题','items':[
                    #{'editor':'com-ti-caption','class':'wow zoomIn',
                     #'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                    #{'editor':'com-ti-caption','class':'wow zoomIn',
                     #'image_url':'http://h1.ioliu.cn/bing/OverwinteringMonarchs_ZH-CN0248511586_1920x1080.jpg','sub_title':'测试鸟类,测试鸟类,测试鸟类,测试鸟类,'},
                    #{'editor':'com-ti-caption','class':'wow zoomIn',
                     #'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                    #{'editor':'com-ti-caption','class':'wow zoomIn',
                     #'image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg','title':'xxx','sub_title':'bbb'},
                   
                #]},
            ]
        }


class ExampleInfoList(ModelTable):
    model = ExampleInfo
    exclude = []
    nolimit = True
    def inn_filter(self, query):
        return query.filter(kind=self.kw.get('kind'))

director.update({
    'example-list':ExampleInfoList
})
    
web_page_dc.update({
    'example':ExamplePage,
})