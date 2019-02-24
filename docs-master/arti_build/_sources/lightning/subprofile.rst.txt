.. include:: /common/global.rst

Lightning sub-profiles
======================

|acquia-product:ld| includes the ability to create sub-profiles that are
based on the default |acquia-product:ld| distribution profile. Making a
sub-profile allows you to customize the installation process to meet one
or more of your specific needs.

If any of the following are true, you should create a sub-profile of
|acquia-product:ld|:

-  You want to prevent some component or subcomponent of
   |acquia-product:ld| from being installed.
-  You want to enable additional modules, themes, or configuration
   during install.
-  You want to customize the look and feel of the installation process.
-  You want to build a distribution that offloads modules such as Media,
   Layout, and Workflow to |acquia-product:ld|.
-  You previously used ``lightning.extend.yml`` to accomplish any of the
   previous items.

Creating a sub-profile
----------------------

Select from the following three primary methods to create a
|acquia-product:ld| sub-profile:

-  `Generate a new sub-profile <#generating-a-new-lightning-sub-profile>`__
-  `Convert lightning.extend.yml into a sub-profile <#converting-lightning-extend-yml-to-a-sub-profile>`__
-  `Switch an existing site’s install profile from Lightning to a sub-profile <#switching-an-existing-sites-install-profile-from-lightning-to-a-sub-profile>`__

Generating a new Lightning sub-profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For simple use cases, such as wanting to exclude some
|acquia-product:ld| components or include a few of your own, you can use
the provided sub-profile generator.

.. note::

   The generator is also a good starting point for more complex sub-profiles.

Requirements
^^^^^^^^^^^^

To run the sub-profile generator, the following items are required for
your application:

-  `DrupalConsole <https://drupalconsole.com/>`__
-  |acquia-product:ld| version 2.0.4 and greater
-  An installed instance of |acquia-product:ld| or Drupal

Running the generator
^^^^^^^^^^^^^^^^^^^^^

After you have ensured that your application meets the previous
requirements, run the following command from your installation's
`docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__:

.. code-block:: none

   drupal lightning:subprofile

Converting ``lightning.extend.yml`` to a sub-profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have previously used the |acquia-product:ld| extend file
(``lightning.extend.yml``), you can also convert the file to a
sub-profile.

Requirements
^^^^^^^^^^^^

To run the conversion, the following items are required for your
application:

-  `DrupalConsole <https://drupalconsole.com/>`__
-  |acquia-product:ld| version 2.0.4 and greater
-  An installed instance of |acquia-product:ld| or Drupal

Running the conversion
^^^^^^^^^^^^^^^^^^^^^^

To convert the subfile, run the following command from your
installation's
`docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__:

.. code-block:: none

  ./vendor/bin/lightning-subprofile /path/to/your/extend/file/lightning.extend.yml

Switching an existing site’s install profile from Lightning to a sub-profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To do this, complete the following steps:

#. Edit the ``settings.php``.
#. In the file, add or update the ``install_profile``:

   .. code-block:: none

      $settings['install_profile'] = '[SUB-PROFILE_NAME]';

#. Run the following command to enable the profile:

   .. code-block:: none

      drush cset core.extension module.[SUB-PROFILE_NAME] 0

#. If you use CMI or have exported the ``core.extension.yml``, export
   the updated extension listing to file.

Comparing sub-profiles and the ``lightning.extend.yml`` file
------------------------------------------------------------

Versions of |acquia-product:ld| prior to 8.x-2.05 included the
``lightning.extend.yml`` file, and installed modules in the following
order:

-  core modules
-  |acquia-product:ld| modules
-  extend modules

Extend modules were installed in the order that they were listed in the
extend file.

As of version 2.05, |acquia-product:ld| defers to the core install
system to determine when modules get installed. With this change, users
cannot rely on all of the modules in |acquia-product:ld| being installed
by the time your additional dependencies are installed. By design,
optional configurations are not installed until the end of the
installation process. Any attempt to modify optional configurations
should happen with ``hook_ENTITY_presave`` rather than ``hook_install``
or similar.

If this causes problems during your installation, one resolution method
is to remove the dependencies from your ``subprofile.info.yml`` file,
and then move them into an install hook in your sub-profile’s install
file. For example:

.. code-block:: php

    $modules = [
        'mymodule',
        'foo',
        'bar',
        // ...
    ];
    foreach ($modules as $module) {
        \Drupal::service('module_installer')->install([$module]);
    }
