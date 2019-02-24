.. include:: /common/global.rst

Implementing security updates
=============================

Acquia uses an automated process to deploy a security update branch to
the `Remote Administration (RA) environment </ra/environment>`__.

-  Acquia’s security update automation requires that your subscription
   `is correctly set up </ra/requirements>`__. Ensure that all required
   setup is fully implemented.
-  Standard RA subscriptions will only receive security updates using
   Acquia’s automated security update process. It is the responsibility
   of your team to ensure that your website is compatible with the
   automated update process.
-  Premium RA clients may request assistance in ensuring your website is
   compatible with Acquia’s security update automation.
-  Acquia’s security update automation behaves according to `RA
   preferences set per subscription </ra/preferences>`__. Unless these
   preferences are manually set, the default preferences will be used.
-  **Inform-Only** subscriptions will receive a ticket noting
   recommended security updates, but no action will be taken. If you
   would like to receive an update, you must change your preference to
   **Full Deploy**. This can be changed back after the specific update
   is complete.

Premium RA subscriptions which are not compatible with Acquia’s security
update automation will receive updates as quickly as possible, but no
timeline can be guaranteed.

.. _who:

Who is informed?
----------------

In the event of a proactive security update, Acquia informs contacts
designated by team administrators. All tickets initiated by the Remote
Administration team are assigned to the primary contact on the account.
You can edit this list on your `Teams and
Permissions </acquia-cloud/teams>`__ pages.

To ensure that specific team members receive notifications, on your
Teams and Permissions page, add the following permission to the
appropriate team members:

-  Include as a collaborator on all help requests by default

.. _timelines:

Ticket timelines
----------------

Security Updates are implemented using a semi-automated queue. At this
time, automated updates are initiated as follows:

-  When a core security update is announced on
   `drupal.org <https://www.drupal.org>`__. The queue will be initiated
   within 24 hours of the release. Clients should receive tickets within
   24-48 hours.
-  Production websites are periodically scanned for core and module
   security updates.
-  Updates can be initiated at the specific request of the client.

After the queue is initiated, update automation will detect security
updates, initiate the update process, and create a new ticket notifying
your team that an updated branch is ready to test on the RA environment.

Security updates are implemented as depending on your subscription
preferences:

-  **Inform Only** subscriptions - Acquia will send out a security
   update notification for Drupal Core SA releases within 24-48 hours of
   the announcement. These tickets are for notification purposes only
   and no action is required on them. They will be automatically
   resolved. If you would like your subscription updated, set your
   preferences to **Full Deploy**, respond on the initial ticket, and
   both an update and new ticket will be created.
-  **Full Deploy** subscriptions - Acquia's RA team will update all Full
   Deploy subscriptions by using an automated process. Your team will
   receive a new ticket detailing all of the changes after updates have
   been deployed and are ready for testing on the RA Environment. Use of
   this environment prevents any disruption to your ongoing development.

All security updates are implemented as follows:

-  After an update is deployed and a ticket is sent, the time to solve
   the ticket depends on testing and troubleshooting.
-  Moving through each update step requires your approval. Acquia will
   not deploy a secure branch to either your testing or production
   environment without explicit approval by a member of your team.
-  After a tag has been approved, Acquia will move to production as soon
   as possible, or during a scheduled and approved deploy window.

.. _scheduling:

Scheduling Production deploy windows
------------------------------------

If you would like an update deployed to production at a specific time,
Acquia can schedule this update to be performed by automation. This
service is available 24/7.

Be aware of the following items when requesting to schedule production
deploys:

-  To allow time for scheduling, all requests must be made with a
   minimum of one full business day's notice. Although we cannot
   guarantee a window with fewer than 24 hours' notice, we will do our
   best to accommodate these requests, when possible.
-  Be sure to provide a one-hour window in your preferred time zone for
   the deploy, and clearly state your time zone in the ticket. Acquia
   will confirm the window. If the deploy is during `standard business
   hours </support/guide#hours>`__, we will assign it to a member of our
   team to monitor the process.
-  Acquia will begin the update during the window. During standard
   business hours, any delays or issues will be communicated through the
   existing ticket.
-  Production deploy requests occurring outside of the `standard
   business hours </support/guide#hours>`__ for your support region will
   be unmonitored. If your production deploy happens at this time and
   you experience issues, `file a critical support
   ticket </support/tickets#urgency>`__ as per standard procedures for
   critical support.
-  If your production deploy scheduled outside of standard business
   hours does not complete successfully, you will not be notified. If
   the scheduled deploy does not complete successfully, let us know by
   updating the existing ticket and we will assist with rescheduling the
   deploy.
