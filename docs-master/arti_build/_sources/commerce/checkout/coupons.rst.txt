.. include:: /common/global.rst

Using coupons with |acquia-product:acm|
=======================================

|acquia-product:acm| supports coupons with carts, enabling your commerce
application to deliver discounts or other promotions to your users
within your Drupal application.

Changing or retrieving a coupon
-------------------------------

The ``coupon`` variable stores the current value of the coupon. To
change an applied coupon code, submit the new coupon code, which will
remove the current coupon code and set the new one in its place.

Usage of coupons
----------------

Only one coupon code can be set at any time. When using coupons:

-  If you submit an incorrect coupon code, no coupon code is set.
-  If you send an incorrect coupon code string to |acquia-product:ccs|,
   any existing coupon code will be removed.

The |acquia-product:acm| Demo theme contains examples of coupon code
usage and theming. Coupons are a standard form element:

``$form_state->getValue('coupon')``
