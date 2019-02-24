.. include:: /common/global.rst

Release notes - |acquia-product:add|
====================================

Looking for the latest and greatest new features and changes to
`|acquia-product:add| <https://www.acquia.com/products-services/dev-desktop>`__?
Read on and check back regularly to see what else we’ve done.

Acquia Dev Desktop - December 21, 2017
-------------------------------------------

*Thu, 21 Dec 2017*

Acquia Dev Desktop (Dec 6 release for macOS \| Nov 12 release for
Microsoft Windows) contains the following updates:

Feature
~~~~~~~~~~~~

-  **Support for Drupal 8.4**
   You can now use Acquia Dev Desktop to help you develop and maintain
   your Drupal 8.4-based websites.

Changes
~~~~~~~~~~~~

-  The following included software was updated:

   -  Updated Drush to version 8.1.15
   -  Updated New Relic to version 7.6.0.201
   -  Updated Memcached to version 1.5.1
   -  Updated MySQL to version 5.6
   -  Updated PHP to versions 7.1.11 and 5.6.32

Fixed issue
~~~~~~~~~~~~

-  The feedback submission feature in Acquia Dev Desktop did not pass
   comments back to Acquia.

Acquia Dev Desktop - April 13, 2017
-------------------------------------------

*Thu, 13 Apr 2017*

Acquia Dev Desktop contains the following updates:

Change
~~~~~~~~~~~~

-  Updated Drush to version 8.1.10. (IN-3023)

Fixed issue
~~~~~~~~~~~~

-  Clicking **Install** when selecting a Drupal distribution did not
   start the website installation process for computers running macOS
   Sierra 10.12.4. (IN-3011)

Acquia Dev Desktop - March 23, 2017
-------------------------------------------

*Thu, 23 Mar 2017*

Acquia Dev Desktop contains the following updates:

Change
~~~~~~~~~~~~

-  Acquia Dev Desktop now identifies itself with a User Agent value of
   ``Dev Desktop``.

Fixed issue
~~~~~~~~~~~~

-  Running the ``pipelines self-update`` command from an Acquia Dev
   Desktop command window caused a certificate exception. (IN-2944)

Acquia Dev Desktop - February 1, 2017
-------------------------------------------

*Wed, 1 Feb 2017*

This release of Acquia Dev Desktop contains updates that will not impact
users' experiences with the product.

Acquia Dev Desktop - September 5, 2016
-------------------------------------------

*Mon, 5 Sep 2016*

Acquia Dev Desktop contains the following updates:

Change
~~~~~~~~~~~~

-  Updated Drush to version 8.1.3. (IN-2764)

Fixed issue
~~~~~~~~~~~~

-  The Pipelines CLI was installed with incorrect permissions. (IN-2768)

Acquia Dev Desktop - August 11, 2016
-------------------------------------------

*Thu, 11 Aug 2016*

Acquia Dev Desktop contains the following update:

Change
~~~~~~~~~~~~

-  In the ``php.ini`` file, updated the value ``GPCS`` (where it
   existed) to ``EGPCS``. (IN-1416)

Acquia Dev Desktop - July 28, 2016
-------------------------------------------

*Thu, 28 Jul 2016*

Acquia Dev Desktop contains the following update:

Change
~~~~~~~~~~~~

-  Acquia Dev Desktop now supports SVN 1.9.*. (IN-2528)

Acquia Dev Desktop - 21 March 2016
-------------------------------------------

*Mon, 21 Mar 2016*

Acquia Dev Desktop contains the following updates:

Changes
~~~~~~~~~~~~

-  Acquia Dev Desktop now generates 4096 bit keys for use with
   connecting websites to Acquia Cloud.
-  Upgraded Drush to version 8.0.5.
-  Upgraded MySQL to version 5.5.48-37.8
-  Upgraded PHP to version 7.0.4.

Fixed issues
~~~~~~~~~~~~

-  The installed version of Drush used PHP 5.4 when no website was
   selected. (IN-1213)
-  In some circumstances, large Acquia Dev Desktop sql.gz files used an
   excessive amount of disk space. (IN-2370)
