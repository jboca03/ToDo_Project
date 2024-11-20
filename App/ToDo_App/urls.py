from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),

    # Login and registration URLs
    # Custom login view for additional control
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('register/', RegisterPage.as_view(), name='register'),  # Registration view
    path('logout/', LogoutView.as_view(next_page='login'),
         name='logout'),  # Logout view with redirect to home

    # Redirected after login
    path('my-to-do-lists/', views.my_to_do_lists,
         name='my_to_do_lists'),  # My To-Do Lists page

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Page with the list of tasks
    path('tasklist/', TaskList.as_view(), name='tasks'),

    # This page shows details of a task
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),

    path('task-create/', TaskCreate.as_view(), name='task-create'),

    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),

    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
