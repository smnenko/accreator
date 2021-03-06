from django.urls import path

from user import views


urlpatterns = [
    path('', views.UserListCreateView.as_view(), name='list_user'),
    path('<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='view_user')
]
