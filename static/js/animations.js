/**
 * AllWorks Company (AWC) - Animations JavaScript
 * Contains specialized animations for the website
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initMenuAnimation();
    initCardHoverEffects();
    initCounterAnimation();
    initParallaxEffect();
});

/**
 * Initialize menu animation
 * Adds animations to the navigation menu
 */
function initMenuAnimation() {
    // Get all nav links
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Add entrance animation to each nav link
    navLinks.forEach((link, index) => {
        link.style.opacity = '0';
        link.style.transform = 'translateY(-10px)';
        
        // Delay each link animation
        setTimeout(() => {
            link.style.transition = 'all 0.3s ease';
            link.style.opacity = '1';
            link.style.transform = 'translateY(0)';
        }, 100 + (index * 100));
    });
    
    // Add hover animation to nav link underline
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', () => {
            const underline = link.querySelector('::after');
            if (underline) {
                underline.style.transition = 'width 0.3s ease';
                underline.style.width = '100%';
            }
        });
        
        link.addEventListener('mouseleave', () => {
            const underline = link.querySelector('::after');
            if (underline && !link.classList.contains('active')) {
                underline.style.width = '0';
            }
        });
    });
}

/**
 * Initialize card hover effects
 * Adds dynamic hover effects to cards
 */
function initCardHoverEffects() {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transition = 'all 0.3s ease';
            card.style.transform = 'translateY(-10px)';
            card.style.boxShadow = '0 15px 30px rgba(0, 0, 0, 0.1)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
            card.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
        });
    });
}

/**
 * Initialize counter animation
 * Animates counting up for statistics sections
 */
function initCounterAnimation() {
    const counters = document.querySelectorAll('.counter');
    
    if (counters.length === 0) return;
    
    const isInViewport = function(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) * 0.8 &&
            rect.bottom >= 0
        );
    };
    
    const animateCounter = function(counter) {
        if (counter.classList.contains('animated')) return;
        
        const target = parseInt(counter.getAttribute('data-target'), 10);
        const duration = 2000; // 2 seconds
        const step = target / (duration / 16); // 60fps
        
        let current = 0;
        counter.textContent = '0';
        counter.classList.add('animated');
        
        const timer = setInterval(() => {
            current += step;
            counter.textContent = Math.round(current);
            
            if (current >= target) {
                counter.textContent = target;
                clearInterval(timer);
            }
        }, 16);
    };
    
    const handleScroll = function() {
        counters.forEach(counter => {
            if (isInViewport(counter)) {
                animateCounter(counter);
            }
        });
    };
    
    // Initial check
    handleScroll();
    
    // Check on scroll
    window.addEventListener('scroll', handleScroll);
}

/**
 * Initialize parallax effect
 * Adds parallax scrolling to hero and section backgrounds
 */
function initParallaxEffect() {
    const parallaxElements = document.querySelectorAll('.parallax');
    
    if (parallaxElements.length === 0) return;
    
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        
        parallaxElements.forEach(element => {
            const speed = element.getAttribute('data-speed') || 0.3;
            element.style.transform = `translateY(${scrollY * speed}px)`;
        });
    });
}

/**
 * Animate element when it comes into view
 * @param {HTMLElement} element - Element to animate
 * @param {string} animationClass - CSS class for animation
 */
function animateOnScroll(element, animationClass) {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add(animationClass);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    observer.observe(element);
}

/**
 * Create staggered animation for multiple elements
 * @param {NodeList} elements - Elements to animate in sequence
 * @param {string} animationClass - CSS class for animation
 * @param {number} staggerDelay - Delay between animations in ms
 */
function createStaggeredAnimation(elements, animationClass, staggerDelay = 100) {
    elements.forEach((element, index) => {
        setTimeout(() => {
            element.classList.add(animationClass);
        }, index * staggerDelay);
    });
}

/**
 * Initialize custom cursor effect
 * Creates a custom cursor that follows mouse movement
 */
function initCustomCursor() {
    const cursor = document.createElement('div');
    cursor.classList.add('custom-cursor');
    document.body.appendChild(cursor);
    
    document.addEventListener('mousemove', e => {
        cursor.style.left = `${e.clientX}px`;
        cursor.style.top = `${e.clientY}px`;
    });
    
    // Add hover effect for interactive elements
    const interactiveElements = document.querySelectorAll('a, button, .card, .feature-box');
    
    interactiveElements.forEach(element => {
        element.addEventListener('mouseenter', () => {
            cursor.classList.add('expanded');
        });
        
        element.addEventListener('mouseleave', () => {
            cursor.classList.remove('expanded');
        });
    });
}
