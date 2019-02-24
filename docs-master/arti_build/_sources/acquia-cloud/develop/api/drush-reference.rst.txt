.. include:: /common/global.rst

Drush Cloud reference
=====================

Using |acquia-product:ac| Drush commands, you can use all of the
features of the `Cloud API </acquia-cloud/api>`__ on the command line or
from shell scripts, using the Drush command-line tool. This reference
describes only the |acquia-product:ac| Drush commands for using the
Cloud API. For information about how to get started with the
|acquia-product:ac| Drush integration, see `Developing with the Cloud
API </acquia-cloud/api>`__.

-  For a reference to core Drush and information about Drush in general,
   see `Drush Commands <http://www.drushcommands.com/>`__.
-  For more information about using Drush on |acquia-product:ac|, see
   `About Drush on |acquia-product:ac| </acquia-cloud/drush>`__.
-  For more information about the Cloud API, see `Developing with the
   Cloud API </acquia-cloud/api>`__ and the `Cloud API
   Reference <https://cloudapi.acquia.com/>`__.

.. _commands:

|acquia-product:ac| API commands
--------------------------------

Type

Command

Description

`**API credentials** <#login>`__

`ac-api-login <#0.1_ac-api-login>`__

Store |acquia-product:ac| API credentials and configuration information.

`**Code deployment** <#code-deploy>`__

`ac-code-deploy <#0.1_ac-code-deploy>`__

Deploy code from one site environment to another.

`ac-code-path-deploy <#0.1_ac-code-path-deploy>`__

Deploy a specific branch or tag in an environment.

`**Database commands** <#database>`__

`ac-database-add <#ac-database-add>`__

Add a database.

`ac-database-copy <#0.1_ac-database-copy>`__

Copy a database from one site environment to another.

`ac-database-delete <#ac-database-delete>`__

Delete a database.

`ac-database-info <#0.1_ac-database-info>`__

Show information about a site database.

`ac-database-instance-backup <#0.1_ac-database-instance-backup>`__

Create a backup of a database instance.

`ac-database-instance-backup-delete <#0.1_ac-database-instance-backup-delete>`__

Delete a database instance backup.

`ac-database-instance-backup-download <#0.1_ac-database-instance-backup-download>`__

Download a database instance backup of a site environment.

`ac-database-instance-backup-info <#0.1_ac-database-instance-backup-info>`__

Show information about a site environment's database instance backup.

`ac-database-instance-backup-list <#0.1_ac-database-instance-backup-list>`__

List a site environment's database instance backups.

`ac-database-instance-backup-restore <#0.1_ac-database-instance-backup-restore>`__

Restore a database instance from a backup.

`ac-database-instance-info <#ac-database-instance-info>`__

Show information about a site environment's database instance.

`ac-database-instance-list <#ac-database-instance-list>`__

List a site environment's database instances.

`ac-database-list <#0.1_ac-database-list>`__

List a website's databases.

`**Domains** <#domains>`__

`ac-domain-add <#0.1_ac-domain-add>`__

Add a domain name to an environment.

`ac-domain-delete <#0.1_ac-domain-delete>`__

Delete a domain name from an environment.

`ac-domain-info <#0.1_ac-domain-info>`__

Show information about a site domain.

`ac-domain-list <#0.1_ac-domain-list>`__

List a website's domains.

`ac-domain-move <#0.1_ac-domain-move>`__

Move one or more domains from one site environment to another.

`ac-domain-purge <#0.1_ac-domain-purge>`__

Purge a domain from the Varnish cache.

`**Environments** <#environments>`__

`ac-environment-info <#0.1_ac-environment-info>`__

Show information about a site environment.

`ac-environment-install <#0.1_ac-environment-install>`__

Install a Drupal distribution from a preselected list, URL, or Drush
Makefile.

`ac-environment-list <#0.1_ac-environment-list>`__

List a website's environments.

`ac-environment-livedev <#0.1_ac-environment-livedev>`__

Enable or disable live development on a site environment.

`**Files** <#files>`__

`ac-files-copy <#0.1_ac-files-copy>`__

