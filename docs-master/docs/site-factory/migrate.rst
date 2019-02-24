.. include:: /common/global.rst

Preparing to migrate sites into |acquia-product:edg|
====================================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/migrate/*

.. container:: message-status
   
   **ADVANCED** - Incorrectly migrating a website without properly preparing for the attempt can involve data loss or a website outage event.

.. container:: internal-navigation

   **Configuring and using Site Factory**

   * :doc:`Setup </site-factory/setup>`
   * Migrate
   * :doc:`Manage </site-factory/manage>`
   * :doc:`Workflow </site-factory/workflow>`
   * :doc:`Extend </site-factory/extend>`
   * :doc:`Monitor </site-factory/monitor>`

Attempting to import an existing Drupal website into
|acquia-product:edg| both requires that you understand how
|acquia-product:edg| structures the websites that it hosts, and that you
complete the required preparatory work to ensure a smooth, repeatable
migration process, which can provide you a local backup of your work
should a rollback of your migration be needed.

The information on this page is intended as preparation for actually
|migrating|_.

.. |migrating| replace:: migrating your website into \ |acquia-product:edg|\ 
.. _migrating: /site-factory/migrate/execute

.. _checklist:

Checklist for website migration
-------------------------------

Acquia has identified a common list of tasks to consider as part of your
initial sprint (Sprint 0) planning for an |acquia-product:edg|
migration. Although the activities described `on the Sprint 0 checklist
page </site-factory/migrate/plan>`__ are not a complete list, they can
help you to identify the work that is necessary for a successful launch,
and also identify the tools (such as |bltlink|_) that can assist you.




File structure in |acquia-product:edg|
--------------------------------------

When you are preparing to migrate a website, it helps to understand how
files are organized in a |acquia-product:edg| installation. Migrating a
website into |acquia-product:edg| involves all three major sections of a
Drupal website:

-  `Shared codebase across all websites <#shared-codebase-across-all-websites>`__
-  `Website-specific files directory <#website-specific-files-directory>`__
-  `Per-website theme directory <#per-website-theme-directory>`__


Shared codebase across all websites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The code in your Factory's main version control repository contains your
Drupal core and contributed module files that are to be used for all
websites in your Factory. You must use version control processes to
modify this code. Because storage and retrieval times are faster here
than in the distributed file storage system used in your
`website-specific files directory <#structure-files>`__, Acquia
recommends that you store website-specific modules in one of the
following directories, based on your distribution:

-  Using a distribution, such as |ldlink|_ - ``profiles/[profilename]/modules``
-  *Not using a distribution* - Drupal 8: The top-level ``modules`` directory; Drupal 7: ``sites/all/modules/``

Acquia discourages the use of the ``sites/default`` directory, with the
exception of ``sites/default/files``, as files in ``sites/default`` will
not be included in website backups.

.. note::  For instructions regarding allowing your codebase access to sensitive credentials, passwords, or other private information, see `Storing sensitive information outside of your codebase </resource/secrets>`__.


Website-specific files directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your website's ``files`` directory should contain the binary file assets
(images and videos) your website needs that cannot be easily stored in
version control. This ``files`` directory, and its contents, reside on a
writable, distributed file system shared by all of your
|acquia-product:edg|-hosted websites. Because this file system is
external to your shared codebase, access times for files stored in your
``files`` directory will be slower than access times for `files stored in the shared codebase <#structure-code>`__.

The ``files`` directory for your website is located at
``sites/g/files/[abcde]``, where ``[abcde]`` is a random string.

Public files reside in the ``sites/g/files/[abcde]/f/`` directory.


Per-website theme directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your website-specific directories each contain a ``themes`` directory.
Acquia strongly encourages that you store your per-website themes in
this location, as storage and retrieval are far faster than the
distributed storage system used in your website-specific files
directory. For information about creating a theme repository for each of
your websites in |acquia-product:edg|, see `Adding external themes to your site </site-factory/theme/external>`__.

If you configure a dedicated theme repository for a website,
``sites/g/files/[abcde]/themes/site`` will be a symlink to local storage
for that repository.

Preparing Drush aliases for the import process
----------------------------------------------

Because the import process uses
`Drush <https://www.drupal.org/project/drush>`__ commands, creating
Drush aliases for your target website allows you to execute Drush
commands without needing to sign in to your target website to copy files
using SSH.

.. note::  You should use Drush 8 when deploying a Drupal 8 codebase, and Drush 6 when deploying a Drupal 7 codebase.

To configure your aliases to run the correct version of Drush, create a
Drush aliases file based on the following example, altering the code to
meet your needs:

.. code:: php
   
   $aliases['acquia-cloud'] = array(
    'path-aliases' => array(
     // '%drush-script' => 'drush8', // uncomment this line if deploying a D8 codebase
     // '%drush-script' => 'drush6', // uncomment this line if deploying a D7 codebase.
      '%dump-dir' => '/mnt/tmp/',
    ),
   );
   $aliases['target'] = array(
    'parent' => '@acquia-cloud',
    'uri' => 'mynewdomain.customername.acsitefactory.com',
    'root' => '/var/www/html/AH_SITE_GROUP.AH_SITE_ENVIRONMENT/docroot/',
    'remote-host' => 'managed-12345.defaultrealm.hosting.acquia.com', 
    'remote-user' => 'YOURUSERNAMEHERE',
    'path-aliases' => array(
      # the following is optional if you want to have a dedicated temp dir without many other files in there:
      '%dump-dir' => '/mnt/tmp/AH_SITE_GROUP.AH_SITE_ENVIRONMENT/drush-import/',
    ),
   );

If you need assistance determining what these values should be, `contact Acquia Support </support#contact>`__.

.. note::  The instructions in the website migration process that reference the ``@target`` alias assume you have created and implemented this file, and will execute ``@target`` commands from your local computer to affect your intended target website.

To verify that your Drush aliases are functioning properly, from a
command line window, run the following command:

``drush @target status``

Examine both the **Site path** to determine if it matches the path
``sites/g/files/[abcde]`` (where ``[abcde]`` is a random string), and
the **File directory path** to determine if it matches
``sites/g/files/[abcde]/f`` (where ``[abcde]`` is a random string).

If your both the **Site path** and **File directory path** values match
the described strings, your Drush aliases are connecting to your server.

Common sources of problems with this file include the following:

-  Incorrect values for ``uri``, ``remote_host``, or ``remote-user``
-  Not committing the ``sites/g/`` directory to the codebase after
   executing ``drush acsf-init``

Next steps
----------

After you ensure that your website will work with the |acquia-product:edg| directory structure and you test your Drush aliases, you should review the `Checklist for migrating your sites </site-factory/migrate/plan>`__ to |acquia-product:edg|.



.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt

.. |ldlink| replace:: \ |acquia-product:ld|\ 
.. _ldlink: /lightning