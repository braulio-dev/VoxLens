<script setup lang="ts">
import Header from './components/Header.vue';
import Hero from './components/Hero.vue';
import Transcriber from './components/Transcriber.vue';
import { useI18n } from 'vue-i18n';
import { ref, onMounted } from 'vue';

const { t, locale } = useI18n();
const theme = ref('dark');

function setTheme(newTheme: string) {
  theme.value = newTheme;
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}

function toggleTheme() {
  setTheme(theme.value === 'dark' ? 'light' : 'dark');
}

function toggleLang() {
  locale.value = locale.value === 'en' ? 'es' : 'en';
  localStorage.setItem('lang', locale.value);
}

onMounted(() => {
  setTheme(localStorage.getItem('theme') || 'dark');
  locale.value = localStorage.getItem('lang') || 'en';
});
</script>

<template>
  <div class="app">
    <div class="background">
      <div class="material-bg"></div>
      <div class="noise-overlay"></div>
      <div class="background-glow"></div>
      <div class="background-grid"></div>
    </div>
    
    <Header :theme="theme" @toggle-theme="toggleTheme" @toggle-lang="toggleLang" />
    
    <div class="app-content">
      <Hero>
        <template #title>{{ t('app.title') }}</template>
        <template #subtitle>{{ t('app.subtitle') }}</template>
        <template #description>{{ t('app.description') }}</template>
      </Hero>
      
      <main class="main-container">
        <Transcriber />
      </main>
    </div>
  </div>
</template>

<style>
@import './assets/main.css';

.app {
  position: relative;
  min-height: 100vh;
  width: 100%;
  overflow-x: hidden;
}

.background {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: -1;
  overflow: hidden;
}

.material-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--color-bg);
}

.noise-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%' height='100%' filter='url(%23noiseFilter)' opacity='0.05'/%3E%3C/svg%3E");
  opacity: 0.2;
}

.background-glow {
  position: absolute;
  top: -10%;
  right: -10%;
  width: 60%;
  height: 60%;
  border-radius: 100%;
  background: radial-gradient(circle, rgba(var(--color-primary-rgb), 0.15) 0%, rgba(var(--color-primary-rgb), 0) 70%);
  filter: blur(60px);
  opacity: 0.8;
  animation: glow-shift 15s ease-in-out infinite alternate;
}

.background-grid {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
  background-size: 40px 40px;
  opacity: 0.3;
}

.app-content {
  position: relative;
  z-index: 1;
}

.main-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
}

@keyframes glow-shift {
  0% {
    opacity: 0.6;
    transform: translate(0, 0);
  }
  50% {
    opacity: 0.8;
  }
  100% {
    opacity: 0.6;
    transform: translate(-15%, 15%);
  }
}

@media (prefers-reduced-motion) {
  .background-glow {
    animation: none;
  }
}
</style>
