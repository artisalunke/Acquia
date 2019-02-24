.. include:: /common/global.rst

Keeping content synchronized
============================

The Acquia Content Hub Status module, included with |acquia-product:ch|,
provides you a Drush command and cron job you can use to verify that
your imported content is synchronized with the latest content updates
that have been pushed to |acquia-product:ch|. The module compares recent
entity events from the history API endpoint against the already imported
entities to determine if they match.

You can configure how many minutes must pass before content is
considered stale, how far back in your log events to check, and what
email addresses to notify if stale content is discovered.

Configuring synchronization monitoring
--------------------------------------

To configure synchronization monitoring, you will need to identify the
content types that you want to monitor, configure how far back in time
you want each check to extend, and configure how many minutes an entity
can be out of date before |acquia-product:ch| sends notifications.

Identify content types to monitor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure the content types that you want to monitor, perform the
following steps:

#. Sign in to |acquia-product:ch|.
#. Go to the Modules page by using one of the following methods:

   -  In the top menu, click **Extend**.
   -  In your browser's address bar, go to
      ``http://[your_site]/admin/modules`` (where ``[your_site]`` is
      your website's URL).

#. In the module list, find **Acquia Content Hub Status**, and then
   select its check box.
#. Scroll to the bottom of the webpage, and then click **Install**.
#. In the top menu, click **Configuration**.
#. Scroll to **Web Services**, and then click **Acquia Content Hub**.
#. By default, all syndicated entities are enabled to updates, unless
   changes are made to the entity on the subscribing website, or if the
   entity on the subscribing website is manually edited to disable
   updates:

   |Updates are enabled on this entity|

Now that you have selected the content types you want to monitor, you
should configure the status checks.

Configure status checks
~~~~~~~~~~~~~~~~~~~~~~~

Entities will be examined during cron runs if the **Acquia Content Hub
Status** module is enabled. To configure these status checks, perform
the following steps:

#. Sign in to |acquia-product:ch|.
#. In the top menu, click **Configuration**.
#. Scroll to the **Web Services** section, and then click **Acquia
   Content Hub**.
#. Click **Content Hub Status**.
#. In the **Threshold** list, click the number of minutes that an entity
   can be behind the entity published in |acquia-product:ch|.
   Differences larger than this threshold signal that an entity is
   outdated.
#. In the **Limit** list, click the number of last history events to
   review for ``update`` or ``create`` events that may have modified
   entities.
#. If you want notifications to be sent when entities found to be out of
   date, select the **Send Email Notification** check box, and then
   enter the email addresses to notify (one email address per line).

If you want to configure status checks outside of normal cron runs, you
can create a cron job to perform status checks using Drush.

For more information about setting up cron jobs on |acquia-product:ace|
see `Using scheduled jobs to maintain your
application </acquia-cloud/manage/cron>`__. For more information about
cron jobs on |acquia-product:edg|, see `Managing cron tasks using the
management console </site-factory/manage/tasks/factory>`__.

Perform status checks using Drush
---------------------------------

You can use the following Drush command to perform content checks with
scheduled cron jobs or on demand, replacing the ``[limit]`` and
``[threshold]`` values with values that are appropriate for your
website:

``drush acquia-contenthub-status-check [limit] [threshold]``

For most websites, a ``limit`` between ``10`` and ``25`` will be
sufficient, but if you are publishing content very frequently, your
website may need a higher limit. An appropriate ``threshold`` value will
depend on your website's architecture and how frequently your content is
updated, but a value between ``5`` and ``10`` will be appropriate for
many websites.

If you set up the check as a cron job, the cron job will scan for
entities that became outdated since the last cron run.

.. note::  

   If you receive a ``You have requested a non-existent service`` error
   message, verify that the Acquia Content Hub Status module is enabled.

.. |Updates are enabled on this entity| image:: https://cdn2.webdamdb.com/1280_IjxKQpMecBJ5.png?1526475631
   :width: 334px
   :height: 214px
