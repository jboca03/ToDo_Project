from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    
    # Login and registration URLs
    path('login/', views.login_user, name='login'),  # Custom login view for additional control
    path('register/', views.register, name='register'),  # Registration view
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout view with redirect to home
    
    # Redirected after login
    path('my-to-do-lists/', views.my_to_do_lists, name='my_to_do_lists'),  # My To-Do Lists page

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
