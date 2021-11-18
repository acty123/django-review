from django.urls import path

from products.views import (
    product_create_view,
    product_delete_view,
    product_detail_view,
    product_list_view,
    product_update_view,
    )

app_name = 'products'
urlpatterns = [    
    path('', product_list_view, name='products-list'),
    path('create/', product_create_view, name='products-create'),
    path('<int:id>/', product_detail_view, name="products-detail"),
    path('<int:id>/update/', product_update_view, name="products-update"),
    path('<int:id>/delete/', product_delete_view, name="products-delete"),
]
