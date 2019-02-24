.. include:: /common/global.rst

Sending information to |acquia-product:ais|
===========================================

.. container:: internal-navigation

   **Using Acquia Insight**

   * :doc:`Intro </acquia-cloud/insight>`
   * :doc:`Using </acquia-cloud/insight/using>`
   * :doc:`Alerts </acquia-cloud/insight/alerts>`
   * :doc:`Modules <acquia-cloud/insight/code>`
   * :doc:`Connector </acquia-cloud/insight/install>`
   * Configure


The |acquia-product:ais| service needs information from the environments
it monitors to create their overall ratings and to report alert
conditions. Environments send their information to |acquia-product:ais|
using the |acquia-product:anc|. This information includes:

-  General application information, including node counts, user counts,
   and non-sensitive basic information
-  Drupal information, including versions of core and enabled modules
-  Security information, testing some common insecure practices
-  PHP, web server, and database versions, configuration information,
   and statistics

For more detailed information, see `What the |anc|
sends <#details>`__.

.. _configure:

Configuring what the |acquia-product:anc| sends
-----------------------------------------------

After you have `installed and enabled the
|anc| </acquia-cloud/insight/install>`__, you can
configure |acquia-product:anc| to limit the scope of information you
want collected and sent to |acquia-product:ais|.

Note

If your administrative username (*user 1*) is too simple,
|acquia-product:ac| will direct you to change your username for security
reasons. Examples of usernames that must be changed include ``admin``,
``administrator``, and ``root``. Although you can use these phrases in
your username, the overall length for a username with these phrases must
be at least 15 characters.

To configure the |acquia-product:anc| settings, complete the following
steps:

#. Go to the **Configuration > Acquia settings** page:

   -  *Drupal 8.x* - Go to
      ``http://[site_URL]/admin/config/system/acquia-connector``
   -  *Drupal 7.x* - Go to
      ``http://[site_URL]/admin/config/system/acquia-agent``

#. Choose the items that you want to collect and monitor.

   |Connector configuration|

   -  **Admin privileges**

      -  Security information for the application, including privileges
         for anonymous and logged-in users and file security
      -  Number of admin users
      -  Whether or not the User ID 1 account has an insecure username,
         such as *admin* or *root*

   -  **Nodes and users**

      -  Titles and types of the last 15 nodes
      -  Titles of the last 15 comments
      -  User names and email addresses of the last 15 created users

   -  **Watchdog logs**

      -  Last failed log-in attempts
      -  List of page-not-found references
      -  Critical, alert, and emergency watchdog messages

   -  **Source code**

      If you enable this option, |acquia-product:ais| checks whether the
      contents of core or contributed Drupal code files (not custom
      files) have been modified.

#. **Allow Insight to update the list of approved variables**.
#. Clear the **Send via Drupal cron** check box. For best performance,
   it is best not to use Drupal's cron process to send your website's
   information to |acquia-product:ais|. Instead, set up a server cron
   process to send the information, as described in `Using server cron
   to send information <#crontab>`__.

.. _crontab:

Using server cron to send information
-------------------------------------

For best performance, set up a server cron process to send your
environment's information to |acquia-product:ais|. Follow this procedure
to add a command for each of your environments in the
|acquia-product:ui| on the **Applications > [Environment] > Scheduled
Jobs** page.

#. On the **Configuration > Acquia settings** page of your Drupal
   website, clear the **Send via Drupal cron** check box. With that
   check box cleared, the page displays the Acquia SPI URL, which is in
   the form ``http://[site URL]/system/acquia-spi-send?key=a1b2c3e4f5``.
#. Sign in to the |cloud-ui|.
   and open the **Scheduled Jobs** page for your application and
   environment.
#. Click **Add job**.
#. In the **Job name** field, enter a name for the job to identify it in
   the |acquia-product:ui|.
#. Under **Command**, enter a command like the following, using the
   Acquia SPI URL from step 1. Do not include a cron time string. For
   example:

   ``/usr/bin/wget -O - -q -t 1 http://[Acquia SPI URL]``

#. Under **Command frequency**, set the cron schedule. Note that the
   time zone for the schedule is UTC. We recommend that you set the cron
   schedule to run not more frequently than once per hour and not less
   frequently than once a day.
#. Click **Add**.

