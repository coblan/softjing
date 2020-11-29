from helpers.pcweb.shotcut import web_page_dc
from helpers.director.shortcut import ModelFields,FieldsPage,ModelTable,director_element
from ..models import Article
from helpers.func.html import textify,truncatehtml

def get_right_side_panel():
    ls = [
        {'editor':'com-ti-msg-panel','title':'关于我们','content':'<p>《成都竞嘉信息科技有限公司》，竭诚为您服务！</p>'},
        {'editor':'com-ti-list-one-page','title':'今日推荐','item_editor':'com-li-article-simple','director_name':'article.list','action':'location="article?pk="+scope.row.pk'},
    ]
    return ls


class ArticleListPage(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_label(self):
        return '最新文章|竞嘉'
    
    def get_context(self):
        return {
            'tops':[
                {'editor':'com-top-action-bar','actions':[
                    {'label':'全部','action':'rootParStore.$emit("change-kind",{})'},
                    {'label':'管理系统','action':'rootParStore.$emit("change-kind",{kind:1})'},
                    {'label':'算法','action':'rootParStore.$emit("change-kind",{kind:2})'}
                    ]},
                {'editor':'com-top-lay-main-small',
                 'main_items':[
                    {
                    'editor':'com-ti-list',
                     'director_name':'article.list',
                     'on_mounted':'rootParStore.$on("change-kind",(event)=>{scope.vc.ctx.preset=event;scope.vc.get_rows()})',
                     'item_ctx':{
                         'editor':'com-li-article',
                          'link_express':'rt="article?pk="+scope.vc.row.pk',
                     }
                     #'action':'location="article?pk="+scope.row.pk'
                    }
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
    
    def inn_filter(self, query):
        query = query.order_by('order')
        if self.kw.get('kind'):
            return query.filter(kind = self.kw.get('kind'))
        else:
            return query
    
    def dict_row(self, inst):
        return {
            'sub_title': textify(  truncatehtml( inst.content,90 ) ),
            
        }

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