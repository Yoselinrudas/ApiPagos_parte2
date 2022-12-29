# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Services, Payment_User, Expire_Paymentsd
# from .serializer import ServicesSerializer, Payment_userSerializer, Expire_PaymentsdSerializer


# # Create your views here.

# @api_view (['GET', 'POST'])
# def services(request):
#     print(request)
#     if request.method == 'GET':
#         snippets = Services.objects.all()
#         serializer = ServicesSerializer(snippets, many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         print (request.data)
#         serializer=ServicesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)