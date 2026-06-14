from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('sayfa/<slug:slug>/', views.page_detail, name='page_detail'),
]