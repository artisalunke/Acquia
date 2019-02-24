.. include:: /common/global.rst

Specifying login authentication mode
====================================

.. container:: message-status

   Applies only to Drupal 7-based websites hosted on |acquia-product:edg|

Depending on how you configure the |acquia-product:edg| websites that
you administer, you can allow all of your users sign-in access to all of
your websites or you can require that each website has its own list of
authorized users. |acquia-product:edg| supports two methods for tracking
and authenticating users who access the |acquia-product:sfi| and
|acquia-product:edg|-hosted websites:

-  **OpenID mode** - All accounts are based on
   `OpenID <http://openid.net/>`__ accounts. Any OpenID-enabled account
   associated with |acquia-product:edg| is an authenticated user. This
   is the default mode.
-  **Hybrid mode** - While users with administrative OpenID accounts can
   log in to the website, the website can create its own local private
   accounts, and site administrative permissions are based on these
   private accounts. Hybrid mode is incompatible with single sign-on
   (SSO) or any process that redirects a user to an external sign in.

To change the mode that |acquia-product:edg| uses for your websites,
`contact Acquia Support </support#contact>`__.


Account registration settings for Hybrid mode
---------------------------------------------

For Hybrid mode to work properly, account registration settings must be
properly configured by following these steps:

#. Sign in as an administrator to the Drupal website that you want to
   change.
#. In the admin menu, click **Configuration**.
#. In the **People** section, click **Account Settings**.
#. In the **Registration and cancellation** section, in the **Who can
   register accounts?** list, click *Visitors*.
#. Click **Save Configuration**.


Important details about Hybrid mode
-----------------------------------

You should not implement hybrid mode without carefully considering the
implications that making the change will have on your website's users.


Switching back to OpenID breaks accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you change the login mode to Hybrid and then change back to OpenID,
any local accounts created on your websites will no longer work, even if
you change back to the Hybrid mode.


Administrative access in Hybrid mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Hybrid mode, OpenID users only have access to the website, and do not
have administrative access. You must manually add administrative
permissions and roles to OpenID accounts that require administrative
access.


First-time logins and OpenID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Hybrid mode, OpenID users must use the management interface when
signing in to websites for the first time for the website to create a
local account based on the OpenID account. After creating the local
account, OpenID accounts can then either sign in directly to the website
or use the management interface.

.. note::  

   If you create a local account for a user before the same user signs in
   with their OpenID account, the website merges the user's local account
   with the OpenID account.
