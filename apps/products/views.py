"""
products/views.py

This module defines Django views for handling product-related functionality, including displaying product lists,
search results, and individual product details.

Classes:
- BaseProductListView: A base class for views that display lists of products with pagination.
- HomePage: View for rendering the home page, inheriting from BaseProductListView.
- SearchResults: View for rendering search results, inheriting from BaseProductListView.
- DetailProductView: View for rendering details of a specific product.

Functions:
- None

"""

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product
from django.db.models import Q

class BaseProductListView(View):
    """
    Base class for views that display lists of products with pagination.

    Attributes:
    - template_name (str): The template file to be used for rendering the view.
    - paginate_by (int): Number of products to be displayed per page in pagination.
    - category_images (list): List of URLs for category images.

    Methods:
    - get_queryset(self, request): Returns the queryset of products based on search parameters.
    - filter_products(self, queryset, search_query): Filters the given queryset based on the search query.
    - get_context_data(self, request, **kwargs): Returns the context data for rendering the template.

    """

    template_name = None
    paginate_by = 10
    category_images = [
        # ... URLs for category images
    ]

    def get_queryset(self, request):
        """
        Returns the queryset of products based on search parameters.

        Args:
        - request (HttpRequest): The request object containing user input.

        Returns:
        - queryset (QuerySet): The queryset of products.

        """
        search_query = request.GET.get('search', '')
        queryset = Product.objects.all().order_by('name')  # Ordena por el campo 'name', ajusta según tus necesidades

        if search_query:
            queryset = self.filter_products(queryset, search_query)

        return queryset

    def filter_products(self, queryset, search_query):
        """
        Filters the given queryset based on the search query.

        Args:
        - queryset (QuerySet): The initial queryset of products.
        - search_query (str): The search query entered by the user.

        Returns:
        - filtered_queryset (QuerySet): The filtered queryset of products.

        """
        return queryset.filter(
            Q(name__icontains=search_query) |
            Q(category__category_name__icontains=search_query) |
            Q(model__icontains=search_query)
        )

    def get_context_data(self, request, **kwargs):
        """
        Returns the context data for rendering the template.

        Args:
        - request (HttpRequest): The request object containing user input.
        - **kwargs: Additional keyword arguments.

        Returns:
        - context (dict): The context data for rendering the template.

        """
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
    """
    View for rendering the home page, inheriting from BaseProductListView.

    Attributes:
    - template_name (str): The template file to be used for rendering the view.

    Methods:
    - get(self, request): Handles GET requests and renders the home page.

    """

    template_name = 'index.html'

    def get(self, request):
        """
        Handles GET requests and renders the home page.

        Args:
        - request (HttpRequest): The request object.

        Returns:
        - response (HttpResponse): The rendered home page.

        """
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

class SearchResults(BaseProductListView):
    """
    View for rendering search results, inheriting from BaseProductListView.

    Attributes:
    - template_name (str): The template file to be used for rendering the view.

    Methods:
    - get(self, request): Handles GET requests and renders search results.

    """

    template_name = 'page/search_results.html'

    def get(self, request):
        """
        Handles GET requests and renders search results.

        Args:
        - request (HttpRequest): The request object.

        Returns:
        - response (HttpResponse): The rendered search results page.

        """
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

class DetailProductView(View):
    """
    View for rendering details of a specific product.

    Attributes:
    - template_name (str): The template file to be used for rendering the view.

    Methods:
    - get(self, request, uuid=None): Handles GET requests and renders the product details page.

    """

    template_name = 'page/detailtProduct.html'

    def get(self, request, uuid=None):
        """
        Handles GET requests and renders the product details page.

        Args:
        - request (HttpRequest): The request object.
        - uuid (str): The unique identifier of the product.

        Returns:
        - response (HttpResponse): The rendered product details page.

        """
        if uuid:
            product = get_object_or_404(Product, uuid=uuid)
            return render(request, self.template_name, {'product': product})
