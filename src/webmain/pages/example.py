from helpers.pcweb.shotcut import web_page_dc
from helpers.maintenance.update_static_timestamp import static_url
from helpers.director.shortcut import ModelTable,director
from webmain.models import ExampleInfo

class ExamplePage(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_label(self):
        return '案例|竞嘉'
    
    def get_context(self):
        return {
            'tops':[
                #{'editor':'com-top-image-top-pad',
                 #'full_width':True,
                 #'image_url':static_url('image/server-2160321_1280.webp'),
                 #'class':'my-top-image',
                 #'css':''' .my-top-image .head{height:70px}
                           #.my-top-image .head img{height:370px}
                           #.my-top-image .content{margin-bottom:40px}''',  
                 #'inn_editor':'com-example-content',
                
                 #},
                {
                    'editor':'com-slot-wrap',
                    'inn_editor':'com-top-image-top-pad',
                    'slot':[
                        {'name':'content','editor':'com-example-content',},
                        ],
                 'full_width':True,
                 'image_url':static_url('image/server-2160321_1280.webp'),
                 'class':'my-top-image',
                 'css':''' .my-top-image .head{height:70px}
                           .my-top-image .head img{height:370px}
                           .my-top-image .content{margin-bottom:40px}
                           ''',  
                 #'inn_editor':'com-example-content',
                
                 },
                
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