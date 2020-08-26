"""View module for handling requests about payment types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from ecommerceapi.models import Customer, PaymentType


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for payment types

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = PaymentType
        url = serializers.HyperlinkedIdentityField(
            view_name='payment_type',
            lookup_field='id'
        )
        fields = ('id', 'url', 'merchant_name', 'account_number')


class ParkAreas(ViewSet):
    """Park Areas for Kennywood Amusement Park"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            area = ParkArea.objects.get(pk=pk)
            serializer = ParkAreaSerializer(area, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        areas = ParkArea.objects.all()
        serializer = ParkAreaSerializer(
            areas,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
