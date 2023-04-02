<template>
  <div id="app">
    
    <div>
      <NavBar v-if="islogin"/>
      <br>
      <router-view :loginstatus="islogin" @check-login="checklogin"/>
      <br>
    </div>
    
  </div>
</template>

<script>

import NavBar from './components/NavBar.vue';



export default {
    name: "App",
    components: { NavBar },
    data() {
      return{
        islogin: true
      }

    },
    methods:{
      checklogin() {
        if (localStorage.getItem('email')){
          this.islogin = true;
        }
        else{
          this.islogin = false;
        }
      }
    },
    beforeUpdate(){
      console.log('in check login')
      this.checklogin()
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;   
}
</style>
