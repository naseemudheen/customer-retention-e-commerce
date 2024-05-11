# api/models.py
from django.db import models

class CustomerPrediction(models.Model):
    # Defining categorical choices
    LOGIN_DEVICE_CHOICES = [
        ('Mobile Phone', 'Mobile Phone'),
        ('Phone', 'Phone'),
        ('Computer', 'Computer')
    ]

    PAYMENT_MODE_CHOICES = [
        ('Debit Card', 'Debit Card'),
        ('COD', 'COD'),
        ('Credit Card', 'Credit Card'),
        ('E wallet', 'E wallet'),
        ('UPI', 'UPI')
    ]

    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male')
    ]

    ORDER_CAT_CHOICES = [
        ('Laptop & Accessory', 'Laptop & Accessory'),
        ('Mobile Phone', 'Mobile Phone'),
        ('Fashion', 'Fashion'),
        ('Mobile', 'Mobile'),
        ('Others', 'Others'),
        ('Grocery', 'Grocery')
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Divorced', 'Divorced'),
        ('Married', 'Married')
    ]

    # Defining the model fields
    customer_id = models.IntegerField()
    churn = models.IntegerField(null=True, blank=True)
    tenure = models.FloatField()
    preferred_login_device = models.CharField(max_length=50, choices=LOGIN_DEVICE_CHOICES)
    city_tier = models.IntegerField()
    warehouse_to_home = models.FloatField()
    preferred_payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    hour_spent_on_app = models.FloatField()
    number_of_device_registered = models.IntegerField()
    prefered_order_cat = models.CharField(max_length=100, choices=ORDER_CAT_CHOICES)
    satisfaction_score = models.IntegerField()
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    number_of_address = models.IntegerField()
    complain = models.IntegerField()
    order_amount_hike_from_last_year = models.FloatField()
    coupon_used = models.FloatField()
    order_count = models.FloatField()
    day_since_last_order = models.FloatField()
    cashback_amount = models.IntegerField()
    predicted_churn_risk = models.CharField(max_length=20)
    predicted_churn_probability = models.DecimalField(max_digits=5, decimal_places=4)
    current_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Risk: {self.predicted_churn_risk}"
