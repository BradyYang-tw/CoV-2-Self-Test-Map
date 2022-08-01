<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <h1 class="green">{{ msg }}</h1>
  <div class="nav">
    <ul>
      <li><a href="#/OpenLayersMap">OpenLayersMap</a></li>
      <li><a href="#/Leaftlet">Leaftlet</a></li>
      <li><a href="#/GoogleMapApi">GoogleMapApi</a></li>
    </ul>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  font-weight: bold;
  color: white;
}

ul {
  display: flex;
  justify-content: flex-start;
  color: inherit; /* 移除超連結顏色 */
  text-decoration: none; /* 移除超連結底線 */
  list-style: none; /* 移除項目符號 */
  margin: 0;
  padding: 0;
}

ul li {
  margin-right: 30px;
}
li a {
  display: block;
  color: white; /* 移除超連結顏色 */
  font-size: 1.2rem;
  text-decoration: none; /* 移除超連結底線 */
  border: 3px;
}

li a:hover {
  background-color: black;
  color: white;
  padding: 0 20px;
}
</style>
