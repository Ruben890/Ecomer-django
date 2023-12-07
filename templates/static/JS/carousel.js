const carouselContainer = document.getElementById('carousel-container');
const btnNext = document.getElementById('btn-next');
const btnBack = document.getElementById('btn-back');

let currentIndex = 0;

btnNext.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % carouselContainer.children.length;
    updateCarousel();
});

btnBack.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + carouselContainer.children.length) % carouselContainer.children.length;
    updateCarousel();
});

function updateCarousel() {
    Array.from(carouselContainer.children).forEach((child, index) => {
        const isVisible = index === currentIndex;
        child.classList.toggle('hidden', !isVisible);
    });

    // Oculta el botón "Atrás" si estamos en la primera imagen
    btnBack.classList.toggle('hidden', currentIndex === 0);
    
    // Puedes añadir más lógica aquí según tus necesidades
}


