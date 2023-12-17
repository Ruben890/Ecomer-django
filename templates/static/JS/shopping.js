// Seleccionar elementos
const subtotalPriceElements = document.querySelectorAll('.subtotal_price');
const totalPriceElement = document.querySelector('.total_prices');
const priceElements = document.querySelectorAll('.price');
const quantityInputs = document.querySelectorAll('#quantity');
const quantityButtons = document.querySelectorAll('.add_quantity, .remove_quantity');

// Inicializar variables
let total = 0;

// Calcular el subtotal
priceElements.forEach((priceElement, index) => {
    const price = parseFloat(priceElement.textContent);
    const quantity = parseFloat(quantityInputs[index].value);
    const subtotal = price * quantity;
    subtotalPriceElements[index].textContent = subtotal.toFixed(2);
    total += subtotal;
});

// Mostrar el total
totalPriceElement.textContent = `Total: ${total.toFixed(2)}`;

/// Manejar eventos de clic en botones de cantidad
quantityButtons.forEach(button => {
    button.addEventListener('click', function () {
        const isAddButton = this.classList.contains('add_quantity');
        const isRemoveButton = this.classList.contains('remove_quantity');
        const form = this.closest('form');
        const quantityInput = form.querySelector('#quantity');
        let newQuantity = parseInt(quantityInput.value);

        if (isAddButton) {
            newQuantity += 1;
        } else if (isRemoveButton) {
            newQuantity = Math.max(1, newQuantity - 1);
        }

        const cartItemId = form.querySelector('#shopping_item_id').value;

        updateQuantity(form, newQuantity, cartItemId);
    });
});

// Función para actualizar la cantidad mediante AJAX
function updateQuantity(form, newQuantity, cartItemId) {
    const csrfToken = form.querySelector('[name="csrfmiddlewaretoken"]').value;

    $.ajax({
        type: 'POST',
        url: `/shopping_cart/update_quantity/${cartItemId}/`,
        data: {
            'quantity': newQuantity,
            'csrfmiddlewaretoken': csrfToken,
        },
        dataType: 'json',
        success: function (data) {
            // Actualizar el valor de la cantidad y el subtotal en la interfaz de usuario
            form.querySelector('#quantity').value = data.quantity;
            const price = parseFloat(form.querySelector('.price').textContent);
            const newSubtotal = price * data.quantity;
            form.querySelector('.subtotal_price').textContent = newSubtotal.toFixed(2);

            // Calcular y mostrar el nuevo total
            recalculateTotal();
        }
    });
}

// Función para recalcular el total
function recalculateTotal() {
    let newTotal = 0;

    // Calcular el subtotal y el nuevo total
    subtotalPriceElements.forEach(element => {
        newTotal += parseFloat(element.textContent);
    });

    // Mostrar el nuevo total en el elemento correspondiente
    totalPriceElement.textContent = `Total: ${newTotal.toFixed(2)}`;
}