
<template>
  <Layout>
    {{ packageName }}
  </Layout>
</template>

<script>
import Layout from '@/components/Layout.vue'

export default {
  name: 'PackageDetail',
  components: {
    Layout
  },
  data() {
    return {
      packageName: this.$route.params.package,
      version: this.$route.params.version
    }
  }
}
</script>