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

      <div class="form-group row">
        <div class="cols-xs-2">
          <label for="exampleInputUsername"></label>
          <input type="text" v-model="form.username" class="form-control" id="exampleInputEmail1"
            aria-describedby="emailHelp" placeholder="Enter Username">
        </div>
      </div>

      <div class="form-group">
        <div class="cols-xs-2">
          <label for="exampleInputPassword1"></label>
          <input type="password" v-model="form.password" class="form-control" id="exampleInputPassword1"
            placeholder="Password">
        </div>
      </div>

      <div class="form-group">
        <div class="cols-xs-2">
          <label for="exampleInputCPassword2"></label>
          <input type="password" v-model="form.password_confirm" class="form-control" id="exampleInputPassword2"
            placeholder="Confirm Password">
        </div>
      </div>

      <button style="margin:10px" type="submit" class="btn btn-primary">Submit</button>
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
        username: '',
        password: '',
        password_confirm: ''
      }
    }
  },
  methods: {
    async submitForm() {
      // submit the form
      if (this.form.password != this.password_confirm){
        alert("Confirm Password is different than password")
      }
      try {
        const response = await fetch('http://localhost:8080/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.form)
        });
        const data = await response.json();
        if (response.ok) {
          console.log(data);
          alert('Registration successful')
          this.$router.push({ name: 'login' })
        } else {
          console.error(data);
          
          alert(JSON.stringify(data['response']['errors']['email'][0]))
        }
      } catch (error) {
        console.error();
        alert('Something went Wrong')
      }
    }
  }
}
</script>