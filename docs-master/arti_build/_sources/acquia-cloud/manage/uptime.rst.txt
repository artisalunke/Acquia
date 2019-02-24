.. include:: /common/global.rst

Monitoring uptime for your application
======================================

.. admonition:: Unsupported for |acquia-product:acfs|

   If you are an |acquia-product:acfs| customer, uptime monitoring is not
   supported. |learnmore|_ and how to upgrade your
   |acquia-product:ac| subscription.

.. |learnmore| replace:: Learn more about \ |acquia-product:acfs|\ 
.. _learnmore: /acquia-cloud/free

The |acquia-product:ac| uptime monitoring service monitors your Drupal
application's uptime and responsiveness. This service checks your
application every minute to see if it is online and serving pages. The
service does this by loading a special, secure URL (the *canary URL*)
served by the |acquia-product:anc| module. The response to this canary
URL informs |acquia-product:ac| that your application can bootstrap
Drupal, and that all of its database and other basic dependencies are
functioning. The uptime monitoring service also checks other pages on
your application (such as your home page) less frequently and tracks
their response time. Only if the page checks return errors repeatedly
does the uptime monitoring service send an alert that the application is
down. This approach helps minimize false alarms.

Uptime monitoring is a self-service feature you can use to monitor
trends in response times and availability. It does not automatically
notify Acquia Support of application outages or issues. Acquia uses
different systems to monitor the health of an application's servers. If
Acquia detects server issues that may impact application availability
for a prolonged period of time, a proactive ticket will be filed by
Acquia Support. However, not all application issues are caused by server
problems, so uptime monitoring will sometimes catch issues that Acquia's
server monitoring does not.

Websites in maintenance mode will not trigger uptime monitoring alerts.

.. admonition:: Multisite installation note

   Uptime monitoring is not supported for
   `multisite </acquia-cloud/multisite>`__ installations.

   Attempting to enable uptime in a multisite installation can cause
   |acquia-product:ac| to display error messages that uptime is already
   enabled, especially if uptime monitoring was enabled for any other
   application in the multisite installation.

.. _before:

Before you begin
----------------

To use the uptime monitoring service, you must also install and enable
`|acquia-product:anc|
module <https://www.drupal.org/project/acquia_connector>`__ on your
|acquia-product:ac| environment. Acquia recommends that you always use
the latest version of the |acquia-product:anc| module. After you update
or install the |acquia-product:anc| module, go to the **Home > Admin >
Reports** page of your Drupal website, and then click **Status
reports**. In the Acquia SPI section, click the **manually send SPI
data** link to register the presence of the new module with
|acquia-product:ais|. You may need to wait a few minutes before you can
then enable the uptime monitoring service.

Roles and permissions for uptime monitoring

To enable uptime monitoring for an environment, you must have the
appropriate |acquia-product:ac| permission, depending on the
environment:

-  Add or remove domains for non-production environments
-  Add or remove domains for the production environment

By default, users with the *Administrator*, *Team Lead*, and *Senior
Developer* roles have these permissions, while users with the
*Developer* role do not. Learn more about `roles and
permissions </acquia-cloud/teams/roles>`__.

.. _enable:

Enabling uptime monitoring
--------------------------

|acquia-product:acs| subscriptions can enable uptime monitoring only on
their Production environment. |acquia-product:ace| subscriptions can
enable uptime monitoring on any environment.

.. note::  

   Acquia does not recommend that you enable uptime monitoring for
   non-production environments, and if you must use this feature it should
   be disabled whenever possible. Acquia will not troubleshoot historical
   downtime for non-production environments.

To enable uptime monitoring, complete the following steps:

#. `Sign in <https://cloud.acquia.com>`__ to the |acquia-product:ui| as
   a user with the appropriate `permission <#permissions>`__.
#. Select your organization, application, and environment and then, in
   the left menu, click **Uptime**.

   |Click Edit on the Uptime page|

#. On the **Uptime** page, click **Edit**.
#. On the **Edit Uptime settings** page, select the **Enable uptime
   monitoring** check box.

   |Enable uptime monitoring|

#. Click **Save**.

As an alternative, you can also use the following procedure:

#. `Sign in <https://cloud.acquia.com>`__ to the |acquia-product:ui| as
   a user with the appropriate `permission <#permissions>`__.
#. In the **Uptime monitoring** section for the environment you want to
   monitor, click **Enable Uptime**.
#. On the **Uptime** page, click **Edit**.
#. On the **Edit Uptime settings** page, select the **Enable uptime
   monitoring** check box.
#. Click **Save**.

.. _view:

Viewing the uptime graph
------------------------

To view information about an environment's uptime, select the list view
for your application. In the **Uptime monitoring** section, the uptime
graph displays your application's responsiveness over time, measured in
milliseconds.

