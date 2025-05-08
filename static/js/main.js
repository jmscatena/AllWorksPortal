/**
 * AllWorks Company (AWC) - Main JavaScript
 * Contains functionality for the website including navigation, animations, filtering
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initNavbarScroll();
    initScrollAnimations();
    initProjectFilters();
    initFormValidation();
    initSmoothScroll();
});

/**
 * Initialize navbar scroll behavior
 * Adds a class to navbar when scrolling down
 */
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    
    if (!navbar) return;
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
            navbar.classList.add('bg-white');
        } else {
            navbar.classList.remove('navbar-scrolled');
            // Only remove bg-white if not mobile menu expanded
            if (!document.querySelector('.navbar-collapse').classList.contains('show')) {
                navbar.classList.remove('bg-white');
            }
        }
    });
    
    // Ensure navbar has correct class on mobile toggle
    const navbarToggler = document.querySelector('.navbar-toggler');
    if (navbarToggler) {
        navbarToggler.addEventListener('click', function() {
            if (document.querySelector('.navbar-collapse').classList.contains('show')) {
                navbar.classList.remove('bg-white');
            } else {
                navbar.classList.add('bg-white');
            }
        });
    }
}

/**
 * Initialize scroll animations
 * Adds animation to elements when they enter the viewport
 */
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.fade-in');
    
    if (animatedElements.length === 0) return;
    
    // Check if element is in viewport
    const isInViewport = function(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) * 0.8 &&
            rect.bottom >= 0
        );
    };
    
    // Activate elements in viewport
    const handleScroll = function() {
        animatedElements.forEach(function(element) {
            if (isInViewport(element) && !element.classList.contains('active')) {
                element.classList.add('active');
            }
        });
    };
    
    // Initial check on load
    handleScroll();
    
    // Check on scroll
    window.addEventListener('scroll', handleScroll);
}

/**
 * Initialize project filters
 * Handles filtering of project cards
 */
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-item');
    
    if (filterButtons.length === 0 || projectCards.length === 0) return;
    
    filterButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            const filter = this.getAttribute('data-filter');
            
            // Show or hide project cards based on filter
            projectCards.forEach(function(card) {
                if (filter === 'all' || card.classList.contains(filter)) {
                    card.style.display = 'block';
                    // Add animation effect
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });
}

/**
 * Initialize form validation
 * Adds custom validation to contact form
 */
function initFormValidation() {
    const contactForm = document.querySelector('#contactForm');
    
    if (!contactForm) return;
    
    contactForm.addEventListener('submit', function(event) {
        if (!contactForm.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        
        contactForm.classList.add('was-validated');
    });
}

/**
 * Initialize smooth scroll for anchor links
 */
function initSmoothScroll() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]:not([href="#"])');
    
    if (anchorLinks.length === 0) return;
    
    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}
