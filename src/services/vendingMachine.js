import api from '@/services/api'

export default {
    loadJson(payload) {
        return api.post(`load_json`, payload)
                    .then(response => response.data);
    },
    getItems() {
        return api.get(`items`)
                .then(response => response.data);
    },
    insertMoney(money) {
        return api.post(`insert_money`, money)
                    .then(response => response.data);
    },
    getItem(itemName) {
        return api.post(`get_item`, itemName)
                    .then(response => response.data);
    }
}