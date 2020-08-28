DELETE FROM ecommerceapi_product;
DELETE FROM ecommerceapi_paymenttype;
DELETE FROM ecommerceapi_order;
DELETE FROM ecommerceapi_orderproduct;

INSERT INTO ecommerceapi_order
  (customer_id, payment_type_id, created_at)
VALUES
  (7, NULL, "2020-09-09");

DELETE FROM ecommerceapi_product;

INSERT INTO ecommerceapi_orderproduct
  (order_id, product_id)
VALUES
  (2, 5);

