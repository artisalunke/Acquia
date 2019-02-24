.. include:: /common/global.rst

What to do if your application is down
======================================

If you are using the `Acquia uptime monitoring
feature </acquia-cloud/manage/uptime>`__ and it reports that your
application is down, here are some steps to take to identify and resolve
the problem:

-  **Check the Acquia status page**

   The `Acquia status page <http://status.acquia.com>`__ reports issues
   that Acquia is aware of that affect our customers' applications,
   including Amazon Web Services issues, external DNS issues, or other
   incidents. In some cases, your applications may be down due to global
   issues that are beyond your control. Incidents that cause
   applications to be down are treated as the highest level of severity
   and Acquia works continuously until they are resolved. Acquia updates
   the status page regularly until the incident is resolved. You can
   also follow the Acquia Support Twitter account at
   `@acquia_support <https://twitter.com/acquia_support>`__.

-  **Check the Acquia Cloud interface Stack Metrics and Production
   environment Overview pages**

   The |acquia-product:ui| provides valuable information about your
   application's health.

   The `Stack Metrics </acquia-cloud/monitor/stackmetrics>`__ page
   reports on your application's CPU, memory, and storage usage. If your
   disk storage space is full, that can cause your applications to go
   down.

   The **Overview** page for an environment shows a task log. Examine
   the task log and look for failed tasks. Check whether there have been
   any changes to the code or database in your Production environment
   that might have caused your application to go down.

-  **Check the logs**

   Check your server error and access logs for errors. For information
   about what to look for, see `Searching the error logs to troubleshoot
   problems </articles/searching-error-logs-troubleshoot-problems>`__.

   You can download your logs from the **Logs** page. For more
   information, see |aboutlogging|_.

 
   .. |aboutlogging| replace:: About \ |acquia-product:ac|\  logging
   .. _aboutlogging: /acquia-cloud/monitor/logs

-  **Contact Acquia Support**

   If your Acquia subscription entitles you to file support tickets, you
   can `contact Acquia Support </support#contact>`__. In general, if
   your application is down due to a global issue noted on the Acquia
   status page, there is no need to create a ticket. Contact Acquia
   Support if an issue is particular to your application.
