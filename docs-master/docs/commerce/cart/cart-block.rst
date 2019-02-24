.. include:: /common/global.rst

Handling your |acquia-product:acm| cart block
=============================================

The *cart block* provides an itemized breakdown of the contents of a
cart.

The cart block is for display purposes, and has the following
characteristics:

-  Summarizes the cart with an itemized list, with each item's quantity
   and price
-  Displays any applied discounts
-  Indicates both the subtotal of the cart's added items (before
   discounts) and the overall total cost
-  Does not allow you to update the quantities of items

The default implementation uses the theme for table to handle displaying
the cart contents. Because the cart object is not added to the render
array, if you are altering the table that is used you will need to
access the cart object from the cart storage service.

.. important::

    You cannot have a cart block and a `cart form
    block </commerce/cart/cart-form-block>`__ on the same webpage, as this
    will prevent the cart form block from updating correctly.
