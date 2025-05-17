import { createI18n } from 'vue-i18n';

const messages = {
  en: {
    app: {
      title: 'VoxLens',
      subtitle: 'Voice to Text Summarization',
      description: 'Convert your voice recordings into concise summaries. Speak naturally and get both transcription and summary instantly.',
      transcriber: {
        title: 'Voice Summarizer',
        record: 'Record Audio',
        stop: 'Stop Recording',
        transcribing: 'Processing...',
        result: 'Results',
        error: 'An error occurred during processing.',
        summary: 'Summary',
        transcription: 'Full Transcription'
      },
      theme: {
        light: 'Light',
        dark: 'Dark'
      },
      lang: {
        en: 'English',
        es: 'Spanish'
      }
    }
  },
  es: {
    app: {
      title: 'VoxLens',
      subtitle: 'Resumidor de Voz a Texto',
      description: 'Convierte tus grabaciones de voz en resúmenes concisos. Habla naturalmente y obtén tanto la transcripción como el resumen al instante.',
      transcriber: {
        title: 'Resumidor de Voz',
        record: 'Grabar Audio',
        stop: 'Detener Grabación',
        transcribing: 'Procesando...',
        result: 'Resultados',
        error: 'Ocurrió un error durante el procesamiento.',
        summary: 'Resumen',
        transcription: 'Transcripción Completa'
      },
      theme: {
        light: 'Claro',
        dark: 'Oscuro'
      },
      lang: {
        en: 'Inglés',
        es: 'Español'
      }
    }
  }
};

const i18n = createI18n({
  legacy: false,
  locale: 'en',
  fallbackLocale: 'en',
  messages,
});

export default i18n; 