from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ItemCreateView, ItemDetailView

app_name = 'api'  # Make sure this line is present

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token obtain endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh endpoint
    path('items/', ItemCreateView.as_view(), name='create-item'),  # Create item endpoint
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),  # Retrieve, update, delete item
]
