from .home import Home
from hello.engin_menu import mb_page

class ArticlePage(Home):
    def get_context(self): 
        return {
            'editor':'live_layout',
            'editor_ctx':{
                'layout_editors':[
                    {'editor':'com-top-html','html':'建站心得体会,敬请期待!'}
                ],
                'footer':self.get_footer(2)
            }
        }

mb_page.update({
    'article':ArticlePage
})