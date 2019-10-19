from django.urls import path

from companies.api.views import (
    api_get_stocks_list,
    api_update_stock,
    api_delete_stock,
    api_create_stock,

    )

app_name = "companies"

urlpatterns = [
    path('stocks/', api_get_stocks_list, name='list'),
    path('stocks/<ticker>/update', api_update_stock, name='update'),
    path('stocks/<ticker>/delete', api_delete_stock, name='delete'),
    path('stocks/create', api_create_stock, name='create'),
]
