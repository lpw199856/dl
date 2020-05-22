<template>
<el-container>
  <el-header>
    <el-container>
      <el-aside width="200px" color="#409EFF"><h2></h2></el-aside>
      <el-main>
        <el-row>
          <el-col :span="8"><h1>  </h1></div></el-col>
          <el-col :span="8" ><h2 font-family="PingFang SC" style="font-size:20px line-height:1.3" >识别程序管理</h2></el-col>
          <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
        </el-row>

      </el-main>
</el-container>

  </el-header>
  <el-container>
    <el-aside width="200px">
    <el-menu default-active="1" class="el-menu-vertical-demo">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>分类展示</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="1-1">
                <el-button class="button" type="primary" plain @click="goletter">letter</el-button>
              </router-link>
          </el-menu-item>
          <el-menu-item index="1-2">
                <el-button class="button" type="primary" plain @click="godigits">数字</el-button>
                </router-link>
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-menu"></i>
        <span>统计</span>
        </template>
          <el-menu-item index="2-1">
           <el-button class="button" type="primary" plain @click="gostatistics">统计</el-button>
            </router-link>
          </el-menu-item>
      </el-submenu>
      <el-menu-item index="3">
        <i class="el-icon-hot-water"></i>
        <span slot="title" @click="home">主页</span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title" @click="out">退出</span>
      </el-menu-item>
    </el-menu>
  </el-aside>
    <el-main><router-view/></el-main>
  </el-container>
</el-container>
</template>

<script>
  import { mapMutations } from 'vuex';
    export default {
        name: "home",
      methods:{
          ...mapMutations(['changeLogin']),
      goletter(){
         let token = localStorage.getItem('Authorization');
         let loginon =localStorage.getItem('loginon');
         if (loginon == 'false' || token == null) {
                 this.$router.push({path: '/login'})
               } else {
           this.$router.push({path: '/letter'})
         }
      },
        godigits(){
         let token = localStorage.getItem('Authorization');
         let loginon =localStorage.getItem('loginon');
         if (loginon == 'false' || token == null) {
                 this.$router.push({path: '/login'})
               } else {
           this.$router.push({path: '/digits'})
         }
      },
        gostatistics(){
         let token = localStorage.getItem('Authorization');
         let loginon =localStorage.getItem('loginon');
         if (loginon == 'false' || token == null) {
                 this.$router.push({path: '/login'})
               } else {
           this.$router.push({path: '/statistics'})
         }
      },
        home(){
         let token = localStorage.getItem('Authorization');
         let loginon =localStorage.getItem('loginon');
         if (loginon == 'false' || token == null) {
                 this.$router.push({path: '/login'})
               } else {
           this.$router.push({path: '/'})
         }
      },
        out(){
            this.$confirm('是否退出?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.changeLogin({Authorization: null,Authorization2: null,loginon:'false'});
          this.$router.push({path: '/login'});
          this.$message({
            type: 'success',
            message: '再见!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '欢迎继续使用'
          });
        });

        }

    }
    }

</script>

<style scoped>

</style>
