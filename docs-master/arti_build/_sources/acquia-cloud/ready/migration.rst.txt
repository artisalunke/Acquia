.. include:: /common/global.rst

External migrations with Acquia Ready
=====================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/ready/migration/*

`|acquia-product:onb| <https://www.acquia.com/customer-success/acquia-ready-services>`__
offers platform migration services to take the burden off your team
while moving your code, database, and files onto the |acquia-product:ac|
platform.

You should anticipate your migration engagement to last at least 2-4
weeks, depending on the size and complexity of the websites you are
migrating, as well as the availability of your resources to conduct the
testing.

Notes

-  For information about how |acquia-product:onb| can help you migrate a
   website from one |acquia-product:ac| sitegroup to another, see
   `Internal migrations with
   |acquia-product:onb| </acquia-cloud/ready/migration/internal>`__.
-  For information about the available migration sizes, see the `Acquia
   Platform Migration Services Product Guide </guide/migrate>`__.

The first step in moving your website onto |acquia-product:ac| is to
provision your new subscription, codebase, and hardware.
|acquia-product:onb| will set up your new subscription for you, and
grant your team with the necessary access. A Customer Onboarding
Engineer will perform your migration remotely (and will require require
administrative access to your website).

The migration process is typically divided into two parts: the `initial
migration <#initial>`__ and `final migration <#finalmigration>`__.
Depending on your needs, an intermediate migration step may also be
included. The duration of the migration process will depend on how much
time you will need to test your website on the |acquia-product:ac|
platform. The initial migration focuses on copying your code, database,
and files to your new subscription, whereas the final migration is a
sync of your website's database and files, including any changes that
occurred since the initial migration.

For more information about each step of your migration, refer to the
following sections of this page:

-  `Prerequisites for migration <#prereqs>`__
-  `Migration call <#call>`__
-  `Granting access to your website <#access>`__
-  `Initial migration <#initial>`__
-  `Quality assurance <#qa>`__
-  `Intermediate Migration <#intermediate>`__
-  `Content Freeze <#freeze>`__
-  `Final Migration <#finalmigration>`__
-  `Final testing and DNS switch <#switch>`__
-  `Migration schedule <#schedule>`__

.. _prereqs:

Prerequisites for migration
---------------------------

The prerequisite for the initial migration is a code freeze. If a code
freeze cannot be put in place before the initial migration, an
intermediate migration will be required before the final sync. The
website should remain in code freeze until after the final migration and
the domain name system (DNS) switch to |acquia-product:ac| are
completed.

The prerequisite for the final migration is a content freeze. The time
required for the Customer Onboarding Engineer to perform your initial
migration will provide a guideline for estimating the duration of your
final migration.

.. _call:

Migration call
--------------

To coordinate the engagement, |acquia-product:onb| will schedule an
introductory migration call to discuss the process, access requirements
for the engineer handling your migration, and the timelines that you
should expect.

.. _access:

Granting access to your website
-------------------------------

After the migration call, |acquia-product:onb| team will create a
proactive ticket and send you an access request with the details of
|acquia-product:onb| engineers who will need to be granted with an
administrative sign-in to the code base that you want to migrate.

.. _initial:

Initial migration
-----------------

In preparation for the initial migration, you will need to coordinate
the timeframe of a code freeze with your development team, as any code
changes committed to your current production website after the initial
migration will be disregarded. Acquia will perform an initial migration
of your website's code, files, and databases to |acquia-product:ac|.
After the initial migration is completed, any new development work
should be performed only on |acquia-product:ac|.

.. _qa:

Quality assurance
-----------------

After the initial migration is completed, you must perform quality
assurance (QA) and regression testing on |acquia-product:ac| using an
alternate domain. You may choose to set up a DNS record for this
alternate domain for testing purposes. You can also simulate a DNS
change locally by modifying the hosts file on your local machine.

During QA testing, you must review all critical website functionality,
including public functions, themes, and related media assets to verify
that everything is working correctly:

-  *Verify administrative functions* - Creating content, creating users,
   administering permissions, and other administrative functions
-  *Verify business critical functions* - Form submissions and third
   party integrations
-  *Validate themes* - Images, CSS, and cross-browser compatibility
-  *Validate risk areas (possible regressions due to changes made
   through the migration process)* - Upgraded contributed modules and
   new modules

|acquia-product:onb| cannot proceed with final migration until you sign
off on testing.

During your QA testing, you should also add any needed custom domains or
SSL certificates to your new |acquia-product:ac| subscription.

.. _intermediate:

Intermediate Migration
----------------------

If you cannot implement a website code freeze before the initial
migration, your Customer Onboarding Engineer may perform an extra
intermediate migration later in the migration process, after you have
put a code freeze in place.

.. _freeze:

Content Freeze
--------------

Your Customer Onboarding Engineer will inform you regarding how long the
initial migration took and, based on that information, will provide an
estimate of time required for the final migration. You should put a
content freeze into effect shortly before the final migration, and keep
the content freeze in place throughout both the final migration process
and final testing, until the DNS switch is complete.

.. _finalmigration:

Final Migration
---------------

Your Customer Onboarding Engineer will conduct the final data migration.
This final migration contains the final sync of your files and database,
to ensure all content changes made on your current production website
after the initial migration are brought over to |acquia-product:ac|.

.. _switch:

Final testing and DNS switch
----------------------------

After the final migration, you must perform final QA testing to verify
that the newly-migrated website is working correctly. If your tests are
successful, you will need to repoint your domain names to your new
subscription. Your |acquia-product:onb| team can provide DNS records if
necessary. After the DNS switch is completed, your code freeze and
content freeze are over and your website is live on |acquia-product:ac|!

.. _schedule:

Migration schedule
------------------

Your Customer Onboarding Manager can provide you with an editable
version of the following plan to help you track the progress of your
migration.

+-----------------------+-----------------------+-----------------------+
| Activity              | Notes                 | Owner                 |
+=======================+=======================+=======================+
| Subscription and      | You will be notified  | |acquia-product:onb|  |
| hardware provisioning | when your             |                       |
|                       | |acquia-product:ac|   |                       |
|                       | subscription is ready |                       |
|                       | for use.              |                       |
+-----------------------+-----------------------+-----------------------+
| Migration call        | Your Customer         | |acquia-product:onb|/ |
|                       | Onboarding Manager    | Customer              |
|                       | will schedule the     |                       |
|                       | call and provide      |                       |
|                       | dial-in details. Both |                       |
|                       | your project manager  |                       |
|                       | and technical lead    |                       |
|                       | should attend.        |                       |
+-----------------------+-----------------------+-----------------------+
| Grant access to       | During the migration  | Customer              |
| Acquia engineer       | call,                 |                       |
|                       | |acquia-product:onb|  |                       |
|                       | team will discuss the |                       |
|                       | level of required     |                       |
|                       | access and share      |                       |
|                       | options regarding how |                       |
|                       | this access can be    |                       |
|                       | granted. You can then |                       |
|                       | provide               |                       |
|                       | |acquia-product:onb|  |                       |
|                       | engineers with the    |                       |
|                       | necessary access.     |                       |
+-----------------------+-----------------------+-----------------------+
| Code freeze           | You need to notify    | Customer              |
|                       | Acquia when your code |                       |
|                       | freeze is in place so |                       |
|                       | that Acquia can       |                       |
|                       | conduct the initial   |                       |
|                       | migration. Any code   |                       |
|                       | changes committed     |                       |
|                       | after the initial     |                       |
|                       | migration will be     |                       |
|                       | disregarded.          |                       |
+-----------------------+-----------------------+-----------------------+
| Initial Migration     | Acquia will perform   | |acquia-product:onb|  |
|                       | an initial migration  |                       |
|                       | of code, files, and   |                       |
|                       | databases. This       |                       |
|                       | initial migration     |                       |
|                       | will help with        |                       |
|                       | estimates regarding   |                       |
|                       | the time needed for   |                       |
|                       | the content freeze    |                       |
|                       | and final migration.  |                       |
|                       | Upon completion,      |                       |
|                       | Acquia will notify    |                       |
|                       | you to begin QA       |                       |
|                       | testing.              |                       |
+-----------------------+-----------------------+-----------------------+
| Install               | Acquia will install   | |acquia-product:onb|  |
| |acquia-product:anc|  | |acquia-product:anc|  |                       |
|                       | as part of the        |                       |
|                       | initial migration.    |                       |
+-----------------------+-----------------------+-----------------------+
| Install               | If applicable, Acquia | |acquia-product:onb|  |
| |acquia-product:as|   | will install          |                       |
| (if applicable)       | |acquia-product:as|   |                       |
|                       | as part of the        |                       |
|                       | initial migration.    |                       |
+-----------------------+-----------------------+-----------------------+
| Provide benchmark for | Based on the time of  | |acquia-product:onb|  |
| final migration       | the initial           |                       |
|                       | migration, Acquia     |                       |
|                       | will be able to       |                       |
|                       | forecast how much     |                       |
|                       | time should be        |                       |
|                       | anticipated for       |                       |
|                       | content freeze/final  |                       |
|                       | migration.            |                       |
+-----------------------+-----------------------+-----------------------+
| SSL upload (if        | If you will be using  | Customer              |
| applicable)           | an SSL certificate    |                       |
|                       | for your website, you |                       |
|                       | should install it on  |                       |
|                       | |acquia-product:ac|   |                       |
|                       | on your               |                       |
|                       | subscription's SSL    |                       |
|                       | page.                 |                       |
|                       | |acquia-product:onb|  |                       |
|                       | team may provide      |                       |
|                       | instructions and      |                       |
|                       | additional assistance |                       |
|                       | with this step, if    |                       |
|                       | required.             |                       |
+-----------------------+-----------------------+-----------------------+
| QA Testing            | You must test the     | Customer              |
|                       | website on            |                       |
|                       | |acquia-product:ac|.  |                       |
|                       | Load testing is       |                       |
|                       | recommended during    |                       |
|                       | this time.            |                       |
+-----------------------+-----------------------+-----------------------+
| Intermediate          | *Optional step*       | |acquia-product:onb|  |
| Migration             |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Website Review        | While your team is    | |acquia-product:onb|  |
|                       | testing, Acquia will  |                       |
|                       | perform a basic       |                       |
|                       | review of your        |                       |
|                       | existing Drupal       |                       |
|                       | website               |                       |
|                       | configuration, module |                       |
|                       | selection, and code   |                       |
|                       | for potential         |                       |
|                       | availability risks.   |                       |
+-----------------------+-----------------------+-----------------------+
| Content freeze        | A content freeze      | Customer              |
|                       | should be put in      |                       |
|                       | place shortly before  |                       |
|                       | the final migration,  |                       |
|                       | and continue          |                       |
|                       | throughout the entire |                       |
|                       | final migration       |                       |
|                       | process and final     |                       |
|                       | testing period, until |                       |
|                       | the DNS switch is     |                       |
|                       | complete.             |                       |
+-----------------------+-----------------------+-----------------------+
| Final Migration       | Acquia will perform a | |acquia-product:onb|  |
|                       | final sync of your    |                       |
|                       | website's database    |                       |
|                       | and files. Upon       |                       |
|                       | completion, Acquia    |                       |
|                       | will notify you to    |                       |
|                       | test your production  |                       |
|                       | website before        |                       |
|                       | cutting over DNS      |                       |
|                       | records.              |                       |
+-----------------------+-----------------------+-----------------------+
| Final testing         | After final migration | Customer              |
|                       | is complete, you will |                       |
|                       | conduct final testing |                       |
|                       | (30-60 minutes) to    |                       |
|                       | ensure that your      |                       |
|                       | website is fully      |                       |
|                       | migrated and that no  |                       |
|                       | content is missing.   |                       |
+-----------------------+-----------------------+-----------------------+
| DNS switch            | After final testing   | Customer              |
|                       | is completed, you can |                       |
|                       | switch DNS to point   |                       |
|                       | to your               |                       |
|                       | newly-migrated        |                       |
|                       | website.              |                       |
+-----------------------+-----------------------+-----------------------+
