from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product
from django.db.models import Q

class BaseProductListView(View):
    template_name = None
    paginate_by = 10
    category_images = [
        # ... your images here
    ]

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

    def get_context_data(self, request, **kwargs):
        selected_currency = request.GET.get('money', 'US')
        categories = Category.objects.all()
        products = self.get_queryset(request)

        page = request.GET.get('page', 1)
        paginator = Paginator(products, self.paginate_by)

        try:
            paginated_products = paginator.page(page)
        except PageNotAnInteger:
            paginated_products = paginator.page(1)
        except EmptyPage:
            paginated_products = paginator.page(paginator.num_pages)

        category_data = zip(categories, self.category_images)
        context = {'selected_currency': selected_currency, 'category_data': category_data, 'products_search': paginated_products}
        return context

class HomePage(BaseProductListView):
    template_name = 'index.html'

    def get(self, request):
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

class SearchResults(BaseProductListView):
    template_name = 'page/search_results.html'

    def get(self, request):
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

class DetailProductView(View):
    template_name = 'page/detailtProduct.html'

    def get(self, request, uuid=None):
        if uuid:
            product = get_object_or_404(Product, uuid=uuid)
            return render(request, self.template_name, {'product': product})
