<template>
    <div class="popup">
        <div class="popup-inner">
            <div class="col-lg-4 col-lg-2" style="margin:auto;
                                                width:100%">
                
                <form @submit.prevent="edit_prof_pic" style="margin-bottom: 10px;">
                    <img :src="current_img" width="200" height="200"/>
                    
                    <div class="form-group row">
                        <label for="image" class="col-sm-2 col-form-label">Image File</label>
                        <div class="col-sm-10">
                            <input type="file" ref="image" class="form-control" id="image">
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
            <button @click="$emit('close')">Close</button>
        </div>
    </div>
</template>
<script>
export default {
    props: ['current_img'],
    data() {
        return {
            form: {
                image:null
            }
        }
    },
    
   
    methods: {
        async edit_prof_pic(){
            const image_file = this.$refs.image.files[0]
            const formData = new FormData();
            formData.append('image',image_file || this.current_img)
            try{
                const response  = await fetch('http://localhost:8080/api/user', {
                    method:'POST',
                    headers: {
                        'Authentication-Token':localStorage.getItem("Authentication-Token"),
                    },
                    body: formData
                })
                if(response.ok){
                    alert("Changes Saved")
                    this.$parent.reload()
                }
            }
            catch(error){
                alert("Something went wrong")
                console.error()
            }
        }
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