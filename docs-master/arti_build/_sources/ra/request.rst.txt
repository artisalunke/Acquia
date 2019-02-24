.. include:: /common/global.rst

Requesting work
===============

There are several types of work that you can request that Remote
Administration (RA) perform for your website:

-  **Security Updates**

   Security Updates are done through automation and may be requested
   with a ticket. Since RA Automation creates a new ticket, the
   requesting ticket will be solved so that all conversation occurs on
   the automatically created update ticket.

   Be sure that an automatically created security update does not
   already exist. If it does, test the deployed branch or request a new
   update through that ticket.

-  **Bug-fix updates**

   All core and module bug-fix updates must be requested through a
   ticket.

   -  Bug-fix updates may alter site behavior, so Acquia takes a
      conservative approach and does not apply bug-fix or feature
      releases automatically. Bug-fix or feature releases may be applied
      upon request. For instructions on how to file a ticket, see `How
      to file a support ticket </support/tickets>`__.
   -  Acquia Automation is able to update specific modules through
      manual flags. Update requests will likely result in a new
      automated ticket listing all updates, and the original ticket will
      be resolved.

.. _request-troubleshooting:

Request for troubleshooting
---------------------------

Troubleshooting requests are made through a support ticket. The more
precise and detailed you can be when requesting troubleshooting help,
the more effective Support Engineers can be in responding to a ticket.
Consider including the following information in your ticket:

-  The nature of the problem you would like solved, both expected and
   actual behavior.
-  Any actions or events that seem to cause the problem.
-  Links to the pages where the problem might be visible.
-  Screenshots of the problem, especially if it is graphic in nature.
-  Any errors that are visible to users, whether anonymous or
   administrative.

Review `How to file a support ticket </support/tickets>`__ for more
information.

.. _request-code-update:

Request a code update or change
-------------------------------

If your Remote Administration request requires changes to code or
database outside of a security update, answer the following questions
when you initiate a ticket.

Note

Your `RA preferences </ra/preferences>`__ will be used as defaults
unless you specify otherwise in your requesting ticket.

-  What branch or tag should be used to create a new, testing branch?
   The default is to branch from the current production tag.
-  What environment should be used for initial testing — Dev or Stage?
-  Unless you are requesting a `security update </ra/security>`__, the
   default environment for testing code changes is Stage. The branch
   will be deployed to a single environment for testing, and once
   tested, it will be merged into the master or trunk and available for
   all environments. If it's a security update, we will use the RA
   environment unless otherwise requested.
-  What database should be used to test against? The default is to copy
   the production database to the Testing environment.

Before requesting work, review the `Out-of-scope
areas </ra/scope#out-of-scope>`__ section of Understanding the scope of
Remote Administration. It's also important to answer the preceding
questions and to address the following items:

-  Specify the code that you would like to be updated. If it's a
   specific file, provide the file's location.
-  If you would like a module or core updated and would like to use a
   specific version, specify the version number in the ticket.
-  If you would like non-security module updates, specify the version
   that you want to apply. For additional information, see
   `Understanding the scope of Remote Administration </ra/scope>`__.
