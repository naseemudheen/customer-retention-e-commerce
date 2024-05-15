from django.contrib import admin

from api.models import CustomerPrediction


# Register your models here.
class CustomerPredictionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "customer_id",
        "tenure",
        "order_count",
        "predicted_churn_risk",
        "predicted_churn_probability",
        "current_date",
    )


admin.site.register(CustomerPrediction, CustomerPredictionAdmin)
