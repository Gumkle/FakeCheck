import Vue from 'vue';
import {store} from './store';
import BootstrapVue from 'bootstrap-vue';

Vue.use(BootstrapVue);
new Vue({
    el: "#app",
    store
});