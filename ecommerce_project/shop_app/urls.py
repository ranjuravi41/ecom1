from django.urls import path
from shop_app import views

app_name = 'shop_app'

urlpatterns = [
    path('', views.allProductsCat, name='allProductsCat'),
    path('<slug:c_slug>/', views.allProductsCat, name='allProductsCat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatedetail'),
]
