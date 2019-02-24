.. include:: /common/global.rst

Copying (cloning) an existing site in Acquia Dev Desktop
========================================================

You can easily make a copy of one of your existing websites in
|acquia-product:add|. To do so, complete the following steps:

#. In the main |acquia-product:add| interface, click the website that
   you want to copy.
#. Click **More**, and then click **Clone local codebase**.
#. Click **OK**.

.. _settingsphp:

Changes to settings.php
-----------------------

When you make a local copy of an |acquia-product:ac| website,
|acquia-product:add| makes a modification to the website's
``settings.php`` file to point to a folder that contains
|acquia-product:add|-specific settings files. This modification ensures
that your local website connects to your local database, while your
|acquia-product:ac| website continues to connect to the
|acquia-product:ac| database.

Be sure to include this change when you push your local code to
|acquia-product:ac|, since it is needed for |acquia-product:add| to run
and has no effect on either |acquia-product:ac| websites or other
developers using those websites.
