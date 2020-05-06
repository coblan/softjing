<template>
    <div class="cus-our-service">
        <div class="web-wrap">
            <h2 class="title">我们的服务</h2>
            <div class="content">
                <p >我们拥有精简的人员配置，主要由富有经验的全栈开发人员组成。我们拥有完全自主研发的开发框架，具备深度/灵活定制化系统的能力。我们的服务对象主要是中小型企业及部分个人用户。为客户提供精简和有针对性的专门化系统。

                </p>
                <p> 未来我们会陆续推出AI/机器学习方面的相关服务，例如企业数据透视图，信息提取与分析等。</p>

                <div class="service-item">
                    <div class="brand">
                        管理后台
                    </div>
                    <div class="service-content">
                        主要是借助浏览器(前端)+python(后端)的架构，为用户提供软件服务。传统的大公司开发的ERP,OA等管理软件功能繁杂，人员需要培训，使得普通用户比较抵触，而我们追求的是小巧，易用和几乎不需要培训的软件。根据用户的需求，富有针对性的定制化软件，砍掉那些用不到的功能，这就是我们存在的意义。
                    </div>
                </div>
                <div class="service-item">
                    <div class="brand">
                        H5开发
                    </div>
                    <div class="service-content">
                        采用vue.js等流行的前端技术，进行模块化H5开发。拥有自主开发框架，能够快速开发公众号和web网站，成本低廉。
                    </div>
                </div>
                <p>
                    除了单独开发软件外。我们还积极的参与到软件外包服务中。如果您的项目需要专业的全栈开发技术，可以联系我们。我们除了拥有技术外，还有诚意。
                </p>
            </div>

        </div>

    </div>
</template>
<script>
    export default {
        props:['ctx'],
    }
</script>
<style scoped lang="scss">
    .cus-our-service{
        margin: 60px 0;

    }
.title{
    text-align: center;
}
.content{
    width: 80%;
    margin: auto;
    color: #767676;
}
    .service-item{
        margin: 40px 10px;
        align-items:center;
        display:flex;
        .brand{
            margin: 10px 30px;
            flex-shrink: 0;
            width: 110px;
            height: 110px;
            border-radius: 58px;
            border: 3px solid grey;
            text-align: center;
            line-height: 110px;
            box-shadow: 0px 0px 10px #ABABAB;
        }

    }
</style>