from hello.engin_menu import mb_page
from django.conf import settings
from helpers.director.kv import get_value
from ..models import Banner
from helpers.maintenance.update_static_timestamp import static_url

class Home(object):
    def __init__(self, request, engin):
        self.request =request
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_context(self):
        banners = []
        for banner in Banner.objects.all():
            banners.append({
                'name':banner.pk,
                'label':banner.title,
                'image_url':banner.cover,
                'action':'''live_root.open_live("live_html",{content:"<div style='height:800px'>hello world</div>"})'''
            })
            
        return {
            'editor':'live_layout',
             'editor_ctx':{
                 'layout_editors':[
                     {'editor':'com-top-swiper','items':banners,},
                     {'editor':'com-top-caption',
                      'image_url':static_url('mobile/python.jpg'),
                      'class':'white-bg material-wave',
                      'css':'.white-bg{background-color:white;margin:.4rem 0}',
                      'title':'核心技术',
                      'sub_title':'Python+Django+Vuejs技术架构，非前后端分离的全栈式开发,1-2天快速响应'},
                     {'editor':'com-top-caption',
                      'image_url':static_url('mobile/v2_q7sorp.jpg'),
                      'class':'white-bg material-wave',
                      'title':'公司理念',
                      'location':'right',
                      'sub_title':'任何功能可追踪至一线开发人员，快速解决问题，不做营销型公司。'},
                     
                    {'editor':'com-top-caption',
                      'image_url':static_url('mobile/v2_q7sq2e.jpg'),
                      'class':'white-bg material-wave',
                      'title':'服务项目',
                      'sub_title':'管理系统开发,数据爬取、挖掘分析,公众号与小程序等。'},
                     
                    #{'editor':'com-top-html','html':get_value('cfg.home_html','')},
                    
                    ],
                 'footer':self.get_footer(0)
                 }
             }
    def get_footer(self,index):
        return {
            'editor':'com-top-footer-btn-pannel',
            'active':index,
            'items':[
                {'label':'首页','icon':'home-o','action':'location = "/mb/home" '},
                {'label':'示例','icon':'gem-o','action':'location = "/mb/example"'},
                {'label':'方案','icon':'description','action':'location = "/mb/article"'}
            ]
        }

mb_page.update({
    'home':Home
})