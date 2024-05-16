from django.db import models

from user.models import MyUser
from shortuuid.django_fields import ShortUUIDField

# Create your models here.


class PaymentTransaction(models.Model):
    id = ShortUUIDField(
        length=11,
        max_length=11,
        primary_key=True,
        alphabet="0123456789",
    )
    TYPE_CHOICES = [
        ("credit", "Credited"),
        ("debit", "Debited"),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    description = models.CharField(
        max_length=255, help_text="Write your expense description."
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-created_at",
        ]

    # def __str__(self):
    # return str(self.category)
class Enquiry(models.Model):
    phone = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    message = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
        ordering = ("-created_at",)

    def __str__(self):
        return ("{}-{}").format(self.name, self.phone)