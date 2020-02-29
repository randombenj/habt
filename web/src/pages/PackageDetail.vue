
<template>
  <Layout>
    <span class="md-headline">{{ debPackage.name }}</span>
    <span class="md-subheading version-header">{{ currentVersion.version }}</span>
    <VersionList :packageName="debPackage.name" :versions="debPackage.versions" class="version-list" />
    <md-card class="no-space version-information">
      <md-card-content>
        <strong>{{ currentVersion.title }}</strong>
        <div class="package-description">{{ currentVersion.description }}</div>
      </md-card-content>

      <md-list>
        <md-list-item>
          <md-icon>email</md-icon>
          <div class="md-list-item-text">
            <span>{{ currentVersion.maintainer }}</span>
            <span class="secondary-information">Maintainer</span>
          </div>
        </md-list-item>

        <md-list-item :href="currentVersion.vcs_browser" target="_blank" v-if="currentVersion.vcs_browser !== ''">
          <md-icon>code</md-icon>
          <div class="md-list-item-text">
            <span>{{ currentVersion.vcs_browser }}</span>
            <span class="secondary-information">Sourcecode</span>
          </div>
        </md-list-item>
      </md-list>

    </md-card>

    <md-card class="no-space source-list" v-if="currentVersion.installtargets !== []">
      <span
        v-for="target in currentVersion.installtargets"
        :key="`${target.architecture_id}/${target.archive_id}/${target.part_id}/${target.distribution_id}`"
      >deb [arch={{ target.architecture.name }}] {{ target.archive.url }} {{ target.distribution.name }} {{ target.part.name }}</span>
    </md-card>

    <span v-if="currentVersion.dependencies !== []" class="md-title">Dependencies</span>
    <DependencyList v-if="currentVersion.dependencies !== []" :dependencies="currentVersion.dependencies" class="version-list" />

    <span v-if="debPackage.referenced_by !== []" class="md-title">Dependants</span>
    <DependantsList v-if="debPackage.referenced_by !== []" :dependants="debPackage.referenced_by" class="version-list" />
  </Layout>
</template>

<script>
import PackageRepository from '@/repositories/PackageRepository'

import Layout from '@/components/Layout.vue'
import VersionList from '@/components/VersionList.vue'
import DependencyList from '@/components/DependencyList.vue'
import DependantsList from '@/components/DependantsList.vue'

export default {
  name: 'PackageDetail',
  components: {
    Layout,
    VersionList,
    DependencyList,
    DependantsList
  },
  data() {
    return {
      debPackage: {},
      currentVersion: {},
    }
  },
  async created() {
    this.debPackage  = (await PackageRepository.package(this.$route.params.package)).data.package
    this.currentVersion = (await PackageRepository.version(
      this.$route.params.package,
      this.$route.params.version || this.debPackage.versions[0].version
    )).data.version
  }
}
</script>
<style lang="scss" scoped>
  .package-description {
    white-space: pre;
    margin-top: 8px;
  }

  .version-header {
    float: right;
    color: #8e8e8e;
  }

  .secondary-information {
    color: #8e8e8e;
  }

  .version-list {
    margin-top: 16px;
    margin-bottom: 8px;
  }

  .version-information {
    border-left: 4px solid #777777;
  }

  .source-list {
    margin-top: 16px;
    padding: 8px;
    background-color: #0e0e0e;
    color: #ffffff;
  }

  .md-title {
    margin-top: 16px;
    display: block;
  }
</style>