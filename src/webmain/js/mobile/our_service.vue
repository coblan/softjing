<template>
    <div class="cus-mb-our-service">
        <h2 class="title">我们的服务</h2>
        <div class="content">
            <div v-html="ctx.about_us"></div>

            <div class="service-item">
                <div class="brand">
                    管理后台
                </div>
                <div class="service-content" v-html="ctx.admin_backend"> </div>
            </div>
            <div class="service-item">
                <div class="brand">
                    H5开发
                </div>
                <div class="service-content" v-html="ctx.h5">   </div>
            </div>
            <div v-html="ctx.after_content"></div>
        </div>
    </div>
</template>
<script>
    export default {
        props:['ctx']
    }
</script>
<style scoped lang="scss">
.cus-mb-our-service{
    padding: 1rem .2rem .4rem .2rem;
}
    .title{
        font-weight: bold;
        font-size: .36rem;
        text-align: center;
        color: #303030;
    }
    .content{
        margin: .2rem 0;
        color: #727272;
        letter-spacing: .02rem;
        line-height: .42rem;

        .service-item{
            position: relative;
            padding: .2rem;
            font-size: .28rem;
            margin: .2rem;
            /*border: 1px solid #c7c7c7;*/
            .brand{
                /*position: absolute;*/
                /*top:.2rem;*/
                /*left: .4rem;*/
                font-weight: bold;
                margin-bottom:.2rem;
                color: #626262;
            }
        }
    }
</style>