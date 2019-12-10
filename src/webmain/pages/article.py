from helpers.pcweb.shotcut import web_page_dc
from helpers.director.shortcut import ModelFields,FieldsPage,ModelTable,director_element
from ..models import Article

def get_right_side_panel():
    ls = [
        {'editor':'com-ti-msg-panel','title':'双攻等是的','content':'<p>hello world</p>'},
        {'editor':'com-ti-list-one-page','title':'今日推荐','item_editor':'com-li-article-simple','director_name':'article.list','action':'location="article?pk="+scope.row.pk'},
    ]
    return ls


class ArticleListPage(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_context(self):
        return {
            'tops':[
                {'editor':'com-top-lay-main-small',
                 'main_items':[
                    {'editor':'com-ti-list','director_name':'article.list','item_editor':'com-li-article','action':'location="article?pk="+scope.row.pk'}
                    ],
                 'small_items':get_right_side_panel()},
            ]
        }

@director_element('article.list')
class ArticleList(ModelTable):
    nolimit=True
    model = Article
    exclude =[]
    simple_dict = True


class ArticlePage(FieldsPage):
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_context(self):
        ctx = {
            'tops':[
                {'editor':'com-top-lay-main-small',
                 'main_items':[
                     {'editor':'com-ti-article','row':self.fields.get_row()}
                 ],
                 'small_items':get_right_side_panel()
                }
            ]
        }
        return ctx
    
    class fieldsCls(ModelFields):
        nolimit = True
        class Meta:
            model = Article
            exclude = []
        
        def get_row(self):
            row = super().get_row()
            return row
        
        def dict_row(self, inst):
            return {
                'content':inst.content
            }
            

web_page_dc.update({
    'articlelist':ArticleListPage,
    'article':ArticlePage,
})