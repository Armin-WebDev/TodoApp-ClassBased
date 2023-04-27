from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate,login,logout
# Create your views here.


# def LoginView(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#                 username =request.POST['username']
#                 password = request.POST['password']
#                 user = authenticate(request , username=username, password=password)
#                 if user is not None:
#                     login(request,user)
#                     return redirect('/accounts/done')
#         return render(request,'registration/login.html')            
#     else:
#         return redirect('/')


class LoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("tasks:task_list") 

class SignUp(FormView):
    form_class = UserCreationForm
    redirect_authenticated_user = True
    template_name = '../templates/registration/signup.html'

    success_url = reverse_lazy('done_task')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request , user)
        return super(SignUp, self).form_valid(form)    

