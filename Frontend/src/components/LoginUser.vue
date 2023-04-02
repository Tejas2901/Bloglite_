
<template>
  <form @submit.prevent="submitForm">
    <div class="col-lg-2 col-md-1" style="margin: auto;
                                              
                                                height: 30%;
                                              
                                                padding: 10px;">
      <div class="form-group row">
        <div class="cols-xs-2">
          <label for="exampleInputEmail1"></label>
          <input type="email" v-model="form.email" class="form-control" id="exampleInputEmail1"
            aria-describedby="emailHelp" placeholder="Enter email">
        </div>
      </div>
      <br>
      <div class="form-group">
        <div class="cols-xs-2">
          <label for="exampleInputPassword1"></label>
          <input type="password" v-model="form.password" class="form-control" id="exampleInputPassword1"
            placeholder="Password">
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </div>
  </form>
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

        const response = await fetch('http://localhost:8080/login?include_auth_token', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.form)
        });
        const data = await response.json();
        if (response.ok) {
          localStorage.setItem('Authentication-Token',
            data.response.user.authentication_token);
          localStorage.setItem('email',
            this.form['email'])
          this.$router.push({ name: 'dashboard' })


        } else {
          const email_err = data.response.errors.email;
          const password_err = data.response.errors.password;
          if(email_err){
            alert(email_err)
          }
          else{
            alert(password_err)
          }

         
        }
      } catch (error) {
        console.error();
        alert('DUHhhhh')
      }
    }
  },
  mounted() {
    localStorage.clear()
  }
}
</script>