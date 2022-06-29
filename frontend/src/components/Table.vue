<template>
  <el-table :data="tableData.data" style="width: 100%">
    <el-table-column
      prop="來源資料時間"
      label="來源資料時間"
      sortable
      width="180"
    />
    <el-table-column prop="醫事機構名稱" label="醫事機構名稱" width="180" />
    <el-table-column
      prop="醫事機構地址"
      label="醫事機構地址"
      :formatter="formatter"
    />
  </el-table>
</template>

<script lang="ts" setup>
import type { TableColumnCtx } from "element-plus/es/components/table/src/table-column/defaults";
import { ref, reactive, onMounted, toRefs } from "vue";

// interface User {
//   date: string
//   name: string
//   address: string
// }

// const formatter = (row: User, column: TableColumnCtx<User>) => {
//   return row.address
// }
// 取得所有快篩資料
const props = defineProps({
  information: {
    type: Object,
    required: true,
    default: [],
  },
});
const { information } = toRefs(props);

const tableData = information;
</script>
