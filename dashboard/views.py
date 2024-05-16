from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from api.models import CustomerPrediction
from client.models import PaymentTransaction
from dashboard.forms import ProfileForm
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


class HomePage(LoginRequiredMixin, ListView):
    model = CustomerPrediction
    template_name = "dashboard/index.html"
    context_object_name = "predictions"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["name"] = user.name
        context["balance"] = user.balance
        predictions = CustomerPrediction.objects.filter(user=user).values(
            "customer_id",
            "tenure",
            "day_since_last_order",
            "cashback_amount",
            "predicted_churn_risk",
            "predicted_churn_probability",
            "created_at",
        )
        context["predictions"] = predictions

        return context


@login_required(login_url="login")
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully — ")
    else:
        form = ProfileForm(instance=request.user)
    context = {
        "name": request.user.name,
        "balance": request.user.balance,
        "form": form,
    }
    return render(request, "dashboard/profile.html", context)


@method_decorator(login_required, name="dispatch")
class DevAPIPage(View):
    template_name = "dashboard/dev_api.html"

    def get(self, request):
        token, created = Token.objects.get_or_create(user=request.user)

        context = {
            "name": request.user.name,
            "balance": request.user.balance,
            "api_token": token.key,
        }
        return render(request, self.template_name, context)


class PaymentListPage(LoginRequiredMixin, ListView):
    model = PaymentTransaction
    template_name = "dashboard/payment.html"
    context_object_name = "transactions"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["name"] = user.name
        context["balance"] = user.balance
        context["transactions"] = PaymentTransaction.objects.filter(user=user)

        return context


@login_required(login_url="login")
def password_change_form(request):
    """A form for allowing a user to change their password."""
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password Change Successfully!")
                return redirect("/dashboard")
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "dashboard/settings.html", {"form": form})
    else:
        return redirect("login")
