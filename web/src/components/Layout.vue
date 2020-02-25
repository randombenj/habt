<template>
  <md-app>
    <md-app-content>
      <div class="md-layout">
        <div class="md-layout-item md-size-15 md-small-hide"></div>
        <div class="md-layout-item">
          <slot></slot>
        </div>
        <div class="md-layout-item md-size-15 md-small-hide"></div>
      </div>
    </md-app-content>
  </md-app>
</template>

<script>
export default {
  name: 'Layout',
}
</script>
<style lang="scss" scoped>
  .md-app,
  .md-app-content,
  .md-layout {
    background-color: #fafafa !important;
  }
</style>