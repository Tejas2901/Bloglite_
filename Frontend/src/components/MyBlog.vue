<template>
  <div style="display: flex; justify-content: center;">
    <div class="post">
      <div class="post-header">
        <img class="avatar" :src=item.pp alt="user avatar" width = "40px" height="40px">
        <h2 class="username">{{ item.title }}</h2>
      </div>

      <div class="post-image">
        <img :src="item.image" class="post-image-img">
      </div>
      <div class="post-actions">
        <button class="edit-button" @click="editblog">Edit</button>
        <button class="delete-button" @click="deleteblog" style="margin-right:300px;">Delete</button>
        <button class="btn btn-primary text-dark" v-if="liked" @click="like_action()"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-hand-thumbs-up" viewBox="0 0 16 16">
  <path d="M8.864.046C7.908-.193 7.02.53 6.956 1.466c-.072 1.051-.23 2.016-.428 2.59-.125.36-.479 1.013-1.04 1.639-.557.623-1.282 1.178-2.131 1.41C2.685 7.288 2 7.87 2 8.72v4.001c0 .845.682 1.464 1.448 1.545 1.07.114 1.564.415 2.068.723l.048.03c.272.165.578.348.97.484.397.136.861.217 1.466.217h3.5c.937 0 1.599-.477 1.934-1.064a1.86 1.86 0 0 0 .254-.912c0-.152-.023-.312-.077-.464.201-.263.38-.578.488-.901.11-.33.172-.762.004-1.149.069-.13.12-.269.159-.403.077-.27.113-.568.113-.857 0-.288-.036-.585-.113-.856a2.144 2.144 0 0 0-.138-.362 1.9 1.9 0 0 0 .234-1.734c-.206-.592-.682-1.1-1.2-1.272-.847-.282-1.803-.276-2.516-.211a9.84 9.84 0 0 0-.443.05 9.365 9.365 0 0 0-.062-4.509A1.38 1.38 0 0 0 9.125.111L8.864.046zM11.5 14.721H8c-.51 0-.863-.069-1.14-.164-.281-.097-.506-.228-.776-.393l-.04-.024c-.555-.339-1.198-.731-2.49-.868-.333-.036-.554-.29-.554-.55V8.72c0-.254.226-.543.62-.65 1.095-.3 1.977-.996 2.614-1.708.635-.71 1.064-1.475 1.238-1.978.243-.7.407-1.768.482-2.85.025-.362.36-.594.667-.518l.262.066c.16.04.258.143.288.255a8.34 8.34 0 0 1-.145 4.725.5.5 0 0 0 .595.644l.003-.001.014-.003.058-.014a8.908 8.908 0 0 1 1.036-.157c.663-.06 1.457-.054 2.11.164.175.058.45.3.57.65.107.308.087.67-.266 1.022l-.353.353.353.354c.043.043.105.141.154.315.048.167.075.37.075.581 0 .212-.027.414-.075.582-.05.174-.111.272-.154.315l-.353.353.353.354c.047.047.109.177.005.488a2.224 2.224 0 0 1-.505.805l-.353.353.353.354c.006.005.041.05.041.17a.866.866 0 0 1-.121.416c-.165.288-.503.56-1.066.56z"/>
