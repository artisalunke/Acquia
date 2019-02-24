.. include:: /common/global.rst

How to install a Drupal 8 module
================================

You can add new functionality to Drupal by adding
`modules </articles/module-definition>`__ from the `module archive at
Drupal.org <https://www.drupal.org/project/modules>`__ to your codebase.

.. container:: message-status

   |Remote Administration logo| If you're a Remote Administration subscriber who has purchased `premium Remote Administration </ra/scope>`__ services, you can `contact Acquia Support </support#contact>`__ to add and enable modules for you.

Adding modules to your codebase
-------------------------------

To add modules to your codebase, use one of the following methods:

-  `Adding a module using Composer <#adding-a-module-using-composer>`__ (recommended)
-  `Adding a module using Drush <#adding-a-module-using-drush>`__

After adding the module to your codebase, `enable it <#enabling-a-module-in-your-codebase>`__ using
the Drupal interface or with a Drush command.

Adding a module using Composer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a new module to your codebase using Composer, complete the
following steps:

#. Ensure that you have Composer `installed locally in your development
   environment </resource/composer>`__.
#. Open a command prompt window to access your website's code.
#. Using the ``cd`` command, navigate to the directory containing your
   website's ``composer.json`` file, which is typically the directory
   above your website's
   `docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__.
#. Run the following command:

   .. code-block:: none
   
        composer require drupal/[module_name]

   where ``[module_name]`` is the project name from Drupal.org. This
   command will download the module to the appropriate place in your
   code repository, and add the following instructions to the
   ``require`` statement in your ``composer.json`` file, again replacing
   ``[module_name]`` with the project name from Drupal.org:

   .. code-block:: none
   
        "require": {
        "drupal/[module_name]": "1.x-dev"
        },

#. Commit the changes to your branch and push the changes to your code
   repository. For information about deploying your code on
   |acquia-product:ac|, see `Code workflows on
   Acquia Cloud </acquia-cloud/develop/code/environments>`__.

After you have added a module, you should `enable <#enabling-a-module-in-your-codebase>`__ it.

.. note::

   To learn more about using Composer to manage dependencies, see `Using Composer to manage Drupal site dependencies <https://www.drupal.org/docs/develop/using-composer/using-composer-to-manage-drupal-site-dependencies>`__ on Drupal.org.

   For procedures that you can use to set up and use Composer locally with your |acquia-product:ac|-hosted websites, see `Using Composer with Drupal 8 sites </resource/composer>`__. The Drupal community also offers support for using Composer `to install Drupal packages <https://www.drupal.org/docs/develop/using-composer>`__ on Drupal.org.

Adding a module using Drush
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases, you can also install and enable modules using a
`Drush <https://www.drupal.org/project/drush>`__ command, though
Composer is the preferred method for Drupal 8. To install and enable a
module using Drush, complete the following steps:

#. Open a command prompt window to access your website's code.
#. Using the ``cd`` command, navigate to your website's
   `docroot </articles/docroot-definition>`__.
#. To download the module, run the following command:

   .. code-block:: none
   
        drush dl [module_name]

   where ``[module_name]`` is the project name from Drupal.org. For
   example, the project name for the `Acquia
   Connector <https://www.drupal.org/project/acquia_connector>`__ module
   is *acquia_connector*, from
   ``https://www.drupal.org/project/acquia_connector``

   .. note::

        You can append ``-y`` to the preceding command to accept the confirmation questions that Drush displays.

#. Commit the change to your branch and push the change to your code
   repository.

After you have added a module, you should `enable <#enabling-a-module-in-your-codebase>`__ it.

Enabling a module in your codebase
----------------------------------

After `adding a module to your codebase <#adding-modules-to-your-codebase>`__, you can enable it by
either using Drush or by using the Drupal user interface.

Enabling a module using Drush
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable the module from the command line, perform the following steps:

#. Open a command prompt window to access your website's code.
#. Using the ``cd`` command, navigate to your website's
   `docroot </articles/docroot-definition>`__.
#. To download the module, run the following command:

   .. code-block:: none
   
        drush en [module_name]

   where ``[module_name]`` is the project name from Drupal.org.

   .. note::

        You can append ``-y`` to the preceding command to accept the confirmation questions that Drush displays.

After enabling your desired module, you should review `next steps <#next-steps>`__ to complete the module's configuration.

Enabling a module using the Drupal user interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable a module from the Drupal user interface, complete the following steps:

#. Sign in to your website as an administrator.
#. Go to the Modules page by using one of the following methods:

   -  In the administrative menu, click **Extend**.
   -  In your browser's address bar, go to ``http://[your_site]/admin/modules`` (where ``[your_site]`` is your website's URL).

#. In the module list, find the module that you want to enable, and then select its check box.
#. Scroll to the bottom of the webpage, and then click **Install**.

After enabling your desired module, you should review `next steps <#next-steps>`__ to complete the module's configuration.

Next steps
----------

After you have added and enabled a module locally, you will probably need to configure the module's settings or make changes to website user permissions. For additional information regarding these next steps, be sure to review the documentation provided either with your module or on your module's Drupal.org project page.

For information about deploying your code on |acquia-product:ac|, see `Code workflows on Acquia Cloud </acquia-cloud/develop/code/environments>`__.

.. |Remote Administration logo| image:: https://cdn4.webdamdb.com/1280_ECrQZjRVhC06.png?-62169955200
   :class: no-sb float-left logo-sm-lift ra-ad
   :width: 36px
