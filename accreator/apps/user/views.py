from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions

from user import permissions as user_permissions
from user import serializers


class BaseUserView(generics.GenericAPIView):
    queryset = get_user_model().objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer


class UserListCreateView(generics.ListCreateAPIView, BaseUserView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.UserCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.request.method == 'GET':
            return permissions.IsAdminUser(),
        return user_permissions.IsNotAuthenticated(),


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView, BaseUserView):
    permission_classes = (permissions.IsAuthenticated, user_permissions.IsCurrentUser)
