<template>
    <div class="popup">
        <div class="popup-inner">
            <div class="col-lg-4 col-lg-2" style="margin:auto;
                                                width:100%">
                <form @submit.prevent="editForm">
                    <div class="form-group row">
                        <label for="title" class="col-sm-2 col-form-label">Title</label>
                        <div class="col-sm-10">
                            <input type="text" v-model="form.title" class="form-control" id="title"
                                placeholder="Enter Title">
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
            <button @click="$emit('close')">Close</button>
        </div>
    </div>
</template>

<script>
  export default {
    props:['item']
      ,
    data() {
      return {
        form: {
          // name: '',
          title: this.item.title,
          image:null,
          description:this.item.description
        },
        imageFile: this.item.image // set the default image file here
      }
    },
    mounted(){
      this.auth_token = localStorage.getItem("Authentication-Token");
      this.email = localStorage.getItem("email");

      // update the form.image property to the imageFile value
      this.form.image = this.imageFile;
    },
    
    methods: {
      async editForm() {
        const imageFile = this.$refs.image.files[0];
        // construct the FormData object
        const formData = new FormData();
        formData.append('title', this.form.title);
        formData.append('description', this.form.description);
        formData.append('image', imageFile || this.imageFile); // use the selected file or the default file
        console.log(formData.get('image'))
        // submit the form
        try {
          
          const response = await fetch(`http://localhost:8080/api/createblog?blog_id=${this.item.blog_id}`,{
            method: 'PUT',
            headers: {
                  
                  'Authentication-Token': `${this.auth_token}`,
                  'email': `${this.email}`
                },
            body: formData
          });
          
          if(response.ok){
            alert('Changes Saved')
          }
          this.$parent.$parent.getUser()
          
          
        }
        catch(error){
            console.log(error)
            alert('something went wrong')
        }
      },
    }
  }
</script>

<style>
  .popup {
    position: fixed;
    z-index: 999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .popup-inner {
    background-color: #fff;
    padding: 30px;
    border-radius: 10px;
    max-width: 900px;
    max-height: 900px;
    overflow: auto;
  }
  
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  
  li {
    padding: 5px 0;
    border-bottom: 1px solid #ccc;
  }
  
  button {
    margin-top: 10px;
  }
  </style>