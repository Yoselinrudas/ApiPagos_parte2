from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    logo = models.URLField()

    class Meta:
        db_table = "services"   
   
    def __str__(self):
        return self.name

class Payment_User(models.Model):

    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='usersk')
    servicio = models.ForeignKey(Services,on_delete =models.CASCADE, related_name='services')
    monto = models.FloatField(default=0.0)
    paymentDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField()

    def __str__(self):
        return str(self.pk)


class Expire_Paymentsd(models.Model):

    payment_user_id = models.ForeignKey(Payment_User,on_delete =models.CASCADE, related_name='payment_user')
    penalty_fee_amount = models.FloatField(default=0.0)

   
    