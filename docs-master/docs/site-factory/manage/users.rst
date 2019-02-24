.. include:: /common/global.rst

Managing Acquia Cloud Site Factory accounts
===========================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/users/*

.. note::  The information on this page describes how to manage accounts on |acquia-product:edg|.
   
   If you want to remove your account from an Acquia subscription or acquia.com, `contact Acquia Support </support#contact>`__ and request that they delete your account.

Regardless of who you are or what permissions you require,
|acquia-product:edg| uses a centralized, OpenID-based system to manage
user accounts. For example, administrators can use this centralized
account registry to access the Factory interface for managing websites,
while site visitors can use the registry to view content on an
|acquia-product:edg|-hosted website.

.. container:: message-status

   |Learning Services logo|\ For additional information, visit |aalink|_ (sign-in required) for the |setup|_ video tutorial.

.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px

.. |aalink| replace:: \ |acquia-product:aa|\ 
.. _aalink: https://customers.acquiacademy.com

.. |setup| replace:: Setting Up  \ |acquia-product:edg|\ 
.. _setup: https://customers.acquiacademy.com/catalog/info/id:220


Editing your user profile
-------------------------

|acquia-product:edg| stores the information you provide about yourself
(such as your name, email address, and user avatar) in your **user
profile**.

To edit your user profile:

#. `Sign in <site-factory/manage/login>`__ to the |acquia-product:sfi|.
#. In the |acquia-product:edg| admin menu, click the **[username]** link, where **[username]** is your account name.

   |Edit profile|

#. Click the **Edit** tab.
#. Click **Save** after you complete your changes to your user profile.


Account levels
--------------

Because both the |acquia-product:sfi| and all of the websites that it
manages use the same OpenID accounts, you can use an account created on
one |acquia-product:edg| website to sign in to your other
|acquia-product:edg| websites and even to the |acquia-product:sfi|
itself (assuming that you've been assigned a |acquia-product:sfi|
`administrative role </site-factory/users/admin>`__).

You can view and manage your |acquia-product:edg| accounts at either the
|acquia-product:sfi| level or in each individual website.

|acquia-product:sfi|
~~~~~~~~~~~~~~~~~~~~

After you sign in to the |acquia-product:sfi|, you can view all accounts
by clicking **Users** in the admin menu.

|Users page overview|

You can use the options on this page to complete user management tasks,
including creating new accounts or editing existing accounts to add
|acquia-product:sfi| roles that provide |acquia-product:edg|
administrator access.

For more information about the different types of |acquia-product:edg|
administrative access, see |SFIroles|_.

.. |SFIroles| replace:: \ |acquia-product:sfi|\  roles 
.. _SFIroles: /site-factory/users/admin

Site owners
~~~~~~~~~~~

Each |acquia-product:edg|-hosted website has a single user who is the
*site owner*. Website ownership can be |restrictto|_.

.. |restrictto| replace:: restricted to individuals with the *platform admin* role
.. _restrictto: /site-factory/users/site-owner#restrict

If you want to delete the user account of a website's site owner, first
`transfer ownership of the
website </site-factory/users/site-owner#transfer>`__ to a different
user. Failing to do this will cause the website to have no site owner,
and only the site owner can transfer ownership or delete a website.

|acquia-product:edg|-hosted websites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just like any other Drupal website, |acquia-product:edg|-hosted websites
provide you with many different user management actions (including
adding new users, removing user accounts, and controlling access to
different parts of the website) and are controlled separately in each of
your |acquia-product:edg|-hosted websites.

.. |Edit profile| image:: https://cdn2.webdamdb.com/1280_YDWZ1zhqyBH6.png?-62169955200
   :width: 750px
   :height: 277px
.. |Users page overview| image:: https://cdn3.webdamdb.com/1280_solUXqFmvpK4.png?-62169955200
   :width: 750px
   :height: 450px
