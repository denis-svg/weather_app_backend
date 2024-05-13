from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, BasePermission
from .models import Comment
from rest_framework.pagination import PageNumberPagination

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Comment.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.error)

class CommentDelete(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Allow admin to delete any comment
        if IsAdmin().has_permission(self.request, self):
            return Comment.objects.all()
        else:
            # Restrict regular users to delete their own comments
            return Comment.objects.filter(author=self.request.user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
