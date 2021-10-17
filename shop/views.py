from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from shop.models import Book


class HomeTemplateView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['books'] = Book.objects.filter(status=True)
        data['newbooks'] = Book.objects.filter(
            status=True).order_by("create_at")
        return data


class CategoryList(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        slug = kwargs.get('slug')
        data = super().get_context_data(**kwargs)
        data['books'] = Book.objects.filter(
            status=True).filter(category__slug=slug)
        data['newbooks'] = Book.objects.filter(status=True).filter(
            category__slug=slug).order_by("create_at")
        return data


class AddToCad(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        if request.session.get('cart', True) is True:
            request.session['cart'] = {}
        cart = request.session.get('cart')
        if cart.get(slug):
            cart[slug] = cart[slug]+1
        else:
            cart[slug] = 1
        request.session['cart'] = cart
        return redirect('home')
