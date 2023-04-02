<template>
  <div class="col-lg-4 col-lg-2" style="margin:auto;
                                              width:50%">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <label for="title" class="col-sm-2 col-form-label">Title</label>
        <div class="col-sm-10">
          <input type="text" v-model="form.title" class="form-control" id="title" placeholder="Enter Title">
        </div>
      </div>
      <div class="form-group row">
        <label for="image" class="col-sm-2 col-form-label">Image File</label>
        <div class="col-sm-10">
          <input type="file" ref="image" class="form-control" id="image">
        </div>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea v-model="form.description" class="form-control" id="description" rows="5"></textarea>
      </div>
      <br>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      form: {
        // name: '',
        title: '',
        image: null,
        description: ''
      }
    }
  },
  mounted() {

    this.auth_token = localStorage.getItem("Authentication-Token");
    this.email = localStorage.getItem("email")

  },

  methods: {

    async submitForm() {
      const imageFile = this.$refs.image.files[0];
      // construct the FormData object
      const formData = new FormData();
      formData.append('title', this.form.title);
      formData.append('description', this.form.description);
      formData.append('image', imageFile);
      console.log(formData.get('image'))
      // submit the form
      try {

        const response = await fetch(`http://localhost:8080/api/createblog?email=${this.email}`, {
          method: 'POST',
          headers: {

            'Authentication-Token': `${this.auth_token}`,
            'email': `${this.email}`
          },
          body: formData
        });

        if (response.ok) {
          alert('Blog has been created')
        }
      }
      catch (error) {
        console.log(error)
        alert('something went wrong')
      }
    },

  }
}
</script>