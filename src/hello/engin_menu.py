
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine, page, fa, can_list, can_touch
from django.contrib.auth.models import User, Group
from helpers.func.collection.container import evalue_container
from helpers.maintenance.update_static_timestamp import js_stamp,static_url
from django.utils.translation import ugettext as _
from django.conf import settings
from helpers.director.access.permit import has_permit
from helpers.pcweb.shotcut import web_page_dc
from helpers.director.base_data import inspect_dict

from django.utils import timezone

class PcAdminMenu(BaseEngine):
    url_name = 'BackEnd'
    title = 'BackEnd'
    brand = 'BackEnd'
    mini_brand = 'BackEnd'
    need_staff=True
    need_login=True
    access_from_internet=True
    @property
    def menu(self):
        crt_user = self.request.user
        menu = [
            {'label':'首页','url':page('enginhome')},
            {'label':'内容管理','icon': fa('fa-truck'),'submenu':[
                 {'label': '文章管理', 'url': page('admin_article'), },
                 {'label':'首页广告图','url':page('banner'),},
                 {'label':'示例管理','url':page('example')}
            ]},
           
            {'label':'设置','url':page('cfgpage'),'icon': fa('fa-truck'),},
        ]

        return menu
    

PcAdminMenu.add_pages(page_dc)


class PcWebMenu(BaseEngine):
    url_name = 'SoftJing'
    title = 'SoftJing'
    brand = '''  <img src="%s" onclick="location='/'" style="height:60px;width:auto"> ''' %static_url('image/logo.png') #'SoftJing'  #
    mini_brand = 'SoftJing'
    need_staff=False
    need_login=False
    access_from_internet=True
    @property
    def menu(self):
        crt_user = self.request.user
        menu = [
        
            {'label': '首页', 'url': page('home'), 'visible': True},
            {'label': '最新文章','url':page('articlelist'),'icon': fa('fa-truck'), 'visible': True},
            {'label': '演示实例','url':page('example'),'icon': fa('fa-truck'), 'visible': True},
            {'label':'联系我们','action':'''
                cfg.pop_vue_com('cus-contact',{wechat_qr:"%s"},{
                title:false,
                area: ['400px', '400px'],
                shade: 0.8,
                skin: 'img-shower',
                shadeClose: true,
            })
            '''%static_url('image/zhang_wechat.jpg') },
            #{'label':'管理','url':'/pc/enginhome','icon': fa('fa-truck'),'visible':True},
        ]

        return menu

    
    def custome_ctx(self, ctx):
        ctx.update({
            'extra_js':['webmain'],
            'navibar':{
                'editor':'com-xiu-menu','menu':ctx.get('menu')
            },
            'footer':{
                #'editor':'com-ft-copyright','copyright':''
                'class':'myfooter',
                'css':'.myfooter{background-color:white;padding:20px;} .myfooter a{text-decoration: none;}',
                'editor':'com-top-html',
                'html':'''
                <div style="text-align:center;">
                  <div>@copyright 2020 SoftJing Infomaion Technology Co</div>
                  <div><a rel="nofollow" href="http://www.beian.miit.gov.cn" target="_blank">蜀ICP备19023278号-1</a></div>
                </div>
              
                '''
            },
            'customize_meta':'''<meta name="keywords" content="互联网 软件 管理后台 公众号" />
<meta name="description" content="竞嘉信息技术有限公司">
<meta name="author" content="竞嘉信息技术有限公司">''',
            'init_express':'if(!ex.os.isPc){location="/mb/home"}'
        })
        return ctx

PcWebMenu.add_pages(web_page_dc)


# 移动页面
mb_page={}
inspect_dict['mb_page']= mb_page


class MBpageEngine(BaseEngine):
    url_name='mb_page'
    access_from_internet=True
    need_login=False
    #login_url='/mb/login'
    menu=[
        #{'label':'user_info','url':page('user_buyrecord')},
        #{'label':'user_washrecord','url':page('user_washrecord')},
        #{'label':'user_info','url':page('user_info')},
          
          ]
    
        
    def custome_ctx(self, ctx):
        ctx.update({
            'extra_js':['webmain'],
        })
        #if 'extra_js' not in ctx:
            #ctx['extra_js'] = []
        #if 'job' not in ctx['extra_js']:
            #ctx['extra_js'].append('job')
        #ctx['extra_js'].append('moment')
        #ctx['extra_js'].append('moment_zh_cn')
        
        
        #ctx['extra_js'].append('moment')
        return ctx

MBpageEngine.add_pages(mb_page)

