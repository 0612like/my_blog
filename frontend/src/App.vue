<script setup>
// 这里可以添加全局的逻辑，如果需要的话
</script>

<template>
  <div id="app">
    <header>
      <nav>
        <router-link to="/">首页</router-link>
        <!-- 可以添加其他导航链接 -->
      </nav>
    </header>
    <main>
      <router-view /> <!-- 路由匹配的组件将在这里渲染 -->
    </main>
    <footer>
      <p>&copy; {{ new Date().getFullYear() }} Koko的技术博客</p>
    </footer>
  </div>
</template>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

header {
  background-color: #f8f9fa;
  padding: 1rem;
  border-bottom: 1px solid #dee2e6;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  margin-right: 1rem;
}

nav a.router-link-exact-active {
  color: #42b983;
}

main {
  flex-grow: 1; /* 让 main 内容区域填充剩余空间 */
  padding: 1rem;
}

footer {
  text-align: center;
  padding: 1rem;
  margin-top: 2rem;
  background-color: #f8f9fa;
  border-top: 1px solid #dee2e6;
  color: #6c757d;
  font-size: 0.9em;
}
</style>
