.. include:: /common/global.rst

Acquia Commerce Manager configuration settings
==============================================

.. toctree::
   :hidden:
   :glob:

   /commerce/configuration/*

As an administrator, you need to configure the various sections of your
Drupal website to ensure that it will synchronize your products,
services, and users, while also ensuring that your website displays
those items in the desired fashion. Understanding your configuration
settings and where to find them will help you set up your commerce
website properly. Here, we discuss the various commerce configuration
settings:

-  `Checkout Settings <#checkout-settings>`__
-  `SKU Settings <#sku-settings>`__
-  `Commerce Connector Service Settings <#conductor-settings>`__
-  `Currency Settings <#currency-settings>`__
-  `Commerce User Settings <#commerce-user>`__
-  `Synchronize <#synchronize>`__

You can access the settings for each of the previous items by completing
the following steps:

#. Sign in to your Drupal website as an administrator.
#. Go to **Commerce > Configuration**.
#. Click the specific configuration link.
#. Make your changes.
#. Click **Save** or **Save configuration**.

Checkout settings
-----------------

Checkout settings control the flow of the checkout process for your
users. You can add custom checkout flows with development work.

-  **Use AJAX** – Selecting this check box changes the checkout flow
   into a single page application.
-  **Allow guest checkout** – Selecting this check box enables customers
   to check out as guests, without creating an account.
-  **Validate saved addresses** – If enabled, this setting will validate
   addresses when saved on the account page. When the check box is
   selected, you may also customize **Saved address validation review
   text** and **Saved address validation failed text**.
-  **Validate billing addresses** – If enabled, this setting will
   validate addresses when saved on the account page. When the check box
   is selected, you may also customize **Billing address validation
   review text** and **Billing address validation failed text**.
-  **Validate shipping addresses** – If enabled, this setting will
   validate addresses when saved on the account page. When the check box
   is selected, you may also customize **shipping address validation
   review text** and **Shipping address validation failed text**.
-  **Checkout Flow Plugin** – This plugin determines what type of
   checkout the commerce services use. By default, it is a mulitstep
   process.

SKU settings
------------

SKU settings control the types of SKUs that your commerce website uses.
These are added by your commerce solution and synchronized to Drupal.
The default types are as follows:

-  Configurable
-  Grouped
-  Simple
-  Variant
-  Virtual

.. _conductor-settings:

|acquia-product:ccs| settings
-----------------------------

|acquia-product:ccs| settings are described in the |acquia-product:acm|
Drupal module installation, in the `Commerce Connector Service
settings </commerce/install/modules#conductor>`__ section.

Currency settings
-----------------

Use the following currency settings to determine how your currency will
display for your products and cart:

-  **ISO currency code** – Your currency's ISO 4217 code.
-  **Currency code position** – Determines where your currency's symbol
   appears.
-  A select list for the number of decimal places to show for your
   currency, from ``0`` to ``4``.

Commerce user settings
----------------------

Various user settings

-  **Storage type** – (required) Determines if your website uses
   **Session storage** or **Database storage** for user sessions.
-  **Use E-Comm Sessions** – When this check box is selected, customers
   are anonymous to the website, and use the commerce back end for user
   sessions.
-  **Customer pages plugin** – The plugin used for customer and account
   management pages.

Synchronize promotions
----------------------

The **Synchronize promotions** button on this page manually synchronizes
promotion information between your Drupal website and your commerce
solution.

Synchronize
-----------

This page has two buttons that enable you to manually synchronize data
between your Drupal website, and your commerce solution. Clicking either
button will attempt to synchronize its respective data, in a queue.

-  **Synchronize Categories** – When clicked, categories are updated
   from your commerce solution synchronously.
-  **Synchronize Products (async)** – When clicked, products are updated
   asynchronously from your commerce solution, in batches. This ensures
   performance and stability for your Drupal website as well as your
   commerce solution.
-  **Synchronize Products (sync)** – When clicked, single products are
   updated synchronously from your commerce solution.
