from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bills/', views.bills_index, name='index'),
    path('bills/<int:bill_id>/', views.bills_detail, name='detail'),
]