</svg> {{ item.no_of_likes }}</button>
    <button class="btn btn-outline text-dark" v-else @click="like_action()"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-hand-thumbs-up" viewBox="0 0 16 16">
      <path d="M8.864.046C7.908-.193 7.02.53 6.956 1.466c-.072 1.051-.23 2.016-.428 2.59-.125.36-.479 1.013-1.04 1.639-.557.623-1.282 1.178-2.131 1.41C2.685 7.288 2 7.87 2 8.72v4.001c0 .845.682 1.464 1.448 1.545 1.07.114 1.564.415 2.068.723l.048.03c.272.165.578.348.97.484.397.136.861.217 1.466.217h3.5c.937 0 1.599-.477 1.934-1.064a1.86 1.86 0 0 0 .254-.912c0-.152-.023-.312-.077-.464.201-.263.38-.578.488-.901.11-.33.172-.762.004-1.149.069-.13.12-.269.159-.403.077-.27.113-.568.113-.857 0-.288-.036-.585-.113-.856a2.144 2.144 0 0 0-.138-.362 1.9 1.9 0 0 0 .234-1.734c-.206-.592-.682-1.1-1.2-1.272-.847-.282-1.803-.276-2.516-.211a9.84 9.84 0 0 0-.443.05 9.365 9.365 0 0 0-.062-4.509A1.38 1.38 0 0 0 9.125.111L8.864.046zM11.5 14.721H8c-.51 0-.863-.069-1.14-.164-.281-.097-.506-.228-.776-.393l-.04-.024c-.555-.339-1.198-.731-2.49-.868-.333-.036-.554-.29-.554-.55V8.72c0-.254.226-.543.62-.65 1.095-.3 1.977-.996 2.614-1.708.635-.71 1.064-1.475 1.238-1.978.243-.7.407-1.768.482-2.85.025-.362.36-.594.667-.518l.262.066c.16.04.258.143.288.255a8.34 8.34 0 0 1-.145 4.725.5.5 0 0 0 .595.644l.003-.001.014-.003.058-.014a8.908 8.908 0 0 1 1.036-.157c.663-.06 1.457-.054 2.11.164.175.058.45.3.57.65.107.308.087.67-.266 1.022l-.353.353.353.354c.043.043.105.141.154.315.048.167.075.37.075.581 0 .212-.027.414-.075.582-.05.174-.111.272-.154.315l-.353.353.353.354c.047.047.109.177.005.488a2.224 2.224 0 0 1-.505.805l-.353.353.353.354c.006.005.041.05.041.17a.866.866 0 0 1-.121.416c-.165.288-.503.56-1.066.56z"/>
    </svg> {{ item.no_of_likes }}</button>
      </div>
      <div class="post-caption">
        <p class="caption">{{ item.description }}</p>
      </div>
      <EditBlog v-if="showEditBlog" :item="this.item" @close="showEditBlog = false" />
      <DeleteBlog v-if="showDeleteBlog" :item="this.item" @close="showDeleteBlog=false"/>
    </div>
  </div>
</template>

<script>

import EditBlog from '../components/EditBlog.vue'
import DeleteBlog from '../components/DeleteBlog.vue'
export default {
  
  props: ['item'],
  components:{
    EditBlog,
    DeleteBlog

  },
  mounted() {
    this.auth_token = localStorage.getItem("Authentication-Token");
    this.email = localStorage.getItem("email")
    this.checklike()
    
    
  },
  data(){
    return {
      id:null,
      showEditBlog:false,
      showDeleteBlog:false,
      liked:false
    }
  },
  methods:{
    editblog(){
      this.showEditBlog = true;
      
    },
    deleteblog(){
      this.showDeleteBlog = true;
    },
    async checklike() {
       try{
        const response  = await fetch(`http://localhost:8080/api/like?blog_id=${this.item['blog_id']}`,{
          method: 'GET',
          headers: {
              'Content-Type': 'application/json',
              'Authentication-Token': `${this.auth_token}`
          }
        })
        const data = await response.json()
        if(data == true){
          this.liked = true
          
        }
        else{
          this.liked = false
        }
       }
       catch(error){
        console.log(this.item)
        console.error()
       }
    },
    async like_action(){
      if(this.liked == false){
        try{
          const response = await fetch(`http://localhost:8080/api/like?blog_id=${this.item['blog_id']}`,{
          method:'POST',
          headers: {
                'Content-Type':'application/json',
                'Authentication-Token':`${this.auth_token}`

          }})
          if(response.ok){
            this.liked = true
            this.$parent.getUser()
          }
          
        }
        catch(error){
          console.error()
        }
      }
      else{
        try{
          const response = await fetch(`http://localhost:8080/api/like?blog_id=${this.item['blog_id']}`,{
          method:'DELETE',
          headers: {
                'Content-Type':'application/json',
                'Authentication-Token':`${this.auth_token}`

          }})
          if(response.ok){
            this.liked = false  
            this.$parent.getUser()
          }
          
        }
        catch(error){
          console.error()
        }
      }
    }
  }
}
</script>

<style>
.post {
  margin-top: 20px;
  margin-right: 50px;
  border: 1px solid #ccc;
  width: 500px;
  border-radius: 5px;
}

.post-header {
  display: flex;
  align-items: center;
  padding: 10px;
}

.avatar {
  border-radius: 50%;
  margin-right: 10px;
}

.post-image {
  text-align: center;
}

.post-image img {
  max-width: 100%;
  height: 400px;
}

.post-actions {
  display: flex;
  justify-content: space-between;
  padding: 10px;
}

.post-caption {
  padding: 10px;
}

.username {
  font-size: 18px;
  font-weight: bold;
}

.caption {
  margin: 0;
}

.edit-button,
.delete-button {
  padding: 5px 10px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}

.edit-button {
  background-color: #f44336;
  color: #fff;
}

.delete-button {
  background-color: #fff;
  color: #000;
  border: 1px solid #ccc;
}
</style>
