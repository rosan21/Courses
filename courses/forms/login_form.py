from django.contrib.auth.forms import AuthenticationForm
from django.forms import PasswordInput, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(AuthenticationForm):
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None
        try:
            user = User.objects.get(username = username)
            result = authenticate(username = username, password =password)
            if result is not None:
                return result
            else:
                raise ValidationError('Username and Password Doesnot match')
        except:
            raise ValidationError('Username and Password Doesnot match')
