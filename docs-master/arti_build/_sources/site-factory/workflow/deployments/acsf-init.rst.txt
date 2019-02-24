.. include:: /common/global.rst

Updating with the acsf-init command
===================================

The ``acsf-init`` Drush command prepares a custom Drupal distribution
for development and deployment on |acquia-product:edg|. The command
overwrites the contents of your website's ``sites/default/settings.php``
file, while also creating any necessary directories, identifying
database credentials, and copying files required by
|acquia-product:edg|.

Because ``acsf-init`` will overwrite your website's
``sites/default/settings.php`` file, be sure to move any customizations
in your ``settings.php`` file to another file or into a
`post-settings.php hook </site-factory/extend/hooks/settings-php>`__.
Failing to move your customizations could cause you to lose them when
your ``settings.php`` is overwritten.

The ``acsf-init`` command must be executed whenever the
`Acquia Cloud Site Factory Connector <https://www.drupal.org/project/acsf>`__
module is updated to a newer version.

.. note::  For more information about the different ``settings.php`` files in 
   your |acquia-product:edg| platform, see |Understanding|_.

.. |Understanding| replace:: Understanding ``settings.php`` file differences
.. _Understanding: /article/acquia-cloud-site-factory-understanding-settingsphp-file-differences


Executing ``acsf-init`` after a Connector module update
-------------------------------------------------------

Whenever the `Acquia Cloud Site Factory Connector <https://www.drupal.org/project/acsf>`__ module is updated to
a newer version, complete the following steps to update the module in
your Drupal distribution:

#. Download and extract the updated `|acquia-product:edg|
   Connector <https://www.drupal.org/project/acsf>`__ module from
   Drupal.org into your distribution.
#. Update your distribution by running the following Drush command:

   .. code-block:: none
   
      drush --include=path/to/acsf/acsf_init acsf-init

   .. note::  Because this command does not bootstrap a Drupal website, 
      you must run the command with a ``--include`` argument that points to
      ``acsf/acsf_init/acsf_init``.

   The Drush command creates several directories and then copies files
   that |acquia-product:edg| requires for its tasks, including locating
   the correct database credentials.

#. Run the following Drush command from the docroot directory to check
   that everything is in order before you commit the custom distribution
   to the repository:

   .. code-block:: php 

      drush --include=/path/to/acsf/acsf_init acsf-init-verify

   The ``acsf-init-verify`` command should display the following
   message:

   ``acsf-init required files ok``

#. Commit and push your custom distribution's files to
   |acquia-product:edg|. For the specific procedure to guide you through
   this process, see `Preparing for the code
   deployment </site-factory/workflow/deployments/steps#prepare>`__.
#. Update your Prod environment with the custom distribution's files
   that you just pushed. For the specific procedure to guide you through
   this process, see |Deployments|_.

.. |Deployments| replace:: Deployments in \ |acquia-product:edg|\ 
.. _Deployments: /site-factory/workflow/deployments/steps

Modifying ``settings.php`` for local development
------------------------------------------------

The |acquia-product:edg| Connector module ensures that the
``settings.php`` file includes only the required settings for
|acquia-product:edg|. If you are developing a custom Drupal distribution
locally for use on |acquia-product:edg|, you may need to make changes to
``settings.php`` that are inconsistent with the requirements enforced by
the |acquia-product:edg| Connector module.

The ``acsf-init`` command has an option that you can use to avoid this
conflict. If you are running a Drupal website that includes the
|acquia-product:edg| Connector module outside of |acquia-product:edg|,
you can run ``acsf-init`` with the ``--skip-default-settings`` parameter
to skip the ``settings.php`` check, by using a command similar to the
following:

.. code-block:: php

   drush --include=/path/to/acsf/acsf_init acsf-init --skip-default-settings

Doing this enables you to locally deploy and test a version of
``settings.php`` with settings needed for local development, while still
ensuring that your production websites use the version of
``settings.php`` required by |acquia-product:edg|.

.. note::  Be sure to run ``acsf-init`` without ``--skip-default-settings`` 
   before you commit and push your custom distribution's files to |acquia-product:edg|.


Troubleshooting: Is settings.php included in .gitignore?
--------------------------------------------------------

The ``sites/default/settings.php`` file is written by ``acsf-init`` when
you 
`prepare a custom Drupal distribution </site-factory/workflow/distro>`__ for development and
deployment on |acquia-product:edg|. If you find that you are unable to
create new websites using your custom Drupal distribution, check the
``.gitignore`` file in your code repository. It may be that your
``.gitignore`` file is set to exclude the ``settings.php`` file, so
``settings.php`` never gets pushed to the |acquia-product:edg|. If your
``.gitignore`` file has a line like this:

.. code-block:: php

   # Ignore configuration files that may contain sensitive information.
   sites/*/settings.php

delete it from .gitignore. Then, commit and push your code again, as
described in 
`Preparing for the code deployment </site-factory/workflow/deployments/steps>`__.


Common problems with ``acsf-init``
----------------------------------

If you do not execute the ``acsf-init`` command after a
|acquia-product:edg| platform release, or execute it incorrectly, you
may encounter one or more of the following errors:


.. list-table::
   :widths: 50 50
   :header-rows: 1 

   * - Error
     - Description
   * - ``Verification failed: Verify that acsf-init has run`` |br|
         ``The file settings.php is out of date``
     - If a hotfix fails, ensure that your user has permission to overwrite the ``settings.php`` file, and then execute the command as described in `Updating the module <#updating-the-module>`__.
   * - ``Command acsf-init needs a higher bootstrap level to run``
     - The ``acsf-init`` command was executed from a directory without Git checkout or write permissions. Execute the command from a directory with these permissions to resolve the problem.
   * - ``settings.php`` included in ``.gitignore``
     - If the ``acsf-init`` command fails, even when executed from the correct directory and by a user with correct permissions, verify that your website's ``settings.php`` is not included in your ``.gitignore`` file, which will cause ``acsf-init`` to fail. Remove ``settings.php`` from your ``.gitignore`` file to resolve the problem.
