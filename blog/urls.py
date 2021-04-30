
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.BlogListView.as_view(), name='home'),
    # /blog/1/
    path('<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    # /blog/new/
    path('new/', views.BlogPostView.as_view(), name='post'),
    path('<int:pk>/edit', views.BlogUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.BlogDeleteView.as_view(), name='delete'),
]
