from django.urls import path,include
from .views import taskAPI,taskid,taskcom

urlpatterns=[

path("get-task/",taskAPI.as_view()),
path("taskid/",taskid.as_view()),
path("taskfilter/",taskcom.as_view()),
]