Copy files from one site environment to another.

`**Servers** <#servers>`__

`ac-server-info <#ac-server-info>`__

Show information about a server.

`ac-server-list <#ac-server-list>`__

List servers for a site and environment.

`**Sites** <#sites>`__

`ac-site-info <#0.1_ac-site-info>`__

Show information about a site.

`**SSH keys** <#sshkey>`__

`ac-sshkey-add <#ac-sshkey-add>`__

Add an SSH key to a site.

`ac-sshkey-delete <#ac-sshkey-delete>`__

Delete an SSH key from a site.

`ac-sshkey-info <#ac-sshkey-info>`__

Show information about a site SSH key.

`ac-sshkey-list <#ac-sshkey-list>`__

List a site's SSH keys.

`**Tasks** <#tasks>`__

`ac-task-info <#0.1_ac-task-info>`__

Show information about a site task.

`ac-task-list <#0.1_ac-task-list>`__

List a website's tasks.

`**API aliases** <#aliases>`__

`acquia-update <#0.1_acquia-update>`__

Retrieves and updates Drush aliases for all accessible
|acquia-product:ac| sites..

.. _common:

Common options
--------------

All |acquia-product:ac| API commands have the following options:

+-----------------------------------+-----------------------------------+
| Command                           | Description                       |
+===================================+===================================+
| ``--cainfo=``                     | Path to a file containing the SSL |
|                                   | certificates needed to verify the |
|                                   | ``ac-api-endpoint``.              |
+-----------------------------------+-----------------------------------+
| ``--caller=``                     | |acquia-product:ac| API caller    |
|                                   | name. Default is the current      |
|                                   | username.                         |
+-----------------------------------+-----------------------------------+
| ``--endpoint=``                   | |acquia-product:ac| API endpoint  |
|                                   | URL.                              |
+-----------------------------------+-----------------------------------+
| ``--format=``                     | Format to output the object. Use  |
|                                   | "var_export" for var_export, and  |
|                                   | "json" for JSON. If not provided, |
|                                   | the output is printed in a        |
|                                   | human-readable format.            |
+-----------------------------------+-----------------------------------+
| ``--email=``                      | |acquia-product:ac| API email     |
|                                   | address. See `Cloud API           |
|                                   | authentication </acquia-cloud/api |
|                                   | /auth>`__.                        |
+-----------------------------------+-----------------------------------+
| ``--key=``                        | |acquia-product:ac| API key. See  |
|                                   | `Cloud API                        |
|                                   | authentication </acquia-cloud/api |
|                                   | /auth>`__.                        |
+-----------------------------------+-----------------------------------+
| ``--acapi-conf-path=``            | By default, the                   |
|                                   | `ac-api-login <#0.1_ac-api-login> |
|                                   | `__                               |
|                                   | command stores default option     |
|                                   | values for future                 |
|                                   | |acquia-product:ac| API commands  |
|                                   | in                                |
|                                   | ``$HOME/.drush/.acapi.drushrc.php |
|                                   | ``.                               |
|                                   | Use this option to specify a      |
|                                   | different file location.          |
+-----------------------------------+-----------------------------------+

.. _detail:

Command detail
--------------

.. _login:

API credentials
~~~~~~~~~~~~~~~

ac-api-login
^^^^^^^^^^^^

| Store |acquia-product:ac| API credentials and configuration
  information.
| This command stores default option values for future
  |acquia-product:ac| API commands in
  ``$HOME/.drush/.acapi.drushrc.php``. This is most useful for stashing
  your API email and key so you do not have to enter it every time. You
  can change the file location where this is stored using the
  ``acapi-conf-path`` option.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__
-  ``--reset`` - Discard any existing stored values from a previous
   call. Without this option, new values will be merged with existing
   values.

--------------

.. _code-deploy:

Code deployment
~~~~~~~~~~~~~~~

.. _0.1_ac-code-deploy:

ac-code-deploy
^^^^^^^^^^^^^^

Deploy code from one site environment to the target environment.

*Arguments*

