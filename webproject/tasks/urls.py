from django.urls import path
from tasks.views.base import index_view
from tasks.views.tasks import add_view, del_view, edit_view, detail_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='task_add'),
    path('del/<int:pk>', del_view, name='task_del'),
    path('edit/<int:pk>', edit_view, name='task_edit'),
    path('task/', index_view),
    path('task/<int:pk>', detail_view, name='task_detail')
]