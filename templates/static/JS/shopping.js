// Seleccionar elementos
const totalPriceElement = document.querySelector('.total_prices');
const subtotalPrice = document.querySelectorAll('.subtotal_price');
const quantityButtons = document.querySelectorAll('.add_quantity, .remove_quantity');

// Inicializar variables
let total = 0;

subtotalPrice.forEach(subtotal =>{
    total += Number(subtotal.textContent)
})

// Mostrar el total
totalPriceElement.textContent = `Total: ${total.toFixed(2)}`;




// Función para recalcular el total
