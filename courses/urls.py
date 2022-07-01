from django.urls import path
from courses.views import home, coursePage, login,register,SignupView,LoginView
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', home, name ='homepage'),
    path('course/<str:slug>',coursePage, name='coursepage' ),
    path('signup/',SignupView.as_view(), name='signup' ),
    path('login/', auth_view.LoginView.as_view(template_name = 'courses/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'courses/logout.html'), name='logout')
    # path('login/', LoginView.as_view(), name='login')
]