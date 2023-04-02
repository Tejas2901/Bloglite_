<template>
  <div>
    <form @submit.prevent="submitForm">
      <br />
      <label>
        Email:
        <input type="email" v-model="form.email" />
      </label>
      <br />
      <label>
        Password:
        <input type="password" v-model="form.password" />
      </label>
      <br />

      <br />
      <button type="submit">Submit</button>
    </form>
  </div>
</template>
  
<script>
export default {
  data() {
    return {
      form: {
        // name: '',
        email: '',
        password: '',

      }
    }
  },
  methods: {

    async submitForm() {
      // submit the form
      try {

        const response = await fetch('http://localhost:8080/logout?include_auth_token', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.form)
        });
        const data = await response.json();
        if (response.ok) {

          this.$router.push({ name: 'homepage' })


        } else {
          console.error(data);
          alert('opps')

        }

      } catch (error) {
        console.error();
        alert('DUHhhhh')
      }
    }
  },

}
</script>