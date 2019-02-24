.. include:: /common/global.rst

Protecting sites with HTTP authentication
=========================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/preferences/*

There are times when you want to control who can visit your website
while it is under development:

-  You want to block normal website visitors from viewing the website
   while developers continue to work on the website.
-  You want to block search engine crawlers or robots that don't respect
   your ``robots.txt`` file.

The |acquia-product:edg| HTTP authentication feature provides an extra
measure of protection to ensure that your hosted websites are not
exposed to unauthorized visitors, while still providing access to users
who are working on the websites.

To accomplish this, |acquia-product:edg| uses the Drupal
`Shield <https://www.drupal.org/project/shield>`__ module to require
website visitors to enter a username and password (which uses HTTP
authentication) to be able to view your website. The
|acquia-product:sfi| can enable the Shield module for your websites, and
therefore require HTTP authentication.

Requirements
------------

To use the HTTP authentication feature, you must add the
`Shield <https://www.drupal.org/project/shield>`__ module to your
|acquia-product:edg| codebase and install it on your
|acquia-product:edg| websites.

.. _procedure:

Enabling HTTP authentication requirements
-----------------------------------------

To require HTTP authentication for your |acquia-product:edg| websites,
complete the following steps:


.. |platform admin| replace:: *Platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin

#. Sign in to the |acquia-product:sfi| using an account with the
   |platform admin|_ role.
#. In the admin menu, click **Administration**, and then, under Site
   Factory management, click the **Require HTTP authentication** link.
#. Click the **Require HTTP authentication** check box, and then enter
   values in the following fields:

   -  **Default site guard message** - Displayed to website visitors in
      the HTTP authentication login dialog box
   -  **HTTP authentication user name** - User name required to access
      the protected websites
   -  **HTTP authentication password** - Password required to access the
      protected websites

   .. note::  

      All users who visit a website protected by HTTP authentication must
      enter the same user name and password in order to view the website.

#. Click **Save**.

Site collections and HTTP authentication
----------------------------------------

If a site collection has a custom domain name, the HTTP authentication
requirement applies to all of the websites in the site collection, other
than the primary website. If a site collection does not have a custom
domain name, the HTTP authentication requirement applies to all sites.

Maintenance mode comparison
---------------------------

As an alternative to using the Shield module to require HTTP
authentication, you could set your website to `maintenance
mode </site-factory/manage/maint-mode>`__ to block access to
non-authorized users. However, with that approach, only administrators
can sign in — lower-level content managers who are not administrators
cannot sign in to websites in maintenance mode.
