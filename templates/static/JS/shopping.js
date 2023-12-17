const totalPriceElement = document.querySelector('.total_prices');
const subtotalPrice = document.querySelectorAll('.subtotal_price');
const quantityButtons = document.querySelectorAll('.increase-quantity, .decrease-quantity');
const formQuantity = document.querySelector('#shopping_item_quantity');

// Inicializar variables
let total = 0;

subtotalPrice.forEach(subtotal => {
    total += Number(subtotal.textContent);
});

// Mostrar el total
totalPriceElement.textContent = `Total: ${total.toFixed(2)}`;

// Función para recalcular el total
function recalculateTotal() {
    total = 0;
    subtotalPrice.forEach(subtotal => {
        total += Number(subtotal.textContent);
    });
    totalPriceElement.textContent = `Total: ${total.toFixed(2)}`;
}

// Función para enviar la cantidad actualizada al servidor mediante AJAX
function updateQuantityOnServer(itemId, newQuantity) {
    // Log the request body before sending the fetch request
    console.log('Request Body:', JSON.stringify({ quantity: newQuantity }));

    fetch(`/shopping_cart/update_quantity/${itemId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': formQuantity.querySelector('input[name="csrfmiddlewaretoken"]').value,
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
            location.reload()
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Event listeners para los botones de cantidad
quantityButtons.forEach(button => {
    button.addEventListener('click', () => {
        const inputElement = button.parentNode.querySelector('input[name="quantity"]');
        const itemId = formQuantity.querySelector('input[name="id_product"]').value;

        let quantity = parseInt(inputElement.value, 10);

        if (button.classList.contains('increase-quantity')) {
            quantity += 1;
        } else if (button.classList.contains('decrease-quantity') && quantity > 1) {
            quantity -= 1;
        }

        inputElement.value = quantity;
        recalculateTotal();

        // Enviar la cantidad actualizada al servidor
        updateQuantityOnServer(itemId, quantity);
    });
});
