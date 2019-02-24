.. include:: /common/global.rst

Private files in |acquia-product:edg|
=====================================

.. container:: message-status

   Requires |acquia-product:edg| Connector version 7.x-1.34 or 8.x-1.34 or greater

|acquia-product:edg| supports the use of private files with its hosted
websites.

From the `File module
overview <https://www.drupal.org/docs/8/core/modules/file/overview>`__
page on Drupal.org, unlike *public* files (which can be directly
accessed and downloaded if their URLs are known), *private* files are
not directly accessible through the web server. Instead of accessing
private files using URLs, links require the use of Drupal path requests.
For example, a private file could be accessible at
``/system/files/name-of-the-file.pdf``, but in this case
``/system/files/`` is not an actual folder, but is instead a virtual URL
managed by Drupal.

The private files directory for newly-created websites is set to the
following directory outside of the
`docroot </article/docroot-definition>`__:

``/mnt/files/[sitegroup].[env]/sites/g/files-private/[database name]``

If you need to use private files, having your website's modules or
content types use files from or write files to this directory will
ensure that the files will be included whenever the website is
duplicated or backed up.

.. note::  

   If you store files in private files directories other than the default
   private files directory, those files in those directories will not be
   included in website backups or duplications.
