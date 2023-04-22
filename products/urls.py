from django.urls import path

from .views import CategoryView, CategoryDetailView, ProductListView, ProductCreateView, ProductDetailView

app_name = "product"

urlpatterns = [
    path("category/", CategoryView.as_view(), name="category_view"),
    path("category/<slug:slug>/", CategoryDetailView.as_view(),
         name="category_detail_view"),

    path("product/", ProductListView.as_view(), name="product_view"),
    path("product/<slug:slug>/create/", ProductCreateView.as_view(),
         name="product_create_view"),
    path("product/<slug:slug>/", ProductDetailView.as_view(),
         name="product_detail_view"),
]
