/**
 * AgriGenius 360° - Main JavaScript
 * 
 * Controls animations, interactive elements, and general site functionality
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize animated elements
    initAnimations();
    
    // Set active navigation link
    setActiveNavLink();
    
    // Add form validation
    initFormValidation();
    
    // Add smooth scrolling
    initSmoothScrolling();
});

/**
 * Initialize various animations across the site
 */
function initAnimations() {
    // Random cloud movement adjustments
    const clouds = document.querySelectorAll('.cloud-1, .cloud-2, .cloud-3');
    clouds.forEach(cloud => {
        const randomDelay = Math.random() * 10;
        const randomDuration = 25 + Math.random() * 15;
        cloud.style.animationDelay = `${randomDelay}s`;
        cloud.style.animationDuration = `${randomDuration}s`;
    });
    
    // Animate cards on scroll
    const cards = document.querySelectorAll('.card');
    
    // Basic intersection observer for card animations
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate__animated', 'animate__fadeInUp');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });
        
        cards.forEach(card => {
            observer.observe(card);
        });
    } else {
        // Fallback for browsers that don't support IntersectionObserver
        cards.forEach(card => {
            card.classList.add('animate__animated', 'animate__fadeInUp');
        });
    }
    
    // Create weather effects
    createWeatherEffects();
}

/**
 * Creates random weather effects in the background
 */
function createWeatherEffects() {
    // Chance of rain animation
    if (Math.random() > 0.7) {
        const rain = document.querySelector('.rain');
        if (rain) {
            setTimeout(() => {
                rain.style.animationPlayState = 'running';
            }, Math.random() * 10000);
        }
    }
    
    // Random sun movement
    const sun = document.querySelector('.sun');
    if (sun) {
        const randomX = 5 + Math.random() * 15;
        const randomY = 5 + Math.random() * 15;
        sun.style.top = `${randomY}%`;
        sun.style.right = `${randomX}%`;
    }
}

/**
 * Sets the active navigation link based on current page
 */
function setActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        }
    });
}

/**
 * Initializes form validation for all forms
 */
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, select, textarea');
        
        inputs.forEach(input => {
            // Add validation classes on input change
            input.addEventListener('blur', function() {
                if (input.checkValidity()) {
                    input.classList.add('is-valid');
                    input.classList.remove('is-invalid');
                } else if (input.value !== '') {
                    input.classList.add('is-invalid');
                    input.classList.remove('is-valid');
                }
            });
        });
    });
}

/**
 * Initializes smooth scrolling for anchor links
 */
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Creates a toast notification
 * @param {string} message - Message to display
 * @param {string} type - Type of toast (success, error, info, warning)
 */
function showToast(message, type = 'info') {
    // Create toast container if it doesn't exist
    let toastContainer = document.querySelector('.toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        document.body.appendChild(toastContainer);
    }
    
    // Create toast element
    const toastId = 'toast-' + Date.now();
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type === 'error' ? 'danger' : type}`;
    toast.id = toastId;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    // Toast content
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    
    // Add toast to container
    toastContainer.appendChild(toast);
    
    // Initialize and show toast
    const bsToast = new bootstrap.Toast(toast, {
        autohide: true,
        delay: 5000
    });
    bsToast.show();
    
    // Remove toast from DOM after it's hidden
    toast.addEventListener('hidden.bs.toast', function() {
        this.remove();
    });
}
