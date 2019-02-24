.. include:: /common/global.rst

Rsync and Drush on Windows
==========================

.. container:: internal-navigation

   **Rsync**

   * :doc:`Unix </acquia-cloud/develop/rsync>`
   * Windows

`Drush <http://www.drupal.org/project/drush>`__ is one of the most
useful tools a Drupal developer or site builder can have in their
arsenal. On UNIX-based systems, it is reasonably straightforward to set
up and get started using. Windows users have a more involved setup.

.. _add:

|acquia-product:add|
--------------------

|ddlink|_ comes with Drush, rsync, and
Composer pre-installed. Using it is one of the fastest ways to set up a
working installation on Windows. When using |acquia-product:add|, you'll
need a separate client for version control (VCS). We recommend `Git
Bash <http://msysgit.github.io/>`__, which includes an SSH client.


.. |ddlink| replace:: \ |acquia-product:add|\ 
.. _ddlink: /dev-desktop

When your version control client is set up, you can directly clone your
|acquia-product:ac| website. For information about cloning your website,
see |starting|_. After cloning your website, you
should `configure your Drush aliases <#aliases>`__, and test your setup
using the Windows command line or your version control client.

.. |starting| replace:: Starting with an  \ |acquia-product:ac|\  site
.. _starting: 

.. _aliases:

Configuring Drush aliases
-------------------------

Drush aliases make it easier to direct where and what websites Drush
needs to work with.

#. Sign in to your `Acquia account <https://cloud.acquia.com>`__.
#. `Download your Drush aliases </acquia-cloud/drush-aliases>`__, and
   follow the instructions on that page to extract the file into the
   proper directory on your local machine. If the directory does not
   exist, you may need to create it.

   When the Drush aliases are saved properly, the path to the
   ``aliases`` file should look like this, where ``username`` is your
   Windows username:
   ``c:\Users\username\.drush\sitename.aliases.drushrc.php``.

#. Edit the ``aliases`` file and add this array entry at the top,
   changing any details to match your local Drupal website setup:

   ::


       // Site sitename, environment local
        $aliases['local'] = array( 'site' => 'sitename', 'env' => 'loc', 'uri' => 'localhost:8082:', 'root' => 'c:/Users/username/Sites/mysite', ); 
        

#. Save the file.
#. Verify your site aliases are functioning properly using the following
   command to return a list of available aliases:

   ::


       drush sa --full

.. _rsync:

rsync files using Drush aliases
-------------------------------

|acquia-product:add| will rsync files for your |acquia-product:ac|
websites, and these commands can be customized to suit your needs.

.. _rsync-all:

Manual rsync of all files
~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to sync your website's files manually, use the following
command, adapting it where necessary, to rsync your entire development
environment to your local computer:

``drush -vd --mode=ruLtvz rsync @mysite.dev @mysite.local``

The ``-vd`` option displays verbose debugging for troubleshooting. Once
you have confirmed the command works as you expect, you can remove the
``-vd`` flag.

.. _rsync-some:

Manual rsync of selected directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the ``drush rsync`` command rsyncs both your website's
`code </acquia-cloud/develop/code>`__ and
`files </acquia-cloud/manage/files/about>`__. If you want to transfer
only the ``files`` directory, add the following lines to your Drush
``aliases`` file, adjusting it to match your actual alias and system
file paths:

::


    // Site mysite, environment local
     $aliases['local'] = array( 'site' => 'mysite', 'env' => 'loc', 'uri' => 'localhost:8082:', 'root' => 'c:/Users/[username]/Sites/mysite', 'path-aliases' => array( '%files' => 'sites/default/files', ) ); 
     

With this alias, you can run your working Drush command with the files
path alias added, as in this example:.

::


    drush -vd rsync @mysite.dev:%files @mysite.local:%files

For more examples, see `Drush Tip: Quickly Sync Files Between Your
Environments With
Rsync <http://soundpostmedia.com/article/drush-tip-quickly-sync-files-between-your-environments-rsync>`__.
