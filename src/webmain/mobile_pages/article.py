from .home import Home
from hello.engin_menu import mb_page
from helpers.mobile.shortcut import ModelTableMobile
from helpers.director.shortcut import director
from helpers.func.html import truncatehtml,textify
from webmain.models import Article

class ArticlePage(Home):
    def get_context(self): 
        return {
            #'editor':'live_layout',
            #'editor_ctx':{
                #'layout_editors':[
                    ##{'editor':'com-top-html','html':'<h2 style="text-align:center;margin:.4rem 0 .2rem 0">最新文章</h2>'},
                    #{'editor':'com-live-list',}
                    
                #],
                #'footer':self.get_footer(2)
            #}
            'editor':'live_list',
            'editor_ctx':{
                **ArticleTable().get_head_context(),
                 'table_editor': 'com-list-general',
                 'row_editor':'com-top-caption',
                 'title':'资讯推荐',
                 'footer':self.get_footer(2)
                 },
            
            
        }

class ArticleTable(ModelTableMobile):
    nolimit = True
    model = Article
    exclude = []
    
    def dict_row(self, inst):
        return {
            'image_url':inst.cover,
            'sub_title': textify ( truncatehtml(inst.content,length=30) ),
             'action':'live_root.open_live("live_html",{"content":scope.head.content,"title":scope.head.title})'
        }

director.update({
    'article':ArticleTable,
})

mb_page.update({
    'article':ArticlePage
})