from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
     #Home Page
     path("", views.home, name="home"),
     
     #Login Page
     path('login/', views.login_view, name='login'),
     
     #Register Page
     path('register/', views.register, name='register'),
     
     #Logout Page with redirect back to Home page
     path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  
     
     #About page
     path('about/', views.about, name='about'),
     
     #Contact Page
     path('contact/', views.contact, name='contact'),

     # Page with the list of tasks
     path('tasklist/', TaskList.as_view(), name='tasks'),

     # This page shows details of a task
     path('task/<int:pk>/', TaskDetail.as_view(), name='task'),

     #This Page creates tasks
     path('task-create/', TaskCreate.as_view(), name='task-create'),

     #This page updates tasks
     path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),

     #This page deletes tasks
     path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
