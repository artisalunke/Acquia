.. include:: /common/global.rst

Importing an application with the |acquia-product:ui|
=====================================================

Importing a site archive

-  `Intro </acquia-cloud/create/import/archive>`__
-  `Prepare </acquia-cloud/create/import/prepare>`__
-  `Create </acquia-cloud/create/import/archive-create>`__
-  Import

After you `create a site archive
file </acquia-cloud/create/import/archive-create>`__, you are ready to
import your site archive. The site archive file must be less than 100MB
in size and be available at a publicly accessible URL. If the site
archive file is larger than that, use one of the following methods:

-  `Import using Drush </acquia-cloud/create/import/drush>`__
-  `Import manually </acquia-cloud/create/import/manual>`__

Use the following steps to import an existing Drupal site archive into
an |acquia-product:ac| environment using the |acquia-product:ui|.

To import your Drupal application (site archive size less than 100MB)
using the |acquia-product:ui|:

#. Sign in to the `|acquia-product:ui| <https://cloud.acquia.com/>`__,
   select your application, and then select the Development environment.

   If you do not want to overwrite the contents of any of your current
   applications with an imported application, you can `create a new
   application </acquia-cloud/create>`__ in your |acquia-product:ac|
   subscription.

#. In the |acquia-product:ui| Development environment page, click
   **Install Drupal**.

   |Click Install Drupal|

   The **Install Distribution** page opens.

#. Click **Import from URL**.
#. Enter the URL of the Drush site archive you want to import and click
   **Import**.

.. _after:

After you import
----------------

Importing an application takes a few minutes. The |acquia-product:ui|
reports when the import task is complete. To ensure that
|acquia-product:ac| imported your application correctly, sign in to the
|acquia-product:ui|, go to the Development environment page, and then
click the URL link.

|URL link to visit your new application|

After |acquia-product:ac| imports your codebase, files and database, it
adds the ``include`` statement to the application's ``settings.php``
file so that your code can access the correct database.

To start developing your application on |acquia-product:ac|, `check out
a local copy of the repository </acquia-cloud/develop/checkout>`__ using
Git.

.. |Click Install Drupal| image:: https://cdn3.webdamdb.com/1280_Aj9mdUANbkh2.png?1527195748
   :width: 1260px
   :height: 438px
.. |URL link to visit your new application| image:: https://cdn4.webdamdb.com/1280_cTm4j5LjMi01.png?1527195742
   :width: 1218px
   :height: 271px
