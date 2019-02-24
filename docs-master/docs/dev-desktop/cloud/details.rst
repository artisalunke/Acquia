.. include:: /common/global.rst

How |acquia-product:add| works with |acquia-product:ac|
=======================================================

|acquia-product:add| is integrated with
`|acquia-product:ac| <https://www.acquia.com/products-services/acquia-cloud>`__.
You can export websites created in |acquia-product:add| into your
|acquia-product:ac| subscription or make a local clone of your
|acquia-product:ac| websites with a couple of clicks. Then, you can
easily sync the local and |acquia-product:ac| versions of your sites,
pushing changes up to the cloud and pulling them down to your local
version. This page describes what's happening when you use
|acquia-product:add| with |acquia-product:ac| sites.

-  `When you host a local site on |acquia-product:ac| <#host>`__
-  `When you make a local clone of an |acquia-product:ac|
   site <#clone>`__
-  `When you push local code to |acquia-product:ac| <#pushcode>`__
-  `When you push a local database to |acquia-product:ac| <#pushdb>`__
-  `When you push local files to |acquia-product:ac| <#pushfiles>`__
-  `When you pull code from |acquia-product:ac| <#pullcode>`__
-  `When you pull a database from |acquia-product:ac| <#pulldb>`__
-  `When you pull files from |acquia-product:ac| <#pullfiles>`__

This is just for your information; |acquia-product:add| does all this
automatically for you. You can see a step-by-step log of these actions
by clicking **More** in the progress dialog.

|Viewing more info in a progress dialog|

.. _host:

When you host a local site on |acquia-product:ac|
-------------------------------------------------

When you use |acquia-product:add| to host a local site on
|acquia-product:ac|, |acquia-product:add|:

#. Creates a site archive from your local site, using the
   ``drush archive-dump`` command. If the local site is a Drupal
   multisite, only the selected multisite is included.
#. Uploads the archive to |acquia-product:ac| using SFTP.
#. Connects to your |acquia-product:ac| using SSH and runs
   ``drush ah-site-archive-import`` to import the uploaded archive into
   your |acquia-product:ac| subscription.
#. Downloads site code from your code repository to a new docroot folder
   (using ``git clone``).
#. Modifies ``settings.php`` in the new local site to connect to the
   existing database.
#. Copies files (and the additional multisites, if any) from the old
   docroot to the new one.

When you make a local clone of an |acquia-product:ac| site
----------------------------------------------------------

When you use |acquia-product:add| to make a local clone of an
|acquia-product:ac| site, |acquia-product:add|:

#. Downloads the site code from your |acquia-product:ac| code repository
   to a new docroot folder (using ``git clone``).
#. If the |acquia-product:ac| site contains multisites,
   |acquia-product:add| asks you which multisite to clone now.
#. Creates a new local database and modifies the site’s ``settings.php``
   to connect to the new database.
#. Imports the database from |acquia-product:ac|. To do so, it connects
   to the |acquia-product:ac| server using SSH, runs ``drush sql-dump``,
   downloads the resulting database archive using SFTP, and then imports
   the downloaded database into the new local database.
#. Downloads the |acquia-product:ac| site's files using ``rsync``. The
   synced folders are: ``[docroot]/files``,
   [``docroot]/sites/all/files``, and
   ``[docroot]/sites/[selected multisite]/files``.
#. Gets the drush aliases associated with the site, using the Cloud API,
   and saves them locally to the
   ``[user home]/.acquia/DevDesktop/Drush/Aliases`` directory.

.. _pushcode:

When you push local code to |acquia-product:ac|
-----------------------------------------------

-  If you have a tag deployed locally and have no local modifications,
   |acquia-product:add| deploys the same tag on the |acquia-product:ac|
   environment and finishes the push operation.
-  If you have a tag deployed locally and have made local modifications
   to the code, |acquia-product:add| displays an error. You can't deploy
   to a tag.
-  If you have a branch deployed locally and have made local
   modifications, |acquia-product:add| presents you with a list of local
   modifications and asks what to do with them. See `Committing local
   changes to |acquia-product:ac| </dev-desktop/cloud/commit>`__ for
   more information.
-  |acquia-product:add| applies the selected changes, pushing changed
   files to the code repository, and adding any designated files to the
   ignore list.

.. _pushdb:

When you push a local database to |acquia-product:ac|
-----------------------------------------------------

When you push a local database to |acquia-product:ac|,
|acquia-product:add|:

#. Creates a dump file from the local database using ``drush sql-dump``.
#. Uploads the database dump to |acquia-product:ac| using SFTP.
#. Connects to the |acquia-product:ac| site using SSH and runs
   ``drush sql-drop`` to drop the old database.
#. Imports the uploaded database dump file into the |acquia-product:ac|
   site's database.

.. _pushfiles:

When you push local files to |acquia-product:ac|
------------------------------------------------

|acquia-product:add| uploads the local site's files to
|acquia-product:ac| using rsync. The synced folders are:
``[docroot]/files``, [``docroot]/sites/all/files``, and
``[docroot]/sites/[selected multisite]/files``.

.. _pullcode:

When you pull code from |acquia-product:ac|
-------------------------------------------

-  If you have a tag deployed locally and it matches what is deployed in
   the |acquia-product:ac| environment, then |acquia-product:add|
   returns an error.
-  If you have a branch deployed locally and it matches what is deployed
   in the |acquia-product:ac| environment, then |acquia-product:add|
   updates the local code from the version control system (using
   ``git pull`` ).
-  If the local and |acquia-product:ac| branches (or tags) don’t match
   and your version control system is Git, then |acquia-product:add|
   switches the local branch to use what's deployed on the
   |acquia-product:ac| environment (same as ``git checkout``).

.. _pulldb:

When you pull a database from |acquia-product:ac|
-------------------------------------------------

When you pull a database from |acquia-product:ac|, |acquia-product:add|:

#. Connects to |acquia-product:ac| using SSH and creates a remote
   database dump file by running ``drush sql-dump``.
#. Downloads the database dump file from |acquia-product:ac| using SFTP.
#. Runs ``drush sql-drop`` to drop the existing local database.
#. Imports the downloaded dump file into the local database.

.. _pullfiles:

When you pull files from |acquia-product:ac|
--------------------------------------------

|acquia-product:add| downloads the |acquia-product:ac| site's files
using ``rsync``. The synced folders are: ``[docroot]/files``,
[``docroot]/sites/all/files``, and
``[docroot]/sites/[selected multisite]/files``.

Related topics
--------------

For more information about syncing local and |acquia-product:ac| sites,
see:

-  `Hosting a site on Acquia Cloud </dev-desktop/cloud>`__
-  `Working with sites on Acquia Cloud </dev-desktop/cloud/working>`__

.. |Viewing more info in a progress dialog| image:: https://cdn4.webdamdb.com/1280_UImWN3kiOpc4.jpg?1526475897
   :width: 590px
   :height: 426px
