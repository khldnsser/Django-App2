from django.urls import path
from .views import home, success, update_book, delete_book

urlpatterns = [
    path('success/', success, name='success'),
    path('', home, name='home'),
    path('update/<int:id>/', update_book, name='update_book'),
    path('delete/<int:id>/', delete_book, name='delete_book'),
]