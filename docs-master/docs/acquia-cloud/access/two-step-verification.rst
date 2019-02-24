.. include:: /common/global.rst

Setting up two-step verification
================================

You can enable two-step verification (two-factor authorization) to
control access to applications through the |acquia-product:ui|. Two-step
verification is more secure than password authentication alone. With
two-step verification enabled, a user signing in to the
|acquia-product:ui| must supply not just a user email address and
password, but also a code sent to a trusted device, using either an
authentication application, such as Google Authenticator or Authy, or an
SMS text message.

This page describes how to set up two-step verification for all of an
application's users with the |acquia-product:ui|. For information about
how to sign in with two-step verification, see `Using two-step
verification with your Acquia user
account </acquia-cloud/access/signin>`__.

.. _enable:

Enabling two-step verification
------------------------------

To enable two-step verification:

#. Sign in to the |acquia-product:ui| with the *Owner* or
   *Administrator* role and select the application you want to work
   with.
#. In the menu on the left side, click **Security**.
#. On the **Security** page, click **Edit** to open the **Edit security
   settings** page.

   |Editing security settings|

#. Under **Two-step verification**, select **Enabled**.
#. Click **Save**.

.. |Editing security settings| image:: https://cdn4.webdamdb.com/1280_WLjRjRHWC721.png?1526475790
   :width: 1275px
   :height: 427px
