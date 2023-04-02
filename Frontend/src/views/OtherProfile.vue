<template>
    <body v-if="profileLoaded">
        <div class="d-flex align-items-center" style="margin-left:30%;">
        <div class="mr-3">
            <img :src=profile_picture class="rounded-circle" :alt="username" width="80" height="80">
            
        </div>
        <h2 style="font-family:verdana">Username: <b>{{ username }}</b></h2>
        <br>
        </div>
        <button class="btn btn-outline-primary text-dark">{{ no_of_blogs }}: Posts</button>&nbsp;&nbsp;
        <button class="btn btn-outline-primary text-dark" @click="showFollowers = true"> {{ no_of_followers }}:
            Followers</button>&nbsp;&nbsp;
        <button class="btn btn-outline-primary text-dark" @click="showFollowing = true">{{ no_of_following }}:
            Following</button>&nbsp;&nbsp;

        <DollowersPopup v-if="showFollowers" :title="title" :followers="followers" @close="showFollowers = false" />
        <DollowersPopup v-if="showFollowing" :title="title2" :followers="following" @close="showFollowing = false" />
        <br>

        <p>
            <br>
            <button class="btn btn-outline-primary text-dark" v-if="buttonlabel !== 'following'" @click="log_follow">{{
                buttonlabel }}</button>
            <button class="btn btn-primary text-dark" v-else @click="log_unfollow">{{ buttonlabel }}</button>
        </p>
        <div style="position:center; left:60px;">
            <BlogComponent v-for="item in listOfDictionaries" :key="item.id" :item="item" />
        </div>
    
</body>
</template>
<script>
import DollowersPopup from '@/components/DollowersPopup.vue';
import BlogComponent from '@/components/BlogComponent.vue';
export default {
    components: {
        DollowersPopup,
        BlogComponent
    },
    data() {
        return {
            username: '',
            profile_picture: '',
            logged_in_user: '',
            no_of_blogs: '',
            no_of_followers: '',
            no_of_following: '',
            title:'Followers',
            title2:'Following',
            followers: [],
            following: [],
            buttonlabel: '',
            showFollowers: false,
            showFollowing: false,
            email: '',
            profileLoaded: false,
            listOfDictionaries: []
        }
    },
    mounted() {
        this.auth_token = localStorage.getItem("Authentication-Token");
        this.loggedin_user = localStorage.getItem('email')
        this.username = this.$route.params.username
        this.getProfile()


    },
    watch: {
        
        '$route.params': {
            handler: function (newParams, oldParams) {  
                if (oldParams.username && newParams && newParams.username !== oldParams.username)  {
                        this.username = newParams.username;
                        this.getProfile();
                        this.showFollowers = false;
                        this.showFollowing = false;
                    }
                    
                }
            },
            immediate: true
        
    },


    methods: {

        async getProfile() {
            try {
                if (this.username == this.loggedin_user) {
                    this.$router.push('userprofile')
                }
                else {
                    if (this.auth_token) {

                        console.log('In getProfile  ')
                        const response = await fetch(`http://localhost:8080/api/user?username=${this.username}`, {
                            method: 'GET',

                            headers: {
                                'Content-Type': 'application/json',
                                'Authentication-Token': `${this.auth_token}`,
                                'username': `${this.username}`
                            },

                        })
                        const data = await response.json()
                        this.email = data[0].email
                        this.profile_picture  = data[0].profile_picture
                        this.no_of_blogs = data[0].no_of_blogs
                        this.no_of_followers = data[0].followers
                        this.no_of_following = data[0].following
                        this.followers = data[1]
                        this.following = data[2]
                        const response_F = await fetch(`http://localhost:8080/api/checkfollow?user1=${this.loggedin_user}&user2=${this.username}`, {
                            method: 'GET',
                            headers: {
                                'Content-Type': 'application/json',
                                'Authentication-Token': `${this.auth_token}`,
                                'user1': `${this.loggedin_user}`,
                                'user2': `${this.username}`
                            }
                        })
                        const data_F = await response_F.json()
                        if (data_F) {
                            this.buttonlabel = "following"
                        }
                        else {
                            this.buttonlabel = "follow"
                        }
                        const blog_response = await fetch(`http://localhost:8080/api/userblogs?username=${this.username}`,{
                            method: 'GET',
                            headers: {
                                'Content-Type':'application/json',
                                'Authentication-Token': `${this.auth_token}`
                                }
                            }
                        )
                        const blogs = await blog_response.json()
                        this.listOfDictionaries = blogs 
                        this.profileLoaded = true
                    }
                }
            }
            catch (error) {
                console.error();
                alert('Enter a valid User')
                this.profileLoaded = false
            }
        },
        async log_follow() {
            try {
                if (this.auth_token) {
                    const response = await fetch(`http://localhost:8080/api/logfollow?user1=${this.loggedin_user}&user2=${this.username}`,
                        {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'Authentication-Token': `${this.auth_token}`,
                                'user1': `${this.loggedin_user}`,
                                'user2': `${this.username}`
                            }
                        })
                    if (response.ok) {
                        console.log('done')
                        this.getProfile()
                    }
                }
            }
            catch (error) {
                console.error()
                alert('Something went wrong')
            }

        },
        async log_unfollow() {
            try {
                if (this.auth_token) {
                    const response = await fetch(`http://localhost:8080/api/logfollow?user1=${this.loggedin_user}&user2=${this.username}`,
                        {
                            method: 'DELETE',
                            headers: {
                                'Content-Type': 'application/json',
                                'Authentication-Token': `${this.auth_token}`,
                                'user1': `${this.loggedin_user}`,
                                'user2': `${this.username}`
                            }
                        })
                    if (response.ok) {
                        console.log('done')
                        this.getProfile()
                    }
                }
            }
            catch (error) {
                console.error()
                alert('Something went wrong')
            }

        }

    }
}
</script>