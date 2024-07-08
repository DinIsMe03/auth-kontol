from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "owner", "nama", "namaPerusahaan", "emailPerusahaan", "nomorTelepon"]
        extra_kwargs = {"owner": {"read_only": True}}