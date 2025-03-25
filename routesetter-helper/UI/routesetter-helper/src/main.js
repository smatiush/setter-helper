import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// Importa gli stili di Vuetify e il plugin
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import '@mdi/font/css/materialdesignicons.css'; // opzionale per le icone

// Crea un'istanza di Vuetify
const vuetify = createVuetify();

const app = createApp(App);
app.use(router);
app.use(vuetify);
app.mount('#app');