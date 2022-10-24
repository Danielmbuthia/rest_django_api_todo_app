from django.urls import path

from api.views import (
    api_overview,
    get_all_tasks,
    create_tasks,
    update_tasks,
    delete_task,
    task_details
    )

urlpatterns = [
    path('',api_overview,name='api'),
    path('task-list',get_all_tasks,name="all_tasks"),
    path('task-detail/<int:pk>',task_details,name='task_details'),
    path('task-create',create_tasks,name="create_task"),
    path('task-update/<int:pk>',update_tasks,name='update_task'),
    path('task-delete/<int:pk>',delete_task,name='delete_task')
]
