from django.urls import path

from cars.apps import CarsConfig
from cars.views import (CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, BlogListView,
                        BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView)

app_name = CarsConfig.name

urlpatterns = [
    path('', CarListView.as_view(), name='product_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='product_detail'),
    # path('contacts/', contacts, name='contacts'),
    # path('blogs/', blogs, name='blogs'),
    path('cars/create', CarCreateView.as_view(), name='product_create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='product_update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='product_delete'),
    path('cars/blogs', BlogListView.as_view(), name='blog_list'),
    path('cars/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('cars/create', BlogCreateView.as_view(), name='blog_create'),
    path('cars/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('cars/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
