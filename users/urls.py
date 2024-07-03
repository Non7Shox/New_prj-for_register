from django.urls import path
from .views import RegisterView, VerifyView, LoginView, UpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', VerifyView.as_view(), name='verify'),
    path('login/', LoginView.as_view(), name='login'),
    path('update/', UpdateView.as_view(), name='update'),
]
