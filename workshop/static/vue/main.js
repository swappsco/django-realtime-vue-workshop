import Vue from "vue"
import App from "./App.vue"
import SurveyDetail from "./SurveyDetail.vue"

if (document.getElementById('app') != null) {
    new Vue({
        render: h => h(App),
    }).$mount('#app')
}

if (document.getElementById('survey-detail') != null) {
    new Vue({
        render: h => h(SurveyDetail),
    }).$mount('#survey-detail')
}
