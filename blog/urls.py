from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<slug:article>/', views.ArticleDetailView.as_view(), name='post_detail'),
]