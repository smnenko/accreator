from django.urls import path

from mail import views


urlpatterns = [
    path('', views.MailListCreateView.as_view())
]
