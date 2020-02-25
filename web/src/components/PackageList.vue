<template>
  <div>{{ packages }}</div>
</template>

<script>
export default {
  name: 'PackageList',
  props: {
    packages: Array
  }
}
</script>
