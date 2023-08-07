from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_orders/<int:user_id>/<int:days>', views.user_orders, name='User_orders'),
]