.. include:: /common/global.rst

Ignoring specific files with .gitignore
=======================================

Drupal's default ``.gitignore`` file contains only a few basic pieces of
information, and is usually located in your website's
`docroot </articles/docroot-definition>`__ directory. Websites hosted on
|acquia-product:ac| can make significant changes to this file, and by
changing the ``.gitignore`` file, you can prevent your repository from
bloat, by preventing storage of images or other large data items.

Important

|acquia-product:ac|-hosted websites have a different ``.gitignore`` file
than the default Drupal version. Because Drupal core upgrades can
overwrite this file, be sure to back up your ``.gitignore`` file. When
the custom file is overwritten by Drupal core, your
`Git <http://git-scm.com/>`__ repository can gain or lose information,
which can be a risk for data loss or a potential security issue.

``.gitignore`` file differences, by Drupal version
--------------------------------------------------

The contents of your website's ``.gitignore`` file depend on the version
of Drupal you have installed.

.. _d8:

Drupal 8
~~~~~~~~

You can modify ``.gitignore`` to ignore ``settings.php`` (not
``settings*.php``), allowing you to then update the standard
``settings.php`` with the Drupal 8 local settings file checker:

``/**  * Load local development override configuration, if existent.  *  * Use settings.local.php to override variables on secondary (staging,  * development, etc) installations of this site. Typically used to disable  * caching, JavaScript/CSS compression, re-routing of outgoing e-mails, and  * other things that should not happen on development and testing sites.  *  * Keep this code block at the end of this file to take full effect.  */  if (file_exists(DRUPAL_ROOT . '/' . $conf_path . '/settings.local.php')) {    include DRUPAL_ROOT . '/' . $conf_path . '/settings.local.php';  }``

.. _d7:

Drupal 7
~~~~~~~~

The Drupal 7 default ``.gitignore`` file on |acquia-product:ac| appears
similar to the following:

``# Ignore paths that contain user-generated content. sites/*/files sites/*/private``

Drupal 7's default file includes a line to ignore any ``settings*.php``
files in the ``docroot`` directory. Because many websites commit their
settings files to Git as part of their workflow, this addition was
problematic and has been changed in Drupal 8.

.. _additional-files:

Excluding additional files
--------------------------

As an example, if you don't want to commit the default text files to
Git, add the following lines to your ``.gitignore`` file:

``# Ignore default text files /CHANGELOG.txt /COPYRIGHT.txt /INSTALL*.txt /LICENSE.txt /MAINTAINERS.txt /UPGRADE.txt /README.txt sites/all/README.txt sites/all/modules/README.txt sites/all/themes/README.txt``

You can also add additional paths that contain user-generated content,
including the same paths that are part of the default file. This can
include image files, documents, or other items that should not be placed
in the repository.

``# Ignore paths that contain user-generated content. cache/ files/ sites/*/files sites/*/private sites/*/files-private``

Note

If you are not sure where your website's private files section is, see
`Setting the private file directory on
|acquia-product:ac| <%5Bacquia-product:kb%5Darticles/setting-private-file-directory-acquia-cloud>`__.

|acquia-product:ac| users may have an ``acquia-files`` directory, which
should be added to your ``.gitignore`` file.

Further additions can make sense in the |acquia-product:ac| environment,
but you should consider each change carefully to ensure that any changed
files that are part of your codebase get backed up.
