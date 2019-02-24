.. include:: /common/global.rst

Managing subscriptions
======================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/subs/*

Your organization on the |acquia-product:ac| platform may include
multiple |acquia-product:ac| subscriptions. If you are the *Owner* or
*Administrator* of an organization, you have access to several available
actions regarding your subscriptions, including viewing and renaming all
of the subscriptions for your organization.

.. _view:

Viewing subscriptions
---------------------

To view your subscriptions, complete the following steps:

#. Sign in to the |acquia-product:ui| as an *Owner* or *Administrator*,
   and then click **Manage** in the top menu.
#. In your organization's information card, click **Manage**.
#. On the **Organizations** page, click **Subscriptions** in the left
   menu.

   .. note::

      You will not see the **Subscriptions** option in the left menu unless
      you are an *Owner* or *Administrator* for the selected organization.

|Viewing Subscriptions|

The |acquia-product:ui| displays all of the |acquia-product:ac|
subscriptions associated with the organization. For each subscription,
|acquia-product:ac| displays the following:

-  Subscription name
-  Type (for example, |acquia-product:ace| or |acquia-product:acfs|)
-  Expiration date

To view additional details about a subscription, click its **View**
link. The subscription overview page additionally displays the following
items:

-  Subscription start date
-  Number of applications used and available in the subscription
-  Number of advisory hours used and available for the subscription

.. _rename:

Renaming a subscription
-----------------------

On the **Manage > Subscriptions** page, you can rename a subscription.
To do so, complete the following steps:

#. On the line that lists the subscription you want to rename, click
   **Rename**.
#. In the **Subscription name** field, enter the new name for the
   subscription.
#. Click **Rename**.

.. _transfer:

Transferring a subscription to another organization
---------------------------------------------------

If you need to move one or more subscriptions to another organization,
`contact Acquia Support </support#contact>`__ to receive assistance with
the process.

.. _region:

Changing a subscription's region
--------------------------------

After you create an |acquia-product:ac| subscription, you cannot change
the region in which it was created to a different value.

Instead, create a new subscription in the different region, export your
website from |acquia-product:ac|, and then import the website into the
new subscription.

.. _ra:

Remote Administration
---------------------

Some subscriptions may use Acquia's `Remote Administration
services </ra>`__. Subscriptions with this service will have an **RA**
link in the left menu, and clicking this link enables you to `configure
the preferences </ra/preferences>`__ for your Remote Administration
service.

.. |Viewing Subscriptions| image:: https://cdn4.webdamdb.com/1280_IABtZCJAHfd8.png?1526475817
   :width: 750px
   :height: 295px
