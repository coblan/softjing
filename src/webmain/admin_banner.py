from helpers.director.shortcut import ModelTable,TablePage,ModelFields,director,page_dc
from .models import Banner

class BannerPage(TablePage):
    def get_label(self):
        return '广告图片'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = Banner
        exclude = []
        pop_edit_fields = ['id']

class BannerForm(ModelFields):
    class Meta:
        model = Banner
        exclude =[]
    
    def dict_head(self, head):
        if head['name'] == 'cover':
            head['can_input'] = True
        return head

director.update({
    'banner':BannerPage.tableCls,
    'banner.edit':BannerForm,
})

page_dc.update({
    'banner':BannerPage
})