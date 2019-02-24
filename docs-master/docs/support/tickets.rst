.. include:: /common/global.rst

Support and TAM ticket information
==================================

.. toctree::
   :hidden:
   :glob:

   /support/tickets/*

If you have 
`access to support tickets </support/guide#ticket_limitations>`__ with your subscription,
filing a ticket with Acquia Support (or, depending on your subscription,
your Technical Account Manager) is as easy as signing in to your Acquia
account, and then visiting the following URL:

**https://insight.acquia.com/support/tickets/new**

Before creating a ticket
------------------------

Before creating a ticket, find out whether your problem is a known issue
by checking the following resources:

-  `Visit the Acquia Status page <https://status.acquia.com>`__ to ensure that 
   Acquia systems are operational . You can click 
   **Subscribe to Updates** on the Status page to receive updates whenever 
   Acquia creates or updates an incident.
-  `Follow Acquia Support on Twitter <https://twitter.com/acquia_support>`__.
-  Search for existing Acquia documentation that relates to your issue.

Creating a Support or TAM ticket
--------------------------------

To create a ticket, you must have an Acquia subscription that allows it
and you must not have used all of your provided support or TAM tickets.
For more information, see the `Support Users Guide </support/guide>`__.

On the ticket creation screen, select whether you want to create a
*Support Ticket* or a *TAM Request*. Enter information about the issue
you're experiencing — including its `urgency <#urgency>`__, if a Support
ticket — an `effective description <#description>`__ of your problem,
and then click **Create**.

You can also create a ticket by signing in to the |acquia-product:ui|,
clicking **Help Center** on the Acquia navigation bar, and then clicking
either **Create TAM request** or **Create support ticket**.

|Create a ticket|


Entering Ticket field information
---------------------------------

The following information will help you determine what to enter in the
ticket creation fields so that Acquia Support can best help you in a
timely manner.


Support tickets: urgency
~~~~~~~~~~~~~~~~~~~~~~~~

Support tickets have an urgency level. This value determines how quickly
Acquia Support will respond to the request and does not impact a
ticket's time-to-resolution. Here's what the different urgency levels
mean:

.. list-table::
   :widths: 15 85
   :header-rows: 1 

   * - Urgency
     - Description
   * - *Critical*
     - Your production system is inoperative, your business operations or productivity are severely impacted with no available workaround, or there is a critical security issue. Critical issues are eligible for 24x7 support for certain Acquia subscriptions.
   * - *High*
     - Your production system is operating, but the issue is causing significant disruption of your business operations; a workaround is inadequate.
   * - *Medium*
     - Your system is operating and the issue’s impact on your business operations is moderate to low; a workaround or alternative is available.
   * - *Low*
     - The issue is a minor inconvenience and does not impact business operations in any significant way; issues with little or no time sensitivity.

Whenever possible, customers are advised to file support tickets as
**Medium** urgency, reserving the use of **High** for exceptional,
non-urgent circumstances that require a more immediate response. **Low**
urgency should be utilized for issues which can be addressed within the
next business day, as this allows Acquia Support to more quickly respond
to other issues which are more time-sensitive. For more information, see
|definitions|_.

.. |definitions| replace:: Issue Urgency Definitions
.. _definitions: https://www.acquia.com/drupal-support/issue-urgency-definitions

Subject
~~~~~~~

Acquia recommends that ticket titles be short and to the point, summing
up the nature of the issue and which websites or environments are
affected. This also allows Acquia to quickly identify and respond to
trends if multiple customers are experiencing the same issue. As you
enter text in the field, related links may appear underneath the subject
field to assist you with solving common problems. Links will open in a
new tab.


Issue description
~~~~~~~~~~~~~~~~~

Provide as complete a description of the issue as you can. A good,
clear, complete description can help Acquia respond to your issue faster
and more accurately, with a first response that is more likely to be a
useful solution, rather than just a request for additional information.
Acquia's ticketing system supports
`Markdown </support/tickets/markdown>`__. Keep the following tips in
mind when you provide your issue description:

-  **Provide the full URLs affected by the issue**
   This includes URLs of pages on your website where you see errors
   listed, Acquia UI URLs, or URLs of third-party services having
   trouble connecting to your Acquia website. We can trace these full
   URLs to exactly what code is running and creating the behavior you
   are seeing. These URLs help determine whether you are having issues
   on Acquia servers, your |acquia-product:ac| servers, or your own web
   servers outside of |acquia-product:ac|. This also shows us, at a
   glance, when you are talking about a local instance of a website or a
   public production website. This is an important part of orienting us
   in these cases.
-  **Describe the context and nature of the problem**
   *I see white screens on every page* is more descriptive than *My site
   is down!*
-  **Include the ticket numbers of related tickets, when possible**
   This enables the Acquia Support team to quickly research related
   changes.
-  **Include the exact text of any error and where it's being
   displayed**
-  **Where applicable, include the Task ID for any failed tasks**
   If your issue involves a failed task while using the
   |acquia-product:ui| or a command line operation, we can use the Task
   ID to help us identify the type and source of the error and
   immediately access the corresponding lines in the logs.
-  **Tell us when the issue occurred (exact time and time zone)**
   This allows us to more accurately correlate the issue with any errors
   or abnormalities in your logs. If you are not sure, try to confirm
   the last time it worked correctly, if ever.
-  **If relevant, attach screenshots or logs**
   Include the browser's URL bar in any screenshots. Tell us the full
   path of the log file.
-  **List the steps that will reproduce the issue**
   Do we need any special access or permissions, or do we need to take
   any atypical actions, to reproduce this issue?
-  **Tell us what you have done to try to resolve the issue yourself**
   Did it change the symptoms you experienced at all? If you explain
   what did not work, you might keep us from trying something you have
   already tried. That could get us on a fruitful path more quickly.
-  **Describe anything that was confusing about what happened**
   This information can help us figure out what parts of our platform
   may be confusing you. This can suggest future improvements to user
   experience or documentation that may help straighten out the issue
   you are having and help other users as well.
-  **Are there any special instructions or warnings we should keep in
   mind when attempting to troubleshoot this issue?**


Support ticket types
~~~~~~~~~~~~~~~~~~~~

Your ticket type helps Acquia direct your request to the appropriate
resource. The following list explains the available ticket types:

.. list-table::
   :widths: 15 85
   :header-rows: 1 

   * - Urgency
     - Description
   * - Drupal Application Support
     - Reporting an issue on your site, or you have a question related to your Drupal site.
   * - Acquia Platform/Services
     - Assistance with a server-related issue or configuration change, or you have a question related to Acquia’s platforms or services.
   * - Advisory Call Request
     - If your subscription includes this ticket type, request for a 30- or 60-minute Advisory Call on a specific topic (For example, What are the pros and cons of SSL?). Advisory Calls require two to three business days of advanced notice and cannot be used for live troubleshooting of an ongoing issue. Advisory Call time includes any research and communications related to the call, in addition to the time spent on the call.
   * - Event Notification
     - Communicate time-sensitive subscription activities such as, but not limited to, website traffic warnings, environment testing, scans, or releases.
   * - Subscription
     - Assistance with a subscription- or account-related issue or question.
   * - Billing
     - Assistance with a billing-related issue or question.
   * - Remote Administration
     - Request for a Security Update, a non-security Drupal or module update, or a limited site configuration or code change in scope_ of our Remote Administration services.
   * - Other
     - Assistance with an issue or question which does not fit in any of the above categories.

.. _scope: /support/guide#ra

Product or Service
~~~~~~~~~~~~~~~~~~

This is a required field that indicates what product or service you
would like support for. Select an item from the list.


After filing a ticket
---------------------

After you file a ticket, you will receive a confirmation e-mail, along
with any users whose roles define them as *Collaborators* on the
subscription. A member of the Acquia Support team, or your TAM, will
respond to the ticket and provide assistance as soon as possible, based
on the ticket’s urgency and subscription level.

In many instances, Acquia will request additional information or provide
technical recommendations in their response. When this happens, it is
important to provide a timely response and ensure that a technical
resource is available (if the issue requires it) to answer questions or
assist in implementing application-related fixes.


Finding a ticket
~~~~~~~~~~~~~~~~

You can filter and sort your tickets by subscription, status, urgency,
and date. You can also search by full text search in all the fields of
the tickets.

If you only have a six-digit ticket number (for example #123456), you
can find it using the following URL pattern:
``https://insight.acquia.com/support/tickets?ticketNum=123456``. That
URL will redirect to the ticket's URL in the ticketing system.


Ticket status
~~~~~~~~~~~~~

After you file your ticket, Acquia will use the **Status** field to let
you know the ticket's relative state in our workflow, based on the
following statuses:

+-----------------------------------+-----------------------------------+
| Status                            | Explanation                       |
+===================================+===================================+
| *New*                             | This ticket has been filed and is |
|                                   | awaiting a response from Acquia.  |
+-----------------------------------+-----------------------------------+
| *In Progress*                     | An Acquia Support engineer or TAM |
|                                   | has accepted the ticket and is    |
|                                   | working on it.                    |
+-----------------------------------+-----------------------------------+
| *Solved*                          | Acquia has provided an answer to  |
|                                   | the issue or completed the        |
|                                   | requested task.                   |
+-----------------------------------+-----------------------------------+
| *Closed*                          | All work on this ticket is        |
|                                   | completed.                        |
+-----------------------------------+-----------------------------------+
| *Your response needed (Pending)*  | Acquia has responded to your      |
|                                   | issue and is awaiting additional  |
|                                   | information or instructions.      |
+-----------------------------------+-----------------------------------+

Replying to a **Solved** ticket changes its status to **In Progress**
until a further solution is reached, at which time the ticket will again
be marked as **Solved**. After the ticket has been marked as **Solved**
for 14 days, it will be permanently set to **Closed**. If you need to
further discuss the issue in the **Closed** ticket, file a follow-up
ticket by opening the **Closed** ticket and clicking **Create
follow-up**.

Sharing tickets with others
---------------------------

Only individuals listed as contacts on the applicable subscription will
be able to access your tickets. These are also the only individuals who
will receive updates of the tickets. You can't *cc* individuals on
tickets unless they are listed in the **Contacts** section of the
applicable subscription.

If you want to ensure that multiple team members are added to every
ticket for a subscription, 
`create a custom role </acquia-cloud/teams/roles#create>`__, give that role 
|perms|_, and assign the role to those team members.


.. |perms| replace:: the **Include as a collaborator on all help requests by default** permissions
.. _perms: /acquia-cloud/teams/permissions

If the person who filed the original ticket files an issue against a
**Closed** ticket, they can choose to open a follow-up ticket by opening
the **Closed** ticket and clicking **Create follow-up**. This will be
visible to the contacts listed on the applicable subscription.

Managing a large number of contacts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add up to 20 contacts to each ticket. If you require for
additional contacts to be able to access a ticket, use an email
distribution list. To do this, complete the following steps:

#. Create an email distribution list containing the additional contacts
   that need to access a ticket.
#. `Add a new member </acquia-cloud/teams/members>`__ to the appropriate
   team.
#. In the **Email address** field, enter the address of the email
   distribution list.
#. If you want these contacts to be copied on new tickets, make sure
   that their `role </acquia-cloud/teams/roles>`__ includes the
   **Include as a collaborator on all help requests by default**
   permission. If it doesn't, you may choose either to change the
   contacts' role, or edit the role to include this permission.
#. Add the distribution list's email address to the ticket.


Issues with autoresponders
--------------------------

Users subscribed to Acquia cannot have any type of autoresponder
functionality enabled. Autoresponders have the potential to create
endless *communication loops* (in which two or more systems repeatedly
send automated emails to one another) which can affect our ability to
respond in a timely manner regarding your issue. Since many types of
systems can use autoresponders, this functionality includes, but is not
limited to, the following:

-  group aliases
-  mailing lists
-  ticketing systems

Acquia reserves the right to suspend any user account that is causing
communication loops.


Problems with conflicting ticketing systems
-------------------------------------------

If you have your own ticketing system that is capable of creating
tickets by email and you add your ticketing system's email address as a
contact for your subscription, Acquia's ticketing system may then create
reciprocal tickets in your system. This can create a communication loop
in which both systems repeatedly send automated emails to one another.
Situations like this can interfere with Acquia's ticketing workflow, and
may result in responses to tickets being lost or missed. You can prevent
this from happening by performing either of the following actions:

-  |removeemail|_ from your subscription
-  |editperms|_ and remove the 
    **Include as a collaborator on all help requests by default** permission 
    from the role

.. |removeemail| replace:: Remove your ticketing system's contact email
.. _removeemail: /acquia-cloud/teams/members

.. |editperms| replace:: Edit your ticketing system's contact permissions
.. _editperms: /acquia-cloud/teams/roles

New subscriptions
-----------------

When filing a ticket, the ticketing system will require you to choose an
existing subscription.

When you file your ticket to create a new one, please choose an existing
subscription with the same contacts as the ones you'd like to have on
your new subscription. This will allow us to make sure the appropriate
contacts are added to your new subscription.

.. _roadblocks:

Ensuring that Acquia can access your website
--------------------------------------------

Ensure that you identify any issue that could prevent Acquia from
accessing your website for troubleshooting purposes.

For example, the Drupal account created during installation (UID 1) has
all permissions by default, so failing to secure this account may result
in potential security risks. To protect against this, you may block UID
1 from accessing your website, but doing so could prevent Acquia from
accessing your website to troubleshoot issues.

There are two methods that you can use to avoid this problem, without
creating a security risk:

-  Remove the block to UID 1 and use other restriction methods instead.
   For more information, see `Website access restriction
   methods </articles/website-access-restriction-methods>`__.
-  Share a persistent username and password that Acquia can use to
   access your website. Do not share this username and password in a
   ticket; instead, add the credentials to a file in the
   ``/home/sitename`` directory.


Satisfaction survey
-------------------

After closing a ticket, you may be offered a brief satisfaction survey
which allows you to rate your experience as **Good** or **Bad**. The
survey also includes an opportunity for you to provide a comment
regarding the ticket.

.. |Create a ticket| image:: https://cdn2.webdamdb.com/1280_A6nbEHjw8W71.png?-62169955200
   :width: 550px
   :height: 349px
