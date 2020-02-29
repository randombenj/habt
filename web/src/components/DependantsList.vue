<template>
  <div>
    <md-card class="package-list-card no-space">
      <md-list class="md-dense">
        <md-list-item
          v-for="dependant in dependants"
          :key="`${dependant.dependency_section_id}/${dependant.package_version_id}`"
        >
          <div class="md-list-item-text">
            {{ dependant.package_version.package.name }} ({{ dependant.package_version.version }})
          </div>
          <md-badge
            :md-content="dependant.dependency_section.name"
            class="md-square version-badge"
          />
        </md-list-item>
      </md-list>
    </md-card>
  </div>
</template>

<script>
// FIXME: remove and combine with DependencyList ...
export default {
  name: 'DependantsList',
  props: {
    dependants: Array
  }
}
</script>

<style lang="scss" scoped>
  .package-list-card {

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
