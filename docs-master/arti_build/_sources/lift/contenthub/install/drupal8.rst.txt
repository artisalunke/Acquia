.. include:: /common/global.rst

Installing |acquia-product:ch| for Drupal 8
===========================================

.. container:: internal-navigation

   **Installing Content Hub**

   * Install
   * :doc:`Configure </lift/contenthub/install/configure>`

Use the following instructions to install the |acquia-product:ch| client
modules on your Drupal 8 website.

Requirements
------------

As you prepare to use |acquia-product:ch| with your website, be sure to
plan for the following requirements:

.. list-table::
   :widths: 20 80
   :header-rows: 1 

   * - Application
     - Component
   * - **Drupal version**
     - Drupal 8.2 or greater
   * - **PHP Dependency manager**
     - Composer (`installation instructions </resource/composer>`__)
   * - **Keys**
     - After you purchase |acquia-product:ch|, Acquia will email you a set of keys which are required to connect to the |acquia-product:ch| content repository.
   * - **Other**
     - |acquia-product:ch| assumes you are using `clean URLs </articles/drupal-paths-and-clean-urls>`__.

Installing |acquia-product:ch|
------------------------------

Use the following steps to install the |acquia-product:ch| client on
your website:

.. |usedd| replace:: using \ |acquia-product:add|\ 
.. _usedd: /dev-desktop/cloud/details

#. Clone the website repository locally (either `manually </acquia-cloud/develop/repository>`__ or by |usedd|_)
#. From a command prompt window, go to the directory that contains your main ``composer.json`` file.  
   
   .. admonition::  Note for |acquia-product:ac| users
     
      The main ``composer.json`` file is located in your website's `docroot </articles/docroot-definition>`__ directory.

#. Run the following commands:

   ``composer config repositories.drupal composer https://packages.drupal.org/8 composer require drupal/acquia_contenthub:~1.0``

#. Commit the changes to your codebase.
#. Sign in to your website as an administrator, and then click **Extend** in the admin menu.
#. Select the following check boxes in the **Acquia Content Hub** section:

   -  **Acquia Content Hub**
   -  **Acquia Content Hub Subscriber**

#. Click **Install**.
#. In the admin menu, click **Configuration**, and then click the **Acquia Content Hub** link (``http://[site_URL]]/admin/config/services/acquia-contenthub``).
#. Use the following steps to obtain and enter the information you need for the **Acquia Lift Credential** section.

   #. In a new tab, `sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm| interface using an account with administrative privileges, and then click the **Admin** tab.
   #. Click the **Manage Customers** link.
   #. Click the customer name with the |acquia-product:ch| settings that you want to inspect.
   #. In the **Content Hub Module** section, obtain the following values:

      -  **Acquia Content Hub Hostname**
      -  **API Key**
      -  **Secret Key**
      -  **Client Name**

      .. note::  If you uninstall and reinstall |acquia-product:ch| at any point, you will not be able to use the **Client Name** that you used during the previous configuration process. In that case, append a unique number to the **Client Name** that you used previously. For example, if you previously used ``LIFTSITE2``, enter ``LIFTSITE3``.
#. Return to your website, and then update the values based on those from the |acquia-product:lpm| interface.
#. Click **Save Configuration**.

Your website is now connected to the |acquia-product:ch| content
repository, and can begin to share content with your other connected
websites.

Upgrading |acquia-product:ch|
-----------------------------

You can use the following set of commands to update |acquia-product:ch|:

.. code-block:: none

   drush upc drupal  
   composer require drupal/acquia_contenthub:~1.0 
   drush cr

`Continue to configuring permissions and adding content > </content-hub/configure>`__
-------------------------------------------------------------------------------------
