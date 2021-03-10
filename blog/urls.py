from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index , name='index'),  
    path('search/', views.search, name='search'),
    path('posts/<int:id>/', views.show , name='show'),  
    path('posts/addPost', views.AddPost , name='add_Post'),  
    path('posts/edit/<int:id>/', views.updatePost , name='updatePost'),  
    path('posts/comment/<int:id>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('posts/delete/<int:id>/', views.deletePost , name='deletePost'),  
    path('comment/<int:id>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:id>/remove/', views.comment_remove, name='comment_remove'),
]
