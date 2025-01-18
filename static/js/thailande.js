document.addEventListener("DOMContentLoaded", () => {
    // Carousel logic
    const slides = document.querySelectorAll(".slide");
    const controls = document.querySelectorAll(".control");
    let currentSlide = 0;

    const updateSlides = (index) => {
        slides.forEach(slide => slide.classList.remove("active"));
        controls.forEach(ctrl => ctrl.classList.remove("active"));

        slides[index].classList.add("active");
        controls[index].classList.add("active");
    };

    controls.forEach((control, index) => {
        control.addEventListener("click", () => {
            currentSlide = index;
            updateSlides(currentSlide);
        });
    });

    /* Optional: Auto-slide functionality
    let autoSlideInterval = setInterval(() => {
        currentSlide = (currentSlide + 1) % slides.length;
        updateSlides(currentSlide);
    }, 3000);

    document.querySelector("#carousel").addEventListener("mouseover", () => {
        clearInterval(autoSlideInterval);
    });

    document.querySelector("#carousel").addEventListener("mouseout", () => {
        autoSlideInterval = setInterval(() => {
            currentSlide = (currentSlide + 1) % slides.length;
            updateSlides(currentSlide);
        }, 3000);
    }); */

    // Scroll-based animation logic
    const detailsSection = document.querySelector(".details");

    window.addEventListener("scroll", () => {
        const sectionPosition = detailsSection.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;

        if (sectionPosition < screenPosition) {
            detailsSection.style.opacity = "1";
            detailsSection.style.transform = "translateY(0)";
        }
    });
});

// Toggle response logic
function toggleReponse(id) {
    const reponse = document.getElementById(id);
    if (reponse.style.display === "none" || reponse.style.display === "") {
        reponse.style.display = "block";
    } else {
        reponse.style.display = "none";
    }
}
const menus = document.querySelector("nav ul");
const menuBtn = document.querySelector(".menu-btn");
const closeBtn = document.querySelector(".close-btn");

menuBtn.addEventListener("click", () => {
  menus.classList.add("display");
});

closeBtn.addEventListener("click", () => {
  menus.classList.remove("display");
});
