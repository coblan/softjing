<template>
    <div class="com-example-info">
        <div class="row" v-for="row in rows">
            <h3 v-text="row.title"></h3>
            <div class="cover" :style="cover_url(row)">
            </div>
            <div class="content" v-html="row.content"></div>
        </div>

    </div>
</template>
<script>
    export default {
        props:['ctx'],
        data(){
            return {
                rows:[]
            }
        },
        mounted(){
            var search_args = ex.eval(this.ctx.preset)
            ex.director_call(this.ctx.director_name,search_args ).then((resp)=>{
                this.rows = resp.rows
            })
        },
        computed:{

        },
        methods:{
            cover_url(row){
                return {
                    'background-image': 'url('+row.cover+')'
                }
            }
        }
    }
</script>
<style scoped lang="scss">
.com-example-info{
    padding: 40px;
}
.row{
    margin-bottom: 60px;
}
    .cover{
        width: 800px;
        height: 400px;
        background-size: cover;
        margin: 40px auto;
    }
    .content{
        color: #5c5c5c;
    }
</style>