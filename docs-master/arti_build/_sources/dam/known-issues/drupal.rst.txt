.. include:: /common/global.rst

Known issues in |acquia-product:dam| Connector for Drupal
=========================================================

This page describes any known issues with the |acquia-product:dam|
`Connector for Drupal 8 </dam/integrate/drupal>`__.

- **Syncing a large asset into Drupal may timeout after 30 seconds**
  *(Affects versions 1.2 & 1.3)*
  |br|
  If you are experiencing difficulty syncing large files from
  |acquia-product:dam| into your Drupal 8 website, you can increase
  the HTTP timeout by editing the ``settings.php`` for your Drupal 8
  website, and then changing the following configuration option to a
  value greater than ``30``:

  ``$settings['http_client_config']['timeout'] = 30; // timeout in seconds``

  If you are an |acquia-product:edg| subscriber, for information about
  making changes to ``settings.php`` values, see `Altering values in
  settings.php with hooks </site-factory/extend/hooks/settings-php>`__.

- **Expired assets are not removed from Drupal** *(Affect version 1.2)*
  |br|
  When you `set an asset to expire </dam/content/asset/upload>`__ on a
  particular date, the asset will continue to persist in your Drupal
  website.
- **No syncing of custom XMP metadata, such as keywords** *(Affects
  version 1.2)*
  |br|
  The metadata fields that |acquia-product:dam| syncs are limited to
  the following fields:

  -  status
  -  description
  -  type_id
  -  filename
  -  filesize
  -  width
  -  height
  -  filetype
  -  colorspace
  -  version
  -  datecreated
  -  datemodified
  -  datecaptured
  -  folderID
