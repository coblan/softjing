
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine, page, fa, can_list, can_touch
from django.contrib.auth.models import User, Group
from helpers.func.collection.container import evalue_container
from helpers.maintenance.update_static_timestamp import js_stamp
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
        
            {'label': '文章管理', 'url': page('admin_article'), 'visible': True},
            {'label':'首页广告图','url':page('banner'),'visible':True},
            {'label':'设置','url':page('cfgpage')},
        ]

        return menu
    

PcAdminMenu.add_pages(page_dc)


class PcWebMenu(BaseEngine):
    url_name = 'SoftJing'
    title = 'SoftJing'
    brand = 'SoftJing'
    mini_brand = 'SoftJing'
    need_staff=False
    need_login=False
    access_from_internet=True
    @property
    def menu(self):
        crt_user = self.request.user
        menu = [
        
            {'label': '首页', 'url': page('home'), 'visible': True},
            {'label': '文章','url':page('articlelist'), 'visible': True},
            {'label': '示例','url':page('example'), 'visible': True},
            {'label':'后台管理','url':'/pc/admin_article','visible':True},
        ]

        return menu
    
    def custome_ctx(self, ctx):
        ctx.update({
            'navibar':{
                'editor':'com-xiu-menu',
            },
            'footer':{
                'editor':'com-ft-copyright','copyright':'@copyright 2019 jingjia Infomaion Technology Co'
            },
            'customize_meta':'''<meta name="keywords" content="互联网 软件 管理后台 公众号" />
<meta name="description" content="竞嘉信息技术有限公司">
<meta name="author" content="竞嘉信息技术有限公司">'''
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
    #def custome_ctx(self, ctx):
        #if 'extra_js' not in ctx:
            #ctx['extra_js'] = []
        #if 'job' not in ctx['extra_js']:
            #ctx['extra_js'].append('job')
        #ctx['extra_js'].append('moment')
        #ctx['extra_js'].append('moment_zh_cn')
        
        
        #ctx['extra_js'].append('moment')
        #return ctx

MBpageEngine.add_pages(mb_page)

