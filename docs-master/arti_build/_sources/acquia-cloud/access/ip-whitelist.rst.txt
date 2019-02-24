.. include:: /common/global.rst

Securing your application with IP address whitelisting
======================================================

As an optional security measure, you can configure an application so
that only specified IP addresses on a whitelist can access it in the
|acquia-product:ui|.

By default, users who have access to an application, by being a `member
of a team </acquia-cloud/teams>`__ assigned to an application, can sign
in to the |acquia-product:ui| and access the application from any IP
address. Their access is controlled using a user name and password, the
`roles and permissions </acquia-cloud/teams/roles>`__ assigned to them,
and optionally, `two-step
verification </acquia-cloud/access/two-step-verification>`__. For an
additional layer of security, you can prohibit users from signing in to
the the |acquia-product:ui| unless they do so from one of the IP
addresses you specify. This feature is called *IP address whitelisting*.
Note that IP address whitelisting affects only access to the
|acquia-product:ui|; it does not affect normal access to a website.

.. _enabling:

Enabling IP address whitelisting
--------------------------------

Only users who have the *Owner* or *Administrator* role for an
application's organization can enable or disable IP address whitelisting
for an application. To enable IP address whitelisting:

#. Sign in to the |acquia-product:ui| with the *Owner* or
   *Administrator* role and select the application you want to work
   with.
#. In the menu on the left side, click **Security**.
#. On the **Security** page, click **Edit** to open the **Edit security
   settings** page.

   |Editing security settings|

#. Under **IP restrictions**, select **Only allow whitelisted IPs**.
#. Enter an IP address that you want to allow to access your application
   through the |acquia-product:ui|. Click **Add another** to add
   additional IP addresses.
#. Click **Save**.

|Add an IP address to the whitelist|

If you need to whitelist Acquia’s IP addresses for your websites or
services, `contact Acquia Support </support#contact>`__ to obtain the
necessary IP address ranges.

Note

Acquia employees with the proper permissions (such as members of the
Acquia Support and Operations teams) will still be able to access your
Acquia applications.

.. |Editing security settings| image:: https://cdn2.webdamdb.com/1280_WLjRjRHWC721.png?1526475790
   :width: 1275px
   :height: 427px
.. |Add an IP address to the whitelist| image:: https://cdn3.webdamdb.com/1280_cPXQfWjpVCa6.png?1526475752
   :width: 1272px
   :height: 734px
