/**
 * Extrae los atributos src de las imágenes y maneja el evento de clic en el contenedor de imágenes.
 * Luego, llama a la función createImage con los atributos recuperados.
 * @returns {string[]} Un array con los atributos src de todas las imágenes.
 */
const extractSrcAttributes = () => {
    const srcArray = [];
    const productImagesList = document.querySelectorAll('.product_images_list');
    const productImagesContainer = document.querySelector('.product_images');

    // Agrega un evento de clic al contenedor de imágenes
    productImagesContainer.addEventListener('click', (event) => {
        // Verifica si el elemento clickeado es una imagen dentro del contenedor
        if (event.target.classList.contains('product_images_list')) {
            console.log('hola')
            // Obtiene los atributos src y alt
            const clickedSrc = event.target.getAttribute('src');
            const clickedAlt = event.target.getAttribute('alt');

            // Llama a la función createImage con los atributos recuperados
            createImage(clickedSrc, clickedAlt);
        }
    });

    // Extrae los atributos src y popula el array srcArray
    productImagesList.forEach((image) => {
        const src = image.getAttribute('src');
        srcArray.push(src);
    });

    // Retorna el array srcArray
    return srcArray;
};

/**
 * Crea una imagen y actualiza el contenido del contenedor .product_image.
 * @param {string} src - La fuente (src) de la imagen.
 * @param {string} alt - El texto alternativo (alt) de la imagen.
 */
const createImage = (src, alt) => {
    const producImageContainer = document.querySelector('.product_image');
    producImageContainer.innerHTML = `
        <div class="images rounded-xl">
            <img 
            src="${src}" 
            alt="${alt}"
            width="500px"
            height="400px"
            loading="lazy"
            class="w-full h-full  object-cover rounded-xl"
            />
    </div>
  
    `;
};

// Llama a la función extractSrcAttributes y guarda el resultado en srcArray
const srcArray = extractSrcAttributes();

// Muestra la primera imagen por defecto si hay al menos una imagen
if (srcArray.length > 0) {
    const firstImageSrc = srcArray[0];
    const firstImageAlt = document.querySelector('.product_images_list').getAttribute('alt');
    createImage(firstImageSrc, firstImageAlt);
}

async function addToCart() {
    try {
        const productUuid = document.getElementById("productUuid").value;
        const cantidad = document.getElementById("cantidad").value;
        const base_url = window.location.origin;
        const url = `${base_url}/shopping_cart/`;

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken'), // Asegúrate de tener una función getCookie para obtener el token CSRF
            },
            body: `product_id=${productUuid}&cantidad=${cantidad}`, // Ajusta según tu estructura de datos
        });

        if (response.ok) {
            const cartDetails = await response.json();
            handleSuccessfulCartAddition(cartDetails);
        } else {
            if (response.status == 500) {
                location.href = '/login'
            }
            handleFailedCartAddition();
        }
    } catch (error) {
        handleNetworkError(error);
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Función para manejar la respuesta exitosa del servidor
function handleSuccessfulCartAddition(cartDetails) {
    // Aquí puedes manejar la respuesta del servidor (cartDetails)
    console.log(cartDetails);

    // Recargar la página después de agregar al carrito exitosamente
    location.reload();
}

// Función para manejar el fallo al agregar al carrito
function handleFailedCartAddition() {
    console.error('Error al agregar al carrito');
}

// Función para manejar errores de red
function handleNetworkError(error) {
    console.error('Error de red:', error);
}

// Obtener el botón y agregar el evento click
const addToCartBtn = document.getElementById("addToCartBtn");
addToCartBtn.addEventListener('click', addToCart);
