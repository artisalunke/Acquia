.. include:: /common/global.rst

Known issues in |acquia-product:acm|
====================================

|acquia-product:acm| has the following known issues:

-  You cannot have a `cart block </commerce/cart/cart-block>`__ and a
   `cart form block </commerce/cart/cart-form-block>`__ on the same
   webpage, as this prevents the cart form block from updating
   correctly.
-  Initial configuration may require you to review the checkout flow
   settings and then save the form to ensure that the checkout flow IDs
   are set correctly.
-  During the checkout process, a Drupal user account is provisioned for
   the customer. This is done without informing the user that they have
   created an account. Returning customers are expected to sign in, as
   email addresses must be unique.
-  If the |acquia-product:ccs| cannot be contacted during the checkout
   process, it will fail.
-  The checkout process can be navigated to without an active cart
   session.
-  When entering a shipping address, using the same address as the
   billing address fails to update the **State** list if the country is
   not ``United States``.
-  If the shipping estimate fails, no indication of the failure is
   provided to the user.
-  You can connect only one Drupal website to the |acquia-product:ccs|.

If you encounter any difficulties with your |acquia-product:acm|
subscription, `contact Acquia Support </support#contact>`__ for
assistance.
