/**
 * Jan Suvidha Portal — Main JavaScript
 */

// CSRF token helper
function getCSRF() {
    const cookies = document.cookie.split(';');
    for (let c of cookies) {
        c = c.trim();
        if (c.startsWith('csrftoken=')) return c.substring(10);
    }
    return '';
}

// Toast notification
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    const icon = type === 'success' ? 'fa-check-circle' : 'fa-times-circle';
    const color = type === 'success' ? 'var(--accent)' : 'var(--danger)';
    toast.innerHTML = `<i class="fas ${icon}" style="color:${color};font-size:18px;"></i><span>${message}</span>`;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 4000);
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Counter animation
function animateCounter(element, target, duration = 1500) {
    let start = 0;
    const increment = target / (duration / 16);
    function update() {
        start += increment;
        if (start >= target) {
            element.textContent = target;
            return;
        }
        element.textContent = Math.round(start);
        requestAnimationFrame(update);
    }
    update();
}

console.log('🏛️ Jan Suvidha Portal loaded');