For more information, see `Using scheduled jobs to maintain your
application </acquia-cloud/manage/cron>`__.

|Configure a cron task on |acquia-product:ac||

.. _details:

What the |acquia-product:anc| sends
-----------------------------------

With its default settings, the |acquia-product:anc| sends the following
information to |acquia-product:ais|:

-  General application information, including node counts, user counts,
   and non-sensitive basic information
-  System variables that enable |acquia-product:ais| to check whether
   your application is responding to requests or in maintenance mode, as
   well as your application's performance and implementation of best
   practices
-  Drupal information, including versions and enabled modules
-  A list of all Drupal code files, including the last change date, the
   user and group of the file owner, and the hash value
-  PHP, web server, and database information, including:

   -  PHP version, extensions, memory limit, maximum post and upload
      size, and cookie lifetime
   -  OS version, Apache version, configuration variables, and running
      statistics
   -  MySQL version, configuration variables, database cache statistics
      and other running statistics

-  Security information, including information needed to check whether:

   -  Drupal installation files and directories are writable by the
      server, except as required.
   -  Users with untrusted roles are allowed to input dangerous HTML
      tags or use the PHP input format.
   -  Dangerous tags were found in any submitted content (fields).
   -  Error reporting is set to a log only, rather than to the screen.
   -  The private files directory is outside the web server root.

.. _never:

Information *never* sent by the |acquia-product:anc|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The |acquia-product:anc| does *not* expose the following information to
|acquia-product:ais|:

-  Passwords or password hashes
-  System-level user account names (excluding system accounts that own
   Drupal code files)
-  Contents of custom files or modules

.. _tech:

How the |acquia-product:anc| connects to Acquia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The |acquia-product:anc|, for Drupal 8, is comprised of two modules:
Acquia Insight and Search. In the 7.x versions, the Acquia Insight
module is divided into separate Acquia Agent and Acquia Site Profile
Information modules. These modules are responsible for retrieving,
parsing, and communicating data between the client (a Drupal website
with modules installed), and the server (|acquia-product:ais|).

All communications between the Drupal application and
|acquia-product:ais| happen with XML-RPC over HTTPS, with the exception
of one case (SPI makes simple HTTPS GET requests to |acquia-product:ais|
for read-only data). Message authenticity and integrity is maintained by
including message authentication code (HMAC) components in the request
and response. This is helpful for secure communications in cases where
the client application does not support SSL. The client and the server
share a private key that's used to sign and validate messages. Messages
are outgoing from the client to the server, except for one feature of
the Insight service that allows for comparing Drupal core and
contributed module code that is invoked by the server.

The SPI module sends configuration and system information for use in the
Insight service. The Search module sends application content to be
indexed by Apache Solr as part of |acquia-product:as|. Information is
sent by default as part of the Drupal cron system, though the
|acquia-product:anc| can be `configured to send data
separately <#crontab>`__. See the `Agent test
module <http://drupalcode.org/project/acquia_connector.git/blob/refs/heads/7.x-2.x:/acquia_agent/tests/acquia_connector_test.module>`__
for a list of server-side XML-RPC methods (though full validation is not
replicated) .

.. _interval:

When the |acquia-product:anc| connects to Acquia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The |acquia-product:anc| module sends information to
|acquia-product:ais| when your environment runs cron, and Insight
updates your environment's scores and alerts every 30 minutes, so you
can expect changes you make to your environment to be reflected in your
Insight scores after 30 minutes plus your environment's cron interval.
Module information is updated not more than every 22 hours, regardless
of the cron interval. Some other information is updated not more than
every six hours. You can cause Insight to update more quickly by sending
information to Insight manually. Do this on your Drupal
application's **Admin > Reports > Status report** page, under **Acquia
SPI**, by clicking **manually send SPI data**.

.. |Connector configuration| image:: https://cdn4.webdamdb.com/md_o3vlYwkUPpN9.png?1526475527
   :alt: Connector configuration fields
.. |Configure a cron task on |acquia-product:ac|| image:: https://cdn3.webdamdb.com/md_09GEnRraA01.png?1526475486
   :alt: Configuring a cron job in the UI

.. |anc| replace:: \ |acquia-product:anc|\ 

.. |cloud-ui| replace:: \ |acquia-product:ui|\ 
.. _cloud-ui: https://cloud.acquia.com
