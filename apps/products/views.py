from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product
from django.db.models import Q

class HomePage(View):
    template_name = 'index.html'
    category_images = [
            'https://images.unsplash.com/photo-1527800792452-506aacb2101f?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://img.freepik.com/foto-gratis/complejidad-silo-controla-orden-industria-comunicacion-global-generado-ia_24640-81722.jpg?w=826&t=st=1700764433~exp=1700765033~hmac=a94f117cca9514f0e6ac23c5a9483c99982517ccff4116de5ff15839c51c05eb',
            'https://img.freepik.com/fotos-premium/vista-superior-equipo-juego_160097-825.jpg?w=740',
            'https://img.freepik.com/foto-gratis/hombre-usando-almacenamiento-externo-usado_23-2149388490.jpg?w=740&t=st=1700765044~exp=1700765644~hmac=c371e58dde7a15bd238437275bbe0e3492c5155b73271d2595863782e059f6b1',
            'https://images.unsplash.com/photo-1522273400909-fd1a8f77637e?q=80&w=1412&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://media.istockphoto.com/id/1334436084/es/foto/vista-de-arriba-hacia-abajo-de-coloridos-accesorios-de-juego-iluminados-sobre-la-mesa.jpg?s=1024x1024&w=is&k=20&c=UHuq_wtA7spu63m7CcVkWBkYtenPD5lh6mAByunQFPU='
        ]

    def get(self, request):
        selected_currency = request.GET.get('money', 'US')
        categories = Category.objects.all()
        products = self.get_queryset(request)

        category_data = zip(categories, self.category_images)
        context = {'selected_currency': selected_currency, 'category_data': category_data, 'products_search': products}
        return render(request, self.template_name, context)

    def get_queryset(self, request):
        search_query = request.GET.get('search', '')
        queryset = Product.objects.all()

        if search_query:
            queryset = self.filter_products(queryset, search_query)

        return queryset

    def filter_products(self, queryset, search_query):
        return queryset.filter(
            Q(name__icontains=search_query) | 
            Q(category__category_name__icontains=search_query) | 
            Q(model__icontains=search_query)
        )

class SearchResults(HomePage):
    template_name = 'page/search_results.html'

    def get_queryset(self, request):
        search_query = request.GET.get('search', '')
        queryset = super().get_queryset(request)

        if search_query:
            queryset = self.filter_products(queryset, search_query)

        return queryset

class detailtProduct(View):
    template_name = 'page/detailtProduct.html'

    def get(self, request, uuid=None):
        if uuid:
            product = get_object_or_404(Product, uuid=uuid)
            return render(request, self.template_name, {'product': product})
