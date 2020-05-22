<template>
  <el-row>

  <el-col :span="8"><h1> </h1>  </el-col>
  <el-col :span="8">
    <p font-family="PingFang SC" style="font-size:20px line-height:1.3">登录</p>
     <el-card shadow="always">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="账号密码登录" name="first">
        <el-row>
          <el-col :span="2"><i class="el-icon-user"></i></el-col>
          <el-col :span="22"><el-input v-model="username" name="userID" placeholder="账号"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :span="2"><i class="el-icon-key"></i></el-col>
          <el-col :span="22"><el-input v-model="pwd" name="password" placeholder="密码" show-password></el-input></el-input></el-col>
        </el-row>
        <el-button @click="handleLogin">登录</el-button>
    </el-tab-pane>
    <el-tab-pane label="手机短信登录" name="second">
        <el-row>
          <el-col :span="2"><i class="el-icon-phone-outline"></i></el-col>
          <el-col :span="22"> <el-input v-model="phone" name="phone" @input="change($event)"placeholder="手机号"></el-input></el-col>
        </el-row>
        <el-row>
          <el-col :span="2"><i class="el-icon-chat-dot-square"></i></el-col>
          <el-col :span="22"><el-input v-model="sms" name="sms"  @input="change($event)" placeholder="验证码" ></el-input></el-col>
        </el-row>
         <el-button @click="smslogin">登录</el-button>
         <el-button @click="getsms" icon="el-icon-s-promotion" type="primary">获取验证码</el-button>
    </el-tab-pane>
  </el-tabs>
     </el-card>
  </el-col>
  <el-col :span="8"> </el-col>
  </el-row>

</template>

<script>
  import { mapMutations } from 'vuex';
    export default {

        name: "login",
      data(){
          return {
            username:'',
            pwd:'',
            token:localStorage.getItem('Authorization'),
             activeName: 'first',
            token2:localStorage.getItem('Authorization2'),
            phone:'',
            sms:'',
            //token:false
          }
      },
      methods:{
        ...mapMutations(['changeLogin']),
          handleLogin(){
             var that = this
             let token = localStorage.getItem('Authorization');
             let token2=localStorage.getItem('Authorization2');
              // console.log(this.token),
              this.$axios
                .put(this.$host+"new_demo/users/",{
                      username:this.username,
                      password:this.pwd,
                      token:this.token,
                      token2:this.token2,
                      project:"1"
                }).then(res=>{
                      console.log(res)
                      if(res.data.code==1000) {
                      this.userToken = res.data.token;
                      this.userToken2 = res.data.token2;
                      // 将用户token保存到vuex中
                      this.loginon=res.data.loginon
                      this.changeLogin({Authorization: this.userToken,loginon:this.loginon,Authorization2:this.userToken2});
                      this.$router.push({path: '/'})

                    }
              })
                .catch(err => {
                  console.log(err);
                });
          },
          getsms(){
              var that = this
              console.log(this.phone)
              this.$axios.put(this.$host+"new_demo/sms/",{
                phone:this.phone
              })
          },
        smslogin(){
          var that = this
          this.$axios
                .put(this.$host+"new_demo/users/",{
                      phone:this.phone,
                      sms:this.sms,
                      project:"2"
                }).then(res=>{
                      console.log(res)
                      if(res.data.code==1000) {
                      //this.userToken = res.data.token;
                      // 将用户token保存到vuex中
                      //this.loginon=res.data.loginon
                      this.changeLogin({loginon:this.loginon});
                      this.$router.push({path: '/'})

                    }
              })
                .catch(err => {
                  console.log(err);
                });
        },
        change(e){
          this.$forceUpdate()
        },
         handleClick(tab, event) {
        console.log(tab, event);
      },
      },

      }
</script>

<style scoped>
 .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 480px;
  }
</style>
