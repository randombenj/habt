
<template>
  <Layout>
    <Search />
    <PackageList :packages="packages" />
  </Layout>
</template>

<script>
import Search from '@/components/Search.vue'
import PackageList from '@/components/PackageList.vue'
import Layout from '@/components/Layout.vue'

export default {
  name: 'Home',
  components: {
    PackageList,
    Search,
    Layout
  },
  computed: {
    packages () {
      return this.$store.state.search.packages
    }
  }
}
</script>