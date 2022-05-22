from rest_framework import generics
from rest_framework import permissions

from mail.models import MailAccount
from mail import serializers


class BaseMailView(generics.GenericAPIView):
    queryset = MailAccount.objects.all()
    serializer_class = serializers.MailSerializer


class MailListCreateView(generics.ListCreateAPIView, BaseMailView):
    permission_classes = (permissions.IsAuthenticated,)
