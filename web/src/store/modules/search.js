import PackageRepository from '@/repositories/PackageRepository'


const state = {
  packages: []
}

const getters = {
  packages (state) {
    return state.packages
  }
}

const actions = {
  async search ({ commit }, query) {
    try {
      let packages = []
      if (query) {
        packages = (await PackageRepository.search(query)).data.results
      }
      commit('setPackages', { packages })
    } catch(err) {
      // TODO: handle error
      console.error('Search error', err)
    }
  }
}

const mutations = {
  setPackages (state, { packages }) {
    state.packages = packages
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}