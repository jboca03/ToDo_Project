from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from .models import Task

#Login Page Code
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('tasks')
            elif user is not None and user.is_user:
                login(request, user)
                return redirect('tasks')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})
            
#Register Page Code 
def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('tasks')
        else:
            msg = 'form is not valid'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})
    
# logout view
def logout_user(request):
    logout(request)
    return redirect('home')


# Home view
def home(request):
    return render(request, "home.html")

# About Page
def about(request):
    return render(request, 'about.html')

# Contact page
def contact(request):
    return render(request, 'contact.html')

#Page with task lists
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks']
        context['count'] = context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
            
        context['search_input'] = search_input
        return context

# This page shows details of specific tasks
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'ToDo_App/task.html'

# This Page creates tasks
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    

#This Page allows for task updates
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['user', 'title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        #If the user is not an admin, restrict from fields
        if self.request.user.is_user:
            form.fields['user'].widget.attrs['disabled'] = 'disabled'
            form.fields['title'].widget.attrs['readonly'] = True
            form.fields['description'].widget.attrs['readonly'] = True
            form.fields['complete'].required = False  # Allow toggling only complete/incomplete
        return form

#This page allows you to delete tasks 
#This page allows you to delete tasks 
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
