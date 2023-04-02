<template>
    <div class="popup">
        <div class="popup-inner">
            <div class="col-lg-4 col-lg-2" style="margin:auto; width:100%">
                <p>Are you sure you want to delete this blog?</p>
                <button class="btn btn-danger" @click="Delete">Yes</button>

                <button style="margin-left:10px" class="btn btn-secondary" @click="$emit('close')">Cancel</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['item'],
    data() {
        return {
            auth_token: '',
            email: ''
        }

    },
    mounted() {
        this.auth_token = localStorage.getItem("Authentication-Token");
        this.email = localStorage.getItem("email")

    },
    methods: {
        async Delete() {
            try {

                const response = await fetch(`http://localhost:8080/api/createblog?blog_id=${this.item.blog_id}`, {
                    method: 'DELETE',
                    headers: {

                        'Authentication-Token': `${this.auth_token}`,
                        'email': `${this.email}`
                    }

                });

                if (response.ok) {
                    alert('Blog deleted')
                }
                this.$parent.$parent.getUser()
                this.$parent.$parent.$parent.getProfile()

            }
            catch (error) {
                console.log(error)
                alert('something went wrong')
            }
        },
    }
}

</script>