<template>
  <div class="cmap-topbar">
    <div class="header">
      <div class="header-left">
        <div class="logo">
          <img src="../../public/static/logo.png" alt="logo">
        </div>
        <div class="menu">
          <ul>
            <li><a>首页</a></li>
            <li><a>校园频道</a></li>
            <li><a>跳蚤市场</a></li>
            <li><a>今日校园</a></li>
            <li><a>平台介绍</a></li>
          </ul>
        </div>
      </div>
      <div class="header-right" v-if="flag1">
        <div class="search">
          <input type="text" placeholder="搜索">
        </div>

        <ul>
          <li @click="login_show"><span class="glyphicon glyphicon-user" aria-hidden="true"></span>
            <router-link to='./login'>登录</router-link>
          </li>
          <li><span class="glyphicon glyphicon-level-up" aria-hidden="true"></span><a>注册</a></li>
        </ul>
      </div>

      <div class="header-right" v-if="flag2">
        <div class="search">
          <input type="text" placeholder="搜索">
        </div>
        <ul>
          <li><img src="../../public/favicon.png" alt="用户头像"></li>
          <li @mouseover="userinfo_show"><a>个人中心</a></li>
        </ul>
        <div class="box" v-if="flag3" @mouseleave="userinfo_hidden">
          <div class="usr-info">
            <ul>
              <li><a>用户名</a></li>
              <li><a>个人信息</a></li>
              <li><a>设置</a></li>
              <li><a>退出</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import HLogin from './HLogin.vue'
  // import axios from "axios"
  export default {
    data() {
      return {
        flag1: true,
        flag2: false,
        flag3: false,
        msurl: 'http://localhost:8080/img/logo.png'
      }
    },
    methods: {
      login_show() {
        // this.flag3 = HLogin.data().logstate
        console.log(HLogin.data().logstate)
      },
      userinfo_show() {
        this.flag3 = true
      },
      userinfo_hidden() {
        this.flag3 = false
      },
      change(){
        this.flag3 = true,
        this.flag2 = false,
        console.log(1111111111111)
      }

    },
    // created() {
    //   this.axios.get('http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20').then(res => {
    //     console.log(res)
    //   })
    // }
  }
</script>

<style lang="less" scoped>
  .cmap-topbar {
    background-color: #333;

  }

  .header {
    display: flex;
    align-items: center;
    align-items: center;
    justify-content: space-between;
    color: #b0b0b0;
    margin: 0px 20px;

    ul {
      font-size: 18px;
      margin: 0;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;

      li {

        height: 40px;
        list-style: none;
        padding: 0px;
        margin: 10px 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;

        a {
          display: inline-block;
          text-decoration: none;
          margin-left: 5px;
          color: #b0b0b0;

          &:hover {
            color: #fff;
          }
        }
      }
    }

    .header-left {
      display: flex;
      align-items: center;
      justify-content: center;

      .logo {
        margin-right: 20px;

        // background-color: wheat;
        overflow: hidden;

        img {
          height: 40px;
          width: 100px;
        }
      }
    }

    .header-right {
      display: flex;
      align-items: center;
      justify-content: center;

      img {
        height: 40px;
        width: 40px;
        border: 1px solid white;
        background-color: wheat;
        border-radius: 20px;
        overflow: hidden;
      }

      .search {
        margin-right: 50px;

        input {
          width: 200px;
          height: 32px;
          padding: 0 3%;
        }
      }
    }

    .box {
      position: absolute;
      top: 10px;
      right: 1%;
      .usr-info {
        margin-top: 50px;
        background-color: rgba(0, 0, 0, 0.8);
        border-radius: 0 0 5px 5px;

        ul {
          flex-direction: column;
        }
      }
    }
  }
</style>
