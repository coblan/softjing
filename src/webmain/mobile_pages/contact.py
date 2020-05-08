from .home import Home
from hello.engin_menu import mb_page
from helpers.mobile.shortcut import ModelTableMobile
from helpers.director.shortcut import director
from helpers.func.html import truncatehtml,textify
from helpers.maintenance.update_static_timestamp import static_url

class ContactPage(Home):
    def get_context(self): 
        return {
            'editor':'live_layout',
            'editor_ctx':{
                'layout_editors':[
                    {'editor':'cus-mb-contact','wechat_qr':static_url('image/zhang_wechat.jpg')}
                ],
                'footer':self.get_footer(3)
            }
          
        }

mb_page.update({
    'contact':ContactPage
})