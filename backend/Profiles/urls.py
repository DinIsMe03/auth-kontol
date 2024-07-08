from django.urls import path
from . import views

urlpatterns = [
    path("profile/create/", views.ProfileCreateView.as_view(), name="profile-list"),
    path("profile/delete/<int:pk>", views.ProfileDelete.as_view(), name="delete-profile"),
] 