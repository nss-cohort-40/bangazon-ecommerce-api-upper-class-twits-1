"""View module for handling requests about park areas"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ecommerceapi.models import Product, Customer, ProductType, Order, OrderProduct
from rest_framework.decorators import action


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Product
        url = serializers.HyperlinkedIdentityField(
            view_name='product',
            lookup_field='id'
        )
        fields = ('id', 'title', 'price', 'description', 'quantity',
                  'location', 'image_path', 'product_type', 'customer_id', 'customer', 'product_type_id')
        depth = 2


class Products(ViewSet):
    """Product for Ecommerce API"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Product instance
        """

        customer = Customer.objects.get(user=request.auth.user)
        # gets the customer that matches the token that is sent with the request
        product_type = ProductType.objects.get(
            pk=request.data["product_type_id"])

        newproduct = Product()
        newproduct.title = request.data["title"]
        newproduct.price = request.data["price"]
        newproduct.description = request.data["description"]
        newproduct.quantity = request.data["quantity"]
        newproduct.location = request.data["location"]
        # newproduct.image_path = request.data["image_path"]
        # newproduct.created_at = request.data["created_at"]
        newproduct.customer = customer
        newproduct.product_type = product_type

        newproduct.save()

        serializer = ProductSerializer(
            newproduct, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single product

        Returns:
            Response -- JSON serialized product instance
        """
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(
                product, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to products resource

        RETURNS:
            response -- JSON serialized product instance
        """
        products = Product.objects.all()
        serializer = ProductSerializer(
            products,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single product

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT requests for product quantity

        Returns:
            Response -- Empty body with 204 status code
        """
        product = Product.objects.get(pk=pk)
        product.quantity = request.data["quantity"]
        product.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

# Example request:
#   http://localhost:8000/orders/cart

    @action(methods=['get', 'post', 'delete'], detail=False)
    def cart(self, request):
        if request.method == "GET":

            current_user = Customer.objects.get(user=request.auth.user)

            try:
                open_order = Order.objects.get(
                    customer=current_user, payment_type=None)
                products_on_order = Product.objects.filter(
                    cart__order=open_order)

            except Order.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

            serializer = ProductSerializer(
                products_on_order, many=True, context={'request': request})
            return Response(serializer.data)

        elif request.method == "POST":

            current_user = Customer.objects.get(user=request.auth.user)

            order = None

            try:
                order = Order.objects.get(
                    customer=current_user, payment_type=None)

            except Order.DoesNotExist:
                order = Order.objects.create(customer=current_user)

            product = Product.objects.get(pk=request.data['product_id'])

            new_order_product = OrderProduct.objects.create(
                order_id=order.id,
                product_id=product.id
            )

            return Response({}, status=status.HTTP_201_CREATED)

        elif request.method == "DELETE":

            current_user = Customer.objects.get(user=request.auth.user)

            try:
                product_on_order = OrderProduct.objects.get(
                    pk=request.data['orderproduct_id'])
                product_on_order.delete()
                return Response({}, status=status.HTTP_204_NO_CONTENT)

            except OrderProduct.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            except Exception as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
