from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token

# Create your views here.


@method_decorator(login_required, name="dispatch")
class HomePage(View):
    template_name = "dashboard/index.html"

    def get(self, request):
        context = {"name": request.user.name, "balance": request.user.balance}
        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class ProfilePage(View):
    template_name = "dashboard/profile.html"

    def get(self, request):
        context = {"name": request.user.name, "balance": request.user.balance}
        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class DevAPIPage(View):
    template_name = "dashboard/dev_api.html"

    def get(self, request):
        token,created = Token.objects.get_or_create(user=request.user)

        context = {
            "name": request.user.name,
            "balance": request.user.balance,
            "api_token": token.key,
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class PaymentPage(View):
    template_name = "dashboard/payment.html"

    def get(self, request):
        context = {"name": request.user.name, "balance": request.user.balance}
        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class SettingsPage(View):
    template_name = "dashboard/settings.html"

    def get(self, request):
        context = {"name": request.user.name, "balance": request.user.balance}
        return render(request, self.template_name, context)
