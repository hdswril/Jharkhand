// ===============================
// Utility: Smooth Scroll to Section
// ===============================
function scrollToSection(selector) {
    const target = document.querySelector(selector);
    if (target) {
        target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// ===============================
// Mobile Menu Toggle
// ===============================
const menuBtn = document.getElementById('menu-btn');
if (menuBtn) {
    menuBtn.addEventListener('click', function () {
        const menu = document.getElementById('mobile-menu');
        if (menu) {
            menu.classList.toggle('hidden');
        }
    });
}

// Close mobile menu when clicking on a link
document.querySelectorAll('#mobile-menu a').forEach(link => {
    link.addEventListener('click', function () {
        const menu = document.getElementById('mobile-menu');
        if (menu) {
            menu.classList.add('hidden');
        }
    });
});

// ===============================
// Scroll to Top Button
// ===============================
const scrollButton = document.getElementById('scroll-top');
if (scrollButton) {
    window.addEventListener('scroll', function () {
        if (window.pageYOffset > 300) {
            scrollButton.classList.add('visible');
        } else {
            scrollButton.classList.remove('visible');
        }
    });

    scrollButton.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// ===============================
// Smooth Scrolling for Navigation Links
// ===============================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===============================
// Form Submission Handlers
// ===============================
function handleFormSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const name = formData.get('name');
    const email = formData.get('email');
    const phone = formData.get('phone');
    const message = formData.get('message');

    alert(`Thank you ${name}! Your message has been received. We'll contact you at ${email} soon.`);
    event.target.reset();
}

function handleNewsletterSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('newsletter_email');

    alert(`Thank you for subscribing with ${email}!`);
    event.target.reset();
}

// ===============================
// Intersection Observer for Animations
// ===============================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', function () {
    // Observe elements for animation
    document.querySelectorAll('.destination-card, .gallery-item').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Handle video error
    const video = document.querySelector('.hero-video');
    if (video) {
        video.addEventListener('error', function () {
            console.log('Video failed to load, using fallback background');
            this.style.display = 'none';
        });
    }
});

// ===============================
// Image Error Handling
// ===============================
document.querySelectorAll('img').forEach(img => {
    img.addEventListener('error', function () {
        this.style.display = 'none';
        console.log('Image failed to load:', this.src);
    });
});
