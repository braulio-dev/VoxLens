<template>
  <section id="transcriber" class="transcriber glassy">
    <h2 class="section-title">
      <span class="highlight-text">{{ $t('app.transcriber.title', 'Voice Summarizer') }}</span>
    </h2>
    
    <div class="transcriber-container">
      <div class="controls-container">
        <div class="audio-controls">
          <button
            :disabled="recording || loading"
            @click="startRecording"
            v-if="!recording"
            class="btn-record"
            :class="{ 'pulse': !recording && !loading }"
          >
            <MicrophoneIcon class="icon" />
            <span>{{ $t('app.transcriber.record', 'Record Audio') }}</span>
            <span class="btn-glow"></span>
          </button>
          
          <button
            :disabled="!recording"
            @click="stopRecording"
            v-if="recording"
            class="btn-stop"
          >
            <StopIcon class="icon" />
            <span>{{ $t('app.transcriber.stop', 'Stop Recording') }}</span>
            <span class="btn-glow"></span>
          </button>
        </div>
      
        <div 
          class="dropzone"
          :class="{ 'active': isDragging }"
          @dragover.prevent="handleDragOver"
          @dragleave.prevent="handleDragLeave"
          @drop.prevent="handleDrop"
          @click="triggerFileUpload"
        >
          <ArrowUpTrayIcon class="icon-upload" />
          <p class="dropzone-text">
            {{ isDragging ? $t('app.transcriber.dropzoneActive', 'Drop to process') : $t('app.transcriber.dropzone', 'Drag & drop audio file here') }}
          </p>
          <p class="dropzone-or">{{ $t('app.transcriber.or', 'or') }}</p>
          <button class="btn-upload">
            {{ $t('app.transcriber.upload', 'Upload Audio') }}
          </button>
          <p class="dropzone-subtext">{{ $t('app.transcriber.uploadSubtext', 'Supports MP3, WAV, M4A, FLAC, OGG') }}</p>
          <input 
            ref="fileInput"
            type="file" 
            accept="audio/*" 
            class="file-input" 
            @change="handleFileSelect"
          />
        </div>
      </div>
      
      <div class="status-indicator">
        <div v-if="loading" class="loading">
          <div class="loading-animation">
            <div class="loading-bar"></div>
            <div class="loading-bar"></div>
            <div class="loading-bar"></div>
            <div class="loading-bar"></div>
          </div>
          <span>{{ $t('app.transcriber.transcribing', 'Processing...') }}</span>
        </div>
        <div v-if="error" class="error">
          <ExclamationCircleIcon class="icon-error" />
          <span>{{ $t('app.transcriber.error', 'An error occurred') }}</span>
        </div>
      </div>
      
      <div v-if="transcription || summary" class="result glassy">
        <div class="result-header">
          <h3>{{ $t('app.transcriber.result', 'Results') }}</h3>
          <button class="btn-copy" @click="copyResult" title="Copy summary to clipboard">
            <ClipboardDocumentIcon class="icon-small" />
          </button>
        </div>
        <div class="result-content">
          <div v-if="summary" class="summary-section">
            <h4>{{ $t('app.transcriber.summary', 'Summary') }}</h4>
            <p>{{ summary }}</p>
          </div>
          <div v-if="transcription" class="transcription-section">
            <h4>{{ $t('app.transcriber.transcription', 'Full Transcription') }}</h4>
            <p>{{ transcription }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { 
  MicrophoneIcon, 
  StopIcon, 
  ExclamationCircleIcon,
  ClipboardDocumentIcon,
  ArrowUpTrayIcon
} from '@heroicons/vue/24/outline';

const recording = ref(false);
const loading = ref(false);
const transcription = ref('');
const summary = ref('');
const error = ref(false);
const isDragging = ref(false);
const fileInput = ref<HTMLInputElement | null>(null);
let mediaRecorder: MediaRecorder | null = null;
let audioChunks: BlobPart[] = [];

function startRecording() {
  transcription.value = '';
  summary.value = '';
  error.value = false;
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      mediaRecorder = new MediaRecorder(stream);
      audioChunks = [];
      mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
        sendAudio(audioBlob, 'recording.webm');
      };
      mediaRecorder.start();
      recording.value = true;
    })
    .catch(() => {
      error.value = true;
    });
}

