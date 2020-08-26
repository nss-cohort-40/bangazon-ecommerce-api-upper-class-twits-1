from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# STATUS USER FOR DESTROY/UPDATE METHODS
from rest_framework import status
from ecommerceapi.models import Customer
from .user import UserSerializer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Customer
        url = serializers.HyperlinkedIdentityField(
            view_name='customer',
            lookup_field='id'
        )
        fields = ('id', 'url', 'user', 'phone_number', 'address')


class CustomerView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(
                customer, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        customers = Customer.objects.all()
        serializer = CustomerSerializer(
            customers, many=True, context={'request': request})
        return Response(serializer.data)