|Uptime graph|

The graph displays the environment's response with bars colored
according to the response:

-  **OK** - Normal response
-  **Impaired** - Impaired response
-  **Error** - Uptime monitoring configuration error or DNS error
-  **Down** - Environment is not reachable

You can use the date menu to change the time period of the data
presented in the graph.

Note

Currently, all uptime monitoring requests originate from the AWS US-East
region. If your servers are located outside of the US-East region,
response times reported by the uptime monitoring service will tend to be
longer than those experienced by website visitors who are located closer
to your servers.

.. _email:

Receiving email notifications
-----------------------------

You can enable email notifications of environment uptime issues. If you
do so, the uptime monitoring service will send an email notification
after three consecutive minutes of errors. This threshold helps reduce
false alarms. You cannot customize this three-minute threshold.

To enable email notifications, complete the following steps:

#. On the **Uptime** page, select **Enable alerts**.
#. Enter one or more email addresses, separated by commas, to which
   uptime alerts should be sent, and then click **Update settings**.

.. _errors:

Getting more information about errors
-------------------------------------

When the uptime service receives an error, a notification of the error
is sent and displayed in the `Insight notification
list </acquia-cloud/notify>`__. The notification describes the type of
error and possible causes. The following categories of errors are
reported:

-  **Site down**. Here are some possible causes:

   -  New code was deployed which may contain an error in the PHP that
      requires a code rollback. Check your PHP error logs for any fatal
      errors.
   -  A new module was enabled and it has created an error condition on
      the website. Disable the module.
   -  Caches were recently cleared and the website is hitting a memory
      limit when attempting to rebuild the cache.

-  **Site impaired**. The website is returning errors for some, but not
   all, of the pages Acquia monitors.
-  **Site online**. The website has come back online.
-  **Site in Maintenance mode**. The website reports that it is in
   Drupal maintenance mode.
-  **Site health monitoring configuration error.** The website is not
   responding to testing. Ensure that the |acquia-product:anc| is
   enabled, the module version is 8.x-1.7, 7.x-2.13, or later, and that
   the website is connected to |acquia-product:ais|.
-  **Site not responding**. This could be due to general internet
   connectivity issues, or the servers hosting the website may be
   offline. If your website is hosted with Acquia and the servers
   powering it are down, we will be opening a support ticket with you
   shortly.
-  **Site DNS error**. The DNS record for the website is failing to
   resolve, meaning we did not receive a timely response during a DNS
   lookup. This usually means either that your DNS provider or registrar
   is having an issue, or that there are networking issues outside of
   Acquia's control. DNS resolution problems are often resolved very
   quickly. If you can load the domain, the issue may be localized or
   already resolved. Acquia cannot investigate DNS errors.

.. _trouble:

Troubleshooting
---------------

To function, the uptime monitoring service needs to be able to receive
an HTTP 200 response from your homepage, the
``https://[site_URL]/filter/tips`` page, and the canary URL,
``https://[site_URL]/system/acquia-connector-status``. If, when you
first enable uptime monitoring, the Site Health graph displays errors,
the most likely causes are:

-  The |acquia-product:anc| module on your environment is not
   up-to-date.
-  |acquia-product:ais| has not yet received confirmation from your
   environment that the |acquia-product:anc| module has been updated.
   Check the last connection date and time shown under **Connection
   history** on the environment's `Insight
   page </acquia-cloud/insight/using>`__. `Run
   cron <https://www.drupal.org/node/158922>`__, if it has not run
   recently.
-  The uptime monitoring service cannot reach the canary URL, the
   ``/filter/tips`` page, or your homepage because it is being
   redirected or blocked. This might happen if the canary URL is
   password-protected, is being affected by redirect rules, or if query
   strings are being stripped out.

If you have questions about an alert and your |acquia-product:aqs|
entitles you to open support tickets, you can `contact Acquia
Support </support#contact>`__. The uptime monitoring service may detect
momentary, transient issues on a website, or in the network between our
service and a website's servers. For this reason, Acquia Support will
not investigate momentary outages. We will, however, investigate
recurring instances of partial or complete downtime detected by this
feature, or issues which are currently in progress. Furthermore, Support
will not investigate DNS errors, which usually mean either that your DNS
provider or registrar (often the same) is having an issue, or that there
are networking issues outside of Acquia's control.

.. |Click Edit on the Uptime page| image:: https://cdn2.webdamdb.com/1280_EMWZZ76C3JG4.png?1526475715

.. |Enable uptime monitoring| image:: https://cdn4.webdamdb.com/1280_kDFwRiNJX0J8.png?1526475663

.. |Uptime graph| image:: https://cdn3.webdamdb.com/1280_sb3Ja5bVDZY7.png?1526475590

