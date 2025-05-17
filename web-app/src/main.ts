import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import i18n from './i18n'
import Transcriber from './components/Transcriber.vue'

const app = createApp(App)
app.component('Transcriber', Transcriber)
app.use(i18n).mount('#app')
