const menus=document.querySelector("nav ul");
const header=document.querySelector("header");
const menuBtn=document.querySelector(".menu-btn");
const closeBtn=document.querySelector(".close-btn");
menuBtn.addEventListener('click', ()=>{
 menus.classList.add("display");
});

closeBtn.addEventListener('click', ()=>{
    menus.classList.remove("display");
   });



window.addEventListener("scroll",() =>{
    if (document.documentElement.scrollTop > 20){
        header.classList.add("sticky");
    }else{
        header.classList.remove("sticky");
    }
    }
);

const countersEL = document.querySelectorAll(".numbers");

countersEL.forEach((counters) => {
    // 
    counters.textContent = 0;
    increamentCounters();

    function increamentCounters(){
        let currentNum = +counters.textContent; // Convertir le contenu textuel en nombre
        const dataCeil = counters.getAttribute("data-ceil"); // Récupérer la valeur cible
        const increament = dataCeil / 25; // Diviser la cible en 25 étapes
        currentNum = Math.ceil(currentNum + increament);
        if (currentNum < dataCeil) {
            counters.textContent = currentNum; // Ajouter l'incrément
            setTimeout(increamentCounters, 70); // Reappeler la fonction après 70ms
        } else {
            counters.textContent = dataCeil; // Assigner la valeur finale
        }
    }
    
});
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 




















