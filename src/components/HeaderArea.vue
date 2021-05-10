<template>
    <b-navbar toggleable="lg" class='navbar-dark navbar-fixed-top'>
        <b-navbar-brand href="" left>
            NHL Expansion Draft Optimizer
        </b-navbar-brand>
        <b-navbar-toggle target="nav-collapse" />
        <b-collapse id="nav-collapse" is-nav right>
            <b-navbar-nav class="ml-auto">
                <b-nav-item href="/blog">
                    Blog
                </b-nav-item>
                <b-nav-item href="/what">
                    What
                </b-nav-item>
                <b-nav-item href="/how">
                    How
                </b-nav-item>
                <b-nav-item href="/about">
                    About
                </b-nav-item>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
export default {
    name: 'HeaderArea'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
