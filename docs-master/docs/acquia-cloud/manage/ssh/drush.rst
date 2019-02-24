.. include:: /common/global.rst

About Drush on Acquia Cloud
===========================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/ssh/drush/*

Drush is a command-line shell for Drupal, and it enables you to perform many administrative and application maintenance tasks from the command line instead of Drupal's administrative interface.

Unless you are using Live Development, *Drush cannot write to the
|acquia-product:ac| file system*, so you cannot use it to manage your
application's code, or install or update modules. To manage your code,
use your version control system, Git. As an alternative, you can enable
the Live Development feature. With Live Development enabled, you can log
into your |acquia-product:ac| server and use Drush or other tools to
write to the file system. You can use Live Development to modify only
your Dev and Stage environments, not your Prod environment. For more
information about Live Development, see `Using Live development mode to
change code on your server </acquia-cloud/develop/livedev>`__. A more
powerful and flexible alternative is to develop locally and use
`Acquia Dev Desktop </dev-desktop>`__ to sync your code between your
local environment and |acquia-product:ac|. |acquia-product:add| provides
`full support for Drush </dev-desktop/sites/drush>`__.

Best practices for application development — Develop locally!
-------------------------------------------------------------

The fastest and easiest way to work with your application is to develop
it on your local computer, rather than attempting to manage code or
modules remotely on |acquia-product:ac|. You can change your
application's code, use Drush locally to add or update modules, and then
send the changes to |acquia-product:ac| using your selected source
control method (Git) or using `|acquia-product:add|. </dev-desktop>`__

You can use Drush on |acquia-product:ac| to help you develop locally.
For example, suppose you want to be able to locally access your
development environment database. To be able to access the database
locally, `enable SSH, securely connect to
|acquia-product:ac| </acquia-cloud/ssh/enable>`__, and then run the
following Drush command:

.. note::

   Drush commands should generally be run from your website's `docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__.

.. code-block:: none

   drush @[site].dev ah-sql-connect

The command provides the MySQL connection settings required to access
the database. Replace ``[site]`` with your application's name and
``dev`` with the environment whose database you want to reach. You can
then provide these settings to a MySQL client installed on your computer
(such as MySQL Workbench or Navicat). After you configure the MySQL
client to connect to the database server using an SSH tunnel, you'll
have access to your development environment's database from your local
computer.

For more information about Drush, see `Introduction to Drush <%5Bacquia-product:kb%5Darticles/drush-intro>`__.

Remote development — Drush resources on Acquia Cloud
----------------------------------------------------

Drush is pre-installed on |acquia-product:ac|, and you can use Drush with your applications after you `enable SSH access to connect to Acquia Cloud using SSH </acquia-cloud/ssh/enable>`__.

The `Acquia Cloud API <https://cloudapi.acquia.com/>`__ is a RESTful web interface that allows developers to extend, enhance, and customize |acquia-product:ac|. It includes Drush commands that allow you to use all features of the Cloud API. For more information, see the `Drush Cloud reference </acquia-cloud/api/drush-reference>`__.

Using different versions of Drush
---------------------------------

|acquia-product:ac| can run most stable versions of Drush, from Drush 9 to Drush 5. Drush 8 is the default, recommended version.

.. important::

   |acquia-product:ac| defaults to the currently installed version of Drush 8. Subscribers who want to upgrade to Drupal 8.4 should use Drush 8.1.12 and greater.

   Although Drush 9 is available for use, Acquia does not recommend its use with Drupal releases prior to Drupal 8.5. Drush 9 must be installed as a project dependency (using Composer), because it no longer includes a global install command.

To run a specific version of Drush, specify the major version in the ``drush`` command. For example, to run Drush 5, use the command ``drush5``. To run the default version of Drush, use the command ``drush``. On |acquia-product:ac|, the default version of Drush is currently Drush 8.

.. note::

   -  |acquia-product:ac| supports Drush 8 with Drupal 8.
   -  Drush 8 is the only `fully supported version <https://github.com/drush-ops/drush>`__ of Drush for |acquia-product:ac| for Drupal releases prior to Drupal 8.5.
   -  Acquia strongly recommends that you always run a specific major version of Drush. Running the default version of Drush is dangerous because the behavior of your cron jobs, Cloud Hooks, or other automated scripts may change unexpectedly when a new version of Drush becomes the default.

If you want to change your personal default Drush version, you can set an alias for drush in a ``.bashrc`` file. For example, to make the ``drush`` command run Drush 7, add this to your ``~/.bashrc`` file:

.. code-block:: none

   alias drush=drush7

This alias will work only for interactive SSH commands; it will have no effect during cron jobs or Cloud Hooks. To use a specific version of Drush in a cron command, you must call it directly, as follows:

.. code-block:: none

   /usr/local/bin/drush7

When you run Drush on your local computer and use a remote Drush alias for your |acquia-product:ac| application (such as those described in `Using Drush aliases </acquia-cloud/drush/aliases>`__), the remote Drush command will be run using the default version of Drush on |acquia-product:ac|. To run a specific version of Drush on |acquia-product:ac| when you use a remote alias, edit the alias file in the ``$HOME/.drush`` folder on your local computer to specify the version you want. For example:

.. code-block:: none

    $aliases['dev'] = array(
      'path-aliases' => array(
        '%drush-script' => 'drush7',
      ),
      // ... other alias settings here
    );

Accessing environment databases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each of an application's environments on |acquia-product:ac| has its own database, and when you use Drush to access these databases, you must refer to them specifically. For example, if you want to use ``drush sql-connect`` for the database in the development environment of your application, use the following command:

.. code-block:: none

   drush @[site].dev ah-sql-connect

Replace ``[site]`` with the name of your application. Replace ``dev`` with ``test`` to reach the staging environment database or with ``prod`` to reach the production environment database.

Finding help for Drush
~~~~~~~~~~~~~~~~~~~~~~

To access help for Drush online, go to `Drush Commands <http://www.drushcommands.com/>`__.

To access command-line help, enter ``drush help`` on the command line while you are signed in to your |acquia-product:ac| server. For a printable version of this list, enter the following command: ``drush help --html``.

Related topics
--------------

-  `Introduction to Drush <%5Bacquia-product:kb%5Darticles/drush-intro>`__
-  `Using Drush aliases </acquia-cloud/drush/aliases>`__
-  `About SSH/Shell access </acquia-cloud/ssh>`__
-  `An introduction to Drush: The Drupal power tool <http://www.opc.com.au/web-development/introduction-drush-drupal-power-tool>`__
