from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from shop.models import Book, Category


class HomeTemplateView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['books'] = Book.objects.filter(status=True)
        data['newbooks'] = Book.objects.order_by("create_at")
        return data
