.. include:: /common/global.rst

How to install a Drupal 7 module
================================

Drupal allows you to add `modules </articles/module-definition>`__ to
your codebase to provide additional functionality by installing modules
that have been contributed to the `module archive at
Drupal.org <https://www.drupal.org/project/modules>`__.

Procedure
---------

After selecting an appropriate new module, you must install and enable
the module on your website in order to use it. The two primary methods
are:

-  `Drupal's user interface <#installing-modules-using-the-user-interface>`__
-  `Command-line installation with Drush <#installing-modules-using-drush>`__

.. admonition:: Note for |acquia-product:ac| subscribers

   For information about uploading the module's files to your codebase, see `Using your code repository </acquia-cloud/develop/repository>`__.

Installing modules using the user interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following procedure to install a module from the Drupal
interface:

#. Download and extract the module that you want to use your website's
   ``docroot/sites/all/modules/`` directory. For more information about
   the ``docroot`` directory, see the `Docroot
   definition </articles/docroot-definition>`__ article.
#. Sign in to your website as an administrator.
#. View the Modules page by using one of the following methods:

   -  In the administrative menu, click **Modules**.
   -  In your browser's address bar, go to
      ``http://[your_site]/admin/modules`` (where ``[your_site]`` is
      your website's URL).

#. In the module list, find the module that you installed, and then
   select its check box.
#. Scroll to the bottom of the webpage, and then click **Save
   configuration**.

Installing modules using Drush
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For more advanced users who are familiar with the command line, you can
also install and enable modules using a
`Drush <https://www.drupal.org/project/drush>`__ command. This process
requires that you connect to your server by using SSH. For more
information, see `Managing applications using the command
line </acquia-cloud/ssh>`__. To install a module using Drush, complete
the following steps:

#. Open a command prompt to access your website's code.
#. Using the ``cd`` command, navigate to your website's `docroot </articles/docroot-definition>`__.
#. Run the following command:

   .. code-block:: none
   
        drush en module_name

   where ``module_name`` is the project name from Drupal.org. (For
   example, the project name for the `Acquia
   Connector <https://www.drupal.org/project/acquia_connector>`__ module
   is *acquia_connector*, from
   ``https://www.drupal.org/project/acquia_connector``.)

   .. note::

        You can append ``-y`` to the preceding command to accept the confirmation questions that Drush displays.

Next steps
----------

After you have installed a module on your website, you will probably
need to configure the module's settings or make changes to website user
permissions. For additional information regarding these next steps, be
sure to review the documentation provided either with your module or on
your module's Drupal.org project page.
