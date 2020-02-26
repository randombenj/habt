<template>
  <div>
    <md-card v-if="packages.length" class="package-list-card">
      <md-list>
        <md-list-item
          v-for="debPackage in packages"
          :to="`/${debPackage.name}`"
          :key="debPackage.id"
        >
          <div class="md-list-item-text">
            {{ debPackage.name }}
          </div>
          <md-badge
            v-for="debVersion in debPackage.versions"
            :key="debVersion.id"
            :md-content="debVersion.version"
            class="md-square version-badge"
          />
        </md-list-item>
      </md-list>
    </md-card>
    <img v-if="!packages.length" class="center" alt="logo" src="@/assets/logo.png" />
  </div>
</template>

<script>
export default {
  name: 'PackageList',
  props: {
    packages: Array
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

    .version-badge {
      background-color: #424242;
    }

    .md-list-item {
      border-bottom: 1px solid var(--md-theme-default-divider, rgba(0,0,0,0.12));
    }
  }
</style>
