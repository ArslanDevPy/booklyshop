from django.urls import path
from shop import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
]
