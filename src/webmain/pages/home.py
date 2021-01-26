from helpers.pcweb.shotcut import web_page_dc
from webmain.models import Banner
from helpers.maintenance.update_static_timestamp import static_url
#from webmain.mobile_pages.home import get_service_html

class SoftJingHome(object):
    def __init__(self, request, engin):
        pass
    def get_template(self):
        return 'pcweb/pcweb.html'
    
    def get_label(self):
        return '成都竞嘉信息科技有限公司'
    
    def get_context(self):
        banners = []
        for banner in Banner.objects.filter(status=1).order_by('order'):
            dc = {
                'name':banner.pk,
                'label':banner.title,
                'editor':'com-swiper-image',
                'image_url':banner.cover,
            }
            if banner.link:
                #dc['click_express']= "location='%s'"%banner.link
                dc['link_express']= "rt='%s'"%banner.link
            banners.append(dc)

        return {
            'tops':[
                {'editor':'com-top-swiper-fade',
                 'items': banners,
                 'delay':10000,
                 'class':'bigbanner',
                 'css':'.bigbanner{height:450px}',
                 
                 #[ 
                    #{'name':'1','label':'犀牛','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/RhinosOxpecker_ZH-CN6392794613_1920x1080.jpg'},
                    #{'name':'2','label':'鸟类','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/PuffinSharing_ZH-CN6330890743_1920x1080.jpg'},
                    #{'name':'3','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/OverwinteringMonarchs_ZH-CN0248511586_1920x1080.jpg'},
                    #{'name':'4','editor':'com-swiper-image','image_url':'http://h1.ioliu.cn/bing/HairyHighlanders_ZH-CN5546635143_1920x1080.jpg'},
                #]
                 },
                {'editor':'our-service','items':[
                    {'cover':static_url('image/管理.png'),
                     'title':'管理系统',
                     'content':'''<ul>
                     <li>10年积累的管理后台开发框架，成熟高效，自主可控。</li>
                     <li>Python+Vue结合,借势当前最火的技术，保证了我们的产品的先进性。</li>
                     <li>开发人员经验丰富,组织结构简洁,对产品的长期维护有保障。</li>
                     </ul>'''
                     #'除ERP,CMS等传统管理系统，还能根据用户需求开发各种定制后台系统。采用高效语言与框架进行开发，除了保证效率外，还能提高系统稳定性'
                     },
                    {'cover':static_url('image/微信公众号.png'),'title':'微信',
                     'content':'''<ul>
                     <li>公众号开发.</li>
                     <li>小程序开发.</li>
                     <li>附带的管理后台,让您可以轻松掌控系统.</li>
                     </ul>'''
                     #'微信公众号，小程序开发。采用最新H5技术，大幅提升开发效率，降低用户成本。为您配备强大的系统管理后台，让您可以轻松掌控系统。'
                     }, 
                    {'cover':static_url( 'image/icon-rgb_机器学习算法引擎.png'),'title':'基于AI的数据统计分析',
                     'content':'''<ul>
                     <li>数据渲染有呈现。</li>
                     <li>基于机器学习的数据分析与信息挖掘。</li>
                     </ul>'''
                     #'各种数据渲染与呈现，普通数据分析，以及基于机器学习的信息挖掘等。'
                     },
                
                    ]},
                #{'editor':'cus-our-service',**get_service_html()},
                
                #{'editor':'com-top-block-ctn','title':'我们的服务','sub_title':'灵活多变,以人为本。',
                 #'items':[
                    #{'editor':'com-ti-caption','class':'wow zoomIn dh-1','css':'.dh-1{height:380px}',
                     #'image_url':static_url('image/admin_sys2.jpg'),
                     #'title':'管理系统','sub_title':'契合业务的管理系统是您的秘密武器!'},
                    #{'editor':'com-ti-caption','class':'wow zoomIn dh-1',
                     #'image_url':static_url('image/admin_sys2.jpg'),
                     #'title':'公众号',
                     #'sub_title':'移动互联网时代'},
                    #{'editor':'com-ti-caption','class':'wow zoomIn dh-1',
                     #'image_url':static_url('image/admin_sys2.jpg'),
                     #'title':'开发中','sub_title':'开发中'},
                    #{'editor':'com-ti-caption','class':'wow zoomIn dh-1',
                     #'image_url':static_url('image/admin_sys2.jpg'),
                     #'title':'开发中','sub_title':'犀牛'},
                   
                    #]},
                    
                                   
                {'editor':'com-top-block-ctn',
                 'title_editor':'com-block-title-line',
                 'title':'关于我们',
                 'sub_title':'ABOUT US',
                 'css':'.about_us{background-color:#100e4e;color:white} .about_us .title{color:white}',
                 'class':'about_us',
                 'items':[
                    #{'editor':'com-about-us'},
                    {'editor':'com-ui-html',
                     'class':'about-us',
                     'css':'''.about-us{
                      width: 90%;
                      text-align: left;
                      padding: 20px 100px;
                      color: #cacaca;
                      font-size: 110%;
                      line-height:40px;
                     }''',
                     'html':'''<div>
                     <p>竞嘉主要由富有经验的全栈开发人员组成，我们拥有完全自主研发的开发框架，具备深度/灵活定制化系统的能力。我们的服务对象主要是中小型企业及部分个人用户。为客户提供精简和有针对性的专门化系统。</p>
                     <p>我们追求几个点:开发效率高一点,用户成本低一点,维护时间长一点,系统成熟一点。</p>

        <p>未来我们会陆续推出AI/机器学习方面的相关服务，例如企业数据透视图，信息提取与分析等。</p>
        </div>
                    '''}
                ]},
                
                {'editor':'com-top-transparent-ctn',
                 'image_url':static_url('image/desert-4791919_1280.jpg'),
                 'title':'大千世界,近在眼前',
                 'subtitle':'互联网技术带来了第四次工业革命，带来了空前的变革,搭上这趟快车，您将拥有无限可能!'}, #'image_url':'http://h1.ioliu.cn/bing/BlueChip_ZH-CN7376022522_1920x1080.jpg'},
                
 
                
                {'editor':'com-top-block-ctn',
                 'title_editor':'com-block-title-line',
                 'title':'我们的特点',
                 'sub_title':'与众不同，独领风骚',
                 'items':[
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':static_url( 'image/admin_sys.jpg' ),
                     'title':'新技术高效率','sub_title':'python+django+vuejs模块化开发，速度惊人'} ,
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':static_url( 'image/collective-3300872_640.png' ),
                     'title':'模块化低成本',
                     'sub_title':'模块化开发，人力成本降低，费用大幅减少'} ,
                    {'editor':'com-ti-caption2','class':'wow zoomIn',
                     'image_url':static_url( 'image/owl-50267_640.jpg' ),
                     'title':'全站开发易维护',
                     'sub_title':'全栈开发，程序统一而连贯，极大提高程序的可维护性。使得项目长期维护成为可能。灵活多变。'} ,
                ]}
                #{'editor':'com-slide-win','images':[
                    #{'url':'xxx'},
                    #{'url':'bbb'},
                #]}
            ]
        }

web_page_dc.update({
    'home':SoftJingHome
})