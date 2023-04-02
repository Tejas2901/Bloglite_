<template>
    <body v-if="data_fetched">
        
        <div class="d-flex align-items-center" style="margin-left:30%;">
        <div class="mr-3">
            <img :src=profile_picture class="rounded-circle" :alt="username" width="80" height="80">
            
        </div>
        <h3 style="font-family:verdana; margin-left: 10px; margin-top: 30px;">Username:<b>{{ username }}</b></h3>
        <button v-if="pref==0" class="btn btn-primary text-dark" style="margin-left: 10px;margin-top:20px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-filetype-html" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M14 4.5V11h-1V4.5h-2A1.5 1.5 0 0 1 9.5 3V1H4a1 1 0 0 0-1 1v9H2V2a2 2 0 0 1 2-2h5.5L14 4.5Zm-9.736 7.35v3.999h-.791v-1.714H1.79v1.714H1V11.85h.791v1.626h1.682V11.85h.79Zm2.251.662v3.337h-.794v-3.337H4.588v-.662h3.064v.662H6.515Zm2.176 3.337v-2.66h.038l.952 2.159h.516l.946-2.16h.038v2.661h.715V11.85h-.8l-1.14 2.596H9.93L8.79 11.85h-.805v3.999h.706Zm4.71-.674h1.696v.674H12.61V11.85h.79v3.325Z"/>
            </svg>
        </button>
        <button v-else class="btn btn-outline-primary text-dark" @click="change_preference(0)" style="margin-left: 10px;margin-top:20px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-filetype-html" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M14 4.5V11h-1V4.5h-2A1.5 1.5 0 0 1 9.5 3V1H4a1 1 0 0 0-1 1v9H2V2a2 2 0 0 1 2-2h5.5L14 4.5Zm-9.736 7.35v3.999h-.791v-1.714H1.79v1.714H1V11.85h.791v1.626h1.682V11.85h.79Zm2.251.662v3.337h-.794v-3.337H4.588v-.662h3.064v.662H6.515Zm2.176 3.337v-2.66h.038l.952 2.159h.516l.946-2.16h.038v2.661h.715V11.85h-.8l-1.14 2.596H9.93L8.79 11.85h-.805v3.999h.706Zm4.71-.674h1.696v.674H12.61V11.85h.79v3.325Z"/>
            </svg>
        </button>
        
        <button v-if="pref==1" class="btn btn-primary text-dark" style="margin-left: 10px;margin-top:20px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-pdf-fill" viewBox="0 0 16 16">
                <path d="M5.523 10.424c.14-.082.293-.162.459-.238a7.878 7.878 0 0 1-.45.606c-.28.337-.498.516-.635.572a.266.266 0 0 1-.035.012.282.282 0 0 1-.026-.044c-.056-.11-.054-.216.04-.36.106-.165.319-.354.647-.548zm2.455-1.647c-.119.025-.237.05-.356.078a21.035 21.035 0 0 0 .5-1.05 11.96 11.96 0 0 0 .51.858c-.217.032-.436.07-.654.114zm2.525.939a3.888 3.888 0 0 1-.435-.41c.228.005.434.022.612.054.317.057.466.147.518.209a.095.095 0 0 1 .026.064.436.436 0 0 1-.06.2.307.307 0 0 1-.094.124.107.107 0 0 1-.069.015c-.09-.003-.258-.066-.498-.256zM8.278 4.97c-.04.244-.108.524-.2.829a4.86 4.86 0 0 1-.089-.346c-.076-.353-.087-.63-.046-.822.038-.177.11-.248.196-.283a.517.517 0 0 1 .145-.04c.013.03.028.092.032.198.005.122-.007.277-.038.465z"/>
                <path fill-rule="evenodd" d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm.165 11.668c.09.18.23.343.438.419.207.075.412.04.58-.03.318-.13.635-.436.926-.786.333-.401.683-.927 1.021-1.51a11.64 11.64 0 0 1 1.997-.406c.3.383.61.713.91.95.28.22.603.403.934.417a.856.856 0 0 0 .51-.138c.155-.101.27-.247.354-.416.09-.181.145-.37.138-.563a.844.844 0 0 0-.2-.518c-.226-.27-.596-.4-.96-.465a5.76 5.76 0 0 0-1.335-.05 10.954 10.954 0 0 1-.98-1.686c.25-.66.437-1.284.52-1.794.036-.218.055-.426.048-.614a1.238 1.238 0 0 0-.127-.538.7.7 0 0 0-.477-.365c-.202-.043-.41 0-.601.077-.377.15-.576.47-.651.823-.073.34-.04.736.046 1.136.088.406.238.848.43 1.295a19.707 19.707 0 0 1-1.062 2.227 7.662 7.662 0 0 0-1.482.645c-.37.22-.699.48-.897.787-.21.326-.275.714-.08 1.103z"/>
            </svg>
        </button>
        <button v-else class="btn btn-outline-primary text-dark" @click="change_preference(1)" style="margin-left: 10px;margin-top:20px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-pdf-fill" viewBox="0 0 16 16">
                <path d="M5.523 10.424c.14-.082.293-.162.459-.238a7.878 7.878 0 0 1-.45.606c-.28.337-.498.516-.635.572a.266.266 0 0 1-.035.012.282.282 0 0 1-.026-.044c-.056-.11-.054-.216.04-.36.106-.165.319-.354.647-.548zm2.455-1.647c-.119.025-.237.05-.356.078a21.035 21.035 0 0 0 .5-1.05 11.96 11.96 0 0 0 .51.858c-.217.032-.436.07-.654.114zm2.525.939a3.888 3.888 0 0 1-.435-.41c.228.005.434.022.612.054.317.057.466.147.518.209a.095.095 0 0 1 .026.064.436.436 0 0 1-.06.2.307.307 0 0 1-.094.124.107.107 0 0 1-.069.015c-.09-.003-.258-.066-.498-.256zM8.278 4.97c-.04.244-.108.524-.2.829a4.86 4.86 0 0 1-.089-.346c-.076-.353-.087-.63-.046-.822.038-.177.11-.248.196-.283a.517.517 0 0 1 .145-.04c.013.03.028.092.032.198.005.122-.007.277-.038.465z"/>
                <path fill-rule="evenodd" d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm.165 11.668c.09.18.23.343.438.419.207.075.412.04.58-.03.318-.13.635-.436.926-.786.333-.401.683-.927 1.021-1.51a11.64 11.64 0 0 1 1.997-.406c.3.383.61.713.91.95.28.22.603.403.934.417a.856.856 0 0 0 .51-.138c.155-.101.27-.247.354-.416.09-.181.145-.37.138-.563a.844.844 0 0 0-.2-.518c-.226-.27-.596-.4-.96-.465a5.76 5.76 0 0 0-1.335-.05 10.954 10.954 0 0 1-.98-1.686c.25-.66.437-1.284.52-1.794.036-.218.055-.426.048-.614a1.238 1.238 0 0 0-.127-.538.7.7 0 0 0-.477-.365c-.202-.043-.41 0-.601.077-.377.15-.576.47-.651.823-.073.34-.04.736.046 1.136.088.406.238.848.43 1.295a19.707 19.707 0 0 1-1.062 2.227 7.662 7.662 0 0 0-1.482.645c-.37.22-.699.48-.897.787-.21.326-.275.714-.08 1.103z"/>
            </svg>
        </button>
        </div>
        <div style="margin-right: 37%;">
            <button class="btn btn-link btn-sm" @click="edit_prof_pic">Edit</button>
        </div>
       

        <button class="btn btn-outline-primary text-dark">{{ no_of_blogs }}: Posts</button>&nbsp;&nbsp;
        <button class="btn btn-outline-primary text-dark" @click="showFollowers = true"> {{ no_of_followers }}:
            Followers</button>&nbsp;&nbsp;
        <button class="btn btn-outline-primary text-dark" @click="showFollowing = true">{{ no_of_following }}:
            Following</button>&nbsp;&nbsp;
        <button class="btn btn-outline-primary text-dark" @click="export_blogs"><svg xmlns="http://www.w3.org/2000/svg"
                width="16" height="16" fill="currentColor" class="bi bi-save" viewBox="0 0 16 16">
                <path
                    d="M2 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H9.5a1 1 0 0 0-1 1v7.293l2.646-2.647a.5.5 0 0 1 .708.708l-3.5 3.5a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L7.5 9.293V2a2 2 0 0 1 2-2H14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h2.5a.5.5 0 0 1 0 1H2z" />
            </svg></button>&nbsp;&nbsp;

        <!--     
        <p>Followers {{ followers }}</p>
        <p>following {{ following }}</p> -->
        <DollowersPopup v-if="showFollowers" :followers="followers" @close="showFollowers = false" />
        <DollowersPopup v-if="showFollowing" :followers="following" @close="showFollowing = false" />
        <EditProf v-if="editprof" :current_img="profile_picture" @close="editprof=false"/>
        <UserBlogs />

    </body>
