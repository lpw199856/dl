<template>

  <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto">
    <el-backtop></el-backtop>
    <el-row>
      <el-col :span="8">
        <h1>  </h1>
      </el-col>
      <el-col :span="8">
      <h1> </h1>
      </el-col>
      <el-col :span="8">
        <h1>筛选</h1>
         <el-switch
    v-model="value"
    active-color="#13ce66"
    inactive-color="#ff4949"
    active-value="100"
    inactive-value="0">

         </el-switch>
      </el-col>
    </el-row>

  <div class="infinite-list-item" v-for="a in this.pageData":gutter="20">
    <el-row :gutter="20">
  <el-col :span="8" v-if="a[0]!==undefined && (value =='100' || a[0].result=='')">
      <el-card :body-style="{ padding: '0px' }">
        <el-row>
      <el-col :span="16">
        <el-image  v-if="a[0]!== undefined"
      style="width: 200px; height: 200px"
      :src=$host+a[0].imgurl.toString()
      />
      </el-col>
          <el-col :span="8">
            <div v-if="a[0]!== undefined">
               <time class="time" >{{ a[0].time | dateFmt('YYYY-MM-DD HH:mm:ss')}}</time>
              <el-alert v-if="a[0].result == ''"
               title="图片未识别成功"
               type="error"
               show-icon
                      :closable="false"
            />
            </div>
          </el-col>
     </el-row>
      </el-card>
  </el-col>
  <el-col :span="8" v-if="a[1]!==undefined && (value =='100' || a[1].result=='')">
      <el-card :body-style="{ padding: '0px' }">
        <el-row>
      <el-col :span="16">
        <el-image  v-if="a[1]!== undefined"
      style="width: 200px; height: 200px"
      :src=$host+a[1].imgurl.toString()
      />
      </el-col>
          <el-col :span="8">
            <div v-if="a[1]!== undefined">
               <time class="time" >{{ a[1].time | dateFmt('YYYY-MM-DD HH:mm:ss')}}</time>
              <el-alert v-if="a[1].result == ''"
               title="图片未识别成功"
               type="error"
               show-icon
                      :closable="false"
            />
            </div>
          </el-col>
     </el-row>
      </el-card>
  </el-col>
  <el-col :span="8" v-if="a[2]!==undefined && (value =='100' || a[2].result=='')">
      <el-card :body-style="{ padding: '0px' }">
        <el-row>
      <el-col :span="16">
        <el-image  v-if="a[2]!== undefined"
      style="width: 200px; height: 200px"
      :src=$host+a[2].imgurl.toString()
      />
      </el-col>
          <el-col :span="8">
            <div v-if="a[2]!== undefined">
               <time class="time"> {{ a[2].time | dateFmt('YYYY-MM-DD HH:mm:ss')}}</time>
               <el-alert v-if="a[2].result == ''"
               title="图片未识别成功"
               type="error"
               show-icon
                      :closable="false"
            />
            </div>
          </el-col>
     </el-row>
      </el-card>
  </el-col>
</el-row>
   <el-divider/>
  </div>
  </ul>

</template>

<script>
    export default {
        name: "digits",
      data(){
          return{
            pageData:[],
            count:0,
            value:'100',
          };
      },
      created(){
          var that = this
              this.$axios
                .get(this.$host+"new_demo/img/")
                .then(res=>{console.log(res);

                var result=[];
　　      for(var i=0,len=res.data.length;i<len;i+=3){
　             result.push(res.data.slice(i,i+3));
　　      }
            this.pageData=result;
                console.log(this.pageData)
                  console.log(localStorage.getItem('Authorization'))
                  })
                .catch(err => {
                  console.log(err);
                });

      },
      methods:{
          load(){

          },
      }
    }
</script>

<style scoped>

</style>
