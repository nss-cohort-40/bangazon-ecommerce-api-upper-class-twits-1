"""View module for handling requests about payment types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ecommerceapi.models import Customer, PaymentType


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for payment types

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = PaymentType
        url = serializers.HyperlinkedIdentityField(
            view_name='payment type',
            lookup_field='id'
        )
        fields = ('id', 'url', 'merchant_name', 'account_number',
                  'customer', 'expiration_date', 'created_date')


class PaymentTypeView(ViewSet):
    """Payment Type for Bangazon"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single payment type

        Returns:
            Response -- JSON serialized payment type instance
        """
        try:
            payment_type = PaymentType.objects.get(pk=pk)
            serializer = PaymentTypeSerializer(
                payment_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to payment types resource

        Returns:
            Response -- JSON serialized list of payment typess
        """
        payment_types = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(
            payment_types,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
