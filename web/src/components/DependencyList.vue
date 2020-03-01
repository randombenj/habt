<template>
  <div>
    <md-card class="package-list-card">
      <md-list class="md-dense">
        <md-list-item
          v-for="dependency in dependencies"
          :key="`${dependency.dependency_section_id}/${dependency.package_id}`"
        >
          <div class="md-list-item-text">
            {{ dependency.package.name }} {{ dependency.version }}
          </div>
          <md-badge
            :md-content="dependency.dependency_section.name"
            class="md-square version-badge"
          />
        </md-list-item>
      </md-list>
    </md-card>
  </div>
</template>

<script>
export default {
  name: 'DependencyList',
  props: {
    dependencies: Array
  }
}
</script>

<style lang="scss" scoped>
  .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .package-list-card {
    margin-left: 0px;
    margin-right: 0px;

    .md-list-item-text {
      font-size: 1.2em;
    }

    .version-badge {
      background-color: #424242;
    }

    .md-list-item:not(:last-child) {
      border-bottom: 1px solid var(--md-theme-default-divider, rgba(0,0,0,0.12));
    }
  }
</style>
