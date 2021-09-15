<template>
    <b-navbar toggleable="lg" class='navbar-dark navbar-fixed-top'>
        <b-navbar-brand :to="'/'" left>
            NHL Expansion Draft Optimizer
        </b-navbar-brand>
        <b-navbar-toggle target="nav-collapse" />
        <b-collapse id="nav-collapse" is-nav right>
            <b-navbar-nav class="ml-auto">
                <b-nav-item :to="'faq'">
                    FAQ
                </b-nav-item>
                <b-nav-item :to="'about'">
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