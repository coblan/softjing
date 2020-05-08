from hello.engin_menu import mb_page
from django.conf import settings
from helpers.director.kv import get_value
from ..models import Banner
from helpers.maintenance.update_static_timestamp import static_url

def get_service_html():
    return {
        'about_us':''' <p >竞嘉主要由富有经验的全栈开发人员组成，我们拥有完全自主研发的开发框架，具备深度/灵活定制化系统的能力。我们的服务对象主要是中小型企业及部分个人用户。为客户提供精简和有针对性的专门化系统。

            </p>
            <p> 未来我们会陆续推出AI/机器学习方面的相关服务，例如企业数据透视图，信息提取与分析等。</p>''',
        'admin_backend':'''  主要是采用浏览器(前端)+python(后端)的架构，为用户提供软件服务。传统的大公司开发的ERP,OA等管理软件功能繁杂，人员需要培训，使得普通用户比较抵触，而我们追求的是小巧，易用和几乎不需要培训的软件。根据用户的需求，富有针对性的定制化软件，砍掉那些用不到的功能，这就是我们存在的意义。
''',
        'h5':'''采用vue.js等流行的前端技术，进行模块化H5开发。拥有自主开发框架，能够快速开发公众号和web网站，成本低廉。''',
        'after_content':'''   <p>
                除了单独开发软件外。我们还积极的参与到软件外包服务中。如果您的项目需要专业的全栈开发技术，可以联系我们。我们除了拥有技术外，还有诚意。
            </p>'''
    }

class Home(object):
    def __init__(self, request, engin):
        self.request =request
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_context(self):
        banners = []
        for banner in Banner.objects.all():
            banners.append({
                'name':banner.pk,
                'label':banner.title,
                'image_url':banner.cover,
                'action':'''live_root.open_live("live_html",{content:"<div style='height:800px'>hello world</div>"})'''
            })
            
        return {
            'editor':'live_layout',
             'editor_ctx':{
                 'layout_editors':[
                     {'editor':'com-top-swiper','items':banners,},
                     {'editor':'cus-mb-our-service',**get_service_html() },
                     
                    {'editor':'com-top-transparent-ctn',
                 'image_url':static_url('image/desert-4791919_1280.jpg'),
                 'title':'大千世界,近在眼前',
                 'subtitle':'互联网技术带来了第四次工业革命，带来了空前的变革,搭上这趟快车，您将拥有无限可能!'},
                       
                     {'editor':'com-top-caption',
                      'image_url':static_url('mobile/python.jpg'),
                      'class':'white-bg material-wave',
                      'css':'.white-bg{background-color:white;margin:.4rem 0}',
                      'title':'核心技术',
                      'sub_title':'Python+Django+Vuejs技术架构，非前后端分离的全栈式开发,1-2天快速响应'},
                     {'editor':'com-top-caption',
                      'image_url':static_url('mobile/v2_q7sorp.jpg'),
                      'class':'white-bg material-wave',
                      'title':'公司理念',
                      'location':'right',
                      'sub_title':'任何功能可追踪至一线开发人员，快速解决问题，不做营销型公司。'},
                     
                    {'editor':'com-top-caption',
                      'image_url':static_url('mobile/v2_q7sq2e.jpg'),
                      'class':'white-bg material-wave',
                      'title':'服务项目',
                      'sub_title':'管理系统开发,数据爬取、挖掘分析,公众号与小程序等。'},
                     
                    #{'editor':'com-top-html','html':get_value('cfg.home_html','')},
                    
                    ],
                 'footer':self.get_footer(0)
                 }
             }
    def get_footer(self,index):
        return {
            'editor':'com-top-footer-btn-pannel',
            'active':index,
            'items':[
                {'label':'首页','icon':'home-o','action':'location = "/mb/home" '},
                {'label':'演示实例','icon':'gem-o','action':'location = "/mb/example"'},
                {'label':'最新文章','icon':'description','action':'location = "/mb/article"'},
                {'label':'联系我们','icon':'phone-o','action':'location = "/mb/contact"'}
              
            ]
        }

mb_page.update({
    'home':Home
})