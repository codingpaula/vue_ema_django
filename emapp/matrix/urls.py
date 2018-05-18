from django.conf.urls import url
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from matrix import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('topics/', views.TopicList.as_view()),
    path('topics/<int:pk>/', views.TopicDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
