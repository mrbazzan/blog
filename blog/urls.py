
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('new/', views.BlogPostView.as_view(), name='post'),
    path('<int:pk>/edit', views.BlogUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.BlogDeleteView.as_view(), name='delete'),
    path('accounts/register', views.register, name='register'),
    path('<int:pk>/comment', views.BlogCommentView.as_view(), name='comment')
]
