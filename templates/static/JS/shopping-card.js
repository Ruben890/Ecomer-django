const fetchData = async (url, options = {}) => {
    try {
        const response = await fetch(url, options);

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Error:', error.message);
    }
};

const createProductCard = (product) => {
    const card = document.createElement('div');
    card.classList.add('product-card');

    const totalCost = calculateTotalCost(product); // Calculate total cost based on quantity

    card.innerHTML = `
        <div class="relative">
            <div>
                <a href="/product/detailtProduc/${product.product_uuid}" class="flex my-4 p-2 cursor-pointer w-full">
                    <p style="margin-right: 5px; font-size: 18px" class="relative top-4">${product.cantidad} - </p>
                    <div>
                        <img src="${product.product_images[0]}" alt="${product.product_name}" class="product-image rounded">
                    </div>
                    <div class="product-details">
                        <h3 class="product-name">${product.product_name}</h3>
                        <p class="product-price">Prince:${product.product_price}</p>
                        <p class="total-cost">Total: ${totalCost}</p> <!-- Display total cost -->
                    </div>
                </a>
                <hr>
                <a href="/shopping_cart/delete/${product.product_cart_id}" 
                    class="deleteProductBtn absolute p-3" 
                    style="top: 1rem;right:0px;
                ">
                    <i class="fa-solid fa-circle-xmark"></i>
                </a>
                
            </div>
        </div>
    `;

    return card;
};

const calculateTotalCost = (product) => {
    // Parse quantity as integer (use default value 1 if undefined)
    const quantity = parseInt(product.cantidad) || 1;
    // Parse product price as float (use default value 0 if undefined)
    const price = parseFloat(product.product_price) || 0;

    // Calculate total cost
    const totalCost = quantity * price;
    return totalCost.toFixed(2); // Format to two decimal places
};

const populateCartContainer = (cartContainer, cartItems) => {
    let totalProducts = 0; // Initialize totalProducts variable

    cartItems.forEach(product => {
        const card = createProductCard(product);
        cartContainer.appendChild(card);

        // Update totalProducts based on quantity
        totalProducts += parseInt(product.cantidad) || 1;
    });

    // Update the display of totalProducts
    updateTotalProducts(totalProducts);
};

const updateTotalProducts = (totalProducts) => {
    const totalProductsElements = document.querySelectorAll('.total-products');
    totalProductsElements.forEach(productLength => {
        if (totalProducts > 0) {
            productLength.textContent = `${totalProducts}`;
            productLength.classList.remove('hidden');
        } else {
            productLength.classList.add('hidden');
        }
    });
};

const shoppingCart = async () => {
    try {
        const base_url = window.location.origin;
        const url = `${base_url}/shopping_cart/`;

        const data = await fetchData(url);

        if (data && data.cart_items.length > 0) {
            const cartContainers = document.querySelectorAll('.shopping-card-contents');

            cartContainers.forEach(cartContainer => {
                populateCartContainer(cartContainer, data.cart_items);
            });
        } else {
            console.log('El carrito está vacío');
        }
    } catch (error) {
        throw new Error(error);
    }
};

const btn_shopping_card = document.querySelectorAll('.btn_shopping_card');

btn_shopping_card.forEach(btnShoppingCard => {
    btnShoppingCard.addEventListener('click', (e) => {
        const cartContainers = document.querySelectorAll('.shopping-card-contents');

        // Itera sobre cada contenedor y aplica la clase 'shopping-card-contents' o la quita
        cartContainers.forEach(cartContainer => {
            cartContainer.classList.toggle('hidden');
        });
    });
});

// Llamar a la función
shoppingCart();
