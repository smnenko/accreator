from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel


class MailAccount(BaseModel):
    user = models.ForeignKey(
        to=get_user_model(),
        null=True,
        blank=True,
        related_name='mail_accounts',
        on_delete=models.SET_NULL
    )

    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    secret = models.CharField(max_length=256)

    def __str__(self):
        return self.email
