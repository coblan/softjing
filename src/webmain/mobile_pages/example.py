from hello.engin_menu import mb_page
from django.conf import settings
from helpers.director.kv import get_value

from helpers.maintenance.update_static_timestamp import static_url
from . home import Home

class ExamplePage(Home):
    def __init__(self, request, engin):
        self.request =request
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_context(self): 
        return {
            'editor':'live_layout',
            'editor_ctx':{
                'layout_editors':[
                    {'editor':'com-top-html','html':'<h2 style="text-align:center;margin:.4rem 0 .2rem 0">移动端</h2>'},
                    {'editor':'com-top-caption',
                      'image_url':static_url('mobile/yizhitong.png'),
                      'class':'white-bg material-wave',
                      'css':'.white-bg{background-color:white;margin:.4rem 0}',
                      'title':'易职通',
                      'action':'cfg.confirm("确定跳转到【样例】易职通?").then(()=>{ location="http://job.softjing.com" })',
                      'sub_title':'一个面向本地的求职平台，比大平台更加贴近普通大众。'},
                    
                     {'editor':'com-top-html','html':'<h2 style="text-align:center;margin:.4rem 0 .2rem 0">PC端</h2>'},
                     {'editor':'com-top-caption',
                      'image_url':static_url('mobile/color.png'),
                      'class':'white-bg material-wave',
                      'css':'.white-bg{background-color:white;margin:.4rem 0}',
                      'title':'COLOR管理后台',
                      'action':'cfg.toast("请在pc端查看该样例")',
                      'sub_title':'一个画图app管理后台面，向本地的求职平台，比大平台更加贴近普通大众。'},

                ],
                'footer':self.get_footer(1)
            }
        }

mb_page.update({
    'example':ExamplePage
})