-  ``target`` - The target environment.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-code-path-deploy:

ac-code-path-deploy
^^^^^^^^^^^^^^^^^^^

Deploy a specific branch or tag in an environment.

*Arguments*

-  ``path`` - The branch or tag to deploy.

*Options*

-  `Common options <#common>`__

--------------

.. _database:

Database commands
~~~~~~~~~~~~~~~~~

ac-database-add
^^^^^^^^^^^^^^^

Add a database.

*Arguments*

-  ``db`` - The name of the database.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-database-copy:

ac-database-copy
^^^^^^^^^^^^^^^^

Copy a database from one site environment to the target environment.

*Arguments*

-  ``db`` - The database.
-  ``target`` - The target environment.

*Options*

-  `Common options <#common>`__

--------------

ac-database-delete
^^^^^^^^^^^^^^^^^^

Delete a database. By default, creates a backup of each instance of the
database before deleting it.

*Arguments*

-  ``db`` - The database.

*Options*

-  `Common options <#common>`__
-  ``--no-backup`` - Do not make a final backup of each instance of this
   database before deleting it.

--------------

.. _0.1_ac-database-info:

ac-database-info
^^^^^^^^^^^^^^^^

Show information about a site database.

*Arguments*

-  ``db`` - Database name.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-database-instance-backup:

ac-database-instance-backup
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a backup of a database instance.

*Arguments*

-  ``db`` - The database.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-database-instance-backup-delete:

ac-database-instance-backup-delete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a database instance backup.

*Arguments*

-  ``db`` - The database.
-  ``backupid`` - The backup ID.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-database-instance-backup-download:

ac-database-instance-backup-download
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download a database instance backup of a site environment.

*Arguments*

-  ``db`` - The database.
-  ``backupid`` - The backup ID.

*Options*

-  `Common options <#common>`__
-  ``--result-file=`` - Save to a file; specify the full path in which
   to store the backup. If no path is provided, the backup is sent the
   standard output.

--------------

.. _0.1_ac-database-instance-backup-info:

ac-database-instance-backup-info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Show information about a site environment's database instance backup.

*Arguments*

-  ``db`` - Database name.
-  ``backup`` - The backup ID.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-database-instance-backup-list:

ac-database-instance-backup-list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

List a site environment's database instance backups.

*Arguments*

-  ``db`` - Database name.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-database-instance-backup-restore:

ac-database-instance-backup-restore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Restore a database instance from a backup.

*Arguments*

-  ``db`` - The database.
-  ``backupid`` - The backup ID.

*Options*

-  `Common options <#common>`__

--------------

ac-database-instance-info
^^^^^^^^^^^^^^^^^^^^^^^^^

Show information about a site environment's database instance.

*Arguments*

-  ``db`` - The database name.

*Options*

-  `Common options <#common>`__

--------------

ac-database-instance-list
^^^^^^^^^^^^^^^^^^^^^^^^^

List a site environment's database instances.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-database-list:

ac-database-list
^^^^^^^^^^^^^^^^

List a website's databases.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__

--------------

Domains
~~~~~~~

.. _0.1_ac-domain-add:

ac-domain-add
^^^^^^^^^^^^^

Add a domain name to an environment.

*Arguments*

-  ``domain`` - The domain name.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-domain-delete:

ac-domain-delete
^^^^^^^^^^^^^^^^

Delete a domain name from an environment.

*Arguments*

-  ``domain`` - The domain name.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-domain-info:

ac-domain-info
^^^^^^^^^^^^^^

Show information about a site domain.

*Arguments*

-  ``domain`` - The domain name.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-domain-list:

ac-domain-list
^^^^^^^^^^^^^^

List a website's domains. If a site has an Elastic Load Balancer (ELB),
also returns the name of the ELB.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-domain-move:

ac-domain-move
^^^^^^^^^^^^^^

Move one or more domains from one site environment to the target
environment.

*Arguments*

-  ``target`` - The target environment to which you are moving the
   domains.
-  ``domains`` - A comma-separated list of the domains to move, or \* to
   move all domains in the source environment.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-domain-purge:

