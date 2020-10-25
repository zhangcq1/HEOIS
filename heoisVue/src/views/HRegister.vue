<template>
  <div class="BlogRegister">
    <div class="register_form">
      <div class="form">
        <div class="login_con">
          <div class="welcome" style="color: chocolate">
            <h1>欢迎注册</h1>
          </div>
          <p class="user_info">
            用户名
            <input type="text" name="userName" placeholder="请输入用户名" class="user_info_input">
          </p>
          <p class="user_info">
            密码
            <input type="password" name="userPwd" placeholder="请输入密码" class="user_info_input" />
          </p>
          <p class="user_info">
            确认密码
            <input type="password" name="userPwd" placeholder="确认密码" class="user_info_input">
          </p>
          <p class="user_info">
            手机号
            <input type="text" name="phone" placeholder="请输入手机号" class="user_info_input" />
          </p>
          <p class="user_info">
            验证码
            <input id="yzm" type="text" placeholder="请输入验证码" class="user_info_input">
            <a href="">
              <button type="button" class="get_yzm">获取验证码</button>
            </a>
          </p>
          <div class="btn">
            <a href="">
              <button type="submit" class="register_button">注册</button>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
  * {
    margin: 0;
    padding: 0;
    font-family: "黑体";
  }

  .BlogRegister {
    display: flex;
    width: 100%;
    height: 100%;
    background: url(../../public/static/login/login_bg.jpg) center center;
    background-attachment: fixed;
    min-width: 600px;
    min-height: 100vh;
    background-size: 100% 100%;
    background-repeat: no-repeat;
  }

  .register_form {
    position: static;
    left: 60%;
    min-width: 300px;
    /*margin-top: 100px;*/
    /*margin: 0 auto;*/
    background-attachment: fixed;
    width: 100%;
    /*min-width: 300px;*/
    padding-top: 50px;
    border-radius: 5px;
  }

  .register_button {
    border: none;
    background-color: orangered;
    /*position: relative;*/
    /*left: 25px;*/
    width: 360px;
    height: 50px;
    font-size: 20px;
    color: azure;
    border-radius: 30px;
    display: inline-block;

  }

  .user_info_input {
    /*position: relative;*/
    /*left: 40px;*/
    width: 300px;
    height: 50px;
    border: 1px solid rgb(178, 178, 178);
    border-radius: 6px;
    display: inline-block;
  }

  .user_info {
    margin: 0;
    margin-left: auto;
    margin-right: auto;
  }

  #yzm {
    width: 200px;
    height: 50px;
  }

  .get_yzm {
    width: 90px;
    height: 50px;
  }

  .form {
    border-radius: 20px;
    margin: 0 auto;
    width: 450px;
    padding: 10px;
    background-color: rgba(255, 255, 255, 0.5);
  }

  .login_con {
    text-align: center;
  }

  .welcome {
    display: inline-block;
    font-weight: 400;
  }

  input {
    background: rgba(255, 255, 255, 0.8);
    padding-left: 20px;
  }
</style>
