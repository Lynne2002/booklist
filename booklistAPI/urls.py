from django.urls import path
from . import views
urlpatterns =[
    path('books/', views.books),
    path('orders', views.Orders.listOrders),
    path('books/<int:pk>', views.BookView.as_view()),
]