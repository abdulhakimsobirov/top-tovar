from django.urls import path
from .views import  ProductListView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
                    CategoryListView, CategoryView, RequestCreateView, RequestView

urlpatterns = [
    path("product/", ProductListView.as_view()),
    path("product/create/", ProductCreateView.as_view()),
    path('product/<int:pk>/', ProductView.as_view()),
    path('product/<int:pk>/update/', ProductUpdateView.as_view()),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view()),

    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view()),

    path('request/create/', RequestCreateView.as_view()),
    path('request/<int:pk>/', RequestView.as_view()),

]