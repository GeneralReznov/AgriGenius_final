/**
 * Weather animations controller for day/night cycle
 */
document.addEventListener('DOMContentLoaded', function() {
    initWeatherAnimations();
});

function initWeatherAnimations() {
    const sunAnimation = document.querySelector('.sun-animation');
    const nightAnimation = document.querySelector('.night-animation');
    
    if (!sunAnimation || !nightAnimation) return;
    
    // Set initial state based on current time
    updateWeatherAnimations();
    
    // Update every minute
    setInterval(updateWeatherAnimations, 60000);
}

function updateWeatherAnimations() {
    const now = new Date();
    const hour = now.getHours();
    
    const sunAnimation = document.querySelector('.sun-animation');
    const nightAnimation = document.querySelector('.night-animation');
    const body = document.body;
    
    if (!sunAnimation || !nightAnimation) return;
    
    // Day time: 6 AM to 6 PM (18:00)
    if (hour >= 6 && hour < 18) {
        // Show sun animation
        sunAnimation.style.opacity = '1';
        nightAnimation.style.opacity = '0';
        
        // Add daytime styling to hero section and body
        const heroSection = document.querySelector('.hero-section');
        if (heroSection) {
            heroSection.classList.add('daytime');
            heroSection.classList.remove('nighttime');
        }
        
        // Apply daytime body styling
        body.classList.add('daytime');
        body.classList.remove('nighttime');
        
        // Update particle colors for daytime
        updateParticleColors('day');
        
    } else {
        // Show night animation
        sunAnimation.style.opacity = '0';
        nightAnimation.style.opacity = '1';
        
        // Add nighttime styling to hero section and body
        const heroSection = document.querySelector('.hero-section');
        if (heroSection) {
            heroSection.classList.add('nighttime');
            heroSection.classList.remove('daytime');
        }
        
        // Apply nighttime body styling
        body.classList.add('nighttime');
        body.classList.remove('daytime');
        
        // Update particle colors for nighttime
        updateParticleColors('night');
    }
}

function updateParticleColors(timeOfDay) {
    const particles = document.querySelectorAll('.particle');
    
    if (timeOfDay === 'day') {
        // Bright, vibrant colors for daytime
        const dayColors = ['#FFD700', '#32CD32', '#87CEEB', '#FF6347', '#9370DB', '#FFB6C1', '#20B2AA', '#F0E68C', '#DDA0DD', '#98FB98'];
        particles.forEach((particle, index) => {
            particle.style.background = dayColors[index % dayColors.length];
        });
    } else {
        // Cooler, darker colors for nighttime
        const nightColors = ['#4169E1', '#2E8B57', '#483D8B', '#8B4513', '#556B2F', '#4682B4', '#2F4F4F', '#191970', '#800080', '#008B8B'];
        particles.forEach((particle, index) => {
            particle.style.background = nightColors[index % nightColors.length];
        });
    }
}

// Optional: Add manual toggle for demonstration
function toggleDayNight() {
    const sunAnimation = document.querySelector('.sun-animation');
    const nightAnimation = document.querySelector('.night-animation');
    
    if (!sunAnimation || !nightAnimation) return;
    
    const isDay = sunAnimation.style.opacity === '1';
    
    if (isDay) {
        sunAnimation.style.opacity = '0';
        nightAnimation.style.opacity = '1';
    } else {
        sunAnimation.style.opacity = '1';
        nightAnimation.style.opacity = '0';
    }
}