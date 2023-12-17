from django.http import JsonResponse, Http404
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from apps.products.models import Product
from .models import ShoppingCartItem
from uuid import UUID
from django.contrib.auth.mixins import LoginRequiredMixin

class ShoppingCart(View, LoginRequiredMixin):
    """
    View for handling shopping cart operations.

    Methods:
    - get: Gets shopping cart details for the current user.
    - post: Adds or updates an item in the shopping cart based on the POST request.
    - get_cart_details: Utility method to get shopping cart details.

    Inherited Attributes:
    - LoginRequiredMixin: Ensures the user is authenticated to access these views.
    """

    def get(self, request):
        """
        Handles GET requests to obtain shopping cart details.

        Returns:
        JsonResponse: Shopping cart details in JSON format.
        """
        # Get the ID of the current user
        user_id = request.user.id
        # Filter cart items for the current user
        shopping_cart_items = ShoppingCartItem.objects.filter(user_id=user_id)
        # Get cart details and return a JSON response
        cart_details = self.get_cart_details(shopping_cart_items, user_id)
        return JsonResponse(cart_details, safe=False)

    def post(self, request):
        """
        Handles POST requests to add or update items in the shopping cart.

        Returns:
        JsonResponse: Updated shopping cart details in JSON format.
        """
        # Get the ID of the current user
        user_id = request.user.id
        # Get product_id and quantity from the POST request
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided

        # Check if product_id is provided in the request
        if not product_id:
            return JsonResponse({'error': 'The product_id parameter is required'}, status=400)

        try:
            # Check if the product exists
            product_uuid = UUID(product_id)
            product = get_object_or_404(Product, uuid=product_uuid)

            # Create or update the cart item with the provided quantity
            cart_item, created = ShoppingCartItem.objects.get_or_create(user_id=user_id, product=product)
            
            # Increment the quantity if the item already exists
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity

            cart_item.save()

            # Get the updated cart items
            shopping_cart_items = ShoppingCartItem.objects.filter(user_id=user_id)
            # Get cart details and return a JSON response
            cart_details = self.get_cart_details(shopping_cart_items, user_id)
            return JsonResponse(cart_details, safe=False)

        except Exception as e:
            # Catch general exceptions and return a JSON error response
            return JsonResponse({'error': str(e)}, status=400)

    def get_cart_details(self, cart_items, user_id):
        """
        Utility method to get shopping cart details.

        Args:
        cart_items (QuerySet): Cart items for the current user.
        user_id (int): ID of the current user.

        Returns:
        dict: Shopping cart details in dictionary format.
        """
        # Build the data structure for cart details
        cart_details = []
        for item in cart_items:
            product = item.product
            images_urls = [image.image.url for image in product.images.all()]
            cart_details.append({
                'product_cart_id': item.id,
                'product_uuid': product.uuid,
                'product_name': product.name,
                'product_images': images_urls,
                'product_price': str(product.price),
                'quantity': item.quantity,
            })

        response_data = {
            'user_id': user_id,
            'cart_items': cart_details,
        }
        return response_data

class DeleteProductCard(View):
    """
    View for handling the removal of a product from the shopping cart.

    Methods:
    - get: Removes the product from the cart and redirects the user to the homepage.
    """

    def get(self, request, id=None):
        """
        Handles GET requests to remove a product from the shopping cart.

        Args:
        id (int): ID of the cart item to be removed.

        Returns:
        JsonResponse or HttpResponseRedirect: JSON error response or redirection to the homepage.
        """
        try:
            # Check if a valid ID is provided
            if not id:
                return JsonResponse({'error': 'No valid ID provided'}, status=400)

            # Get the ID of the current user
            user_id = request.user.id
            # Get the cart item by ID and user
            cart_item = get_object_or_404(ShoppingCartItem, id=id, user_id=user_id)
            # Remove the cart item
            cart_item.delete()
            # Redirect to the homepage after removing the product from the cart
            return redirect("/")
        except Exception as e:
            # Log errors using the logging system instead of printing
            print(f'Error removing product from cart: {e}')
            return JsonResponse({'error': 'Internal server error'}, status=500)

class ShoppingViews(LoginRequiredMixin, View):
    template_name = 'shopping/shopping.html'

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        shopping_cart = ShoppingCartItem.objects.filter(user_id=user_id)
        return render(request, self.template_name, {'shopping_items': shopping_cart})

class UpdateQuantity(View):
    def post(self, request, id=None):
        try:
            if not id:
                return JsonResponse({'error': 'No valid ID provided'}, status=400)

            user_id = request.user.id
            cart_item = get_object_or_404(ShoppingCartItem, id=id, user_id=user_id)
            new_quantity = int(request.POST.get('quantity', 1))

            cart_item.quantity = max(1, new_quantity)
            cart_item.save()

            # Calcular el subtotal
            subtotal = cart_item.product.price * cart_item.quantity

            response_data = {
                'quantity': cart_item.quantity,
                'subtotal': str(subtotal),
            }

            return JsonResponse(response_data, safe=False)

        except Exception as e:
            print(f'Error updating quantity in cart: {e}')
            return JsonResponse({'error': 'Internal server error'}, status=500)