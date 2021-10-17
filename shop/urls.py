from django.urls import path
from shop import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('<slug>/', views.CategoryList.as_view(), name='category-items'),
    path('add-cart/<slug>/', views.AddToCad.as_view(), name='cart'),
]
