.. include:: /common/global.rst

Starting with an existing local website
=======================================

This page describes how to create a new Drupal website, starting from an
existing website on your local computer.

If you already have a Drupal website you've been working on locally, you
can import it into |acquia-product:add|. You can also follow this
procedure:

-  If you want to start with a Drupal distribution that isn't included
   with |acquia-product:add|, then you need to first download the Drupal
   distribution to your computer.
-  If you have an existing Drupal website that's hosted elsewhere than
   on |acquia-product:ac|, then you need to first export your Drupal
   website to your computer.

If you are starting from a Drupal distribution or a Drupal website
archive exported from another hosting environment, extract the website
archive before you import the website into |acquia-product:add|.

Importing an existing website
-----------------------------

To import an existing website into |acquia-product:add|, complete the
following steps:

#. Based on the options that |acquia-product:add| is currently providing
   to you, start the import process:

   -  *Welcome to Acquia Dev Desktop dialog box* (as described in
      `Getting started </dev-desktop/start>`__) - Click **Start with an
      existing Drupal site located on my computer**.
   -  *Default |acquia-product:add| interface* - Click the **+** button,
      and then click **Import local Drupal site**.

#. In the **Import local Drupal site** dialog box, enter the following
   information:

   -  **Local codebase folder** - Enter the local folder that contains
      your Drupal codebase (your local website's docroot).
   -  **Local site name** - Enter a name for your local website. The
      local website URL will be based on this name, so it can use only
      characters that are valid for a URL.
   -  **Use PHP** - Select a PHP version to use. Although you can accept
      the default PHP version, be aware that some Drupal distributions
      or modules may require specific PHP versions.
   -  **Database** - Specify how to set up the database for your Drupal
      website. If you're starting from scratch, select **Create a new
      database**. If you have content in your existing website's
      database that you want to import into |acquia-product:add|, import
      the existing website's database, as described in `Importing a
      database </dev-desktop/start/db>`__.
   -  **New database name** - Enter a name for your Drupal website's
      database. In most cases, you can accept the default value, which
      will match the local website name that you chose.

#. Click **OK**.

|Importing a local website|

.. |Importing a local website| image:: https://cdn4.webdamdb.com/1280_cA6mKxADwtl8.jpg?1526475783
   :width: 590px
   :height: 390px
