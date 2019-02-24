.. include:: /common/global.rst

Handling your |acquia-product:acm| cart form block
==================================================

The *cart form block* displays an interactive overview of the items that
have been added to the cart, and is displayed on the cart review page by
default. The block displays information from the `cart
block </commerce/cart/cart-block>`__, and also provides a quantity box
to allow customers to alter the items in their cart.

The cart form block has the following attributes:

-  Summarizes the cart with an itemized list
-  Allows you to apply discounts and change item quantity
-  Shows a **Checkout** button to allow you to begin the checkout
   process

This block loads the **Customer Cart Form** which is a `Form
Controller <https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Controller%21FormController.php/class/FormController/8.2.x>`__.
This may be used directly if you want a more complex cart than the one
provided by the ``/cart`` controller in |acquia-product:acm|
(``acq_cart``).

This does not attach the current order to the form so when preprocessing
or templating the block, you will need to access the cart by using the
cart storage service.

``\Drupal::service(‘acq_cart.cart_storage’)->getCart();``

.. important::

    You cannot have a `cart block </commerce/cart/cart-block>`__ and a cart
    form block on the same webpage, as this will prevent the cart form block
    from updating correctly.
