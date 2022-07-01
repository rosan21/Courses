from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from courses.forms import SignUpForm,LoginForm
from django.contrib import messages
from django.views import View

  
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'courses/signup.html', {'form': form})
    

def login(request):
    form = LoginForm()
    context = {'form':form}
    return render(request, 'courses/login.html',context)

class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'courses/signup.html', {'form': form})
    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('homepage')

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {'form':form}
        return render(request, 'courses/login.html', context)
    def post(self,request):
        form = LoginForm(request=request, data = request.POST)
        context = {'form': form}
        if form.is_valid():
            return HttpResponse('Login')
        

