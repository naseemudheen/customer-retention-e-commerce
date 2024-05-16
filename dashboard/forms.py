from django.contrib.auth.forms import UserChangeForm

from user.models import MyUser

class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = MyUser
        fields = [
            "email",
            "name",
            "phone",
        ]
        labels = {
            "email": "Email",
            "phone": "Phone",
            "name": "Name",

        }
