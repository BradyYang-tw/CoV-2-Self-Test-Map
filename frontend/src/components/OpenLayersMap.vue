<script setup>
import { ref } from "vue";

const center = ref([40, 40]);
const projection = ref("EPSG:4326");
const zoom = ref(16);
const rotation = ref(0);

// console.log(center.value)
function successHandler(position) {
    center.value[0] = position.coords.longitude;
    center.value[1] = position.coords.latitude;
    
//   console.log(position.coords.latitude, position.coords.longitude);
}

function errorHandler(err) {
  console.log(err);
}

navigator.geolocation.getCurrentPosition(successHandler, errorHandler, {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0,
});
</script>

<template>
  <ol-map
    :loadTilesWhileAnimating="true"
    :loadTilesWhileInteracting="true"
    style="height: 1000px;"
  >
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

    <ol-overlay :position="[ 120.3061704837771, 22.64975823049841 ]">
        <template v-slot="slotProps">
            <div class="overlay-content">
                Home<br>
                Position: {{ slotProps.position }}
            </div>
        </template>
    </ol-overlay>
    <ol-overlay :position="[ 120.3061704837771, 22.643912738628673 ]">
        <template v-slot="slotProps">
            <div class="overlay-content">
                Basketball Court<br>
                Position: {{ slotProps.position }}
            </div>
        </template>
    </ol-overlay>
    
  </ol-map>
</template>

<style>
.overlay-content {
    background: #efefef;
    box-shadow: 0 5px 10px rgb(2 2 2 / 20%);
    padding: 10px 20px;
    font-size: 16px;
}
</style>