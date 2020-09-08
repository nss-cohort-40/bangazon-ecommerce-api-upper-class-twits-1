import json
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from ecommerceapi.models import Product, Customer, ProductType
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# *  Good rules-of-thumb include having:
#     * a separate TestClass for each model or view, or for us --- every endpoint
#     * a separate test method for each set of conditions you want to test
#     * test method names that describe their function

class TestProducts(TestCase):

    # setUp() is called before every test function to set up any objects that may be modified by the test (every test function will get a "fresh" version of these objects).
    def setUp(self):
        self.username = 'testuser'
        self.password = 'foobar'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.customer = Customer.objects.create(user=self.user, address="123 Sesame", phone_number="1234566677")
        self.product_type = ProductType.objects.create(name="Uggs")

    def test_post_product(self):

        new_product = {
              "title": "Halloween Uggs",
              "price": 210.00,
              "description": "spooky, sweaty boots",
              "quantity": 2,
              "location": "Franklin",
              "product_type_id": 1
        
            }

         #  Use the client to send the request and store the response
        response = self.client.post(
            reverse('product-list'), new_product, HTTP_AUTHORIZATION='Token ' + str(self.token)
          )

        # Getting 200 back because we have a success url
        self.assertEqual(response.status_code, 200)

        # Query the table to see if there's one ParkArea instance in there. Since we are testing a POST request, we don't need to test whether an HTTP GET works. So, we just use the ORM to see if the thing we saved is in the db.
        self.assertEqual(Product.objects.count(), 1)

        # And see if it's the one we just added by checking one of the properties. Here, name.
        self.assertEqual(Product.objects.get().title, 'Halloween Uggs')

    # def test_get_products(self):

    #     new_product = Product.objects.create(
    #         title="Christmas Uggs",
    #         price=310.00,
    #         description="festive, sweaty boots",
    #         quantity=4,
    #         location="Franklin",
    #         product_type_id=1,
    #         customer_id=1
    #          )

    #     # Now we can grab all the area (meaning the one we just created) from the db
    #     response = self.client.get(reverse('product-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))

    #     # Check that the response is 200 OK.
    #     # This is checking for the GET request result, not the POST. We already checked that POST works in the previous test!
    #     self.assertEqual(response.status_code, 200)

    #     # response.data is the python serialized data used to render the JSON, while response.content is the JSON itself.
    #     # Are we responding with the data we asked for? There's just one parkarea in our dummy db, so it should contain a list with one instance in it
    #     self.assertEqual(len(response.data), 1)

    #     # test the contents of the data before it's serialized into JSON
    #     self.assertEqual(response.data[0]["title"], "Christmas Uggs")

    #     # Finally, test the actual rendered content as the client would receive it.
    #     # .encode converts from unicode to utf-8. Don't get hung up on this. It's just how we can compare apples to apples
    #     self.assertIn(new_product.title.encode(), response.content)

    def test_delete_product(self):

        new_product = Product.objects.create(
            title="Easter Uggs",
            price=110.00,
            description="festive, sweaty boots",
            quantity=4,
            location="Franklin",
            product_type_id=1,
            customer_id=1
             )

        # Now we can grab all the area (meaning the one we just created) from the db
        response = self.client.get(reverse('product-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))

        # Check that the response is 200 OK.
        # This is checking for the GET request result, not the POST. We already checked that POST works in the previous test!
        self.assertEqual(response.status_code, 200)

        # response.data is the python serialized data used to render the JSON, while response.content is the JSON itself.
        # Are we responding with the data we asked for? There's just one parkarea in our dummy db, so it should contain a list with one instance in it
        self.assertEqual(len(response.data), 1)

        # test the contents of the data before it's serialized into JSON
        self.assertEqual(response.data[0]["title"], "Easter Uggs")

        # Finally, test the actual rendered content as the client would receive it.
        # .encode converts from unicode to utf-8. Don't get hung up on this. It's just how we can compare apples to apples
        self.assertIn(new_product.title.encode(), response.content)
        
        url = reverse('product-detail', kwargs={'pk': new_product.id})

           
        delete_response = self.client.delete(url, HTTP_AUTHORIZATION='Token ' + str(self.token)
          )
        self.assertEqual(delete_response.status_code, 204)

        