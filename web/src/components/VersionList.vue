<template>
  <div>
    <md-card class="package-list-card">
      <md-list class="md-dense">
        <md-list-item
          v-for="version in versions"
          :to="`/${packageName}/${version.version}`"
          :key="version.id"
        >
          <div class="md-list-item-text">
            {{ version.version }}
          </div>
          <md-badge
            v-for="installtarget in version.installtargets"
            :key="`${installtarget.distribution.id}/${installtarget.part.id}`"
            :md-content="`${installtarget.distribution.name}/${installtarget.part.name}`"
            class="md-square version-badge"
          />
        </md-list-item>
      </md-list>
    </md-card>
  </div>
</template>

<script>
export default {
  name: 'VersionList',
  props: {
    packageName: String,
    versions: Array
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
