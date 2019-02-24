.. include:: /common/global.rst

Acquia require line
===================

Acquia-hosted websites load a specific set of global configurations to
ensure minimum basic operations are fulfilled. This code exists in your
website's ``settings.php`` file, and looks like:

``// On Acquia Cloud, this include file configures Drupal to use the correct // database in each site environment (Dev, Stage, or Prod). To use this // settings.php for development on your local workstation, set $db_url // (Drupal 5 or 6) or $databases (Drupal 7 or 8) as described in comments above. if (file_exists('/var/www/site-php')) {   require('/var/www/site-php/mysite/mysite-settings.inc'); }``

where ``mysite`` is the
`docroot <%5Bacquia-product:kb%5Darticle/docroot-definition>`__ of your
website.

These settings ensure that your website operates correctly on
|acquia-product:ac|, and is communicating with the correct database and
code.

Important

Modifications to the ``settings.php`` file should be made *after* this
require line. Modifications made before the require line may be
overwritten by Acquia's required file.

The file added by the Acquia require line performs the following
functions:

-  Ensures that a valid version of Drupal core is installed
-  Determines what version of Drupal core is in use
-  Establishes the trusted host patterns for Drupal 8
-  Establishes the Memcached servers and connection information
-  Builds all of the database connection information
-  Suppresses error reporting in the production environment
