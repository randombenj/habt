<template>
  <div>
    <Layout>
      <Search />
    </Layout>
    <router-view></router-view>
  </div>
</template>

<script>
import Layout from '@/components/Layout.vue'
import Search from '@/components/Search.vue'

export default {
  name: 'app',
  components: {
    Search,
    Layout
  }
}
</script>
