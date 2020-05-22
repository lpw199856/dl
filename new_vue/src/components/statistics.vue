<template>


  <el-container>
  <el-aside width="200px">
    <el-button type="primary" plain @click="drawLine">刷新</el-button>

  </el-aside>
  <el-main>
    <el-row>
      <el-col :span="18">
         <div id="main" style="width: 600px;height:400px;"/>
      </el-col>
      <el-col :span="6">
        <el-card class="box-card">
         <div>
          <span>总识别率：{{this.z +'%'}}</span>
        </div>
        </el-card>
      </el-col>
    </el-row>

  </el-main>
</el-container>
</template>

<script>
    export default {
        name: "statistics",
        data(){
          return {
            pageData: [],
            datetime :new Array(),
            resultok:new Array(),
            resultno:new Array(),
            datalen :[],
            a:[],
            b:[],
            d:[],
            e:[],
            f:[],
            z:0,
          };
        },
        mounted(){
          this.drawLine();
        },
        created(){

      },
      methods: {
          drawLine() {
            var that = this
              this.$axios
                .get(this.$host+"new_demo/img/")
                .then(res=>{console.log(res);
                this.pageData=res.data;
                for(let i=0;i < this.pageData.length;i++){
                  let date=this.$moment(this.pageData[i].time).format('YYYY-MM-DD')
                  if(!this.datetime[date]){
                    this.datetime[date]=1
                    if(this.pageData[i].result==''){
                      this.resultok[date]=0
                      this.resultno[date]=1
                    }else{
                      this.resultok[date]=1
                      this.resultno[date]=0
                    }
                  }else {
                    this.datetime[date]++
                    if (this.pageData[i].result == '')
                          this.resultno[date]++
                        else
                          this.resultok[date]++
                  }
                  }
                  var c=0,x=0,y=0
                  for(let i in this.datetime){
                    this.a[c]=this.datetime[i]
                    this.d[c]=this.resultok[i]
                    this.e[c]=this.resultno[i]
                    this.b[c]=i
                    this.f[c]= Math.round(this.d[c]/this.a[c]*10000)/100
                    x=x+this.d[c]
                    y=y+this.e[c]
                    c++
                  }
                  console.log(x)
                  console.log(y)
                  this.z=Math.round(x/(y+x)*10000)/100
            var myChart = this.$echarts.init(document.getElementById('main'));
            // 指定图表的配置项和数据
                var option = {
            title: {
                text: '识别统计'
            },
            tooltip: {
              trigger:'axis'
            },
            legend: {
                data:['数量','识别成功','识别失败','识别率(%)']
            },
            toolbox: {
              show: true,
              feature: {
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore: {show: true},
                saveAsImage: {show: true}
                  }
              },
            calculable: true,
            xAxis: {
                data: this.b
            },
            yAxis: {},
            series: [
              {
                name: '数量',
                type: 'bar',
                data: this.a
               },
              {
                name:'识别成功',
                type:'bar',
                data:this.d
              },
              {
                name:'识别失败',
                type:'bar',
                data:this.e
              },
              {
                name:'识别率(%)',
                type:'bar',
                data:this.f
              },
            ]
        };
            myChart.setOption(option);
            this.datetime = new Array
                  })
                .catch(err => {
                  console.log(err);
                });

          }
    }

    }

</script>

<style scoped>
  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 180px;
  }
</style>
