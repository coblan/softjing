import example_info from './example_info.vue'
import our_service from  './our_service.vue'
import contact from  './contact.vue'
import  example_content from './pcpage/example_content.vue'

Vue.component('com-example-info',example_info)
Vue.component('cus-our-service',our_service)
Vue.component('cus-contact',contact)
Vue.component('com-example-content' ,example_content)

import * as mb_main from   './mobile/main'