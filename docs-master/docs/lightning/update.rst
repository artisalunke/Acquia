.. include:: /common/global.rst

Updating Lightning
==================

|acquia-product:ld| has a two-pronged update process. When initially
installed, |acquia-product:ld| includes a useful, near-complete default
configuration for your website, but after installation, all of that
configuration is owned by your website. Since your website owns the
configuration from that point on, |acquia-product:ld| cannot safely
modify your website without potentially changing its behavior, or, in a
worst-case scenario, causing data loss.

As it evolves, the |acquia-product:ld| default configuration can change,
and in certain limited cases, |acquia-product:ld| will attempt to safely
update configuration that it depends on. This configuration will usually
be locked to prevent you from modifying it. Otherwise,
|acquia-product:ld| will not modify your configuration, respecting the
fact that your website owns it.

This set of behaviors, then, requires that you use the following process
to update your |acquia-product:ld| installation.

.. note::

  *Critical security updates, in general, can be accomplished without waiting for the Lightning distribution update.* However, Acquia will attempt to update the distribution as quickly as possible after any security updates.

Before you begin
----------------

Depending on the modules or libraries included with an
|acquia-product:ld| release, specific versions of |acquia-product:ld|
may require additional configuration or upgrade steps. Before starting a
version upgrade, to determine if your version requires these needed
steps, see the `Configuration
updates <https://github.com/acquia/lightning/blob/8.x-2.x/UPDATE.md>`__
section of the |acquia-product:ld| update instructions on GitHub.

You must follow any additional update instructions specific to your
version of |acquia-product:ld| when upgrading your files and database.

Procedure
---------

After you ensure that you have addressed any `additional
requirements <#version>`__, if you previously used our `Composer-based
project template <https://github.com/acquia/lightning-project>`__ to
install |acquia-product:ld|, complete the following steps to update your
codebase's installed version of |acquia-product:ld|:

#. From a command prompt window, navigate to your your project: ``cd [/path/to/YOUR_PROJECT]``
#. Execute ``composer update`` to download updates to modules and libraries
#. Perform any needed database updates by using one of the following methods:

   -  *Drupal user interface* - Visit ``http://mysite.com/update.php`` (where ``mysite.com`` is the URL for your website) and follow the on-screen instructions.
   -  *Drush* - Update your database manually from a command prompt window by using the following steps:

      #. Perform any needed database updates by executing the following command:

         .. code-block:: none

         drush updatedb --yes

      #. Clear and rebuild caches by executing the following command:

         .. code-block:: none
         
         drush cache-rebuild

#. Perform any needed configuration |acquia-product:ld| updates by using
   the instructions from one of the following resources:

   -  The manual update instructions listed in the |acquia-product:ld| release notes
   -  The ``UPDATE.md`` file included with |acquia-product:ld|
