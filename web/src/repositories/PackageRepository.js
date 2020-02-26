import Repository from '@/repositories/Repository'

export default {

  /**
   * Returns all projects
   */
  search(query) {
    return Repository.get(`${Repository.defaults.baseURL}/search/${query}`)
  },

  /**
   * Returns details of a package
   * @param {string} packageName Name of the package
   */
  package(packageName) {
    return Repository.get(`${Repository.defaults.baseURL}/package/${packageName}`)
  },

  /**
   * Returns detail of a package version
   * @param {string} packageName Name of the package
   * @param {string} version Name of the package version
   */
  version(packageName, version) {
    return Repository.get(`${Repository.defaults.baseURL}/package/${packageName}/version/${version}`)
  }
}