from django.urls import path
from  . import views


urlpatterns = [
      path('contact/', views.send_email, name='comtactlist'),
]