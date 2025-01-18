const swiper = new Swiper('.swiper', {
    slidesPerView: 1, 
    effect: "creative", 
    creativeEffect: {
        prev: {
            translate: [0, 0, -400], 
        },
        next: {
            translate: ["100%", 0, 0], 
        },
    },
    loop: true, 
    direction: "horizontal", 
    autoplay: {
        delay: 5000, 
    },
    speed: 400, 
    spaceBetween: 100, 
});





//const swiper2 = new Swiper('.swiper2', {
    // slidesPerView: 3, // Correction : "slidesPerView" au lieu de "slideperView"
    // spaceBetween: 35,
    // slidesPerGroup: 1,
    //  loop: true,
    // fade: true,
    // centerSlide: true,
    // loopfillGroupwithBlank: true,
    // 
    // 
    // autoplay: {
        // delay: 5000, // Délai entre chaque diapositive (en millisecondes)
    // },
    // speed: 400, // Vitesse de transition entre les diapositives (en millisecondes)
    // spaceBetween: 100, // Espacement entre les diapositives
//});

const swiper2 = new Swiper('.swiper2', {
    slidesPerView: 3, // Nombre de diapositives visibles
    spaceBetween: 35, // Espacement entre les diapositives
    slidesPerGroup: 1, // Nombre de diapositives déplacées par interaction
    loop: true, // Activer la boucle
    fade: true, // Utiliser l'effet de fondu (optionnel, choisissez selon votre design)
    centerSlide: true,
    grabCursor:true, // Centrer les diapositives
    loopFillGroupWithBlank: true, // Ajouter des diapositives vides pour compléter les groupes si nécessaire

    autoplay: {
        delay: 5000, // Délai entre les diapositives (en millisecondes)
    },
    speed: 400,
    breakpoints:{
        320: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        968: {
            slidesPerView: 3,
        }
    }, // Vit,esse de transition (en millisecondes)
});




const swiper3 = new Swiper('.swiper3', {
    slidesPerView: 2, // Nombre de diapositives visibles
    spaceBetween: 35, // Espacement entre les diapositives
    slidesPerGroup: 1, // Nombre de diapositives déplacées par interaction
    loop: true, // Activer la boucle
    fade: true, // Utiliser l'effet de fondu (optionnel, choisissez selon votre design)
    centerSlide: true,
    grabCursor:true, // Centrer les diapositives
    loopFillGroupWithBlank: true, // Ajouter des diapositives vides pour compléter les groupes si 

    autoplay: {
        delay: 5000, // Délai entre les diapositives (en millisecondes)
    },
    speed: 400,
    breakpoints:{
        320: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        968: {
            slidesPerView: 2,
        }
    }, // Vit,esse de transition (en millisecondes)
});





const swiper4 = new Swiper('.swiper4', {
    slidesPerView: 1, // Nombre de diapositives visibles
    spaceBetween:95, // Espacement entre les diapositives
    slidesPerGroup: 1, // Nombre de diapositives déplacées par interaction
    loop: true, // Activer la boucle
    fade: true, // Utiliser l'effet de fondu (optionnel, choisissez selon votre design
    centerSlide: true,
    grabCursor:true, // Centrer les diapositives
    loopFillGroupWithBlank: true, // Ajouter des diapositives vides pour compléter les

    autoplay: {
        delay: 5000, // Délai entre les diapositives (en millisecondes)
    },
    speed: 400,
    breakpoints:{
        320: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 1,
        },
        968: {
            slidesPerView: 1,
        }
    }, // Vit,esse de transition (en millisecondes)
});
