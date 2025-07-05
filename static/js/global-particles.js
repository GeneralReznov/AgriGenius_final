/**
 * Global particle system for all pages
 */
document.addEventListener('DOMContentLoaded', function() {
    initializeGlobalParticles();
    initializeGlobalAnimations();
});

function initializeGlobalParticles() {
    const globalParticles = document.querySelector('.global-particles');
    if (!globalParticles) return;

    // Configure sky particles with faster speeds
    const skyParticles = document.querySelectorAll('.global-particles .sky-particle');
    skyParticles.forEach((particle, index) => {
        const randomX = Math.random() * 100;
        const randomDelay = Math.random() * 12;
        const randomDuration = 6 + Math.random() * 6;
        const randomY = Math.random() * 60;
        
        particle.style.left = randomX + '%';
        particle.style.top = randomY + '%';
        particle.style.animationDelay = randomDelay + 's';
        particle.style.animationDuration = randomDuration + 's';
        
        // Add random movement properties
        const randomRotation = Math.random() * 360;
        const randomScale = 0.6 + Math.random() * 1.4;
        particle.style.transform = `rotate(${randomRotation}deg) scale(${randomScale})`;
        
        // Add random directional movement
        const randomDirection = Math.random() * 360;
        particle.style.setProperty('--random-direction', `${randomDirection}deg`);
    });

    // Configure ground particles with faster speeds
    const groundParticles = document.querySelectorAll('.global-particles .ground-particle');
    groundParticles.forEach((particle, index) => {
        const randomX = Math.random() * 100;
        const randomDelay = Math.random() * 15;
        const randomDuration = 8 + Math.random() * 8;
        const randomY = 70 + Math.random() * 30;
        
        particle.style.left = randomX + '%';
        particle.style.top = randomY + '%';
        particle.style.animationDelay = randomDelay + 's';
        particle.style.animationDuration = randomDuration + 's';
        
        // Add random movement properties
        const randomRotation = Math.random() * 360;
        const randomScale = 0.7 + Math.random() * 1.3;
        particle.style.transform = `rotate(${randomRotation}deg) scale(${randomScale})`;
        
        // Add random directional movement
        const randomDirection = Math.random() * 360;
        particle.style.setProperty('--random-direction', `${randomDirection}deg`);
    });

    // Configure floating particles with fastest speeds and random movement
    const floatingParticles = document.querySelectorAll('.global-particles .floating-particle');
    floatingParticles.forEach((particle, index) => {
        const randomX = Math.random() * 100;
        const randomDelay = Math.random() * 18;
        const randomDuration = 8 + Math.random() * 8; // Faster movement
        const randomY = Math.random() * 100;
        
        particle.style.left = randomX + '%';
        particle.style.top = randomY + '%';
        particle.style.animationDelay = randomDelay + 's';
        particle.style.animationDuration = randomDuration + 's';
        
        // Add random transform for each particle
        const randomRotation = Math.random() * 360;
        const randomScale = 0.5 + Math.random() * 1.5;
        particle.style.transform = `rotate(${randomRotation}deg) scale(${randomScale})`;
        
        // Add random directional movement
        const randomDirection = Math.random() * 360;
        particle.style.setProperty('--random-direction', `${randomDirection}deg`);
        
        // Randomly assign different animation types for floating particles
        const animations = ['randomFloat1', 'randomFloat2', 'randomFloat3', 'floatingParticleMove'];
        const randomAnimation = animations[Math.floor(Math.random() * animations.length)];
        particle.style.animationName = randomAnimation;
    });
}

function initializeGlobalAnimations() {
    // Add scroll-based animations for cards
    if ('IntersectionObserver' in window) {
        const cards = document.querySelectorAll('.card');
        
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
        
        cards.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px)';
            card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(card);
        });
    }
    
    // Add dynamic particle color changes
    setInterval(changeGlobalParticleColors, 8000);
}

function changeGlobalParticleColors() {
    const particles = document.querySelectorAll('.global-particles .particle');
    const colors = ['#FFD700', '#32CD32', '#87CEEB', '#FF6347', '#9370DB', '#FFB6C1', '#20B2AA'];
    
    particles.forEach(particle => {
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        particle.style.backgroundColor = randomColor;
        particle.style.boxShadow = `0 0 12px ${randomColor}, 0 0 24px ${randomColor}`;
    });
}

// Create wind effect for global particles
function createGlobalWindEffect() {
    const particles = document.querySelectorAll('.global-particles .particle');
    
    particles.forEach(particle => {
        const windStrength = Math.random() * 50 - 25;
        const currentTransform = particle.style.transform || '';
        
        particle.style.transform = currentTransform + ` translateX(${windStrength}px)`;
        
        setTimeout(() => {
            particle.style.transform = currentTransform;
        }, 2000);
    });
}

// Trigger wind effect occasionally
setInterval(createGlobalWindEffect, 15000 + Math.random() * 10000);