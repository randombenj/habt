
<template>
  <Layout>
    <PackageList :packages="packages" />
  </Layout>
</template>

<script>
import PackageList from '@/components/PackageList.vue'
import Layout from '@/components/Layout.vue'

export default {
  name: 'PackageSearch',
  components: {
    PackageList,
    Layout
  },
  computed: {
    packages () {
      return this.$store.state.search.packages
    }
  }
}
</script>