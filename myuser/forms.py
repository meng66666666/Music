from django.forms import ModelForm

from mymusic.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'userpwd', 'usertel', 'user_sex',)