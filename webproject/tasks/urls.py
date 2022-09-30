from django.urls import path
from tasks.views.base import index_view
from tasks.views.tasks import add_view, del_view, edit_view, detail_view, del_confirm_view, tasks_del_view, tasks_del_confirm_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='task_add'),
    path('del/<int:pk>', del_view, name='task_del'),
    path('del_confirm/<int:pk>', del_confirm_view, name='confirm_delete'),
    path('edit/<int:pk>', edit_view, name='task_edit'),
    path('task/', index_view),
    path('task/<int:pk>', detail_view, name='task_detail'),
    path('tasks_del', tasks_del_view, name='tasks_del'),
    path('tasks_del_confirm', tasks_del_confirm_view, name='tasks_del_confirm')
]