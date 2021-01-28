from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director,RowSort

from .models import Article

class ArticlePage(TablePage):
    def get_label(self):
        return '文章管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        
        model = Article
        exclude =[]
        pop_edit_fields=['id']
        
        class sort(RowSort):
            names = ['order']
        

class ArticleForm(ModelFields):
    class Meta:
        model = Article
        exclude =[]

director.update({
    'admin_article':ArticlePage.tableCls,
    'admin_article.edit':ArticleForm
})

page_dc.update({
    'admin_article':ArticlePage
})