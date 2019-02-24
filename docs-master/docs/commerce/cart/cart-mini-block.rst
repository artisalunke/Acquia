.. include:: /common/global.rst

Handling your |acquia-product:acm| Cart Mini blocks
===================================================

The *cart mini block* displays limited information to the user, and is
intended to give customers a quick cart overview, including the number
of items they have in their cart and the total cost. Normal use of this
block type is for inclusion in the header or sidebar of your website, to
remind the user of their cart contents.

If there is no cart in the session, |acquia-product:acm| will create a
new cart when the block is rendered.

The information in the block is based on the contents from the session
stored cart object, and does not make a request to the
|acquia-product:ccs| when displaying its information. The cart mini
block displays items that are stored in the session variable
``acq_cart``.

Theming
-------

No template suggestions are provided with the cart. To override the
default theming, add the following code to the your theme:

``block--acqminicart.html.twig``

The only variable to which you have access in the minicart template is
``price``.

By default, the mini cart block attempts to format the price to a fixed
number of decimals as defined by a configuration value. If this is not
set, you can have price display issues, as the default behavior of
``number_format`` is to round to the nearest decimal.
