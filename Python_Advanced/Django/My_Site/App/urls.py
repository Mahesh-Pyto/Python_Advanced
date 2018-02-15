from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'details/', views.app_details,name='details'),

]