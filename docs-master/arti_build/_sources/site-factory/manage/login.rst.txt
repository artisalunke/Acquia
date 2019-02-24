.. include:: /common/global.rst

Signing in to |acquia-product:edg|
==================================

To view all of your websites on your Production or Stage environments,
or to perform website maintenance tasks, you must first sign in to your
|acquia-product:sfi|.

If you do not know the domain name for your |acquia-product:sfi|,
complete the following steps:

#. In your browser, `sign in <https://cloud.acquia.com>`__ to the |acquia-product:ac| interface.
#. To select your |acquia-product:edg| application, click its name. If
   you have many applications, you can also use the **Filter
   Applications** field to limit which applications are displayed.
#. Click the name of the environment for which you want to sign in.

   |Select an environment|

#. Click **Site Factory Management Console** to display your
   administrative interface.
#. Enter your |acquia-product:sfi| username and password, and then click
   **Log in**.

.. admonition::  Note for non-production environments

   When |acquia-product:edg| copies websites as part of the staging
   process, by default the websites are *scrubbed* of personal data,
   including the email addresses of user accounts, and you may not be able
   to use your usual email address to sign in to the |acquia-product:sfi|.

   You can either attempt to sign in with your scrubbed username (which by
   default replaces your email address username with ``userXXXXX``, where
   ``XXXXX`` is your user account number), or you can use the procedures
   described in `Protecting Site Factory accounts during
   staging </site-factory/workflow/scrub#protectsf>`__ or `Protecting
   hosted website accounts during
   staging </site-factory/workflow/scrub#protecthosted>`__ to prevent your
   email address from being scrubbed.

.. |Select an environment| image:: https://cdn3.webdamdb.com/1280_c5jY9SCQH03.png?1526475665
   :width: 694px
   :height: 303px
