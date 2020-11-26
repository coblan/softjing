import example_info from './example_info.vue'
import our_service from  './our_service.vue'
import contact from  './contact.vue'
import  example_content from './pcpage/example_content.vue'
import  com_service from  './pcpage/service.vue'

Vue.component('com-example-info',example_info)
Vue.component('cus-our-service',our_service)
Vue.component('cus-contact',contact)
Vue.component('com-example-content' ,example_content)
Vue.component('our-service',com_service)

import * as mb_main from   './mobile/main'

import * as pcuis_main from  './pcuis/main.js'