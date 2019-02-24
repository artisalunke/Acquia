.. include:: /common/global.rst

Installing |acquia-product:leb| for Drupal 8
============================================

.. container:: internal-navigation

   **Installing Experience Builder**

   * :doc:`Install </lift/exp-builder/install>`
   * :doc:`Access </lift/exp-builder/access>`
   * :doc:`Content </lift/exp-builder/content-hub>`


Use the following instructions to install and configure the
|acquia-product:leb| client module on your Drupal 8 website.

Requirements
------------

As you are preparing to use |acquia-product:leb| with your website, be
sure to plan for the following requirements:

+-----------------------------------+-----------------------------------+
| Component                         | Requirement                       |
+===================================+===================================+
| **Drupal version**                | Drupal 8                          |
+-----------------------------------+-----------------------------------+
| **PHP Dependency manager**        | Composer (installation            |
|                                   | instructions_                     |
+-----------------------------------+-----------------------------------+
| **Keys**                          | After you purchase                |
|                                   | |acquia-product:cha|, Acquia will |
|                                   | email you a set of keys which are |
|                                   | required to connect to the        |
|                                   | |acquia-product:leb| service.     |
+-----------------------------------+-----------------------------------+

.. _instructions: /resource/composer

Installing |acquia-product:leb|
-------------------------------

.. |docrootdir| replace:: ``docroot`` directory
.. _docrootdir: /articles/docroot-definition

Use the following steps to install the |acquia-product:leb| client on
your website:

#. Open a command prompt window, and then navigate to the directory that
   contains your main ``composer.json`` file.

   .. admonition::  Note for |acquia-product:ac| users

      The main ``composer.json`` file is located in your website's |docrootdir|_.

#. Run the following commands:

   .. code-block:: none

      composer config repositories.drupal composer https://packages.drupal.org/8 composer update composer require drupal/acquia_lift:~3.0 cd .. && git add --all && git commit -a -m 'Adding Experience Builder modules' && git push origin master

#. `Deploy the updated master </acquia-cloud/develop/code/environments>`__
   to your website on |acquia-product:ac|.
#. Sign in to your website as an administrator, and then click **Extend**
   in the admin menu.
#. Select the check boxes for the **|acquia-product:cha|** module.
#. Click **Install**.
#. In the admin menu, click **Configuration**, and then click the 
   **Acquia Lift** link.
#. Use the following steps to obtain and enter the information you need for
   the **|acquia-product:cha| Credential** section.

   a. In a new tab, `sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
      interface using an account with
      administrative privileges, and then click the **Admin** tab.
   #. Click the **Manage Customers** link.
   #. Click the customer name for whom you are installing
      |acquia-product:leb|.
   #. Obtain the following values from the webpage:

      -  **Account ID**
      -  **Site ID**
      -  **Assets URL**
      -  **Decision API URL**
      -  **Authentication URL**

      Important

      Each website must have a unique Site ID. This includes development
      and testing environments. For more information, see `Per-environment
      configuration settings <#env>`__.

#. Return to your website, and then update the values based on those
   from the |acquia-product:lpm| interface.
#. Click **Save configuration**.

Next, you must configure your `per-environment settings <#per-environment-configuration-settings>`__ in
your website's ``settings.php`` file.

Per-environment configuration settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unless you specifically take action, data collected by testing
environments can *contaminate* data collected on your production
environment.

To avoid this issue, `download this
code <https://gist.github.com/acquialibrary/3bb1907308b23cffc4cf239d99c896a9>`__
and add it to your website's ``settings.php`` file. Modify the provided
code to set the variables associated with |acquia-product:cha| and its
components (including ``$config['acquia_lift.settings']`` and
``$config['acquia_contenthub.admin_settings']``) for different values
depending on the environment in which they exist.

After you have ensured that all required modules are installed and
available for use, your production website has the ability to connect to
the |acquia-product:leb| service, and your non-production website should
not interfere with data collection for your production website.

`Continue to accessing the Experience Builder sidebar > </lift/exp-builder/access>`__
---------------------------------------------------------------------------------------
