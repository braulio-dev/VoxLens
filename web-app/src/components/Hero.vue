<template>
  <section class="hero-section">
    <div class="hero-container">
      <div class="hero-content">
        <h1 class="hero-title">
          <span class="highlight-wrapper">
            <slot name="title" />
            <span class="title-accent"></span>
          </span>
        </h1>
        <h2 class="hero-subtitle"><slot name="subtitle" /></h2>
        <p class="hero-description"><slot name="description" /></p>
        <div class="hero-cta">
          <a href="#transcriber" class="btn-primary">
            <span class="btn-content">Start Summarizing</span>
            <span class="btn-glow"></span>
          </a>
          <a href="https://github.com/braulio-dev/VoxLens" target="_blank" rel="noopener" class="btn-secondary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 8px;">
              <path d="M12 2C6.477 2 2 6.484 2 12.017C2 16.455 4.865 20.127 8.84 21.43C9.34 21.528 9.522 21.221 9.522 20.958C9.522 20.721 9.513 20.033 9.508 19.241C6.728 19.861 6.139 17.924 6.139 17.924C5.684 16.821 5.027 16.516 5.027 16.516C4.132 15.878 5.097 15.891 5.097 15.891C6.092 15.964 6.626 16.942 6.626 16.942C7.521 18.47 8.969 17.973 9.541 17.717C9.637 17.052 9.909 16.554 10.212 16.258C7.976 15.958 5.636 15.074 5.636 11.156C5.636 10.017 6.039 9.084 6.647 8.357C6.539 8.105 6.183 7.053 6.747 5.594C6.747 5.594 7.587 5.328 9.497 6.771C10.308 6.552 11.175 6.442 12.034 6.438C12.89 6.442 13.757 6.552 14.571 6.771C16.479 5.328 17.317 5.594 17.317 5.594C17.883 7.053 17.527 8.105 17.419 8.357C18.029 9.084 18.429 10.017 18.429 11.156C18.429 15.085 16.084 15.954 13.842 16.249C14.219 16.609 14.559 17.326 14.559 18.419C14.559 19.974 14.546 20.631 14.546 20.958C14.546 21.225 14.726 21.535 15.234 21.429C19.206 20.125 22.067 16.454 22.067 12.017C22.067 6.484 17.591 2 12.067 2H12Z" fill="currentColor"/>
            </svg>
            View on GitHub
          </a>
        </div>
      </div>
      <div class="hero-image">
        <div class="hero-graphic glassy">
          <!-- Sound wave and microphone icons -->
          <div class="icon-container">
            <!-- Microphone Icon -->
            <svg xmlns="http://www.w3.org/2000/svg" class="mic-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18.75a6 6 0 006-6v-1.5m-6 7.5a6 6 0 01-6-6v-1.5m6 7.5v3.75m-3.75 0h7.5M12 15.75a3 3 0 01-3-3V4.5a3 3 0 116 0v8.25a3 3 0 01-3 3z" />
            </svg>
            <!-- Sound Wave Animation -->
            <div class="sound-wave">
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
            </div>
          </div>
          <div class="pulse-ring"></div>
        </div>
      </div>
    </div>
    <div class="hero-pattern"></div>
    <div class="hero-particles"></div>
  </section>
</template>

<style scoped>
.hero-section {
  position: relative;
  min-height: 80vh;
  padding-top: 72px;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.hero-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 5rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 1;
}

.hero-content {
  max-width: 600px;
}

.hero-title {
  font-size: 4.2rem;
  font-weight: 900;
  line-height: 1.2;
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
  position: relative;
  display: inline-block;
}

