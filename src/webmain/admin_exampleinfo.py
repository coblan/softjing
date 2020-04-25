from helpers.director.shortcut import ModelTable,ModelFields,TablePage,page_dc,director
from . models import ExampleInfo

class ExampleInfoPage(TablePage):
    def get_label(self):
        return '示例管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = ExampleInfo
        exclude =[]

class ExampleForm(ModelFields):
    class Meta:
        model = ExampleInfo
        exclude =[]

director.update({
    'example':ExampleInfoPage.tableCls,
    'example.edit':ExampleForm,
})

page_dc.update({
    'example':ExampleInfoPage
})
    
