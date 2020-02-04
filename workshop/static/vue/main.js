import Vue from "vue"
import App from "./App.vue"

if (document.getElementById('app') != null) {
    new Vue({
        render: h => h(App),
    }).$mount('#app')
}
