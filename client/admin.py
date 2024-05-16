from django.contrib import admin

from client.models import Enquiry, PaymentTransaction

# Register your models here.


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message", "created_at")

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(Enquiry, EnquiryAdmin)


class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ("id","user", "type", "amount", "description", "created_at")

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(PaymentTransaction, PaymentTransactionAdmin)
