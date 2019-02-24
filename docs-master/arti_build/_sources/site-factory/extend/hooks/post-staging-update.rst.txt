.. include:: /common/global.rst

post-staging-update hook in |acquia-product:edg|
================================================

.. container:: message-status

   This feature requires 
   `Acquia Cloud Site Factory Connector <https://www.drupal.org/project/acsf>`__ 
   version 1.44 or greater

After you `stage your production
websites </site-factory/workflow/staging>`__ to a non-production
environment, to synchronize with your source environment's data
structure changes and module changes you will need to execute commands
against your newly-staged websites.

To do this, you can use the ``post-staging-update``
`hook </site-factory/extend/hooks>`__ for your environment. If you do
not provide a ``post-staging-update`` hook script, |acquia-product:edg|
will instead execute the default ``drush updatedb`` command.

.. note::  

   The ``post-staging-update`` hook executes only if the non-production and
   production environments are not running the same code.


Using the ``post-staging-update`` hook
--------------------------------------

Like several of the other `hooks in use </site-factory/extend/hooks>`__ by
|acquia-product:edg|, you will create a
script file that follows `best practices for hook
scripts </site-factory/extend/hooks#writing>`__ and then place it in a
particular directory, which will be executed after the data copying
process for each website being staged.

To use the ``post-staging-update`` hook, complete the following steps:

#. Create a script file that includes the commands to run after a
   staging deployment. You can create more than one script file for use
   with this hook, but the scripts will be executed in alphabetical
   order.
#. Ensure that you have created a directory called ``factory-hooks`` in
   the root of your code repository.

   .. note::  

      The ``factory-hooks`` and
      `docroot </articles/docroot-definition>`__
      directories are separate directories at the same level in your code
      repository.

#. In the ``factory-hooks`` directory, ensure that you have created a
   ``post-staging-update`` directory.
#. In the ``/factory-hooks/post-staging-update`` directory, add the
   script file or files that you created for this procedure.
#. Examine the files that you created to ensure that they have the
   executable flag. Failing to set the executable flag for scripts can
   prevent |acquia-product:edg| from executing the files.

After executing a staging deployment, review the newly-staged website as
well as any logging output created by your hook script to determine if
your hook script executed successfully.


Providing hook arguments
------------------------

The hook receives alphanumeric arguments, separated by spaces, in the
following order:

#. Sitegroup
#. Environment
#. Database role
#. Domain


Troubleshooting database update hooks
-------------------------------------

If a script in the ``post-staging-update`` directory ends with an error
(a non-zero exit code), no additional scripts will be executed in the
directory, and the task logs will display error messages in
``SynchronizeSingleSite`` lines. For information about accessing and
reading task logs, see `Logging in
Acquia Cloud Site Factory </site-factory/manage/logs>`__.


Example scripts
---------------

Modify the following script to meet your needs:

.. code-block:: bash

   #!/usr/bin/env bash
   SITEGROUP="$1"
   ENVIRONMENT="$2"
   DB_ROLE="$3"
   DOMAIN="$4"

   echo "domain: $DOMAIN"
   echo "sitegroup: $SITEGROUP"
   echo "env: $ENVIRONMENT"
   echo "db role: $DB_ROLE"

   \drush8 -r /var/www/html/$SITEGROUP.$ENVIRONMENT/docroot -l $DOMAIN ev 'echo "Hello world";'