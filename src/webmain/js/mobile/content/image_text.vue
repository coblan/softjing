<template>
    <div class="com-image-text">
        <img class="icon" :src="ctx.icon" alt="">
        <div class="detail">
            <div class="title" v-text="ctx.title"></div>
            <div class="content" v-html="ctx.content"></div>
        </div>
    </div>
</template>
<script>
    export default {
        props:['ctx']
    }
</script>

<style scoped lang="scss">
.com-image-text{
    display: flex;
    padding: .2rem;
    border-top: 1px solid #ececec;
    margin: .3rem 0;
    align-items: center;
}
.icon{
    width: .6rem;
    height: auto;
    padding: .2rem;
    flex-shrink: 0;
}
.detail{
    flex-grow: 10;
    padding: .2rem;
}
    .title{
        text-align: center;
        color: green;
        margin: .2rem ;
    }
    .content{
        line-height: .4rem;
        font-size: .26rem;
    }
</style>