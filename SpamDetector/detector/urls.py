from django.urls import path

from detector.views import index

urlpatterns = [
    path('' , index , name='index' ),
]