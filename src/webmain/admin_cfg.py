from helpers.director.shortcut import FieldsPage,Fields,page_dc,director
from helpers.director.kv import set_value,get_value

class CfgPage(FieldsPage):
    def get_label(self):
        return '配置页面'
    
    def get_template(self, prefer=None):
        return 'jb_admin/fields.html'
    
    class fieldsCls(Fields):
        def get_heads(self):
            return [
                {'name':'cfg.home_html','label':'主页html','editor':'com-field-richtext'},
                {'name':'cfg.example_html','label':'示例html','editor':'com-field-richtext'},
            ]
        
        def dict_row(self):
            return {
                'cfg.home_html':get_value('cfg.home_html',''),
                'cfg.example_html':get_value('cfg.example_html','')
            }
        
        def save_form(self):
            set_value('cfg.home_html',self.kw.get('cfg.home_html'))
            set_value('cfg.example_html',self.kw.get('cfg.example_html'))

director.update({
    'cfgpage':CfgPage.fieldsCls
})

page_dc.update({
    'cfgpage':CfgPage
})