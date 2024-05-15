from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path('login', LoginPageView.as_view(), name="login"),
    path('', HomePageView.as_view(), name="index"),
    path('logout/',LogoutPageView.as_view(),name ="logout"),
    path('register/',RegisterPageView.as_view(), name ="register"),

    path('password-reset/',ResetPasswordView.as_view()
        ,name ="password_reset"), 
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(
        template_name = 'auth/password_reset_done.html')
        ,name ="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view
    (
        success_url=reverse_lazy('user:password_reset_complete'),
        template_name = 'auth/password_reset_confirm.html'
        ),
        name ="password_reset_confirm"),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(
        template_name = 'auth/password_reset_complete.html')
        ,name ="password_reset_complete"),  
]