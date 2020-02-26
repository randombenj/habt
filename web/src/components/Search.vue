<template>
  <md-autocomplete
    @md-changed="search"
    v-model="selected"
    :md-options="[]"
    md-layout="box"
    md-dense>
    <label>Search debian packages</label>
  </md-autocomplete>
</template>

<script>
export default {
  name: 'Search',
  data: () => ({
    selected: null
  }),
  methods: {
    search(query) {
      this.$store.dispatch('search/search', query)
      if (this.$route.path !== '/') {
        this.$router.replace('/')
      }
    }
  }
}
</script>
