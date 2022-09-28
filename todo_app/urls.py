from django.urls import path
from .views import TaskDetail, TaskList, TaskCreate, TaskUpdate, TaskDelete, UserLogin, RegisterUser
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('register/', RegisterUser.as_view(), name = 'register'),

    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name = 'logout'),

    path('', TaskList.as_view(), name = 'task_list'),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name = 'task_detail'),
    path('task_create/', TaskCreate.as_view(), name = 'task_create'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name = 'task_update'),    
    path('task_delete/<int:pk>', TaskDelete.as_view(), name='task_delete')

]



