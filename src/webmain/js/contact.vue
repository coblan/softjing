<template>
    <div class="cus-contact">
        <div  class="wechat">
            <img :src="ctx.wechat_qr" alt="">
        </div>
        <div style="margin: .2rem;text-align: center">扫码添加客服微信</div>
    </div>
</template>
<script>
    export default {
        props:['ctx']
    }
</script>
<style scoped lang="scss">
.cus-contact{

        position: absolute;
        top:50%;
        left: 50%;
        transform: translate(-50%,-50%);
        img{
            width: 200px;
            height: auto;
        }

}
</style>