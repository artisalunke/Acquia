.. include:: /common/global.rst

Checkout and payment methods
============================

.. toctree::
   :hidden:
   :glob:

   /commerce/checkout/flow/
   /commerce/checkout/coupons/

The |acquia-product:acm| Drupal modules provide a pluggable checkout
experience that interfaces with your commerce solution, by way of the
|acquia-product:ccs|. The default checkout flow captures customer
information and places an order with the commerce solution. After the
order has been placed, all order management tasks happen from the
commerce solution.

This functionality can be enabled and disabled independently of the core
|acquia-product:acm| module, as the checkout process is provided by the
**Acquia Commerce Checkout** submodule.

The |acquia-product:acm| modules introduce a concept known as *Checkout
Flows*. These are configurable steps that customers will need to
complete before their order is placed with the commerce solution. To
begin the checkout process, a customer is expected to review their cart
from the Cart Page (``http://mysite.com/cart``) — which uses a Checkout
Pane — and then continue through the checkout with the Payment Method.

Checkout Panes, Flows, and Payment Methods are plugins, which can be
modified by a developer.

The default checkout flow defines five steps for placing an order:

-  Adding `shipping and billing addresses <#addresses>`__
-  Choosing a `payment method <#payment-methods>`__
-  Selecting a `delivery method <#shipment>`__
-  `Reviewing the order <#review-the-order>`__
-  Completing the order

Addresses
---------

Shipping and billing addresses is handled by the **Address** Drupal
module, which is installed when setting up |acquia-product:acm|.

To enable addresses for your users, complete the following steps:

#. Sign in to your Drupal website as an administrator.
#. Go to **Configuration > Account settings > Manage fields**.
#. Click **Add new field**.
#. In the list, select **Address**, and then click **Save and
   continue**.
#. Fill out the fields as appropriate for your website.

When complete, address forms will appear on the user's account page. If
this is a new customer, |acquia-product:acm| will automatically select
the **Save address** check box. If the user already has stored an
address, this check box will not be selected, but the user may choose to
select it and store additional addresses.

Payment methods
---------------

Payments are handled by the commerce solution. Drupal will interface
with the |acquia-product:ccs| to initialize the payment processes when
the order is placed. Credit card information will be passed between the
|acquia-product:acm| components, but will not be stored in Drupal.

Drupal can support multiple payment methods. The following payment
methods are currently supported by |acquia-product:acm|:

-  Authorize.net
-  Braintree
-  Cheque/Money order

Shipment
--------

Shipping details should be configured in the commerce solution. The
|acquia-product:ccs| will coordinate between the Drupal website and the
commerce solution to display relevant shipping information, based on the
configured shipping values in the commerce solution.

Review the order
----------------

This step in the process displays a summary of each completed step
throughout the checkout. It allows the customer to verify their entered
information, and perform any alterations prior to sending the order to
the |acquia-product:ccs| for processing.
