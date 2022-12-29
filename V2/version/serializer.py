from V2.models import *
from rest_framework.serializers import ModelSerializer

class ServicesSerializers(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class PaymentUsersSerializers(ModelSerializer):
    class Meta:
        model = Payment_User
        fields = "__all__"

class ExpiredPaymentsSerializers(ModelSerializer):
    class Meta:
        model = Expire_Paymentsd
        fields = "__all__"