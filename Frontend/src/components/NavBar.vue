<template>
  <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Bloglite_v2</a>

    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav"
      aria-expanded="false" aria-label="Toggle navigation" @click="toggleNavbar()">
      <span class="navbar-toggler-icon"></span>

    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" @click.prevent="$router.push('/dashboard')">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click.prevent="$router.push('/createblog')">New Post</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click.prevent="$router.push('/userprofile')">Your Profile</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click.prevent="Logout">Logout</a>
        </li>

        <li>
          <form class="form-inline">
            <input class="form-control-sm" type="search" placeholder="Search" aria-label="Search" v-model="username">
            <button class="btn btn-outline-success btn-sm" type="search" style="margin-left:10px"
              @click.prevent="searchuser">Search</button>
          </form>
          <div v-if="showresults" class="search-results">
            <ul>
              <li v-for="(result, index) in searchresults" :key="index" @click="showprofile(result)">

                {{ result }}

              </li>
            </ul>
          </div>

        </li>
      </ul>
    </div>
  </nav>
</template>
    
<script>
export default {
  name: 'NavBar',
  data() {
    return {
      email: '',
      username: '',
      auth_token: '',
      searchresults: [],
      showresults: false
    }
  },
  mounted() {
    this.email = localStorage.getItem('email'),
      this.auth_token = localStorage.getItem('Authentication-Token')
  },

  methods: {

    async Logout() {
      try {
        const response = await fetch('http://localhost:8080/logout', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: { "email": this.email }
        });
        if (response.ok) {
          localStorage.clear()
          this.$router.push({ name: 'homepage' })
        }
      }
      catch (error) {
        console.error;
      }
    },
    async searchuser() {
      try {
        const response = await fetch(`http://localhost:8080/api/search?q=${this.username}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authentication-Token': `${this.auth_token}`
          }
        })
        const data = await response.json()
        console.log(data)
        this.searchresults = data
        if(data){
          this.showresults = true
        }
          
      }
      catch (error) {
        console.error;
      }
    }


    ,
    toggleNavbar() {
      var navbarCollapse = document.getElementById("navbarNav");
      if (navbarCollapse.style.display === "block") {
        navbarCollapse.style.display = "none";
      } else {
        navbarCollapse.style.display = "block";
      }
    },
    showprofile(user) {
      this.$router.push({
        name: 'otherprofile',
        params: {
          username: user
        }
      })
      this.showresults = false
    }
  }
}



</script>
<style>
@media (min-width: 992px) {
  .navbar-collapse {
    display: none !important;
  }

}

.search-results {
  position: absolute;
  top: 100%;
  left: 28%;
  background-color: #fff;
  border: 1px solid #ccc;
  border-top: none;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-height: 200px;
  overflow-y: auto;
  z-index: 1;
  width: 28%;
  border-radius: 8px;
}

.search-results ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.search-results li {
  padding: 8px 16px;
  cursor: pointer;
}

.search-results li:hover {
  background-color: #bdce9f;
}
</style>