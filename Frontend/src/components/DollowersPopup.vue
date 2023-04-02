<template>
  <div class="popup">
    <div class="popup-inner">
      <h2>{{title}}</h2>
      <ul>
        <li v-for="follower in followers" :key="follower" @click="openpro(follower)">{{ follower }}</li>
      </ul>
      <button @click="$emit('close')">Close</button>
    </div>
  </div>
</template>
  
<script>



export default {
  props: {
    'title':{
      type:String
    },
    followers: {
      type: Array,
      required: true,
    },
  },

  methods: {
    openpro(follower) {
      this.$router.push({
        name: 'otherprofile',
        params: {
          username: follower

        }
      })
      console.log(follower)
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
  padding: 20px;
  border-radius: 10px;
  max-width: 400px;
  max-height: 400px;
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