from django.urls import path
from  . import views

urlpatterns = [
      path('', views.Posting.as_view(), name='listinglist'),
      path('<int:advert_id>/id', views.put, name='updateAll'),
      path('<int:advert_id>', views.patch, name='update'),
      path('<int:advert_id>/delete', views.delete, name='delete'),

]