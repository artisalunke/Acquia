.. include:: /common/global.rst

Installing |acquia-product:ch| for Drupal 7
===========================================

.. container:: internal-navigation

   **Installing Content Hub**

   * Install
   * :doc:`Configure </lift/contenthub/install/configure>`
   
Use the following instructions to install the |acquia-product:ch| client
modules on your Drupal 7 website.

.. note::  

   The |acquia-product:ch| installation process creates default rules, which you should not modify or delete.

Requirements
------------

As you prepare to use |acquia-product:ch| with your website, be sure to
plan for the following requirements:

.. list-table::
   :widths: 15 85
   :header-rows: 1 

   * - Component
     - Requirement
   * - **Drupal version**
     - Drupal 7
   * - **PHP version**
     - PHP 5.4 or greater
   * - **Modules**
     - 

       * `Date <https://www.drupal.org/project/date>`__ version 7.x-2.9 or greater
       * `Diff <https://www.drupal.org/project/diff>`__ version 7.x-3.2 or greater
       * `Entity API <https://www.drupal.org/project/entity>`__ version 7.x-1.7 or greater
       * `File Entity <https://www.drupal.org/project/file_entity>`__ version 7.x-2.0-beta2 or greater
       * `Media <https://www.drupal.org/project/media>`__ version 7.x-2.0-beta1 or greater
       * `Rules <https://www.drupal.org/project/rules>`__ version 7.x-2.9 or greater
       * `Universally Unique IDentifier <https://www.drupal.org/project/uuid>`__ version 7.x-1.0-beta1 or greater
       * `Views <https://www.drupal.org/project/views>`__ version 7.x-3.13 or greater

   * - **Keys**
     - After you purchase |acquia-product:ch|, Acquia will email you a set of keys which are required to connect to the |acquia-product:ch| content repository.
   * - **Other**
     - |acquia-product:ch| assumes you are using `clean URLs </articles/drupal-paths-and-clean-urls>`__.


Installation instructions
-------------------------

.. important::  We *strongly* recommend that you test your website with |acquia-product:ch| on a clone or copy of your Drupal website in a test server environment before you upgrade your production server.

Use the following steps to install |acquia-product:ch| on each of your
websites:

#. Download and extract the following modules into separate directories
   in your ``docroot/sites/all/modules/`` directory:

   -  `Date <https://www.drupal.org/project/date>`__
   -  `Diff <https://www.drupal.org/project/diff>`__
   -  `Entity API <https://www.drupal.org/project/entity>`__
   -  `File Entity <https://www.drupal.org/project/file_entity>`__
   -  `Media <https://www.drupal.org/project/media>`__
   -  `Rules <https://www.drupal.org/project/rules>`__
   -  `Universally Unique IDentifier <https://www.drupal.org/project/uuid>`__
   -  `Views <https://www.drupal.org/project/views>`__

#. Obtain the following modules from the most recent
   |acquia-product:ch| `release note </content-hub/release-notes>`__,
   and then extract them into separate directories in your
   ``docroot/sites/all/modules/`` directory:

   -  Content Hub
   -  |acquia-product:chc|

   .. note::  The |acquia-product:ch| module package includes the following features, which prevents the modules from being distributed on Drupal.org:

      -  All Composer dependencies, which assists in the effort of setting up a Composer workflow
      -  All required front-end libraries

#. Sign in to your website as an administrator, and then click
   **Modules** in the admin menu to view the Modules page.
#. Select the **Content Hub** check box.
#. Click **Save configuration** to save your module settings.
#. In the admin menu, click **Configuration**, and then click the
   **Content Hub Connector** link
   (``http://[site_URL]]/admin/config/services/content-hub``).
#. Click the **Connection** tab, and then complete the following fields:

   -  **API Key** - Acquia-provided value
   -  **Secret Key** - Acquia-provided value
   -  **Content Hub Connector Hostname** - The URL for the
      |acquia-product:ch| API
      Your Acquia technical contact will provide you with this URL.
      Ensure the URL does not include a trailing slash (``/``).
   -  | **Client Name** - A name for this website
      | This name is used internally in the |acquia-product:ch| and the
        |acquia-product:ch| API to identify the different member
        websites of your content network, and cannot be changed after
        you set its value. This name may contain a hyphen or underscore.

      .. note::  If you uninstall and reinstall |acquia-product:ch| at any point, you will not be able to use the **Client Name** that you used during the previous configuration process. In that case, append a unique number to the **Client Name** that you used previously. For example, if you previously used ``LIFTSITE2``, enter ``LIFTSITE3``.

#. Click **Save Configuration**.

Your website is now connected to the |acquia-product:ch| content
repository, and can begin to share content with your other connected
websites.

`Continue to configuring permissions and adding content > </content-hub/configure>`__
-------------------------------------------------------------------------------------
