<template>
  <layout>
    <md-autocomplete
      v-model="selected"
      :md-options="[]"
      md-layout="box"
      md-dense>
      <label>Search debian packages</label>
    </md-autocomplete>
  </layout>
</template>

<script>
import Layout from './components/Layout.vue'

export default {
  name: 'App',
  components: {
    Layout
  },
  data: () => ({
    selected: null
  })
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
