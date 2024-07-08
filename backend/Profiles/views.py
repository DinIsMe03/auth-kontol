from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Profile
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class ProfileListCreate(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        else:
            print(serializer.errors)

class ProfileDelete(generics.DestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(owner=user)

class ProfileCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            # Create or get a default user
            default_user, created = User.objects.get_or_create(username='default_user')
            serializer.save(owner=default_user)