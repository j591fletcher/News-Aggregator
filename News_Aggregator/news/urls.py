from django.conf.urls import url
from . import views

#display index from views
urlpatterns = [
    url('', views.index),
]