</template> 


<script>
import DollowersPopup from '../components/DollowersPopup.vue'
import UserBlogs from './UserBlogs.vue'
import EditProf from '@/components/EditProf.vue'

export default {
    components: {
        DollowersPopup,
        UserBlogs,
        EditProf
    },
    data() {
        return {
            profile_picture: '',
            editprof: false,
            username: '',
            no_of_blogs: '',
            no_of_followers: '',
            followers: [],
            following: [],
            no_of_following: '',
            showFollowers: false,
            showFollowing: false,
            pref:'',
            data_fetched:false
        }
    },
    mounted() {
        this.auth_token = localStorage.getItem("Authentication-Token");
        this.email = localStorage.getItem("email")
        this.getProfile()
    },
    methods: {
        async getProfile() {
            try {
                if (this.auth_token) {
                    const response = await fetch(`http://localhost:8080/api/user?email=${this.email}`, {
                        method: 'GET',

                        headers: {
                            'Content-Type': 'application/json',
                            'Authentication-Token': `${this.auth_token}`,
                            'email': `${this.email}`
                        },

                    })
                    const data = await response.json()
                    this.profile_picture = data[0].profile_picture
                    this.username = data[0].username
                    this.pref = data[0].pref
                    this.no_of_blogs = data[0].no_of_blogs
                    this.no_of_followers = data[0].followers
                    this.no_of_following = data[0].following
                    this.followers = data[1]
                    this.following = data[2]
                    this.data_fetched = true
                }
            }
            catch (error) {
                console.error();
                alert('DUHhhhh')
            }
        },
        async export_blogs() {
            try {
                const response = fetch(`http://localhost:8080/api/blogscsv?email=${this.email}`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': `${this.auth_token}`,
                        'email': `${this.email}`
                    },
                })
                alert('We have mailed you your blogs')
                if (response.ok) {
                    alert('We have mailed you the Blogs.csv')
                }
            }
            catch (error) {
                console.log(error)
                alert("Something went wrong")
            }
        },
        edit_prof_pic(){
            this.editprof = true
        },
        reload(){
            location.reload()
        },
        async change_preference(arg){
            try{
                this.pref = arg
                const response = await fetch(`http://localhost:8080/api/pref?pref=${this.pref}`,{
                    method : 'POST',
                    headers : {
                        'Content-Type':'application/json',
                        'Authentication-Token': `${this.auth_token}`
                    }})
                
                if(response.ok){
                    this.pref = arg
                }   
            }
            catch(error){
                console.error()
            }
            
        }
    }
}
</script>


