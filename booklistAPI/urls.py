from django.urls import path
from . import views
""" from rest_framework.routers import SimpleRouter, DefaultRouter

router = SimpleRouter(trailing_slash=False)
router = DefaultRouter(trailing_slash=False)
router.register('booksrouter', views.books, basename='booksrouter') """

urlpatterns =[
    path('books/', views.books),
    path('orders', views.Orders.listOrders),
    path('books/<int:pk>', views.BookView.as_view()),
    path('books_viewsets', views.BookView_viewsets.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    )),
    path("books_viewsets/<int:pk>", views.BookView_viewsets.as_view(
        {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
        }
    )),
   """  router.urls """
]