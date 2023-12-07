from django.http import JsonResponse, Http404
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from apps.products.models import Product
from .models import CarritoItem
from uuid import UUID
from django.contrib.auth.mixins import LoginRequiredMixin

class ShoppingCart(View, LoginRequiredMixin):
    def get(self, request):

        
        id_user = request.user.id
        shopping_cart_items = CarritoItem.objects.filter(user_id=id_user)
        cart_details = self.get_cart_details(shopping_cart_items, id_user)
        return JsonResponse(cart_details, safe=False)

    def post(self, request):
        id_user = request.user.id
        product_id = request.POST.get('product_id')
        cantidad = int(request.POST.get('cantidad', 1))  # Default to 1 if cantidad is not provided

        # Verificar si el producto_id se proporciona en la solicitud
        if not product_id:
            return JsonResponse({'error': 'Se requiere el parámetro product_id'}, status=400)

        try:
            # Verificar si el producto existe
            product_uuid = UUID(product_id)
            product = get_object_or_404(Product, uuid=product_uuid)

            # Crear o actualizar el elemento del carrito con la cantidad proporcionada
            cart_item, created = CarritoItem.objects.get_or_create(user_id=id_user, product=product)
            
            # Incrementar la cantidad si el elemento ya existe
            if not created:
                cart_item.cantidad += cantidad
            else:
                cart_item.cantidad = cantidad

            cart_item.save()

            shopping_cart_items = CarritoItem.objects.filter(user_id=id_user)
            cart_details = self.get_cart_details(shopping_cart_items, id_user)
            return JsonResponse(cart_details, safe=False)

        except Http404:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)

        except ValueError:
            return JsonResponse({'error': 'El valor de product_id no es un UUID válido'}, status=400)

    def get_cart_details(self, cart_items, user_id):
        cart_details = []
        for item in cart_items:
            product = item.product

            # Obtener las URL de las imágenes como una lista
            images_urls = [image.image.url for image in product.images.all()]  # Ajusta 'image' según tu modelo de imágenes

            cart_details.append({
                'product_cart_id': item.id,
                'product_uuid': product.uuid,
                'product_name': product.name,
                'product_images': images_urls,
                'product_price': str(product.price),  # Convertir DecimalField a string
                'cantidad': item.cantidad,  # Agregar la cantidad al detalle del carrito
            })

        response_data = {
            'user_id': user_id,
            'cart_items': cart_details,
        }
        return response_data

class DeleteProductCard(View):
    def get(self, request, id=None):
        try:
            if not id:
                return JsonResponse({'error': 'No se proporcionó un ID válido'}, status=400)

            user_id = request.user.id
            cart_item = get_object_or_404(CarritoItem, id=id, user_id=user_id)
            cart_item.delete()
            return redirect("/")
        except Exception as e:
            print(f'Error al borrar el producto del carrito: {e}')
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)



