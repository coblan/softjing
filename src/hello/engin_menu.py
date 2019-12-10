
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine, page, fa, can_list, can_touch
from django.contrib.auth.models import User, Group
from helpers.func.collection.container import evalue_container
from helpers.maintenance.update_static_timestamp import js_stamp
from django.utils.translation import ugettext as _
from django.conf import settings
from helpers.director.access.permit import has_permit
from helpers.pcweb.shotcut import web_page_dc

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
            {'label': '代理管理2','url':page('proxy'), 'visible': True},
        ]

        return menu
    
    def custome_ctx(self, ctx):
        ctx.update({
            'navibar':{
                'editor':'com-xiu-menu',
            },
            'footer':{
                'editor':'com-ft-copyright','copyright':'@copyright 2019 jingjia Infomaion Technology Co'
            }
        })
        return ctx

PcWebMenu.add_pages(web_page_dc)