.highlight-wrapper {
  background: linear-gradient(45deg, var(--color-primary) 0%, var(--color-accent) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  position: relative;
  display: inline-block;
}

.title-accent {
  position: absolute;
  bottom: 4px;
  left: 0;
  width: 30%;
  height: 4px;
  background: var(--gradient-primary);
  border-radius: var(--radius-full);
  opacity: 0.6;
}

.hero-subtitle {
  font-size: 1.6rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: var(--color-text);
  letter-spacing: -0.01em;
}

.hero-description {
  font-size: 1.2rem;
  line-height: 1.7;
  margin-bottom: 2.5rem;
  color: var(--color-text-secondary);
  font-weight: 300;
}

.hero-cta {
  display: flex;
  gap: 1rem;
}

.btn-primary {
  background: var(--gradient-primary);
  color: white;
  border: none;
  padding: 0.9rem 2.2rem;
  font-weight: 700;
  border-radius: var(--radius-md);
  font-size: 1.05rem;
  text-decoration: none;
  transition: all 0.3s var(--transition-bounce);
  box-shadow: var(--shadow-md);
  display: flex;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.btn-content {
  position: relative;
  z-index: 2;
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
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}

.btn-primary:hover .btn-glow {
  opacity: 0.15;
  transform: scale(1);
}

.btn-secondary {
  background: transparent;
  color: var(--color-text);
  border: var(--border-thin);
  padding: 0.9rem 2.2rem;
  font-weight: 700;
  border-radius: var(--radius-md);
  font-size: 1.05rem;
  text-decoration: none;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.05);
}

.btn-secondary:hover {
  background: rgba(var(--color-primary-rgb), 0.15);
  transform: translateY(-4px);
  border-color: var(--color-primary);
  box-shadow: var(--shadow-sm), var(--border-glow);
}

.hero-image {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-graphic {
  position: relative;
  animation: float 6s ease-in-out infinite;
  border-radius: 50%;
  padding: 2rem;
  box-shadow: var(--shadow-glow);
  width: 280px;
  height: 280px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}

.mic-icon {
  width: 80px;
  height: 80px;
  color: var(--color-primary);
  margin-bottom: 1.5rem;
  filter: drop-shadow(0 0 8px rgba(var(--color-primary-rgb), 0.6));
}

.sound-wave {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  height: 80px;
}

.wave-bar {
  width: 10px;
  height: 10px;
  background-color: var(--color-primary);
  border-radius: 6px;
  animation: wave-animation 1.5s ease-in-out infinite;
}

.wave-bar:nth-child(2) {
  animation-delay: 0.1s;
  height: 20px;
}

.wave-bar:nth-child(3) {
  animation-delay: 0.2s;
  height: 30px;
}

.wave-bar:nth-child(4) {
  animation-delay: 0.3s;
  height: 40px;
}

.wave-bar:nth-child(5) {
  animation-delay: 0.4s;
  height: 50px;
}

.wave-bar:nth-child(6) {
  animation-delay: 0.3s;
  height: 40px;
}

.wave-bar:nth-child(7) {
  animation-delay: 0.2s;
  height: 30px;
}

.wave-bar:nth-child(8) {
  animation-delay: 0.1s;
  height: 20px;
}

.wave-bar:nth-child(9) {
  height: 10px;
}

@keyframes wave-animation {
  0%, 100% {
    transform: scaleY(1);
    opacity: 0.7;
  }
  50% {
    transform: scaleY(1.5);
    opacity: 1;
  }
}

.pulse-ring {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 50%;
  border: 2px solid rgba(var(--color-primary-rgb), 0.3);
  animation: pulse-ring 2s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
}

.hero-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='20' cy='20' r='1' fill='%236200ee' fill-opacity='0.1'/%3E%3C/svg%3E");
  opacity: 0.3;
  z-index: 0;
}

.hero-particles {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: radial-gradient(circle at 50% 50%, var(--color-primary) 1px, transparent 1px),
                    radial-gradient(circle at 70% 30%, var(--color-accent) 1px, transparent 1px);
  background-size: 70px 70px, 100px 100px;
  opacity: 0.1;
  animation: particles 20s linear infinite;
  z-index: 0;
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
  100% { transform: translateY(0px); }
}

@keyframes pulse-ring {
  0% {
    transform: scale(0.95);
    opacity: 0.7;
  }
  50% {
    opacity: 0.2;
  }
  100% {
    transform: scale(1.1);
    opacity: 0;
  }
}

@keyframes particles {
  0% { background-position: 0 0, 0 0; }
  100% { background-position: 100px 100px, -100px 100px; }
}

@media (max-width: 1024px) {
  .hero-container {
    flex-direction: column;
    text-align: center;
    gap: 4rem;
  }
  
  .hero-cta {
    justify-content: center;
  }
  
  .hero-title {
    font-size: 3.5rem;
  }
  
  .title-accent {
    left: 35%;
    width: 30%;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.8rem;
  }
  
  .hero-subtitle {
    font-size: 1.3rem;
  }
  
  .hero-container {
    padding: 3rem 1.5rem;
  }
  
  .hero-cta {
    flex-direction: column;
    gap: 1rem;
  }
  
  .title-accent {
    left: 25%;
    width: 50%;
  }
}
</style> 