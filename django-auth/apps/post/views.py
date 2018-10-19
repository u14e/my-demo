from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == 'create':
            return [permission() for permission in self.permission_classes]
        else:
            return []

    def list(self, request, *args, **kwargs):
        print(request.user)
        return super(PostViewSet, self).list(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)