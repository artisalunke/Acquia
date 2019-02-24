.. include:: /common/global.rst

Overriding drush updatedb
=========================

It can be helpful to perform actions on your websites immediately prior
to or after a database update. To accomplish this, |acquia-product:edg|
provides the ``db-update`` hook for your use, allowing you to override
the behavior of ``drush updatedb``. It does this by allowing you to
inject custom scripts for execution both before and after the command is
run for your websites.

Using the ``db-update`` hook
----------------------------

Like several of the other hooks in use by |acquia-product:edg|, you will
create a script file and place it in a particular directory, which will
be executed at the appropriate time when doing database updates for your
websites. To use the hook, complete the following steps:

#. | Create a script that includes the commands to to run before and
     after ``drush updatedb``. You can create more than one script for
     use with this hook, but the scripts will be executed in
     alphabetical order. However, a single script can contain both pre-
     and post-update instructions.
   | Place the ``drush updatedb`` instruction at the point you wish
     database updates to be executed.

   .. important::  

      Because this hook replaces ``drush updatedb``, be sure that your
      script includes the ``drush updatedb`` command.
      
      If you do not include the command and you use the ``db-update``
      hook, |acquia-product:edg| will not run ``drush updatedb`` on your
      websites.

#. Ensure that you have created a directory called ``factory-hooks`` at
   the root of your code repository.

   .. note::  

      The ``factory-hooks`` directory and your
      `docroot </articles/docroot-definition>`__ are
      separate directories at the same level in your code repository.

#. In the ``factory-hooks`` directory, ensure that you have created a
   ``db-update`` directory.
#. In the ``/factory-hooks/db-update`` directory, add the script file(s)
   that you created for this procedure.
#. Examine the files that you created to ensure that they have the
   executable flag for |acquia-product:edg| to execute them.

If your scripts require additional arguments, you can provide the
``db_update_arguments`` argument by either using the ``/update`` `Site
Factory REST API <https://www.demo.acquia-cc.com/api/v1>`__ call, or by
signing in to the |acquia-product:edg| user interface to specify
arguments to be passed to the hook.


Providing arguments to the hook
-------------------------------

The hook accepts alphanumeric arguments, separated by spaces. To supply
arguments to the ``db-update`` hook from the |acquia-product:edg| user
interface, perform the following steps:

#. Sign in to the |acquia-product:edg| interface.
#. In the top menu, click **Administration**.
#. In the **Code management and deployment** section, click **Update
   code**.
#. Scroll to the **Site update action** section, and then in the
   **Update argument** field, enter your arguments, separated by spaces.
#. Select the **Select this check box to confirm that you want to update
   your public-facing production environment** check box.
#. Click **Update**.


Troubleshooting database update hooks
-------------------------------------

Database updates will be performed normally using ``drush updatedb`` if
any of the following conditions are met:

-  The ``/factory-hooks/db-update`` directory does not exist, or is not
   in the right place.
-  The ``/factory-hooks/db-update`` directory exists, but contains no
   files.
-  The ``/factory-hooks/db-update`` directory exists and contains files,
   but none are executable.

If a script in the ``db-update`` directory ends with an error (a
non-zero exit code), no additional scripts will be executed in the
directory, and the task logs will display errors in ``TaskUpdate``
lines. For information about accessing and reading task logs, see
|logging|_.


.. |logging| replace:: Logging in \ |acquia-product:edg|\ 
.. _logging: /site-factory/manage/logs


Example scripts
---------------

The following scripts are available for your use, and include examples
that `do *not* use Acquia BLT <#not-using-acquia-product-blt>`__ and that `do use
Acquia BLT <#using-acquia-product-blt>`__.

*Not* using |acquia-product:blt|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following script can be modified to suit your needs, but the script
*must* contain the ``drush updatedb`` command.

.. code-block:: bash

    #!/bin/sh
    #
    # Factory Hook: db-update
    #
    # The existence of one or more executable files in the
    # /factory-hooks/db-update directory will prompt them to be run *instead of* the
    # regular database update (drush updatedb) command. So that update command will
    # normally be part of the commands executed below.
    #
    # Usage: post-code-deploy site env db-role domain custom-arg1 custom-arg2 ...
    # Map the script inputs to convenient names.
    # Acquia hosting site / environment names
    site="$1"
    env="$2"
    # database role. (Not expected to be needed in most hook scripts.)
    db_role="$3"
    # The public domain name of the website.
    domain="$4"
    # Custom argument: we will run entity updates if it is in any way nonempty.
    update_entities="$5"

    # The websites' document root can be derived from the site/env:
    docroot="/var/www/html/$site.$env/docroot"

    # Acquia recommends the following two practices:
    # 1. Hardcode the drush version.
    # 2. When running drush, provide the docroot + url, rather than relying on
    #    aliases. This can prevent some hard to trace problems.
    DRUSH_CMD="drush8 --root=$docroot --uri=https://$domain"

    $DRUSH_CMD updatedb
    # Run entity updates if the updatedb command didn't fail.
    if [ $? -eq 0 -a -n "$update_entities" ] ; then
      # Possibly do some preparation here...
      $DRUSH_CMD entity-updates
    fi


Using |acquia-product:blt|
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following script can be modified to suit your needs. Because the
final ``deploy`` command calls ``drush updatedb``, a separate
``drush updatedb`` command is not needed.

.. code-block:: bash

    #!/bin/sh
    #
    # Factory Hook: db-update
    #
    # The existence of one or more executable files in the
    # /factory-hooks/db-update directory will prompt them to be run *instead of* the
    # regular database update (drush updatedb) command. So that update command will
    # normally be part of the commands executed below.
    #
    # Usage: post-code-deploy site env db-role domain custom-arg
    # Map the script inputs to convenient names.
    # Acquia hosting site / environment names
    site="$1"
    env="$2"
    # database role. (Not expected to be needed in most hook scripts.)
    db_role="$3"
    # The public domain name of the website.
    domain="$4"
    # BLT executable:
    blt="/var/www/html/$site.$env/vendor/acquia/blt/bin/blt"

    com="$blt deploy:update --define environment=$env --define drush.uri=$domain -v -y"

    $com