import stockService from '../../services/vendingMachine'

const state = {
    items: []
}

const getters = {
    items: state => {
        return state.items
    }
}

const actions = {
    loadJson({ commit }, json) {
        stockService.loadJson(json)
        .then(() => {
            commit('loadJson', json)
        })
    },
    getItems({ commit }) {
        stockService.getItems()
        .then(items => {
            commit('setItems', items)
        })
    },
    insertMoney({ commit }, money) {
        stockService.insertMoney(money)
        .then(() => {
            commit('insertMoney', money)
        })
    },
    getItem({ commit }, itemName) {
        stockService.getItem(itemName)
        .then(() => {
            commit('getItem', itemName)
        })
    }
}

const mutations = {
    setItems (state, items) {
        state.items = items;
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}