<script setup>
import {
  ref,
  reactive,
  getCurrentInstance,
  onMounted,
  onBeforeMount,
  computed,
} from "vue";
import HelloWorld from "./components/HelloWorld.vue";
import Table from "./components/Table.vue";
import OpenLayersMap from "./components/OpenLayersMap.vue";
import { getData } from "@/api/openData";
// 取得所有快篩資料
// first
const information = reactive({ data: [] });
const getD = function () {
  getData()
    .then((response) => {
      console.log(response);
      information.data = response.data;
    })
    .catch()
    .finally();
};

onMounted(() => {
  getD();
});

const routes = {
  "/": OpenLayersMap,
  "/table": Table,
};
const currentPath = ref(window.location.hash);

window.addEventListener("hashchange", () => {
  currentPath.value = window.location.hash;
});

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || "/"] || NotFound;
});
</script>

<template>
  <header>
    <!-- <img
      alt="Vue logo"
      class="logo"
      src="./assets/logo.svg"
      width="125"
      height="125"
    /> -->
  </header>
  <HelloWorld msg="快篩實名制" />
  <main>
    <nav>
      <ul>
        <li><a href="#/">Map</a></li>
        <li><a href="#/table">Table</a></li>
      </ul>
    </nav>
    <article>
      <!-- <OpenLayersMap v-if="currentPath.value == '#/'" :information="information" />
      <Table v-else :information="information" /> -->
      <component :is="currentView" :information="information" />
    </article>
  </main>
</template>

<style>
@import "./assets/base.css";

/* #app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;

  font-weight: normal;
} */

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

a,
.green {
  text-decoration: none;
  color: hsla(160, 100%, 37%, 1);
  transition: 0.4s;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}

@media (min-width: 1024px) {
  /* body {
    display: flex;
    place-items: center;
  }

  #app {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
  } */

  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  /* Create two columns/boxes that floats next to each other */
  nav {
    float: left;
    width: 10%;
    height: 100vh; /* only for demonstration, should be removed */
    background: #ccc;
    padding: 20px;
  }

  /* Style the list inside the menu */
  nav ul {
    list-style-type: none;
    padding: 0;
  }

  nav a {
    color: inherit; /* 移除超連結顏色 */
    font-size: 1.2rem;
    text-decoration: none; /* 移除超連結底線 */
  }
  nav li:hover {
    background-color: rgb(115, 115, 115);
    color: white;
  }

  article {
    float: left;
    padding: 20px;
    width: 90%;
    background-color: #f1f1f1;
    height: 300px; /* only for demonstration, should be removed */
  }
}
</style>
