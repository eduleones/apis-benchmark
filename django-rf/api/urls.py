from django.urls import path
from .views import ProductList

app_name = 'api'
urlpatterns = [
    path('', ProductList.as_view(), name='product-list'), 

]