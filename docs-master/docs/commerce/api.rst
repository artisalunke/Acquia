.. include:: /common/global.rst

Acquia Commerce Manager API
===========================

|acquia-product:acm| provides a robust API that allows developers to
both customize their Drupal websites and those websites' interactions with your 
eCommerce solution.

The following APIs are available for use with |acquia-product:acm|:

-  | |acquia-product:acm| API - Enables direct interaction with
     |acquia-product:acm|
   | The base URI for your |acquia-product:acm| API endpoint is:

   .. code-block:: none
   
      https://api.{region}.acm.acquia.io

   where your region is either ``us-east-1`` or ``eu-west-1``.

-  `HMAC API <https://github.com/acquia/http-hmac-postman>`__ -
   Enables you to create custom authorization interactions

Creating Newsletters
--------------------

The |acquia-product:acm| API provides a call that can be used to
subscribe your users to newsletters.

.. code-block:: none

    APIWrapperInterface::subscribeNewsletter($email)

This call can be used with the user's email address to subscribe your
users. If you want to create a subscription system, you could add a
custom `Checkout Pane </commerce/checkout/flow>`__ and `Checkout
Flow </commerce/checkout>`__ that includes asking if customers would
like to subscribe.
