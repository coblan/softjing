<template>
    <div class="cus-mb-contact">
        <div class="content">

            <div  style="margin: .2rem" class="wechat">
                <img :src="ctx.wechat_qr" alt="">
            </div>
            <div style="margin: .2rem;text-align: center">扫码添加客服微信</div>
        </div>
    </div>
</template>
<script>
    export default {
        props:['ctx'],
        basename:'cus-live-mb-contact'
    }
</script>
<style scoped lang="scss">
.cus-mb-contact{
    position: relative;
    height: calc(100vh - 80px);
    background-color: white;
    width:100vw;
    .content{
        position: absolute;
        top:50%;
        left:50%;
        transform:translate(-50%,-50%);
        color: grey;

        .wechat{
            img{
                width: 4rem;
                height: auto;
            }
        }
    }
}
</style>