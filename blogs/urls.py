from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('blog/<int:id>', views.blog, name='blog'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_blog', views.add_blog, name='add_blog'),
    path('category/<int:id>', views.categorywise, name='category')
]
