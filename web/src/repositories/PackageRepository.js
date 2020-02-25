import Repository from '@/repositories/Repository'

export default {

  /**
   * Returns all projects
   */
  search(query) {
    return Repository.get(`${Repository.defaults.baseURL}/search/${query}`)
  }
}