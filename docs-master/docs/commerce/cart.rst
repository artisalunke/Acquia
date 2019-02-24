.. include:: /common/global.rst

Handling your Acquia Commerce Manager cart
==========================================

.. toctree::
   :hidden:
   :glob:

   /commerce/cart/cart-mini-block/
   /commerce/cart/cart-block/
   /commerce/cart/cart-form-block/

The |acquia-product:acm| Drupal modules provide an **Add to Cart**
button for every product page, along with several blocks for displaying
cart information to your customers. The cart blocks interface with the
|acquia-product:ccs| to manage the cart and relay this information to
the commerce backend so all of your systems remain synchonized.

When a visitor is signed in and shopping, the state of their cart is
saved even if the visitor leaves the website and then returns to sign in
later.

The cart blocks display their contents from the session stored cart
object and do not make a request back to the |acquia-product:ccs| when
displaying their information.

Available cart blocks
---------------------

+-----------------+-----------------+-----------------+-----------------+
| Feature         | `Cart           | `Cart form      | `Cart mini      |
|                 | block </commerc | block </commerc | block </commerc |
|                 | e/cart/cart-blo | e/cart/cart-for | e/cart/cart-min |
|                 | ck>`__          | m-block>`__     | i-block>`__     |
+=================+=================+=================+=================+
| Per-item list   | |Yes|           | |Yes|           | |No|            |
| summary         |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Displays        | |Yes|           | |Yes|           | |No|            |
| discounts       |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Accepts         | |No|            | |Yes|           | |No|            |
| customer        |                 |                 |                 |
| changes         |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Displays totals | |Yes|           | |Yes|           | |Yes|           |
+-----------------+-----------------+-----------------+-----------------+

Using cart blocks
-----------------

Blocks provided by |acquia-product:acm| are used in the same fashion as
any other Drupal block. They are provided in the custom block list, and
can be placed using the normal block system. For more details about
blocks, see `Working with
blocks <https://www.drupal.org/docs/8/core/modules/block/overview>`__ on
Drupal.org.

As an example to quickly get started using blocks, the following
procedure describes adding a cart mini block to your website's header:

#. Sign into your Drupal website as an administrator.
#. Go to **Structure > Block layout**.
#. Select a region to add a block to (in this case, **Header**), and
   then click **Place block** next to that region's name.
   The list of available blocks appears.
#. Next to your block (for this example, **Cart Mini Block**), click
   **Place block**.
#. In the **Configure block** dialog box, make your configuration
   changes.
#. Click **Save block**.

Your cart block will now appear in your header.

Theming cart blocks
-------------------

In general, cart block theming is handled by standard Drupal theming for
tables and related items. Any specialized theming requirements are noted
on a cart block's documentation page.

.. |Yes| image:: https://cdn2.webdamdb.com/1280_EqxUKAqtA07.png?-62169955200
   :class: no-sb
   :height: 18px
.. |No| image:: https://cdn2.webdamdb.com/1280_MIQySTMO5Mh1.png?-62169955200
   :class: no-sb
   :height: 18px
