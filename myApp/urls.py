from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='home'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.UpdateNewsVeiw.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
    path('news/add', views.CreateNewsVeiw.as_view(), name='news-add'),
    path('contacts', views.contacts, name='contacts')
]