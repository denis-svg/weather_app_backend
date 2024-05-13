from django.urls import path
from . import views

urlpatterns = [
    path("comment", views.CommentListCreate.as_view(), name='comment list'),
    path("comment/<int:pk>", views.CommentDelete.as_view(), name="delete comment")
]