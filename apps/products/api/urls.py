from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name = 'indicator'),
    path('category_product/', CategoryProductListAPIView.as_view(), name = 'category_product'),
    #path('product/list/', ProductListAPIView.as_view(), name = 'product_list'),
    path('product/', ProductListCreateAPIView.as_view(), name = 'product_create'),
    path('product/retrieve-update-destroy/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name = 'retrieve-update-destroy'),
    #path('product/retrieve/<int:pk>', ProductRetrieveAPIView.as_view(), name = 'product_retrieve'),
    #path('product/destroy/<int:pk>', ProductDestroyAPIView.as_view(), name = 'product_destroy'),
    #path('product/update/<int:pk>', ProductUpdateAPIView.as_view(), name = 'product_update'),

]