-  Acquia Dev Desktop created keys that could not be used to connect to
   Acquia Cloud 1.89.1 or greater. (IN-2436)
-  Attempting to update Composer displayed the following error, and did
   not complete successfully: Composer\Downloader\TransportException]
   The "https://getcomposer.org/version" file could not be downloaded:
   SSL operation failed with code 1. (IN-2437)
-  The link to the Known Issues documentation page was broken. (IN-2487)
-  Acquia Dev Desktop was not compatible with SVN version 1.9.*.
   (IN-2528)

Acquia Dev Desktop - 22 November 2015
-------------------------------------------

*Sun, 22 Nov 2015*

Acquia Dev Desktop contains the following updates and fixes:

Change
~~~~~~~~~~~~

-  Upgraded Drush to version 8.0.0.

Fixed issues
~~~~~~~~~~~~

-  When using Acquia Dev Desktop on Windows 8 or Windows 10 computers,
   operations requiring an Apache restart (such as installing another
   distribution) would fail. (IN-2259)
-  Attempting to clone local Drupal 8 websites displayed the following
   error and did not complete successfully:
   ``Could not get database configuration of the default multisite. drush-sql conf failed. Make sure that your site in the Cloud works correctly with drush.``
   (IN-2302)
-  On computers using OS X, if both the RSA and DSA keys are stored in
   the user's SSH agent, Acquia Dev Desktop failed to complete some
   operations (including cloning a website). (IN-2305)

Acquia Dev Desktop - 22 October 2015
-------------------------------------------

*Thu, 22 Oct 2015*

Acquia Dev Desktop contains the following new features, updates, and
fixes:

Features
~~~~~~~~~~~~

-  **Generate SSH key pairs**

   In order to sync a local website with Acquia Cloud, you need to
   register an SSH key in your Acquia user profile. If you don't already
   have one, you can now generate a public/private key pair using Acquia
   Dev Desktop. `Learn more </dev-desktop2/keygen>`__.

-  **Connect using a proxy**

   You can now configure Acquia Dev Desktop to connect to your Acquia
   Cloud subscription through a proxy. `Learn
   more </dev-desktop2/config#proxy>`__.

-  **PHP 7 support**

   Acquia Dev Desktop now includes PHP 7. This version of PHP provides
   substantial performance benefits, especially for Drupal 8. Note,
   however, that PHP 7 does not include many PHP extensions that are
   included with the PHP 5 versions, because they are not available yet.

Changes
~~~~~~~~~~~~

