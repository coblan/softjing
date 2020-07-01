<template>
    <div class="com-example-content">
        <div>
            <div class="title">
                管理后台
            </div>

            <div style="margin-top: 50px;">
                <div>
                    <div >
                        这里是一个演示管理后台，包括了一些实用的功能
                    </div>
                    <ol style="margin-top: 20px;">
                        <li>部门管理</li>
                        <li>颜色管理</li>
                        <li>权限管理</li>
                    </ol>
                </div>
                <p>
                    <a href="http://demo.softjing.com/" target="_blank">演示后台 (pc端适配)</a>
                    <a href="http://demo.softjing.com/doc" style="display: inline-block;margin-left: 20px" target="_blank">说明文档</a>
                </p>

                <div>
                    <div>账号:demo</div>
                    <div>密码:demo</div>
                </div>

            </div>
        </div>
        <div style="margin-top: 100px">
            <div class="title">
                移动端
            </div>
            <div style="margin-top: 50px">
                <div class="mobile">
                    <div>
                        易职通求职是一个本地求职的公众号。
                        <ol>
                            <li>H5页面(公众号入口),手机扫描二维码进入</li>
                            <li>管理后台 </li>
                        </ol>
                        <div style="margin-bottom: 15px">
                            <a href="http://job.softjing.com/pc" target="_blank">管理后台(pc端适配)</a>
                        </div>
                        <div>
                            账号:demo
                        </div>
                        <div>
                            密码:demo
                        </div>
                    </div>
                    <div class="qr">

                        <img src="/d/qr?content=aHR0cDovL3d3dy5iYWlkdS5jb20=&encode=base64" alt="">
                        <div  class="lit-grey">
                            扫描二维码进入页面
                        </div>
                    </div>
                </div>
                <div class="mobile">
                    <div>星月山湖是某某房地产项目宣传页面。可以向客户展示户型结构。</div>
                    <div class="qr">
                        <img src="/d/qr?content=aHR0cDovL3h5LmVuam95c3QuY29tL21iL2luZGV4P19saXZlPWxpdmUtaG9tZQ==&encode=base64" alt="">
                        <div class="lit-grey">
                            扫描二维码进入页面
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
    export default {
        props:['ctx']
    }
</script>
<style scoped lang="scss">
.com-example-content{
    padding: 80px 150px;
    /*border-radius: 10px;*/

}

.title{
    font-weight: bold;
    font-size: 24px;
    text-align: center;
}
.mobile{
    display: flex;
    border-bottom: 1px solid #bdbdbd;
    margin-bottom: 40px;
    padding-bottom: 20px;
    justify-content: space-between;

    .qr{
        text-align: center;

        img{
            width: 200px;
            height: auto;
        }
        .lit-grey{
            color: #9e9e9e;
        }
    }

}
</style>