<template>
  <div>
<el-carousel :interval="4000" type="card" height="400px">
    <el-carousel-item v-for="item in this.index " :key="item.id">
      <img
      :src=$host+item.url
      />
    </el-carousel-item>
</el-carousel>
  </div>
</template>

<script>
    export default {
        name: "test1",
      data(){
          return{
            pageData:[],
            index:new Array(),
          };
      },
      created(){
               this.$axios
                .get(this.$host+"new_demo/img/")
                .then(res=>{console.log(res)
                   this.pageData=res.data
                   this.index[0] = { url:this.pageData[Math.floor(Math.random() * this.pageData.length)].imgurl,id:0}
                   this.index[1] = { url:this.pageData[Math.floor(Math.random() * this.pageData.length)].imgurl,id:1}
                   this.index[2] = { url:this.pageData[Math.floor(Math.random() * this.pageData.length)].imgurl,id:2}
                   this.index[3] = { url:this.pageData[Math.floor(Math.random() * this.pageData.length)].imgurl,id:3}
                   this.index[4] = { url:this.pageData[Math.floor(Math.random() * this.pageData.length)].imgurl,id:4}
                   this.index[5] = { url:this.pageData[Math.floor(Math.random() * this.pageData.length)].imgurl,id:5}
                   console.log(this.index)
                   this.$forceUpdate();
                ;})

      }
    }

</script>

<style scoped>
 .el-carousel__item img {
    width: 500px;
    height: 400px;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
