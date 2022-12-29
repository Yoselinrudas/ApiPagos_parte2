from V2.version.serializer import ExpiredPaymentsSerializers, PaymentUsersSerializers, ServicesSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from V2.models import Services, Expire_Paymentsd, Payment_User
from V2.version.pagination import SimplePagination

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser




class ServicesViewUser(ModelViewSet):
    queryset = Services.objects.all()

    throttle_scope = 'Servicios'
    

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list','retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update','partial_update','destroy','retrieve','create']:
            permission_classes = [IsAdminUser]
        return [permissions() for permissions in permission_classes]
    def get_serializer_class(self):
        return ServicesSerializers
        

class PaymentUsersViewUser(ModelViewSet):
    queryset = Payment_User.objects.all()
    pagination_class = SimplePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['paymentDate', 'expirationDate']
    
    throttle_scope = 'pagos'

    def get_permissions(self):
       
        permission_classes = []
        if self.action in  ['list','retrieve','create']:
        
            permission_classes = [IsAuthenticated]
        elif self.action in ['update','partial_update','destroy']:
            permission_classes = [IsAdminUser]
        return [permissions() for permissions in permission_classes]

    def get_serializer_class(self):
        return PaymentUsersSerializers

    def create(self, request, *args, **kwargs):
        Payment_User_id = super().create(request, *args, **kwargs)
        last_pay = Payment_User.objects.order_by('id').first()
        payment = Payment_User.objects.get(id=last_pay.id)
        if payment.expirationDate < payment.paymentDate:
            penalty = payment.monto * 5.00
            expired_payment = Expire_Paymentsd(Payment_User_id=payment,penalty_free_amount=penalty)
            expired_payment.save()
        return Payment_User_id



class ExpiredPaymentViewUser(ModelViewSet):
    queryset = Expire_Paymentsd.objects.all()
    pagination_class = SimplePagination

    throttle_scope = 'Expirado'

    def get_permissions(self):
        permission_classes = []
        if self.action in  ['list','retrieve','create']:
            permission_classes = [IsAuthenticated]

        elif self.action in  ['update','partial_update','destroy','retrieve']:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        return ExpiredPaymentsSerializers