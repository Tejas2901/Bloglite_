<template>
  <div style="position:center; left:60px;">
    <BlogComponent v-for="item in listOfDictionaries" :key="item.id" :item="item" />
  </div>
</template>

<script>

import BlogComponent from '../components/BlogComponent.vue'
export default {
  components: { BlogComponent },
  data() {
    return {
      message: '',
      auth_token: '',
      email: '',
      username: '',
      listOfDictionaries: []
    }
  },
  mounted() {
    if (!localStorage.getItem('Authentication-Token')) {
      alert('Login First')
      this.$router.push('/login')
    }
    else {
      this.auth_token = localStorage.getItem("Authentication-Token");
      this.email = localStorage.getItem("email")
      this.getUser()

    }
  },

  methods: {
    async getUser() {
      try {
        if (this.auth_token) {
          fetch(`http://localhost:8080/api?email=${this.email}`, {
            method: 'GET',

            headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': `${this.auth_token}`,
              'email': `${this.email}`
            },

          })

            .then(response => response.json())
            .then(data => this.listOfDictionaries = data)
            

        }
      }
      catch (error) {
        console.error();
        alert('DUHhhhh')
      }
    },

  },

}
</script>