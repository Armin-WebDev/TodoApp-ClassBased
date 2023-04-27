
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('' , views.TaskList.as_view() , name='task_list'),
    path('create/' , views.AddTask.as_view(), name='create_task'),
    path('update/<int:pk>/' , views.UpdateTask.as_view(), name='update_task'),
    path('delete/<int:pk>/' , views.TaskDelete.as_view(), name='delete_task'),
    path("complete/<int:pk>/", views.DoneTask.as_view(), name="complete_task"),
]
