.. include:: /common/global.rst

Modules and applications incompatible with |acquia-product:ac|
==============================================================

|acquia-product:ac| module and application issues

-  Do not use
-  `Caution </acquia-cloud/develop/drupal/module-caution>`__

The |acquia-product:ac| platform and security require permissions and
installs to be built in a particular fashion. This can sometimes cause
incompatibilities with Drupal contributed modules.

Note

For information on other software that is incompatible with
|acquia-product:ac|, see `Unsupported
software </acquia-cloud/develop/non-drupal#unsupported>`__.

+-----------------------------------+-----------------------------------+
| Module/App                        | Issue                             |
+===================================+===================================+
| `ApacheSolr                       | Customers are unable to modify    |
| file <https://www.drupal.org/proj | the ``solrconfig.xml`` file on    |
| ect/apachesolr_file>`__           | |acquia-product:ac|.              |
+-----------------------------------+-----------------------------------+
| `APC <https://www.drupal.org/proj | Alternative PHP cache is not      |
| ect/apc>`__                       | recommended on                    |
|                                   | |acquia-product:ac|. It stores    |
|                                   | data on a per-server basis, which |
|                                   | can lead to different data being  |
|                                   | served by different servers. It   |
|                                   | also uses memory that would       |
|                                   | otherwise be used by OPcache. We  |
|                                   | recommend `using                  |
|                                   | Memcached </acquia-cloud/performa |
|                                   | nce/memcached>`__                 |
|                                   | instead.                          |
+-----------------------------------+-----------------------------------+
| `AutoSlave <https://www.drupal.or | The |acquia-product:ac| platform  |
| g/project/autoslave>`__           | is configured to auto-detect the  |
|                                   | primary and subordinate servers   |
|                                   | and handle failover situations.   |
|                                   | This module hardcodes the         |
|                                   | settings and can cause your       |
|                                   | server to read or write to the    |
|                                   | incorrect database.               |
+-----------------------------------+-----------------------------------+
| Background Process                | The Background Process Apache     |
|                                   | server status module is not       |
|                                   | compatible with the               |
|                                   | |acquia-product:ac| platform.     |
+-----------------------------------+-----------------------------------+
| `Backup and                       | Not supported on                  |
| Migrate <https://www.drupal.org/p | |acquia-product:ac|. For more     |
| roject/backup_migrate>`__         | information, see `Backup and      |
|                                   | Migrate module not supported on   |
|                                   | |acquia-product:ac| <%5Bacquia-pr |
|                                   | oduct:kb%5Darticle/backup-and-mig |
|                                   | rate-module-not-supported-acquia- |
|                                   | cloud>`__.                        |
+-----------------------------------+-----------------------------------+
| `Block Cache                      | This module causes issues with    |
| Alter <https://www.drupal.org/pro | caching, and has not been updated |
| ject/blockcache_alter>`__         | in several years. It is not       |
|                                   | recommended for use.              |
+-----------------------------------+-----------------------------------+
| `Boost <https://www.drupal.org/pr | This creates many disk writes,    |
| oject/boost>`__                   | which can cause problems on       |
|                                   | shared servers. See `Boost and    |
|                                   | |acquia-product:ac| <%5Bacquia-pr |
|                                   | oduct:kb%5Darticles/boost-acquia- |
|                                   | cloud>`__                         |
|                                   | for more details.                 |
+-----------------------------------+-----------------------------------+
| `CiviCRM <https://www.drupal.org/ | CiviCRM is dependent on stored    |
| project/civicrm>`__               | procedures and triggers that do   |
|                                   | not work on the                   |
|                                   | |acquia-product:ac| platform.     |
+-----------------------------------+-----------------------------------+
| `Configuration                    | This module requires a writeable  |
| Management <https://www.drupal.or | directory that is also trackable  |
| g/project/configuration>`__       | at the same time by Git; this is  |
|                                   | not currently possible on         |
|                                   | |acquia-product:ac|.              |
+-----------------------------------+-----------------------------------+
| `Facebook                         | Require session cookies to be     |
| Connect <https://www.drupal.org/p | set, preventing Varnish from      |
| roject/fbconnect>`__              | caching pages.                    |
+-----------------------------------+-----------------------------------+
| `File                             | The File Cache module moves       |
| Cache <https://www.drupal.org/pro | caching to Gluster, which can     |
| ject/filecache>`__                | cause major load on the Gluster   |
|                                   | file system and can cause the     |
|                                   | site (or multiple sites in the    |
|                                   | case of shared hosting) to go     |
|                                   | down.                             |
+-----------------------------------+-----------------------------------+
| File Conveyor                     | GlusterFS, used by                |
|                                   | |acquia-product:ace|, does not    |
|                                   | support ``inotify``, which this   |
|                                   | module requires for operation.    |
|                                   | However, this is related to       |
|                                   | content delivery networks (CDNs)  |
|                                   | and using Origin Pull mode will   |
|                                   | still work.                       |
+-----------------------------------+-----------------------------------+
| `Global                           | Sets session cookies to filter    |
| Filter <https://www.drupal.org/pr | views, which prevents Varnish     |
| oject/global_filter>`__           | from caching pages.               |
+-----------------------------------+-----------------------------------+
| `IP Geolocation Views &           | Require session cookies to be     |
| Maps <https://www.drupal.org/proj | set, preventing Varnish from      |
| ect/ip_geoloc>`__                 | caching pages.                    |
+-----------------------------------+-----------------------------------+
| `Memcache                         | Although not incompatible, Acquia |
| Storage <https://www.drupal.org/p | discourages using this module's   |
| roject/memcache_storage>`__       | due to its developer's limited    |
|                                   | updates. Instead, Acquia          |
|                                   | encourages the use of the         |
|                                   | `Memcache API and                 |
|                                   | Integration <https://www.drupal.o |
|                                   | rg/project/memcache>`__           |
|                                   | module, which integrates better   |
|                                   | with Acquia's memcached           |
|                                   | implementation.                   |
+-----------------------------------+-----------------------------------+
| Mobile Tools                      | Mobile Tools prevents the use of  |
|                                   | Varnish. See `Enabling            |
|                                   | device-based                      |
|                                   | redirects </acquia-cloud/develop/ |
|                                   | mobile>`__                        |
|                                   | for other options that work with  |
|                                   | |acquia-product:ac|.              |
+-----------------------------------+-----------------------------------+
| `Purge <https://www.drupal.org/pr | The Purge (7.x-1.x) module is not |
| oject/purge>`__                   | specifically incompatible, but    |
|                                   | can be difficult to set up        |
|                                   | correctly. We suggest using       |
|                                   | `Acquia                           |
|                                   | Purge <https://www.drupal.org/pro |
|                                   | ject/acquia_purge>`__             |
|                                   | instead. It is specifically       |
|                                   | intended for use on               |
|                                   | |acquia-product:ac|. Over time,   |
|                                   | these modules are planned to      |
|                                   | merge.                            |
+-----------------------------------+-----------------------------------+
| `reCAPTCHA <https://www.drupal.or | Require session cookies to be     |
| g/project/recaptcha>`__           | set, preventing Varnish from      |
|                                   | caching pages.                    |
+-----------------------------------+-----------------------------------+
| `Role memory                      | This module overrides memory      |
| limit <https://www.drupal.org/pro | limits set in ``settings.php``.   |
| ject/role_memory_limit>`__        |                                   |
+-----------------------------------+-----------------------------------+
| `Serial                           | Serial is based on an             |
| Field <https://www.drupal.org/pro | ``auto_increment`` of 1.          |
| ject/serial>`__                   | `|acquia-product:ac| uses an      |
|                                   | ``auto_increment`` of             |
|                                   | 5. <%5Bacquia-product:kb%5Darticl |
|                                   | e/why-do-node-ids-increment-more- |
|                                   | one>`__                           |
+-----------------------------------+-----------------------------------+
| `Session                          | Requires session cookies to be    |
| API <https://www.drupal.org/proje | set, preventing Varnish from      |
| ct/session_api>`__                | caching pages.                    |
|                                   | Session API sets cookies on the   |
|                                   | user. Because of this, cron can   |
|                                   | run intense queries to join the   |
|                                   | ``session`` and ``session_api``   |
|                                   | tables. This can cause major      |
|                                   | slowdowns.                        |
+-----------------------------------+-----------------------------------+
| `Session Cache                    | This module is generally          |
| API <https://www.drupal.org/proje | incompatible with Varnish         |
| ct/session_cache>`__              | caching. It may also cause file   |
|                                   | system performance issues.        |
+-----------------------------------+-----------------------------------+
| `Shibboleth                       | Shibboleth is not supported on    |
| Authentication <https://www.drupa | |acquia-product:ac|. Other        |
| l.org/project/shib_auth>`__       | methods of achieving this         |
|                                   | functionality are                 |
|                                   | `SimpleSAMLphp <%5Bacquia-product |
|                                   | :kb%5Darticles/using-simplesamlph |
|                                   | p-acquia-cloud-site>`__           |
|                                   | or                                |
|                                   | `LDAP </acquia-cloud/develop/ldap |
|                                   | >`__.                             |
+-----------------------------------+-----------------------------------+
| `Smart                            | This module can be configured to  |
| IP <https://www.drupal.org/projec | set session cookies for anonymous |
| t/smart_ip>`__                    | users, making it incompatible     |
|                                   | with Varnish.                     |
+-----------------------------------+-----------------------------------+
| `Supercookie <https://www.drupal. | Stores sessions outside of the    |
| org/project/supercookie>`__       | session table, and sets no cache  |
|                                   | headers. This module is also      |
|                                   | incompatible with Varnish.        |
+-----------------------------------+-----------------------------------+
| `TB Mega                          | This module can cause performance |
| Menu <https://www.drupal.org/proj | problems for your website and is  |
| ect/tb_megamenu>`__               | not covered by Drupal's security  |
|                                   | policy. If it must be used,       |
|                                   | `patch <https://www.drupal.org/no |
|                                   | de/2370309>`__                    |
|                                   | the module to reduce calls made   |
|                                   | to your website's database.       |
+-----------------------------------+-----------------------------------+
| `Text                             | Require session cookies to be     |
| Size <https://www.drupal.org/proj | set, preventing Varnish from      |
| ect/textsize>`__                  | caching pages.                    |
+-----------------------------------+-----------------------------------+
| `Varnish <https://www.drupal.org/ | This Drupal module attempts to    |
| project/varnish>`__               | replicate the effort of the       |
|                                   | Varnish Cache that is already     |
|                                   | available to |acquia-product:ac|  |
|                                   | applications. It will not work    |
|                                   | with |acquia-product:ac|          |
|                                   | applications because it requires  |
|                                   | connections to the load           |
|                                   | balancers, which Acquia does not  |
|                                   | provide. The Varnish caching      |
|                                   | provided by Acquia works out of   |
|                                   | the box, as long as you use       |
|                                   | caching.                          |
+-----------------------------------+-----------------------------------+
| `Views Filter                     | This module sets a ``SESSION``    |
| Harmonizer <https://www.drupal.or | cookie, preventing Varnish        |
| g/project/filter_harmonizer>`__   | caching.                          |
+-----------------------------------+-----------------------------------+
