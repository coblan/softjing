from .article import ArticleListPage,get_right_side_panel
from helpers.pcweb.shotcut import web_page_dc

class Example2Page(ArticleListPage):
    def __init__(self, *args, **kwargs):
        pass
    
    def get_label(self):
        return '样例'
    
    article_tag = "example"
    


#@director_element('article.list')
#class ArticleList(ModelTable):
    #nolimit=True
    #model = Article
    #exclude =[]
    #simple_dict = True
    
    #def inn_filter(self, query):
        #query = query.filter(status=1).order_by('order')
        #if self.kw.get('kind'):
            #return query.filter(kind = self.kw.get('kind'))
        #else:
            #return query
    
    #def dict_row(self, inst):
        #return {
            #'sub_title': textify(  truncatehtml( inst.content,90 ) ),
            
        #}

web_page_dc.update({
    'sample':Example2Page
})
