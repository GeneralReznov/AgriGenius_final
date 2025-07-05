/**
 * Homepage particle system and enhanced animations
 */
document.addEventListener('DOMContentLoaded', function() {
    initializeParticleSystem();
    initializeHomepageAnimations();
});

function initializeParticleSystem() {
    const particleContainer = document.querySelector('.particles-container') || document.querySelector('.global-particles');
    if (!particleContainer) return;

    // Configure sky particles with faster speeds
    const skyParticles = document.querySelectorAll('.sky-particle');
    skyParticles.forEach((particle, index) => {
        const randomX = Math.random() * 100;
        const randomDelay = Math.random() * 12;
        const randomDuration = 8 + Math.random() * 8; // Much faster
        const randomY = Math.random() * 60; // Upper 60% of screen
        
        particle.style.left = randomX + '%';
        particle.style.top = randomY + '%';
        particle.style.animationDelay = randomDelay + 's';
        particle.style.animationDuration = randomDuration + 's';
    });

    // Configure ground particles with faster speeds
    const groundParticles = document.querySelectorAll('.ground-particle');
    groundParticles.forEach((particle, index) => {
        const randomX = Math.random() * 100;
        const randomDelay = Math.random() * 15;
        const randomDuration = 10 + Math.random() * 10; // Much faster
        const randomY = 70 + Math.random() * 30; // Lower 30% of screen
        
        particle.style.left = randomX + '%';
        particle.style.top = randomY + '%';
        particle.style.animationDelay = randomDelay + 's';
        particle.style.animationDuration = randomDuration + 's';
    });

    // Configure floating particles with fastest speeds
    const floatingParticles = document.querySelectorAll('.floating-particle');
    floatingParticles.forEach((particle, index) => {
        const randomX = Math.random() * 100;
        const randomDelay = Math.random() * 18;
        const randomDuration = 8 + Math.random() * 8; // Faster movement
        const randomY = Math.random() * 100; // Anywhere on screen
        
        particle.style.left = randomX + '%';
        particle.style.top = randomY + '%';
        particle.style.animationDelay = randomDelay + 's';
        particle.style.animationDuration = randomDuration + 's';
        
        // Add random movement properties
        const randomRotation = Math.random() * 360;
        const randomScale = 0.5 + Math.random() * 1.5;
        particle.style.transform = `rotate(${randomRotation}deg) scale(${randomScale})`;
        
        // Add random directional movement
        const randomDirection = Math.random() * 360;
        particle.style.setProperty('--random-direction', `${randomDirection}deg`);
    });
}

function initializeHomepageAnimations() {
    // Initialize logo glow animation
    const logoWrapper = document.querySelector('.logo-wrapper');
    if (logoWrapper) {
        logoWrapper.addEventListener('mouseenter', function() {
            const logoGlow = this.querySelector('.logo-glow');
            if (logoGlow) {
                logoGlow.style.opacity = '0.8';
                logoGlow.style.transform = 'translate(-50%, -50%) scale(1.2)';
            }
        });
        
        logoWrapper.addEventListener('mouseleave', function() {
            const logoGlow = this.querySelector('.logo-glow');
            if (logoGlow) {
                logoGlow.style.opacity = '';
                logoGlow.style.transform = '';
            }
        });
    }
    
    // Add scroll-based animations for feature cards
    if ('IntersectionObserver' in window) {
        const featureCards = document.querySelectorAll('.feature-card');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, index * 100);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        
        featureCards.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px)';
            card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(card);
        });
    }
    
    // Add dynamic particle color changes
    setInterval(changeParticleColors, 8000);
}

function changeParticleColors() {
    const particles = document.querySelectorAll('.particle');
    const body = document.body;
    
    const isNight = body.classList.contains('nighttime');
    
    if (isNight) {
        const nightColors = [
            '#4169E1', '#2E8B57', '#483D8B', '#8B4513', '#556B2F', 
            '#4682B4', '#2F4F4F', '#191970', '#800080', '#008B8B',
            '#6495ED', '#708090', '#778899', '#B0C4DE', '#9370DB'
        ];
        
        particles.forEach(particle => {
            const randomColor = nightColors[Math.floor(Math.random() * nightColors.length)];
            particle.style.background = randomColor;
            particle.style.transition = 'background-color 2s ease';
        });
    } else {
        const dayColors = [
            '#FFD700', '#32CD32', '#87CEEB', '#FF6347', '#9370DB', 
            '#FFB6C1', '#20B2AA', '#F0E68C', '#DDA0DD', '#98FB98',
            '#FFA500', '#FF69B4', '#00CED1', '#ADFF2F', '#FF1493'
        ];
        
        particles.forEach(particle => {
            const randomColor = dayColors[Math.floor(Math.random() * dayColors.length)];
            particle.style.background = randomColor;
            particle.style.transition = 'background-color 2s ease';
        });
    }
}

// Add random wind effect to particles
function createWindEffect() {
    const particles = document.querySelectorAll('.particle');
    
    particles.forEach(particle => {
        const windStrength = Math.random() * 50 - 25; // -25 to +25px
        const currentTransform = particle.style.transform || '';
        
        particle.style.transform = currentTransform + ` translateX(${windStrength}px)`;
        
        setTimeout(() => {
            particle.style.transform = currentTransform;
        }, 2000);
    });
}

// Trigger wind effect occasionally
setInterval(createWindEffect, 15000 + Math.random() * 10000);

// Add parallax effect to background layers
function addParallaxEffect() {
    const skyLayer = document.querySelector('.sky-layer');
    const groundLayer = document.querySelector('.ground-layer');
    
    if (!skyLayer || !groundLayer) return;
    
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const rate = scrolled * -0.5;
        
        skyLayer.style.transform = `translateY(${rate}px)`;
        groundLayer.style.transform = `translateY(${rate * 0.3}px)`;
    });
}

// Initialize parallax effect
addParallaxEffect();