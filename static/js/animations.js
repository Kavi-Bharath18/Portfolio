// Reveal on scroll
function revealOnScroll() {
  let reveals = document.querySelectorAll('.reveal');

  for (let i = 0; i < reveals.length; i++) {
    let windowHeight = window.innerHeight;
    let elementTop = reveals[i].getBoundingClientRect().top;
    let revealPoint = 100; // adjust for earlier/later reveal

    if (elementTop < windowHeight - revealPoint) {
      reveals[i].classList.add('active');
    } else {
      reveals[i].classList.remove('active'); // remove if scrolling up
    }
  }
}

// window.addEventListener('scroll', revealOnScroll);
