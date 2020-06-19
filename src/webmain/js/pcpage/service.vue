<template>
    <div class="com-service">
        <div class="web-wrap">
            <div class="title">
                <div style="font-weight: bold;font-size: 130%;padding: 8px;" >业务服务</div>
                <span style="color: #979797;font-size: 80%;">应用最新技术、高效灵活。</span>
                <div>
                    <div style="width: 50px;border-bottom: 2px solid #0aa938;display: inline-block;padding-top: 8px"></div>
                </div>

            </div>

            <div class="content web-wrap">
                <div class="item" v-for="item in items">
                    <img :src="item.cover" alt="">
                    <div class="item-title" v-text="item.title"></div>
                    <div v-text="item.content"></div>
                </div>

            </div>

        </div>
    </div>
</template>
<script>
    export default {
        props:['ctx'],
        data(){
            return {
                items:this.ctx.items
            }
        }
    }
</script>

<style scoped lang="scss">
    .com-service{
        margin-bottom: 60px;
    }
    .content{
        width: 80%;
        display: flex;
        justify-content: space-around;


    }
    .item-title{
        font-size: 120%;
        color: green;
        padding: 20px;
    }
    .item{
        margin-top: 50px;
        text-align: center;
        padding: 20px;
        width: 300px;
    }
    .com-service{
        padding-top: 50px;
    }
.title{
    text-align: center;
}
</style>