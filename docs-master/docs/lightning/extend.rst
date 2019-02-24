.. include:: /common/global.rst

Extending |acquia-product:ld|
=============================

.. note::  The information on this page applies only to |acquia-product:ld| 
   version 8.x-2.04 or any previous versions.

If you are using |acquia-product:ld| version 8.x-2.05 or greater, you
must convert any previously created extend files to |acquia-product:ld|
`subprofiles </lightning/subprofile>`__.

Business requirements dictate the need to provide a specific, unique
out-of-the-box experience. With Drupal, this need is often filled by
profiles. Distributions such as |acquia-product:ld| include their own
profiles, which usually preclude the use of other, personalized
profiles.

However, |acquia-product:ld| provides a way for website builders to
extend the out-of-the-box experience by using configuration information
contained in the ``lightning.extend.yml`` file. This extension
capability enables website builders to change the theme, define new
content types or other entity bundles, and enable Feature modules by
enabling builders to override, delete, and add to the default
|acquia-product:ld| configuration.

``lightning.extend.yml`` is provided in the codebase:

.. code-block:: yaml

   # Defines additional tasks for Lightning to perform during and after site
   # installation.

   # List of additional modules to enable after Lightning is installed.
   modules: { }

   # A system path to redirect to once installation is complete.
   redirect:
   path: ''
   # Optional query string parameters.
   query: { }
   

``lightning.extend.yml`` enables website builders to define:

-  A list of additional modules to enable after |acquia-product:ld| has
   finished installation.
-  A path that users should be redirected to after installation of
   |acquia-product:ld| and the additional modules is complete.

If you need to customize your |acquia-product:ld| build, you can
`download the Acme Lightning Extend <https://github.com/balsama/acme-lightning-extend>`__ example.
This example will:

-  Enable the Acme Custom module, which sets a new theme, and deletes
   the default content types that come with |acquia-product:ld|.
-  Enable the `Features <https://www.drupal.org/project/features>`__
   module and activate the following Features:

   -  **Lightning Settings**: Disables automatic creation of roles in
      |acquia-product:ld|.
   -  **Product**: Creates a **Product** content type and associated
      taxonomy.
   -  **Theme Settings**: Defines some settings for the Acme theme.

-  Redirect the user to a custom messaging page.
