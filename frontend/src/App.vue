<script setup>
import {
  ref,
  reactive,
  getCurrentInstance,
  onMounted,
  onBeforeMount,
  computed,
} from "vue";
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import Table from "./components/Table.vue";
import GoogleMapApi from "./components/GppgleMapApi.vue";
import Leaftlet from "./components/Leaftlet.vue";
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

// Router
const routes = {
  "/": OpenLayersMap,
  "/OpenLayersMap": OpenLayersMap,
  "/Leaftlet": Leaftlet,
  "/GoogleMapApi": GoogleMapApi,
};
const currentPath = ref(window.location.hash);

window.addEventListener("hashchange", () => {
  currentPath.value = window.location.hash;
});

const currentView = computed(() => {
  console.log(currentPath.value.slice(1));
  return routes[currentPath.value.slice(1) || "/"] || NotFound;
});
</script>

<template>
  <header>
    <!-- <img
      alt="Vue logo"
      class="logo"
      src="./assets/logo.svg"
      width="50"
      height="70"
    /> -->
    <Header msg="快篩試劑查詢" />
  </header>

  <main>
    <component :is="currentView" :information="information" />
  </main>
  <footer>
    <Footer />
  </footer>
</template>

<style>
@import "./assets/base.css";

header {
  line-height: 1.5;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgb(255, 174, 0);
  height: 80px;
}

footer {
  display: flex;
  justify-content: space-between;
  height: 30px;
  background-color: rgb(255, 174, 0);
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}
</style>
