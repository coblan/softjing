<template>
    <div class="cus-our-service">
        <div class="web-wrap">
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
                    <div class="service-content" v-html="ctx.h5"> </div>
                </div>
                <div v-html="ctx.after_content"></div>
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