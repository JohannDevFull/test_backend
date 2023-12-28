from django.urls import path
from products import views


urlpatterns = [
    
    # path( '' , views.ProductList.as_view() ),
    # path( '<int:id>/' , views.ProductDetail.as_view() ),

    path( '' , views.ProductListAPIView.as_view() , name='product-list' ),
    path( '<int:id>/' , views.ProductDetailAPIView.as_view() , name='product-detail' ),
    path( '<int:id>/detalle' , views.ProductAPIView.detail, name="detail" ),

]

