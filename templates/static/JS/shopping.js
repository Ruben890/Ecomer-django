// Selección de elementos del DOM
const totalPriceElement = document.querySelector('.total_prices');
const subtotalPriceElements = document.querySelectorAll('.subtotal_price');
const quantityButtons = document.querySelectorAll('.increase-quantity, .decrease-quantity');
const formQuantityElements = document.querySelectorAll('#shopping_item_quantity');

// Inicializar la variable total
let total = calculateTotal();

// Mostrar el total inicial
updateTotalDisplay();

// Función para calcular el total
function calculateTotal() {
    return Array.from(subtotalPriceElements)
        .reduce((accumulator, subtotal) => accumulator + Number(subtotal.textContent), 0);
}

// Función para actualizar el display del total
function updateTotalDisplay() {
    totalPriceElement.textContent = `Total: ${total.toFixed(2)}`;
}

// Función para enviar la cantidad actualizada al servidor mediante AJAX
function updateQuantityOnServer(itemId, newQuantity) {
    const csrfToken = getCsrfToken();

    // Log the request body before sending the fetch request
    console.log('Request Body:', JSON.stringify({ quantity: newQuantity }));

    fetch(`/shopping_cart/update_quantity/${itemId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ quantity: newQuantity }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error updating quantity on server');
            }
            // Handle the server response as needed
            return response.json();
        })
        .then(data => {
            location.reload();
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Función para obtener el token CSRF
function getCsrfToken() {
    let csrfToken = '';
    formQuantityElements.forEach(formQuantity => {
        csrfToken = formQuantity.querySelector('input[name="csrfmiddlewaretoken"]').value;
        // Tu lógica adicional aquí, si es necesario.
    });
    return csrfToken;
}

function getItemId(button) {
    const formQuantity = button.closest('form');
    return formQuantity.querySelector('input[name="data-item-id"]').value;
}
// Event listeners para los botones de cantidad
quantityButtons.forEach(button => {
    button.addEventListener('click', () => {
        const inputElement = button.parentNode.querySelector('input[name="quantity"]');
        const itemId = getItemId(button); // Pasar el botón como argumento
        let quantity = parseInt(inputElement.value, 10);

        if (button.classList.contains('increase-quantity')) {
            quantity += 1;
        } else if (button.classList.contains('decrease-quantity') && quantity > 1) {
            quantity -= 1;
        }
        console.log(itemId)
        inputElement.value = quantity;
        total = calculateTotal();
        updateTotalDisplay();

        // Enviar la cantidad actualizada al servidor
        updateQuantityOnServer(itemId, quantity);
    });
});
