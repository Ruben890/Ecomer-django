const inputResetForm = (inputElement, btnReset) => {
    inputElement.addEventListener('input', () => {
        const inputValue = inputElement.value.trim();
        btnReset.classList.toggle('hidden', inputValue === '');
    });
};

const resetForm = (formElement, inputElement, btnReset) => {
    formElement.addEventListener('reset', () => {
        btnReset.classList.add('hidden');
        inputElement.classList.add('hidden');
        formElement.classList.remove('bg-white', 'rounded-3xl', 'text-black');
    });
};

const updateFormViews = (inputElement, formElement) => {
    const inputValue = inputElement.value.trim();
    if (inputValue !== '') {
        inputElement.classList.remove('hidden');
        formElement.classList.add('bg-white', 'rounded-3xl', 'text-black');
    }
};

const formSearchList = [...document.getElementsByClassName('form_search')];

formSearchList.forEach((formSearch) => {
    const inputElement = formSearch.querySelector('.input_search');
    const btnReset = formSearch.querySelector('.reset_search');

    inputResetForm(inputElement, btnReset);
    resetForm(formSearch, inputElement, btnReset);
    updateFormViews(inputElement, formSearch);

    formSearch.addEventListener('submit', (e) => {
        const inputValue = inputElement.value.trim();
        if (inputValue !== '') {
            e.submit();
        } else {
            e.preventDefault();
            inputElement.classList.remove('hidden');
            formSearch.classList.add('bg-white', 'rounded-3xl', 'text-black');
        }
    });
});

const menuMobie = document.querySelector('.menu_mobie');
const closeMobileMenuButton = document.querySelector('.close_mobile_menu_button');
const menuDesplegableHidden = document.querySelector('.hidden_menu');

menuMobie.addEventListener('click', toggleMenu);
closeMobileMenuButton.addEventListener('click', toggleMenu);

function toggleMenu() {
    menuDesplegableHidden.classList.toggle('menu');

    // Obtener el estado actual del menú
    const isMenuOpen = menuDesplegableHidden.classList.contains('menu');

    // Deshabilitar o habilitar el scroll del body según el estado del menú
    document.body.style.overflow = isMenuOpen ? 'hidden' : 'auto';

    // Deshabilitar o habilitar el scroll de la ventana cuando se detecte un cambio en el tamaño
    if (isMenuOpen) {
        window.addEventListener('resize', disableScroll);
    } else {
        window.removeEventListener('resize', disableScroll);
    }
}

function disableScroll() {
    // Deshabilitar el scroll del body si el menú está abierto durante un cambio en el tamaño de la ventana
    document.body.style.overflow = 'hidden';

    // Después de un breve tiempo, volver a habilitar el scroll
    setTimeout(() => {
        document.body.style.overflow = 'auto';
    }, 200);
}
