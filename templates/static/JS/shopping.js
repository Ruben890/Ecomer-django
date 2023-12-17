const subtotalPrice = document.querySelectorAll('.subtotal_price');
const totalPrice = document.querySelector('.total_prices');
let total = 0;

subtotalPrice.forEach(element => {
    total += Number(element.textContent);
});

totalPrice.textContent = `Total: ${total.toString()}`;

