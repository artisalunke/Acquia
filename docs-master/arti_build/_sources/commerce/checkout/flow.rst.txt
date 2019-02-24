.. include:: /common/global.rst

|acquia-product:acm| checkout flow plugins
==========================================

By default, the |acquia-product:acm| checkout (``acq_checkout``) module
defines the ``MultistepDefault`` checkout flow as the enabled checkout
flow for your Drupal website. Because there is nothing in the user
interface to change this, you will need to manually update the
configuration value for ``checkout_flow_plugin`` in the
``acq_checkout.settings`` configuration object.

Checkout pane plugins
---------------------

Checkout pane plugins are responsible for defining form operations. A
pane should define both a ``buildPaneForm`` method and a
``submitPaneForm`` method. The build method is responsible for returning
a render array that will be used to collect user information. The submit
method should update the session cart object with relevant information.

When defining the checkout pane plugin, be aware of the ``defaultStep``
annotation property, as this determines in which step the pane will
appear.

Shipment plugins
----------------

After the customer provides their billing information, a request is made
to the |acquia-product:ccs| to fetch a shipping estimate. It is at this
stage that a cart is initialized.

Your commerce platform uses the customer information, the billing
address, and the default shipping method to build an initial estimate.
The customer can then update the cart by providing a separate address
and selecting a shipping method. The default shipping method is
retrieved by the |acquia-product:ccs| from your commerce platform, and
needs to be configured in your commerce platform.

Payment pane and default payment methods
----------------------------------------

The ``acq_payment`` module defines a checkout pane that will be visible
on the payment step. When the pane is building the form, it will make a
request to the |acquia-product:ccs| to retrieve the configured payment
gateways from the commerce platform.

Payments operate using tokens. When a customer makes a payment from the
Drupal website, the website sends a request to the |acquia-product:ccs|
to generate a payment token.

Payment methods and payment method plugins
------------------------------------------

Payment methods are defined using a payment method plugin
(``ACQPaymentMethod``) which is defined in the ``acq_payment`` module.
The default payment method for all orders is the *Checkmo* payment
plugin, and this method does not accept payment information.

When defining a custom payment method, the identifier of the plugin
should match the response from the commerce platform.

The payment checkout pane will display all available payment plugins to
allow customers to determine which payment method with which they want
to pay.

Note

The payment gateways defined in the commerce platform require a
corresponding Drupal payment plugin.

Review
------

The review pane displays a summary of all active panes in the checkout
flow. The pane will call a ``buildPaneSummary`` method to get a
representation of each pane that the customer filled out during the
checkout process.

To change how the review pane displays, you can use
``hook_form_multistep_default_alter`` and inspect the form to determine
which step you are on, and alter the forms render array. Depending on
the customizations it may be better to define custom panes and a custom
flow to ensure the checkout process matches your use case.

Checkout progress indication
----------------------------

The ``acq_checkout`` module provides a block that displays the
customer’s progress through the checkout process. This block is named
*Checkout progress* and is not placed when the module is enabled.

If required, this block should be added and made visible on
``/cart/checkout`` and ``/cart/checkout/*``.

Theming
-------

The ``acq_checkout`` module defines a template for the checkout progress
block. This can be overridden by adding the following template file to
your custom theme:

``acq_checkout_progress.html.twig``

Route customization
-------------------

By default, the ``acq_checkout`` module defines the following
`routes <https://www.drupal.org/docs/8/api/routing-system/routing-system-overview>`__:

-  ``/cart/checkout``
-  ``/cart/checkout/[step id]``

If you need routes to differ, you can define a custom route using
``/cart/checkout`` as a guide.
