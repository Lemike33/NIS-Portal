from django.urls import path
# Импортируем созданное нами представление
from . import views

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('news/', views.ShowNewsView.as_view(), name='news-main'),
   path('articles/', views.ShowNewsView.as_view(), name='articles-main'),
   path('articles/<int:pk>', views.NewsDetailView.as_view(), name='articles-detail'),
   path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
   path('search', views.SearchNewsView.as_view(), name='news-search'),
   path('news/create', views.CreatePostsView.as_view(), name='news-create'),
   path('articles/create', views.CreatePostsView.as_view(), name='articles-create'),
   path('news/<int:pk>/update/', views.UpdatePostView.as_view(), name='news-update'),
   path('news/<int:pk>/delete/', views.DeletePost.as_view(), name='news-delete'),
   path('articles/<int:pk>/update/', views.UpdatePostView.as_view(), name='articles-update'),
   path('articles/<int:pk>/delete/', views.DeletePost.as_view(), name='articles-delete'),
]
