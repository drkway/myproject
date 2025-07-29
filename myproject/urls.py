from django.urls import path
from Crudapp import views,views_api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/new/', views.product_create, name='product_create'),
    path('product/<str:pk>/edit/', views.product_update, name='product_update'),
    path('product/<str:pk>/delete/', views.product_delete, name='product_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


    path('api/products/', views_api.ProductListCreate.as_view(), name='product_list_create'),
    path('api/products/<str:pk>/', views_api.ProductDetail.as_view(), name='product_detail'),

    # JWT endpoints:
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
