.. include:: /common/global.rst

Modules to use with caution on |acquia-product:ac|
==================================================

|acquia-product:ac| module and application issues

-  `Do not
   use </acquia-cloud/develop/drupal/module-incompatibilities>`__
-  Caution

The following Drupal modules can be used on |acquia-product:ac|, but may
require additional configuration or use cases which could cause
problems:

Note

In addition to the following modules, some modules require symlinks to
work properly on |acquia-product:ac|. For more information, see `File
permissions while using
|acquia-product:ac| <%5Bacquia-product:kb%5Darticles/file-permissions-while-using-acquia-cloud>`__.

+-----------------------------------+-----------------------------------+
| Module/App                        | Issue/Resolution                  |
+===================================+===================================+
| `Adaptive                         | Exercise some care when using     |
| Image <https://www.drupal.org/pro | this module because it may have   |
| ject/adaptive_image>`__           | issues storing image derivatives  |
|                                   | when caching is turned on. When   |
|                                   | this module is in use, users who  |
|                                   | visit a page directly after a     |
|                                   | cache clear will set the image    |
|                                   | size for that page and that image |
|                                   | size is used for all visitors,    |
|                                   | regardless of what their browser  |
|                                   | is.                               |
+-----------------------------------+-----------------------------------+
| `Authcache <https://www.drupal.or | This requires an evaluation of    |
| g/project/authcache>`__           | performance issues versus         |
|                                   | application complexity. Caching   |
|                                   | pages or blocks is often a better |
|                                   | option. This module can           |
|                                   | significantly increase the size   |
|                                   | of your page cache.               |
+-----------------------------------+-----------------------------------+
| `Bean <https://www.drupal.org/pro | Specifically, we recommend        |
| ject/bean>`__                     | against the use of                |
|                                   | ``bean_entitycache``. When        |
|                                   | combined with the Memcache        |
|                                   | module, its behavior is           |
|                                   | unpredictable, and its use can    |
|                                   | have a negative performance       |
|                                   | impact on your application.       |
+-----------------------------------+-----------------------------------+
| `CAS <https://www.drupal.org/proj | Check the **Check with the CAS    |
| ect/cas>`__                       | server to see if the user is      |
|                                   | already logged in** setting. This |
|                                   | requires session cookies to be    |
|                                   | set, preventing Varnish from      |
|                                   | caching pages. We suggest         |
|                                   | `Bakery <https://www.drupal.org/p |
|                                   | roject/bakery>`__                 |
|                                   | or                                |
|                                   | `SimpleSAML <%5Bacquia-product:kb |
|                                   | %5Darticles/using-simplesamlphp-a |
|                                   | cquia-cloud-site>`__              |
|                                   | as an alternative.                |
+-----------------------------------+-----------------------------------+
| `Contact                          | Issue due to its reliance on      |
| Importer <https://www.drupal.org/ | `Open                             |
| project/contact_importer>`__      | Inviter <http://openinviter.com/> |
|                                   | `__.                              |
|                                   | `Create a                         |
|                                   | symlink <%5Bacquia-product:kb%5Da |
|                                   | rticles/adding-flexibility-your-s |
|                                   | erver-structure-using-symlinks>`_ |
|                                   | _                                 |
|                                   | to your private files area.       |
+-----------------------------------+-----------------------------------+
| DBLog                             | Using Drupal core's DBLog module  |
|                                   | can cause performance issues for  |
|                                   | high-traffic applications.        |
|                                   | Instead, Acquia recommends `using |
|                                   | syslog </acquia-cloud/performance |
|                                   | #syslog>`__.                      |
+-----------------------------------+-----------------------------------+
| `DB                               | Using this module improperly can  |
| Maintenance <https://www.drupal.o | potentially cause slowdowns or    |
| rg/project/db_maintenance>`__     | outages. If you believe that your |
|                                   | application has tables that need  |
|                                   | optimizing, `open a ticket with   |
|                                   | Acquia                            |
|                                   | Support </support/tickets>`__.    |
+-----------------------------------+-----------------------------------+
| `Devinci <https://www.drupal.org/ | This module does not include      |
| project/devinci>`__               | settings for the Acquia `Remote   |
|                                   | Administration </ra/environment>` |
|                                   | __                                |
|                                   | environment.                      |
+-----------------------------------+-----------------------------------+
| `Elysia                           | Elysia Cron `requires careful     |
| Cron <https://www.drupal.org/proj | setup <%5Bacquia-product:kb%5Dart |
| ect/elysia_cron>`__               | icles/elysia-cron-acquia-cloud>`_ |
|                                   | _.                                |
|                                   | Acquia Support has seen           |
|                                   | implementations of this module    |
|                                   | that call some hooks too          |
|                                   | frequently, causing performance   |
|                                   | problems significant enough to    |
|                                   | take a production application     |
|                                   | down.                             |
+-----------------------------------+-----------------------------------+
| `Filefield                        | Using this module on              |
| Sources <https://www.drupal.org/p | |acquia-product:ac| causes issues |
| roject/filefield_sources>`__      | with `Acquia Remote               |
|                                   | Administration                    |
|                                   | services </ra/environment#sfp>`__ |
|                                   | .                                 |
|                                   | If you are using this module, it  |
|                                   | conflicts with the Stage File     |
|                                   | proxy module, and you will not be |
|                                   | able to see images on your RA     |
|                                   | environment.                      |
+-----------------------------------+-----------------------------------+
| `Honeypot <https://www.drupal.org | This has a time-based session     |
| /project/honeypot>`__             | variable that can make pages      |
|                                   | uncacheable by Drupal or Varnish  |
|                                   | caches. If you don't use this     |
|                                   | setting, cache should be          |
|                                   | unaffected.                       |
+-----------------------------------+-----------------------------------+
| `HTML                             | `Create a                         |
| Purifier <https://www.drupal.org/ | symlink <%5Bacquia-product:kb%5Da |
| project/htmlpurifier>`__          | rticles/adding-flexibility-your-s |
|                                   | erver-structure-using-symlinks>`_ |
|                                   | _                                 |
|                                   | to your private files area.       |
+-----------------------------------+-----------------------------------+
| `HTTPRL <https://www.drupal.org/p | May require some special          |
| roject/httprl>`__                 | configuration to use on           |
|                                   | |acquia-product:ac|, or it can    |
|                                   | generate errors. `Learn           |
|                                   | more </acquia-cloud/develop/httpr |
|                                   | l>`__.                            |
+-----------------------------------+-----------------------------------+
| `Lightweight Directory Access     | LDAP alone without SSO can work   |
| Protocol                          | on |acquia-product:ac|. SSO       |
| (LDAP) <https://www.drupal.org/pr | requires NTLM (NT LAN Manager)    |
| oject/ldap>`__                    | support, which is an Apache       |
|                                   | module that Acquia does not       |
|                                   | currently support.                |
+-----------------------------------+-----------------------------------+
| `Link                             | The Link Checker module can       |
| Checker <https://www.drupal.org/p | sometime cause timeouts when cron |
| roject/linkchecker>`__            | is run.                           |
+-----------------------------------+-----------------------------------+
| `Node view                        | This statistics module can be     |
| count <https://www.drupal.org/pro | configured to count each node     |
| ject/nodeviewcount>`__            | visit, which can trigger multiple |
|                                   | database writes. This behavior    |
|                                   | can cause serious performance     |
|                                   | issues with the database — use    |
|                                   | caution when configuring this on  |
|                                   | high traffic websites.            |
+-----------------------------------+-----------------------------------+
| `OptimizeDB <https://www.drupal.o | Using this module improperly can  |
| rg/project/optimizedb>`__         | potentially cause slowdowns or    |
|                                   | outages. If you feel your site    |
|                                   | has tables that need optimizing,  |
|                                   | `contact Acquia                   |
|                                   | Support </support#contact>`__.    |
+-----------------------------------+-----------------------------------+
| `Print <https://www.drupal.org/pr | If not properly secured, this     |
| oject/print>`__                   | module can open up your           |
|                                   | application to being abused as a  |
|                                   | spam relay. If you use this       |
|                                   | module, be sure to configure it   |
|                                   | so that anonymous users cannot    |
|                                   | send email.                       |
+-----------------------------------+-----------------------------------+
| `Quick                            | When a page loads, QuickTabs also |
| Tabs <https://www.drupal.org/proj | loads content a user does not     |
| ect/quicktabs>`__                 | immediately see. It creates       |
|                                   | additional links, which can cause |
|                                   | webcrawlers to visit the page     |
|                                   | additional times (2-n times), and |
|                                   | this can cause slowdowns. It also |
|                                   | can consume extra resources when  |
|                                   | in "AJAX Mode" by potentially     |
|                                   | generating multiple simultaneous  |
|                                   | requests to the backend to fetch  |
|                                   | tab content.                      |
+-----------------------------------+-----------------------------------+
| `Radioactivity <https://www.drupa | This module requires that         |
| l.org/project/radioactivity>`__   | memcache servers be hardcoded in  |
|                                   | a separate configuration file,    |
|                                   | which directly conflicts with     |
|                                   | Acquia's high availability        |
|                                   | services. Acquia's platform       |
|                                   | dynamically modifies available    |
|                                   | memcache servers, and hardcoded   |
|                                   | servers can cause application     |
|                                   | outages.                          |
+-----------------------------------+-----------------------------------+
| `Redirect 403 to User             | This may cause issues with        |
| Login <https://www.drupal.org/pro | anonymous session cookies.        |
| ject/r4032login>`__               | Disable the **Access denied. You  |
|                                   | must log in to view this page.**  |
|                                   | check box in the module settings. |
+-----------------------------------+-----------------------------------+
| `Search                           | This useful module triggers a     |
| 404 <https://www.drupal.org/proje | search when a user lands on a 404 |
| ct/search404>`__                  | page. This is best used with      |
|                                   | `Fast                             |
|                                   | 404 <%5Bacquia-product:kb%5Dartic |
|                                   | les/using-fast-404-drupal>`__     |
|                                   | to prevent missing files from     |
|                                   | also triggering a search.         |
+-----------------------------------+-----------------------------------+
| Statistics                        | Using Drupal core's statistics    |
|                                   | module `can cause performance     |
|                                   | issues </acquia-cloud/performance |
|                                   | #statistics>`__                   |
|                                   | for high-traffic applications.    |
+-----------------------------------+-----------------------------------+
| `TCPDF <https://www.drupal.org/pr | `Create a                         |
| oject/tcpdf>`__                   | symlink <%5Bacquia-product:kb%5Da |
|                                   | rticles/adding-flexibility-your-s |
|                                   | erver-structure-using-symlinks>`_ |
|                                   | _                                 |
|                                   | to your private files area.       |
+-----------------------------------+-----------------------------------+
| `Workbench                        | This module does not work out of  |
| Moderation <https://www.drupal.or | the box with ApacheSolr search    |
| g/project/workbench_moderation>`_ | integration. `Learn more about    |
| _                                 | problems and a                    |
|                                   | solution <%5Bacquia-product:kb%5D |
|                                   | articles/workbench-moderation-can |
|                                   | -cause-problems-apachesolr>`__.   |
+-----------------------------------+-----------------------------------+
| `WURFL <https://www.drupal.org/pr | `Create a                         |
| oject/wurfl>`__                   | symlink <%5Bacquia-product:kb%5Da |
|                                   | rticles/adding-flexibility-your-s |
|                                   | erver-structure-using-symlinks>`_ |
|                                   | _                                 |
|                                   | to your private files area.       |
+-----------------------------------+-----------------------------------+
| `WYSIWYG                          | `Create a                         |
| CKFinder <https://www.drupal.org/ | symlink <%5Bacquia-product:kb%5Da |
| project/WYSIWYG-CKFinder>`__      | rticles/adding-flexibility-your-s |
|                                   | erver-structure-using-symlinks>`_ |
|                                   | _                                 |
|                                   | to your private files area.       |
+-----------------------------------+-----------------------------------+

.. _other:

Additional module issues
------------------------

When you use modules that upload multiple files, applications with
multiple web servers may see writes to different servers for each file
that is uploaded. When the upload process is complete, the module cannot
find all of the images and fails. Customers who have a single web server
for their Staging and Development environments and multiple web servers
for their Production environment will likely see these modules work in
Staging and Development, but fail in the Production environment.
`Plupload <https://www.drupal.org/project/plupload>`__ is an option, but
also read `Correcting broken file
uploads </acquia-cloud/develop/files/broken>`__.
