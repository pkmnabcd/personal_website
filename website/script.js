document.addEventListener('DOMContentLoaded', () => {

    // --- Mobile Navigation Menu ---
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');

    burger.addEventListener('click', () => {
        // Toggle Nav Bar
        nav.classList.toggle('nav-active');

        // Burger Animation
        burger.classList.toggle('toggle');
    });

    // --- Fade-in Reveal on Scroll ---
    const revealElements = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        for (let i = 0; i < revealElements.length; i++) {
            let windowHeight = window.innerHeight;
            let elementTop = revealElements[i].getBoundingClientRect().top;
            let elementVisible = 150; // trigger point

            if (elementTop < windowHeight - elementVisible) {
                revealElements[i].classList.add('active');
            }
        }
    };

    // Run once on load to show elements already in view
    revealOnScroll();

    // Attach listener to scroll event
    window.addEventListener('scroll', revealOnScroll);
});
