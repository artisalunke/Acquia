.. include:: /common/global.rst

Using Views Data Export
=======================

Resolving upload issues with |acquia-product:ace|

-  `General </acquia-cloud/manage/files/broken>`__
-  VDE

You may run into various issues when uploading files to applications
running on |acquia-product:ace|. For cases when you're using something
like the `Views Data
Export <https://drupal.org/project/views_data_export>`__ (VDE) module,
setting a special temp directory is not quite as simple as the case of
``plupload``, because VDE uses Drupal's stream wrapper mechanism for its
temp files.

In order to make VDE use a temp directory different than the default,
you must provide an alternative stream wrapper. This is what the
`Alternative Stream
Wrappers <https://drupal.org/project/alt_stream_wrappers>`__ module
does.

To make VDE work on |acquia-product:ace| with a special temp directory:

#. `Install and enable </acquia-cloud/develop/install-module>`__ the
   Alternative Stream Wrappers module.
#. Set a variable to configure the ``alt_stream_wrappers_alt-temp_path``
   variable to use a directory on Gluster. For example:

   -  `Drush <http://drupal.org/project/drush>`__:

      ``drush vset alt_stream_wrappers_alt-temp_path '/mnt/gfs/[docroot].[environment]/tmp'``

   -  Or, edit the ``settings.php`` file and add:

      ``$conf['alt_stream_wrappers_alt-temp_path'] = '/mnt/gfs/[docroot].[environment]/tmp';``

#. Configure VDE to use the alt-temp stream wrapper.

   -  Drush

      ``drush vset views_data_export_directory 'alt-temp://'``

   -  Or, edit the ``settings.php`` file and add:

      ``$conf['views_data_export_directory'] = 'alt-temp://';``

Your uploads should work once these are set. You can also use this
method for ``plupload`` using ``plupload_temporary_uri: "alt-temp://"``.
However, if you're only using ``plupload``, this method may be more than
you need.
