from django.urls import path

from . import views
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('', views.ProductsListView.as_view(), name='products_changelist'),
    path('add/', views.ProductsCreateView.as_view(), name='products_add'),
    path('<int:pk>/', views.ProductsUpdateView.as_view(), name='products_change'),
]
