<template>
  <nav class='navbar navbar-default navbar-fixed-top'>
		<div class='fluid-container'>
			<div class='navbar-header'>
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class='navbar-brand hidden-mobile' href='/'>NHL Expansion Draft Optimizer</a>
			</div>
			<div id='navbar' class='navbar-collapse collapse'>
				<ul class='nav navbar-nav navbar-right'>
					<li><a class='navbar-brand visible-mobile' href='/'>NHL Expansion Draft Optimizer</a></li>
					<li><a href='/blog'>Blog</a></li>
					<li><a href='/what'>What</a></li>
					<li><a href='/how'>How</a></li>
					<li><a href='/about'>About</a></li>
				</ul>
			</div>
		</div>
	</nav>
</template>

<script>
export default {
  name: 'HeaderArea'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
