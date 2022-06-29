<script setup>
import { ref, reactive, getCurrentInstance, onMounted, onBeforeMount, toRefs } from "vue";
// import { getData } from "@/api/openData";

// 地圖基本資訊
const center = ref([40, 40]);
const projection = ref("EPSG:4326");
const zoom = ref(17);
const rotation = ref(0);

// 取得座標位置
let map = getCurrentInstance();
function successHandler(position) {
  center.value[0] = position.coords.longitude;
  center.value[1] = position.coords.latitude;
  console.log(map);
  map.ctx.$refs.map.render()
}

function errorHandler(err) {
  console.log(err);
}
function getMyLocation() {
  console.log("WTF");
  navigator.geolocation.getCurrentPosition(successHandler, errorHandler, {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0,
  });
}


// 取得所有快篩資料
const props = defineProps({
  information: {
    type: Array,
    required: true,
    default: [],
  },
});
const { information } = toRefs(props);

// first
// const information = reactive({ data: [] });
// const getD = function () {
//   getData()
//     .then((response) => {
//       console.log(response);
//       information.data = response.data;
//     })
//     .catch()
//     .finally();
// };

// second (Vue有Bug)
// const information = ref([]);
// const getD = function () {
//   getData()
//     .then((response) => {
//       // information.value = information.value.concat(response.data.msg);
//       information.value = response.data.msg;
//       console.log(information.value)
//     })
//     .catch()
//     .finally();
// };

onMounted(() => {
  getMyLocation();
  // getD();
  // console.log(getCurrentInstance().ctx.$refs.map);
  // console.log(information);
  
});

// 每30秒更新
// window.setInterval(() => {
//   setTimeout(getD, 0);
// }, 30000);

const overrideStyleFunction = (feature, style) => {
  let clusteredFeatures = feature.get("features");
  let size = clusteredFeatures.length;
  style.getText().setText(size.toString());
};
</script>

<template>
  <!-- <div class="div-right" v-if="information.data.length > 0">
    上次更新時間 ： {{ information.data[0].來源資料時間 }}
  </div> -->
  <el-button type="primary" @click="getMyLocation"> 現在位置</el-button>

  <ol-map
   ref="map"
    :loadTilesWhileAnimating="true"
    :loadTilesWhileInteracting="true"
    style="height: 1000px"
  >
    <!-- <ol-zoomtoextent-control
      :extent="[22.6465861, 120.3089428]"
      tipLabel="Fit to Turkey"
    />
    <ol-scaleline-control />
    <ol-rotate-control />
    <ol-zoom-control />
    <ol-zoomslider-control /> -->
    <!-- <ol-zoomtoextent-control :extent="[120.3089428, 22.6465861, 22.6465861, ]" tipLabel="Fit to Turkey" /> -->

    <ol-view
      ref="view"
      :center="center"
      :rotation="rotation"
      :zoom="zoom"
      :projection="projection"
    />
    <ol-tile-layer>
      <ol-source-osm />
    </ol-tile-layer>

    <!-- <div v-for="(item, index) in information.value" :key="index"> -->
    <div v-for="(item, index) in information.data" :key="index">
      <ol-overlay :position="[item.經度, item.緯度]">
        <div class="overlay-content">
          {{ item.醫事機構名稱 }}<br />
          地址: {{ item.醫事機構地址 }} <br />
          電話: {{ item.醫事機構電話 }}<br />
          存貨數量:
          {{ item.快篩試劑截至目前結餘存貨數量 }}
        </div>
      </ol-overlay>
    </div>
    <!-- <ol-vector-layer>
      <ol-source-cluster :distance="40">
        <ol-source-vector>
          <ol-feature v-for="(item, index) in information.data" :key="index">
            <ol-geom-point
              :coordinates="[item.經度, item.緯度]"
            ></ol-geom-point>
          </ol-feature>
        </ol-source-vector>
      </ol-source-cluster>

      <ol-style :overrideStyleFunction="overrideStyleFunction">
        <ol-style-stroke color="red" :width="2"></ol-style-stroke>
        <ol-style-fill color="rgba(255,255,255,0.1)"></ol-style-fill>

        <ol-style-circle :radius="10">
          <ol-style-fill color="#3399CC"></ol-style-fill>
          <ol-style-stroke color="#fff" :width="1"></ol-style-stroke>
        </ol-style-circle>
        <ol-style-text>
          <ol-style-fill color="#fff"></ol-style-fill>
        </ol-style-text>
      </ol-style>
    </ol-vector-layer> -->
  </ol-map>
</template>

<style>
.overlay-content {
  background: #efefef;
  box-shadow: 0 5px 10px rgb(2 2 2 / 20%);
  padding: 10px 20px;
  font-size: 16px;
}

.div-right {
  font-family: DFKai-sb;
  font-weight: bold;
  float: right;
}
</style>
