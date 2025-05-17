<template>
  <div class="lang-toggle">
    <button
      v-for="lang in langs"
      :key="lang"
      :class="{ active: current === lang }"
      @click="setLang(lang)"
      :aria-label="$t('app.lang.' + lang)"
      class="lang-btn"
    >
      {{ lang.toUpperCase() }}
    </button>
  </div>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { ref, onMounted } from 'vue';

const langs = ['en', 'es'];
const { locale } = useI18n();
const current = ref(locale.value);

function setLang(lang: string) {
  locale.value = lang;
  current.value = lang;
  localStorage.setItem('lang', lang);
}

onMounted(() => {
  const saved = localStorage.getItem('lang');
  if (saved && langs.includes(saved)) setLang(saved);
});
</script>

<style scoped>
.lang-toggle {
  display: flex;
  background: rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-md);
  padding: 0.25rem;
}

.lang-btn {
  background: none;
  border: none;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  color: var(--color-text-secondary);
  padding: 0.3rem 0.6rem;
  border-radius: var(--radius-sm);
  transition: all var(--transition-fast);
}

.lang-btn.active {
  background: var(--color-primary);
  color: white;
}

.lang-btn:not(.active):hover {
  color: var(--color-text);
  background: rgba(255, 255, 255, 0.1);
}
</style> 