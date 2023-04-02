<template>
    <div>Welcome to the home page
        <button v-on:click="Login"> Click here to login</button>
        <button v-on:click="Register">Register here</button>
    </div>
</template>

<script>
export default {
    props:
        ['loginstatus'],
    methods: {
        Login() {
            this.$router.push({ name: 'login' })

        },
        Register() {
            this.$router.push({ name: 'register' })
        }
    },
    mounted() {
        localStorage.clear()

        this.$emit('check-login')
        console.log('emit')


    }
}

</script>