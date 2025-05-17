<template>
  <button 
    @click="toggleTheme" 
    :aria-label="theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'"
    class="theme-toggle-btn"
  >
    <SunIcon v-if="theme === 'dark'" class="icon" />
    <MoonIcon v-else class="icon" />
  </button>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { SunIcon, MoonIcon } from '@heroicons/vue/24/outline';

const theme = ref('dark');

function setTheme(newTheme: string) {
  theme.value = newTheme;
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}

function toggleTheme() {
  setTheme(theme.value === 'dark' ? 'light' : 'dark');
}

onMounted(() => {
  const saved = localStorage.getItem('theme');
  setTheme(saved === 'light' ? 'light' : 'dark');
});
</script>

<style scoped>
.theme-toggle-btn {
  background: none;
  border: none;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--color-text-secondary);
  transition: all var(--transition-fast);
}

.theme-toggle-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--color-primary);
}

.icon {
  width: 1.5rem;
  height: 1.5rem;
}
</style> 