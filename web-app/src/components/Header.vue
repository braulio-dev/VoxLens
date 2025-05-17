<template>
  <header class="main-header">
    <div class="header-container">
      <div class="logo">
        <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="16" cy="16" r="16" fill="var(--color-primary)"/>
          <path d="M10 16C10 13.2386 12.2386 11 15 11C17.7614 11 20 13.2386 20 16C20 18.7614 17.7614 21 15 21C12.2386 21 10 18.7614 10 16Z" fill="#fff"/>
        </svg>
        <span class="logo-text">Vox<span class="highlight">Lens</span></span>
      </div>
      <nav class="nav">
        <a href="#" class="nav-link">Home</a>
        <a href="https://github.com/braulio-dev/VoxLens" target="_blank" rel="noopener" class="nav-link">
          <GithubIcon class="icon-small" />
          GitHub
        </a>
      </nav>
      <div class="header-controls">
        <button class="icon-btn glassy" @click="$emit('toggle-lang')" aria-label="Language">
          <GlobeAltIcon class="icon" />
        </button>
        <button class="icon-btn glassy" @click="$emit('toggle-theme')" aria-label="Theme">
          <component :is="theme === 'dark' ? SunIcon : MoonIcon" class="icon" />
        </button>
        <a href="#transcriber" class="btn-primary">
          <span>Try It</span>
          <span class="btn-glow"></span>
        </a>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { GlobeAltIcon, SunIcon, MoonIcon } from '@heroicons/vue/24/outline';
import { defineProps } from 'vue';

// Import GitHub icon
const GithubIcon = {
  template: `
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 2C6.477 2 2 6.484 2 12.017C2 16.455 4.865 20.127 8.84 21.43C9.34 21.528 9.522 21.221 9.522 20.958C9.522 20.721 9.513 20.033 9.508 19.241C6.728 19.861 6.139 17.924 6.139 17.924C5.684 16.821 5.027 16.516 5.027 16.516C4.132 15.878 5.097 15.891 5.097 15.891C6.092 15.964 6.626 16.942 6.626 16.942C7.521 18.47 8.969 17.973 9.541 17.717C9.637 17.052 9.909 16.554 10.212 16.258C7.976 15.958 5.636 15.074 5.636 11.156C5.636 10.017 6.039 9.084 6.647 8.357C6.539 8.105 6.183 7.053 6.747 5.594C6.747 5.594 7.587 5.328 9.497 6.771C10.308 6.552 11.175 6.442 12.034 6.438C12.89 6.442 13.757 6.552 14.571 6.771C16.479 5.328 17.317 5.594 17.317 5.594C17.883 7.053 17.527 8.105 17.419 8.357C18.029 9.084 18.429 10.017 18.429 11.156C18.429 15.085 16.084 15.954 13.842 16.249C14.219 16.609 14.559 17.326 14.559 18.419C14.559 19.974 14.546 20.631 14.546 20.958C14.546 21.225 14.726 21.535 15.234 21.429C19.206 20.125 22.067 16.454 22.067 12.017C22.067 6.484 17.591 2 12.067 2H12Z" fill="currentColor"/>
    </svg>
  `
};

const props = defineProps<{ theme: string }>();
</script>

<style scoped>
.main-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
  height: 72px;
  backdrop-filter: blur(var(--glass-blur));
  -webkit-backdrop-filter: blur(var(--glass-blur));
  background: var(--color-bg-glass);
  border-bottom: var(--border-thin);
  box-shadow: var(--shadow-sm);
}

.header-container {
  max-width: 1280px;
  margin: 0 auto;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2rem;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  font-size: 1.5rem;
  font-weight: 900;
  color: var(--color-text);
  letter-spacing: -0.02em;
}

.logo-text {
  background: linear-gradient(90deg, var(--color-text) 0%, var(--color-primary) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.highlight {
  color: var(--color-primary);
  font-weight: 900;
}

.nav {
  display: flex;
  gap: 2.5rem;
}

.nav-link {
  color: var(--color-text);
  text-decoration: none;
  font-weight: 500;
  font-size: 1rem;
  position: relative;
  transition: color 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--gradient-primary);
  transition: width 0.3s ease;
  border-radius: var(--radius-full);
}

.nav-link:hover {
  color: var(--color-primary);
}

.nav-link:hover::after {
  width: 100%;
}

.header-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.icon-btn {
  background: none;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  cursor: pointer;
  color: var(--color-text);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
  overflow: hidden;
  backdrop-filter: blur(var(--glass-blur));
  -webkit-backdrop-filter: blur(var(--glass-blur));
  background: rgba(255, 255, 255, 0.05);
  border: var(--border-thin);
}

.icon-btn:hover {
  background: rgba(var(--color-primary-rgb), 0.15);
  color: var(--color-primary);
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}

.icon {
  width: 1.5em;
  height: 1.5em;
}

.icon-small {
  width: 1.2em;
  height: 1.2em;
}

.btn-primary {
  background: var(--gradient-primary);
  color: white;
  border: none;
  padding: 0.7rem 1.5rem;
  font-weight: 700;
  border-radius: var(--radius-full);
  font-size: 0.95rem;
  text-decoration: none;
  transition: all 0.3s var(--transition-bounce);
  box-shadow: var(--shadow-md);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-glow {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0) 70%);
  opacity: 0;
  transform: scale(0.5);
  transition: transform 0.6s, opacity 0.6s;
}

.btn-primary:hover {
  transform: translateY(-2px) scale(1.05);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}

.btn-primary:hover .btn-glow {
  opacity: 0.15;
  transform: scale(1);
}

@media (max-width: 768px) {
  .nav {
    display: none;
  }
  
  .header-container {
    padding: 0 1rem;
  }
}
</style> 