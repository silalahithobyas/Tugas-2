from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, tambah_task, delete, status, tambah_task, show_json, tambah_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', tambah_task, name='tambah_task'),
    path('delete/<int:id>', delete, name='delete'),
    path('status/<int:update_status>', status, name='status'),
    path('json/', show_json, name='show_json'),
    path('add/', tambah_task_ajax, name='tambah_task_ajax'),
]