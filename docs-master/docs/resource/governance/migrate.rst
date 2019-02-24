.. include:: /common/global.rst

Planning migrations based on governance
======================================================

.. container:: internal-navigation

   **Platform governance**

   * :doc:`Intro </resource/governance>`
   * :doc:`Types </resource/governance/types>`
   * :doc:`Models </resource/governance/models>`
   * :doc:`Architect </resource/governance/arch>`
   * :doc:`Build </resource/governance/build>`
   * Migrate
   * :doc:`Maintain </resource/governance/maintain>`

When creating a digital governance plan, you should not leave migration
planning to chance. Migrations without advance planning will generally
require additional resources and time. Be sure to consider the following
questions as you determine the phases of your launch when planning your
migration onto a new platform:

-  How has your data structure changed from your former platform to your
   new platform?
-  How will content be moved from your old platform to your new
   platform?
-  Should your rollout strategy start with a single website, or a few
   related websites?
-  Should your launch be a soft launch, or a hard cutover?
-  How will you handle bugs and feedback for the newly-launched
   websites?

When developing your migration process for governance plan, Acquia
recommends you include the following steps:

-  `Set up a migration team <#team>`__
-  `Review your content inventory <#inventory>`__
-  `Map your data to a migration plan <#map>`__
-  `Involve a migration specialist <#specialist>`__

Setting up a migration team
---------------------------

To ensure a successful migration and launch, your migration team should
include members with the following roles:

-  *Project manager* - Ensures the migration adheres to the schedule
-  *Product owner* - Oversees over the project, approves the migration
   plan, and provides final signoff after launch
-  *Developers* - Owns the technical details of your migration,
   understands the data model, and performs the migration tasks
-  *Partner project manager* - Coordinates between the organization's
   and Acquia's teams

Depending on the size of your migration, your project may also require a
`migration specialist <#specialist>`__ to assist with planning
migration.

Reviewing your content inventory
--------------------------------

Your migration should not move unneeded content to your new platform. To
avoid this from happening, your governance team should review the
content inventory created while designing your content architecture and
establish a plan to ensure the unneeded content is not moved to your new
platform. For more information, see 
`Creating a content inventory </resource/governance/arch>`__.

Mapping your data to a migration plan
-------------------------------------

After creating an 
`inventory of your content </resource/governance/arch>`__ you should create a 
spreadsheet to map your existing fields and attributes to the fields and 
attributes in your new platform. You will need to determine which content types 
can be migrated programmatically and which ones must be migrated manually.

In both cases, your migration plan must account for the types of effort
required:

-  *Manual migrations* require time for copying and error-checking data.
   You should test how much time is needed to not just copy over the
   data to the new platform, but to also clean the data and cross-link
   it, if necessary.
-  *Programmatic migrations* require time for creating, testing, and
   rehearsing each individual script that will migrate a single content
   type. Scripts and their rollbacks should be tested both early and
   often during your development process.

For additional information about migrations, see 
`10 Tips to Streamline Migration Review <https://dev.acquia.com/blog/10-tips-streamline-migration-review>`__
on `dev.acquia.com <http://dev.acquia.com>`__.

Involving a migration specialist
--------------------------------

Your migration specialist will need to investigate the technical details
of your migration, such as assessing the size of your databases, both to
determine the number of content types but also how long will be needed
to transmit data from one source to another.

Your migration specialist should also perform small test migrations with
your proposed data mappings to identify issues or inconsistencies that
should be resolved prior to the final migration.

Additionally, your migration specialist should review the security of
your data and determine your needs for security certifications and
password protection.

On the next page in this series, you'll learn more about 
`maintaining your governance plans </resource/governance/maintain>`__ over 
time.
