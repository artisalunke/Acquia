.. include:: /common/global.rst

|acquia-product:ac| technology platform and supported software
==============================================================

|acquia-product:ac| runs on the following technology stack:

.. list-table::
   :widths: 50 50 
   :header-rows: 1

   * - Component
     - Version
   * - **Web server OS**
     - Ubuntu 16.04 (`changelog <https://wiki.ubuntu.com/XenialXerus/ReleaseNotes>`__)
   * - **Web server**
     - Apache 2.4.18 (`upgrade notes <https://httpd.apache.org/docs/2.4/upgrading.html>`__)
   * - **Load Balancer** 
     - Nginx 1.12.1 (`changelog <https://nginx.org/en/CHANGES-1.12>`__)
   * - **Database**
     - Percona Server 5.6 (`changelog <https://www.percona.com/doc/percona-server/5.6/release-notes/release-notes_index.html>`__)
       (MySQL 5.6 (`changelog <http://changelogs.ubuntu.com/changelogs/pool/universe/m/mysql-5.6/mysql-5.6_5.6.33-0ubuntu0.14.04.1/changelog>`__)
   * - PHP
     - PHP 5.6.34 (`changelog <http://php.net/ChangeLog-5.php>`__), 
       PHP 7.1.17 (`changelog <http://php.net/ChangeLog-7.php#7.1.15>`__), 
       PHP 7.2.5 (`changelog <http://php.net/ChangeLog-7.php#7.2.5>`__)
   * - **Caching proxy and load balancer**
     - Varnish 4.1.8 (`changelog <https://github.com/varnishcache/varnish-cache/blob/master/doc/changes.rst>`__)
       Nginx (`changelog <http://changelogs.ubuntu.com/changelogs/pool/universe/n/nginx/nginx_1.1.19-1ubuntu0.7/changelog>`__)
   * - **Memory cache**
     - memcached 1.5.1 (`changelog <https://launchpad.net/ubuntu/precise/+source/memcached/+changelog>`__), 
       memcached 2.2.0

.. admonition:: Notes regarding memcached

    -  To use memcached 2.2.0 with PHP 5.6, add the following code to your
        settings file:

       .. code-block:: none
        
          # Drupal 7 $conf['memcache_extension'] = 'Memcached';
          # Drupal 8 $settings['memcache']['extension'] = 'Memcached';

    -  Memcached is not available on |acquia-product:acfs|

.. _supported:

Supported software and features
-------------------------------

|acquia-product:ac| supports:

-  Your Drupal 8 or Drupal 7 code
-  Drush 5 through 8
-  Integrated version management (Git)
-  SSL Certificates (additional fee required)
-  Automated disaster recovery backup
-  Custom cron jobs
-  Shell access using SSH
-  File access using sftp and rsync
-  MySQL administration using the MySQL CLI or other tools
-  The current and prior major release of the Chrome, Firefox, Internet
   Explorer, and Safari web browsers

In addition, |acquia-product:ace| supports the following Enterprise
features:

-  High-availability failover using multiple Amazon Web Services data
   centers (Availability Zones)
-  Outgoing VPN access (Cisco VPN compatible - additional fee required)
-  Shared authentication or single sign-on using LDAP or SAML (contact
   your Sales Engineer for cost and compatibility information)
-  Multi-region replication (additional fee required)

All Acquia subscribers receive access to the following Acquia services:

-  |as|_ - Easily add scalable search
   to your website
-  `Insight </acquia-cloud/insight>`__ - Information about your Drupal
   website's optimization and security

Users of Node.js features on |acquia-product:ac| can find stack
information at `Resources and limitations for Node.js
environments </acquia-cloud/node-js/resources>`__.

.. _included:

Included software
-----------------

Your |acquia-product:ac| server includes the following (non-complete)
list of software packages:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Software
     - Version
   * - APCu
     - 4.0.11 (`changelog <https://pecl.php.net/package-changelog.php?package=APCu>`__)
   * - ClamAV
     - 0.99.3 (`changelog <https://github.com/Cisco-Talos/clamav-devel/blob/master/ChangeLog>`__)
   * - Development tools (vim, emacs, gcc)
     - 
   * - Drush 5 through 8 (default version: Drush 8)
     - 5.11, 6.6, 7.1, 8.1.15 (`changelog <https://github.com/drush-ops/drush/releases>`__)
   * - Git
     - 2.7.4
   * - Ghostscript (`changelog <https://ghostscript.com/doc/current/History9.htm>`__)
     - 
   * - jpegtran
     - 
   * - OpenSSL
     - 1.0.2 series (`changelog <http://changelogs.ubuntu.com/changelogs/pool/main/o/openssl/>`__)
   * - pngcrush
     - 
   * - ssh2
     - 0.13 (`changelog <https://pecl.php.net/package-changelog.php?package=ssh2>`__)
   * - sysgdig
     - 0.13.0


The following programming languages are included with
|acquia-product:ac|:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Language
     - Version
   * - C
     - 
   * - Perl
     - 
   * - PHP
     - 5.6.34 (`changelog <http://php.net/ChangeLog-5.php>`__), 7.1.17 (`changelog <http://php.net/ChangeLog-7.php#7.1.15>`__), 7.2.5 (`changelog <http://php.net/ChangeLog-7.php#7.2.5>`__)
   * - Python
     - 2.7.14 (`changelog <https://www.python.org/downloads/release/python-2713/>`__), 3.5.x (`changelog <https://docs.python.org/3.5/whatsnew/changelog.html>`__)
   * - Ruby
     - 2.1.9 (`changelog <http://svn.ruby-lang.org/repos/ruby/tags/v2_1_9/ChangeLog>`__)

.. admonition:: PHP 7 support note

    -  *Drupal 8* - PHP 7 is fully supported on Drupal 8, and the official
       Drupal core test suite passes for all supported database engines
       (including MySQL, SQLite, and PostgreSQL). For details, see `Support
       PHP 7 <https://www.drupal.org/node/2454439>`__ on Drupal.org.
    -  *Drupal 7* - Drupal core `officially
       supports <https://www.drupal.org/docs/7/system-requirements/overview>`__
       PHP 7. Acquia recommends fully testing before upgrading your
       production website, as there are several `backwards incompatible
       changes <http://php.net/manual/en/migration70.incompatible.php>`__.

|acquia-product:ac| also includes the following items:

-  Common Linux command-line utilities
-  Standard networking tools (including curl, wget, and traceroute)
-  Performance analysis tools (including ps, top, and strace).
-  Common PEAR and PECL libraries
-  Common PHP modules (including PDO, FreeTDS, OpenSSL, json, curl, and
   xml). For detailed information, go to your Drupal website's PHP
   information page at ``/admin/reports/status/php``

.. _unsupported:

Unsupported software
--------------------

|acquia-product:ac| does not support the following software:

-  Moodle (not compatible with high availability)
-  piwik (we have repeatedly seen this cause performance issues)
-  Any non-Drupal Content Management System (CMS)
-  CA Single Sign-on (formerly CA SiteMinder)

The following software cannot be installed on |acquia-product:ac|:

-  Non-standard database software, such as Oracle or Microsoft SQL
   Server
-  Custom daemons or services, such as Jabber or Microsoft Exchange
-  Custom package installations that require ``apt-get``

You can still install custom executables using your code repository.

Some Drupal contributed modules are incompatible with
|acquia-product:ac|, or may require special configuration or care. For
more information, see `Module incompatibilities with
Acquia Cloud </acquia-cloud/develop/drupal/module-incompatibilities>`__.

.. _config:

Configuration changes
---------------------

The |acquia-product:ac| platform uses configuration management systems
to ensure stability and consistency. As a result, we do not support
custom OS configuration changes, nor are we able to make arbitrary
customizations to configuration files such as Apache virtualhosts. Among
other problems, such changes can cause your installation to fall outside
the test suite for releases and upgrades, and any changes may not
reliably survive a relaunch.

Supported customizations include:

-  `Custom Varnish
   configuration </acquia-cloud/performance/varnish/custom>`__
-  `Custom Apache Solr search configuration </acquia-search/config>`__
-  `.htaccess
   changes </acquia-cloud/manage/htaccess>`__

.. |as| replace:: \ |acquia-product:as|\
.. _as: /acquia-search