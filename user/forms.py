from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from user.models import MyUser


class UserRegistrationForm(UserCreationForm):
    """
      Form for Registering new users 
    """
    email = forms.EmailField(max_length=60, help_text = 'Required. Add a valid email address')
    class Meta:
        model = MyUser
        fields = ('name','email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['name'],self.fields['email'],self.fields['password1'],self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})

class UserAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    class Meta:
        model  =  MyUser
        fields =  ('email', 'password')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            
# class UserAuthenticationForm(forms.ModelForm):

# 	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'required form-control',}))
# 	email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control'},))
# 	class Meta:
# 		model = MyUser
# 		fields = ('email', 'password')

	# def clean(self):
	# 	if self.is_valid():
	# 		username = self.cleaned_data['username']
	# 		password = self.cleaned_data['password']
	# 		if not authenticate(username=username, password=password):
	# 			raise forms.ValidationError("Invalid login")

class UserUpdateform(forms.ModelForm):
    """
      Updating User Info
    """
    class Meta:
        model  = MyUser
        fields = ('email',)
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(AccountUpdateform, self).__init__(*args, **kwargs)
        for field in (self.fields['email']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk = self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' already in use." %email)
    
# class UserUpdateForm(forms.ModelForm):

# 	class Meta:
# 		model = MyUser
# 		fields = ('email', )

	# def clean_email(self):
	# 	email = self.cleaned_data['email'].lower()
	# 	try:
	# 		user = MyUser.objects.exclude(pk=self.instance.pk).get(email=email)
	# 	except MyUser.DoesNotExist:
	# 		return email
	# 	raise forms.ValidationError('Email "%s" is already in use.' % user)

	# def clean_username(self):
	# 	username = self.cleaned_data['username']
	# 	try:
	# 		user = MyUser.objects.exclude(pk=self.instance.pk).get(username=username)
	# 	except MyUser.DoesNotExist:
	# 		return username
	# 	raise forms.ValidationError('Username "%s" is already in use.' % username)


