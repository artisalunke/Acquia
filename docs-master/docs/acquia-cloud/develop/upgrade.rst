.. include:: /common/global.rst

Upgrading Drupal core on |acquia-product:ac|
============================================

From time to time, you will need to upgrade Drupal core in your
|acquia-product:ac| applications. This may occur when there are new
Drupal core features that you want or security updates that you need.

This page describes two ways to upgrade Drupal core:

-  `Upgrading with |acquia-product:add| <#devdesktop>`__
-  `Upgrading with Git <#git>`__

.. _devdesktop:

Upgrading Drupal 7 with |acquia-product:add|
--------------------------------------------

The easiest way to upgrade Drupal 7 core for an |acquia-product:ac|
application is to use `|acquia-product:add| </dev-desktop>`__, which
provides a full Drupal-specific stack that includes Apache, MySQL, and
PHP. You can use |acquia-product:add| to develop Drupal applications
locally on your computer, and then sync it with the same application on
|acquia-product:ac|. Since it is closely integrated with
|acquia-product:ac|, using |acquia-product:add| can be the easiest way
to import your application into |acquia-product:ac|. This section
assumes that you have already `installed
|acquia-product:add| </dev-desktop/install>`__ and `synced
it </dev-desktop/cloud>`__ with your applications on
|acquia-product:ac|.

First, upgrade Drupal core on the local environment with
|acquia-product:add|:

#. In |acquia-product:add|, select the application you want to upgrade.
#. Next to **Local code**, click the **Open Drush console** button.
#. In the Drush console, run this command:

   ``drush up``

   Drush upgrades Drupal core to the latest release.

#. Next to **Local site**, click the URL link. Your upgraded Drupal
   application opens in a browser window. You can test this local copy
   of your upgraded Drupal application before you sync it with your
   |acquia-product:ac| Development environment.

Next, sync the local copy of your upgraded Drupal application with your
|acquia-product:ac| Development environment:

#. In |acquia-product:add|, select **Push to Cloud Dev**, and select the
   **Code** checkbox.
#. Click **Push code to Cloud Dev**.
#. |acquia-product:add| pushes your upgraded Drupal application to the
   |acquia-product:ac| Development environment and commits the code to
   the |acquia-product:ac| code repository.

.. _git:

Upgrading with Git
------------------

To upgrade Drupal 8, if you use a Git repository:

#. Download the `latest version of Drupal
   8 <https://www.drupal.org/project/drupal>`__.
#. Ensure that any upstream changes to the ``docroot`` directory are
   pulled into your local working directory and that you have no locally
   modified, added, or deleted files.

   ``git pull``

   If you have any locally modified, added, or deleted files, resolve
   any conflicts before you move on in the procedure.

#. Remove the ``core`` and ``vendor`` directories. Also remove all of
   the files in the top-level directory, except any that you added
   manually.

   ``rm -rf core vendor rm -f *.* .*``

#. Extract the Drupal tar file into the ``docroot`` directory inside
   your local checkout or clone of your |acquia-product:ac| repository.

   ``cd /path/to/checkout/trunk/docroot tar --strip-components=1 -xzf /path/to/drupal-8.2.3.tar.gz``

#. Add the new files to your code repository.

   ``git status --untracked-files=all # On branch master # Untracked files: #   (use "git add ..." to include in what will be committed) # #   some/new/file.inc nothing added to commit but untracked files present (use "git add" to track) git add some/new/file.inc``

#. Remove any files that you don't need.

   ``git rm [filename]``

#. Commit your changes.

   ``git commit -a -m "Upgrade to Drupal 8.2.3."``

   Note that at this point, |acquia-product:ac| does not deploy your
   changes. The commit command affects only your local working
   repository.

#. Push your local version of the branch to the remote repository at
   Acquia.

   ``git push``

#. Run ``update.php`` by visiting ``http://[dev-env-URL]/update.php``
   (replace [dev-env-URL] with the URL of your Development environment).
   This will update the core database tables.
#. Test the upgraded application on your Development environment. Once
   you are satisfied, deploy your code in the Staging environment, and
   then to Production.
#. Run ``update.php`` in your production environment to update the core
   database tables there.

.. _related:

Related topics
--------------

-  `About your code repository </acquia-cloud/develop/repository>`__