function stopRecording() {
  if (mediaRecorder && recording.value) {
    mediaRecorder.stop();
    recording.value = false;
  }
}

async function sendAudio(blob: Blob, filename: string) {
  loading.value = true;
  error.value = false;
  transcription.value = '';
  summary.value = '';
  try {
    const formData = new FormData();
    formData.append('file', blob, filename);
    const response = await fetch('http://localhost:8000/summarize', {
      method: 'POST',
      body: formData,
    });
    const data = await response.json();
    transcription.value = data.transcription || '';
    summary.value = data.summary || '';
  } catch (e) {
    error.value = true;
  } finally {
    loading.value = false;
  }
}

function copyResult() {
  if (summary.value) {
    navigator.clipboard.writeText(summary.value);
  }
}

function handleDragOver(e: DragEvent) {
  e.preventDefault();
  isDragging.value = true;
}

function handleDragLeave() {
  isDragging.value = false;
}

function handleDrop(e: DragEvent) {
  isDragging.value = false;
  
  if (!e.dataTransfer) return;
  
  const files = e.dataTransfer.files;
  if (files.length > 0 && files[0].type.startsWith('audio/')) {
    processFile(files[0]);
  } else {
    error.value = true;
  }
}

function handleFileSelect(e: Event) {
  const target = e.target as HTMLInputElement;
  if (target.files && target.files.length > 0) {
    processFile(target.files[0]);
  }
}

function processFile(file: File) {
  if (file.type.startsWith('audio/')) {
    sendAudio(file, file.name);
  } else {
    error.value = true;
  }
}

function triggerFileUpload() {
  if (fileInput.value) {
    fileInput.value.click();
  }
}
</script>

<style scoped>
.transcriber {
  max-width: 800px;
  margin: 3.5rem auto;
  padding: 3.5rem 2.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  backdrop-filter: blur(var(--glass-blur));
}

.section-title {
  font-size: 2.2rem;
  font-weight: 800;
  margin-bottom: 2.5rem;
  text-align: center;
  position: relative;
}

.highlight-text {
  position: relative;
  color: var(--color-primary);
  display: inline-block;
}

.highlight-text::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 30%;
  width: 40%;
  height: 3px;
  background: var(--gradient-primary);
  border-radius: var(--radius-full);
}

.transcriber-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.controls-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.audio-controls {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.btn-record, .btn-stop {
  font-size: 1.1rem;
  padding: 1rem 2.5rem;
  border-radius: var(--radius-full);
  border: none;
  font-weight: 700;
  cursor: pointer;
  box-shadow: var(--shadow-md);
  transition: all 0.3s var(--transition-bounce);
  display: flex;
  align-items: center;
  gap: 0.8rem;
  position: relative;
  overflow: hidden;
}

.btn-record {
  background: var(--gradient-primary);
  color: white;
}

.btn-stop {
  background: var(--gradient-accent);
  color: white;
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

.btn-record:hover, .btn-stop:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}

.btn-record:hover .btn-glow, .btn-stop:hover .btn-glow {
  opacity: 0.15;
  transform: scale(1);
}

.btn-record:disabled, .btn-stop:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
  box-shadow: var(--shadow-sm);
}

.dropzone {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  border: 2px dashed rgba(var(--color-primary-rgb), 0.3);
  border-radius: var(--radius-md);
  background: rgba(var(--color-primary-rgb), 0.03);
  transition: all 0.3s ease;
  cursor: pointer;
  margin-top: 1rem;
}

.dropzone:hover {
  border-color: rgba(var(--color-primary-rgb), 0.7);
  background: rgba(var(--color-primary-rgb), 0.05);
}

