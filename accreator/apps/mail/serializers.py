from rest_framework import serializers

from mail.models import MailAccount


class BaseMailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MailAccount
        fields = (
            'id',
            'email',
            'password',
            'secret',
            'created_at'
        )


class MailSerializer(BaseMailSerializer):
    pass
