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
                    {'editor':'com-top-html','html':'敬请期待!'}
                ],
                'footer':self.get_footer(1)
            }
        }

mb_page.update({
    'example':ExamplePage
})