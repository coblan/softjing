from hello.engin_menu import mb_page
from django.conf import settings
from helpers.director.kv import get_value

class Home(object):
    def __init__(self, request, engin):
        self.request =request
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_context(self):
        return {
            'editor':'live_layout',
             'editor_ctx':{
                 'layout_editors':[
                     
                    {'editor':'com-top-html','html':get_value('cfg.home_html','')},
                    ]
                 }
             }

mb_page.update({
    'home':Home
})