from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet,basename='products')
router.register('collections',views.CollectionViewSet)
router.register('carts',views.CartViewSet)


products_router = routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews',views.ReviewViewSet,basename='products-reviews')

carts_router = routers.NestedDefaultRouter(router,'carts', lookup='cart')
carts_router.register('items',views.CartItemViewSet,basename='cart-items')

# URLConf
urlpatterns =router.urls + products_router.urls + carts_router.urls

# urlpatterns = [
#     path('products/',views2.product_list),
#     path('product/<int:id>',views2.product_detail),
#     path('collections/',views2.collection_list),
#     path('collection/<int:pk>',views2.collection_detail,name='collection-detail'),
    
# ]`