ac-domain-purge
^^^^^^^^^^^^^^^

Purge a domain from the Varnish cache.

*Arguments*

-  ``domain`` - The domain name.

*Options*

-  `Common options <#common>`__

--------------

Environments
~~~~~~~~~~~~

.. _0.1_ac-environment-info:

ac-environment-info
^^^^^^^^^^^^^^^^^^^

Show information about a site environment.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-environment-install:

ac-environment-install
^^^^^^^^^^^^^^^^^^^^^^

Install a Drupal distribution into an environment from a URL or a Drush
Make file.

*Arguments*

-  ``type`` - Type of distro source. One of ``distro_url`` or
   ``make_url``.
-  ``source`` - Depending on ``type``, one of:

   -  ``distro_url`` - A publicly accessible URL to any Drupal
      distribution in standard format.
   -  ``make_url`` - A publicly accessible URL to a Drush Make file.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-environment-list:

ac-environment-list
^^^^^^^^^^^^^^^^^^^

List a website's environments.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-environment-livedev:

ac-environment-livedev
^^^^^^^^^^^^^^^^^^^^^^

Enable or disable `live development </acquia-cloud/develop/livedev>`__
on a site environment.

*Arguments*

-  ``action`` - The action to take: ``enable`` or ``disable`` live
   development on the environment.

*Options*

-  `Common options <#common>`__

--------------

Files
~~~~~

.. _0.1_ac-files-copy:

ac-files-copy
^^^^^^^^^^^^^

Copy files from one site environment to the the target environment.

*Arguments*

-  ``target`` - The target environment.

*Options*

-  `Common options <#common>`__

--------------

Servers
~~~~~~~

ac-server-info
^^^^^^^^^^^^^^

Show information about a server.

*Arguments*

-  ``server`` - The server name.

*Options*

-  `Common options <#common>`__

--------------

ac-server-list
^^^^^^^^^^^^^^

List servers for a site and environment.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__

--------------

Sites
~~~~~

.. _0.1_ac-site-info:

ac-site-info
^^^^^^^^^^^^

Show information about a website.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__

--------------

.. _sshkey:

SSH keys
~~~~~~~~

ac-sshkey-add
^^^^^^^^^^^^^

Add an SSH key to a website.

*Arguments*

-  ``ssh_pub_key`` - File containing the SSH public key.
-  ``nickname`` - The SSH key nickname.

*Options*

-  `Common options <#common>`__

--------------

ac-sshkey-delete
^^^^^^^^^^^^^^^^

Delete an SSH key from a site.

*Arguments*

-  ``sshkeyid`` - The ID of the SSH key to delete.

*Options*

-  `Common options <#common>`__

--------------

ac-sshkey-info
^^^^^^^^^^^^^^

Show information about a website SSH key.

*Arguments*

-  ``sshkeyid`` - The ID of the SSH key.

*Options*

-  `Common options <#common>`__

--------------

ac-sshkey-list
^^^^^^^^^^^^^^

List a website's SSH keys.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__

--------------

Tasks
~~~~~

.. _0.1_ac-task-info:

ac-task-info
^^^^^^^^^^^^

Show information about a site task.

*Arguments*

-  ``task`` - The task ID.

*Options*

-  `Common options <#common>`__

--------------

.. _0.1_ac-task-list:

ac-task-list
^^^^^^^^^^^^

List a website's tasks. By default, returns only the last 7 days of
tasks and no more than 50 tasks. You can modify this default behavior by
using the ``limit`` or ``days`` arguments in the command.

*Arguments*

-  ``days`` - Return tasks from the past n days. Default is 7.
-  ``limit`` - Maximum number of tasks to return. Default is 50.

*Options*

-  `Common options <#common>`__

--------------

.. _aliases:

API aliases
~~~~~~~~~~~

.. _0.1_acquia-update:

acquia-update
^^^^^^^^^^^^^

Retrieves and updates Drush aliases for all accessible
|acquia-product:ac| sites.

*Arguments*

-  None

*Options*

-  `Common options <#common>`__
