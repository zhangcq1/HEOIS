<template>
  <div class="HLogin">
    <div class="HLogin-Left">
      <div class="Logo"><img src="../../public/static/logo.png"></div>
      <div>
        <h2>校园互助平台</h2>
      </div>
      <div class="Introduction">
        <span>作者 工作室</span>
        <p>大学生奖赏互助平台是一个为在校大学生提供的免费平台,你可以在平台上发布任务,如代取快递,外卖代取,商品代买,以及二手商品出售,
          我们平台将免费为你们展示任务信息,接收任务的学生可以通过接受任务,来获得你的联系方式来处理你发布的任务,同时你也可以领取别人的
          任务来获取报酬.
        </p>
      </div>
      <div class="LFoot">
        <p>测试版-校园互助平台</p>
      </div>
    </div>

    <div class="HLogin-Right">
      <div class="RHeader">
        <h2 @click="test">登录</h2>
      </div>
      <div class="RBody">
        <form>
          <!-- action="" method="post" -->
          <input type="text" placeholder="请输入用户名" v-model="username" />
          <input type="password" placeholder="请输入密码" v-model="password" />
          <div class="identifybox">
            <input placeholder="请输入验证码" v-model="yzm" />
            <identify v-on:update:value="getCode" ref="child"></identify>
          </div>
          <input class="submit" type="button" value="登录" @click="Hlogin">
        </form>
      </div>
      <div class="RFoot">
        <p>使用其他方式登录</p>
      </div>
    </div>
  </div>
</template>

<script>
  import identify from '../components/identify.vue'
  export default {
    data() {
      return {
        iconclass: 'icon-yonghu',
        username: '',
        password: '',
        yzm: "",
        yzmcode: '',
      }
    },
    props: {

    },
    components: {
      identify
    },
    methods: {
      getCode(data) {
        this.yzmcode = data
          console.log(data)
      },
      Hlogin() {
        if (this.yzmcode.toUpperCase() === this.yzm.toUpperCase()) {
          this.axios({
              url: '/api/user/login/',
              method: "post",
              data: {
                username: this.username,
                password: this.password,
              },
              transformRequest: [function(data) {
                // Do whatever you want to transform the data
                let ret = ''
                for (let it in data) {
                  // 如果要发送中文 编码
                  ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
                }
                return ret
              }],
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
              }
            })
            .then(function(response) {
              console.log(response.data.state)
              if (response.data.state) {
                alert('登录成功')
              } else {
                alert('用户名或密码错误')
              }
            })
            .catch(function(error) {
              console.log(error)
            })
        } else {
          alert('验证码错误')
          this.$refs.child.refreshCode()
        }

      },

      test() {
        this.axios.get('/api/user/getuser').then(response => {
          if (response.data) {
            console.log(response.data)
          }
        }).catch(err => {
          alert('请求失败')
        })
      }
    },

  }
</script>

<style lang="less" scoped>
  * {
    margin: 0;
    padding: 0;
    font-family: "黑体";
  }

  .HLogin {
    height: 600px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50px;

    div {
      width: 480px;
      height: 500px;
    }

    .HLogin-Left {
      border-radius: 6px 0 0 6px;
      display: flex;
      color: white;
      flex-direction: column;
      align-content: space-between;
      align-items: center;
      justify-content: center;
      box-shadow: 10px 10px 10px rgba(64, 74, 94, 0.5);
      background-color: rgba(64, 74, 94);

      div {
        padding: 20px 60px;
      }

      .Logo {
        padding: 0px 48px;
      }

      img {
        margin-top: 50px;
        display: block;
        width: 200px;
        height: 80px;
      }

      h2 {
        display: block;
        color: white;
      }

      .Introduction {
        span {
          color: rgba(255, 255, 255, 0.3);
        }
      }

      .LFoot {
        p {
          border-top: 1px solid rgba(255, 255, 255, 0.6);
          padding-top: 20px;
        }
      }
    }

    .HLogin-Right {
      border-radius: 0 6px 6px 0;
      display: flex;
      box-shadow: 10px 10px 10px rgba(64, 74, 94, 0.5);
      background-color: rgba(255, 255, 255);
      border: 1px solid;
      border-left: none;
      flex-direction: column;
      align-content: space-between;
      align-items: center;
      justify-content: center;

      div {
        padding: 20px 60px;
      }

      .RHeader {
        h2 {
          margin-top: 50px;
          font-weight: 700;
        }
      }

      .RBody {
        display: flex;
        flex-direction: column;
        align-content: space-between;
        align-items: center;
        justify-content: center;

        input {
          margin-bottom: 26px;
          display: block;
          width: 350px;
          height: 40px;
          border: 1px solid rgba(0, 0, 0, 0.2);
          color: rgba(0, 0, 0, 0.6);
          padding: 0 3%;
          border-radius: 4px;
        }

        .identifybox {
          margin-bottom: 26px;
          display: block;
          width: 350px;
          height: 40px;
          padding: 0%;
          border-radius: 4px;
          display: flex;
          align-items: center;
          justify-content: space-between;

          input {
            width: 220px;
            margin-bottom: 0;

          }
        }

        .submit {
          background-color: #f38d30;
          margin-bottom: 0;
        }
      }

      .RFoot {}
    }
  }
</style>
