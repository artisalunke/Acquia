.. include:: /common/global.rst

Troubleshooting |acquia-product:acm|
====================================

Despite our best efforts, there may be occasions when
|acquia-product:acm| may not perform as you would expect. Use this
troubleshooting guide as you attempt to resolve any issues that you
encounter, and to better prepare for a conversation with Acquia Support
if you continue to experience issues.

Cart block/checkout mismatch
----------------------------

If the cart session with the commerce solution times out or is unable to
connect, the cart block and the checkout process will display a data
mismatch, which can be represented in the following ways:

-  Updating a cart does not successfully update the display for all cart
   blocks
-  Having a cart that displays less items at checkout than it should
   have (for example, a cart with 20 items having only 2 items at
   checkout)

This mismatch can be a result of the following:

-  The commerce solution returns a 404 Not Found HTTP response to a
   request during the checkout process.
-  You have navigated to the shipping page without an active cart
   session.