.dropzone.active {
  border-color: var(--color-primary);
  background: rgba(var(--color-primary-rgb), 0.1);
}

.icon-upload {
  width: 2.5rem;
  height: 2.5rem;
  color: var(--color-primary);
  margin-bottom: 1rem;
}

.dropzone-text {
  font-size: 1.1rem;
  color: var(--color-text);
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.dropzone-or {
  margin: 0.5rem 0;
  color: var(--color-text-secondary);
}

.dropzone-subtext {
  margin-top: 0.8rem;
  font-size: 0.9rem;
  color: var(--color-text-secondary);
}

.btn-upload {
  background: transparent;
  border: 1px solid rgba(var(--color-primary-rgb), 0.5);
  color: var(--color-primary);
  padding: 0.6rem 1.5rem;
  border-radius: var(--radius-full);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-upload:hover {
  background: rgba(var(--color-primary-rgb), 0.1);
  transform: translateY(-2px);
}

.file-input {
  display: none;
}

.icon {
  width: 1.5em;
  height: 1.5em;
}

.icon-small {
  width: 1.2em;
  height: 1.2em;
}

.icon-error {
  color: var(--color-error);
  width: 1.2em;
  height: 1.2em;
}

.status-indicator {
  display: flex;
  justify-content: center;
  min-height: 2.5rem;
}

.loading {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  color: var(--color-accent);
  font-weight: 500;
}

.loading-animation {
  display: flex;
  align-items: flex-end;
  height: 1.5rem;
  gap: 0.2rem;
}

.loading-bar {
  width: 0.3rem;
  height: 0.5rem;
  background-color: var(--color-accent);
  border-radius: var(--radius-sm);
  animation: loading-bar 1.2s ease-in-out infinite;
}

.loading-bar:nth-child(1) {
  animation-delay: 0s;
}

.loading-bar:nth-child(2) {
  animation-delay: 0.2s;
}

.loading-bar:nth-child(3) {
  animation-delay: 0.4s;
}

.loading-bar:nth-child(4) {
  animation-delay: 0.6s;
}

@keyframes loading-bar {
  0%, 100% {
    height: 0.5rem;
  }
  50% {
    height: 1.5rem;
  }
}

.error {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--color-error);
  font-weight: 500;
}

.result {
  width: 100%;
  overflow: hidden;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  transition: transform 0.3s, box-shadow 0.3s;
}

.result:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 1.5rem;
  background: rgba(var(--color-primary-rgb), 0.1);
  border-bottom: var(--border-thin);
}

.result h3 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--color-primary);
}

.btn-copy {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: var(--color-text-secondary);
  cursor: pointer;
  padding: 0.5rem;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}

.btn-copy:hover {
  background: rgba(var(--color-primary-rgb), 0.15);
  color: var(--color-primary);
  transform: scale(1.1);
}

.result-content {
  padding: 1.8rem;
  color: var(--color-text);
  max-height: 300px;
  overflow-y: auto;
}

.result-content p {
  margin: 0;
  line-height: 1.7;
  font-size: 1.05rem;
}

.summary-section, .transcription-section {
  margin-bottom: 1.5rem;
}

.summary-section h4, .transcription-section h4 {
  color: var(--color-primary);
  margin-bottom: 0.5rem;
  font-size: 1.05rem;
  font-weight: 600;
}

.summary-section {
  border-bottom: var(--border-thin);
  padding-bottom: 1rem;
}

.pulse {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(var(--color-primary-rgb), 0.6);
  }
  70% {
    box-shadow: 0 0 0 15px rgba(var(--color-primary-rgb), 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(var(--color-primary-rgb), 0);
  }
}

@media (max-width: 768px) {
  .transcriber {
    padding: 2.5rem 1.5rem;
    margin: 2rem auto;
  }
  
  .section-title {
    font-size: 1.8rem;
  }
  
  .btn-record, .btn-stop {
    padding: 0.8rem 1.8rem;
    font-size: 1rem;
  }
}
</style> 