-  Apache has been upgraded to version 2.4.16.
-  MySQL (Percona Server has been upgraded to version 5.5.44-37.3.
-  PHP has been upgraded to versions 5.5.30 and 5.6.14.
-  phpMyAdmin has been upgraded to version 4.4.14.
-  Drush has been upgraded to version 8.0.0 rc1.

Fixed issues
~~~~~~~~~~~~

-  In some circumstances, when syncing databases for a multisite
   installation, the wrong database was updated. (IN-2069)
-  When you install Drupal 8, the installer skips the **Set up
   database** phase, since Acquia Dev Desktop provides the database
   credentials. (IN-2117)
-  Added ``patch.exe`` to the Windows version of Acquia Dev Desktop, so
   that ``drush make`` now works. (IN-2123)
-  Added support for JPEG in the imagick library. (IN-2135)
-  An issue with git checkout could cause errors in cloning sites.
   (IN-2150)
-  In some circumstances, Acquia Dev Desktop could crash when the OS
   wakes up from sleep mode. (IN-2185)
-  An error occurred when making a local clone of a site that has a tag
   deployed. (IN-2199)
-  Importing a site with very long file names on Windows could cause
   Acquia Dev Desktop to crash. (IN-2215)

Acquia Dev Desktop 2 (27 July 2015)
-------------------------------------------

*Mon, 27 Jul 2015*

This release of Acquia Dev Desktop includes the following updates and
fixes:

Features
~~~~~~~~~~~~

-  You can now configure local Acquia Dev Desktop websites to use port
   numbers less than 1024, enabling you to use the default HTTP port of
   80 and the default HTTPS/SSL port of 443. `Learn
   more </dev-desktop2/config#ports>`__.
-  When you clone an Acquia Cloud website, you can choose not to clone
   the database or files. This can be helpful if your database or file
   system is very large and takes too long to clone. `Learn
   more </dev-desktop2/start/cloud>`__.
-  Acquia Dev Desktop now provides simulated HTTPS support using a
   self-signed SSL certificate, which supports local testing and
   development of websites that rely on SSL. `Learn
   more </dev-desktop2/sites>`__.

Changes
~~~~~~~~~~~~

-  The version of Drush included in Acquia Dev Desktop is now Drush
   8.0.0 beta 12.
-  The Windows version of Acquia Dev Desktop now enables OpenSSL by
   default in the ``php.ini`` file. (IN-2029)

Fixed issues
~~~~~~~~~~~~

-  A cURL path error could prevent Acquia Dev Desktop websites from
   connecting with the Acquia Connector. (IN-1918)
-  An issue with Git tags could prevent creating a local clone of an
   Acquia Cloud website. (IN-1941)
-  Exporting a Drupal archive (backup) of a multisite could fail when
   one or more multisites did not have a database. (IN-1961)
-  If you attempted to clone a misconfigured database, the clone process
   would fail without the ability to cancel the operation. (IN-1969)
-  Improved handling of syncing where a multisite's list of databases in
   one branch of code differs from another branch. (IN-2041)
-  Having more than one remote Git URL could cause Acquia Dev Desktop to
   crash. Acquia Dev Desktop does not support pushing to more than one
   Git repository. (IN-2084)

Acquia Dev Desktop 2 (3 April 2015)
-------------------------------------------

*Fri, 3 Apr 2015*

The April 3, 2015 release of Acquia Dev Desktop (`Mac
download <http://www.acquia.com/sites/default/files/downloads/dev-desktop/AcquiaDevDesktop-2-2015-04-03.dmg>`__
\| `Windows
download <http://www.acquia.com/sites/default/files/downloads/dev-desktop/AcquiaDevDesktop-2-2015-04-03.exe>`__)
is the GA release. It includes the following bug fixes:

-  When a user is removed from an Acquia subscription, the corresponding
   local site is now marked as disconnected, rather than being removed.
   (IN-1875)
-  When you click **Host this site on Acquia Cloud** for a local
   multisite, the selected multisite is now synced to Acquia Cloud.
   Formerly, the default multisite would be synced. (IN-1881)
-  If you have cloned a multisite, Acquia Dev Desktop now displays the
   correct domain name for each multisite, instead of the default domain
   name (IN-1882)
-  In some circumstances on Windows where a directory contained a
   symlink, syncing a local site to Acquia Cloud would fail because of a
   name conflict. (IN-1891)

Acquia Dev Desktop 2 (18 March 2015)
---------------------------------------

*Wed, 18 Mar 2015*

The March 18, 2015 release of Acquia Dev Desktop includes the following
new enhancements and bug fixes:

-  Added support for databases with table prefixes.
-  The default PHP version is now PHP 5.5. You can select your PHP
   version when you create or view a new Drupal site, and you can change
   the default PHP version on the Preferences > Config tab, as described
   in `Configuring Dev Desktop </dev-desktop2/config#config>`__.
-  Clarified the message that Acquia Dev Desktop sends when it completes
   file transfers. (IN-1788)
-  Fixed an issue where Acquia Dev Desktop failed to import sites that
   used symlinks. (IN-1789)
-  Fixed an issue for some Mac OS X users where MySQL would fail to
   start. (IN-1792)
-  Fixed an issue that could cause Acquia Dev Desktop to crash during
   installation. (IN-1799)
-  Fixed a file permissions issue on Mac OS X that could prevent Acquia
   Dev Desktop from creating a new site. (IN-1802)
-  Fixed an error that could occur on installation if the installer was
   unable to delete an old backup folder. (IN-1817)
-  Fixed an issue introduced in the March 10 release where some local
   sites on Windows would not display. As a workaround, switching the
   default PHP version fixed the issue, but this fixes the original
   problem. (IN-1598)