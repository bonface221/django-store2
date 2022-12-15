from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('collections/',views.CollectionList.as_view()),
    path('collection/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
]

# urlpatterns = [
#     path('products/',views2.product_list),
#     path('product/<int:id>',views2.product_detail),
#     path('collections/',views2.collection_list),
#     path('collection/<int:pk>',views2.collection_detail,name='collection-detail'),
    
# ]`