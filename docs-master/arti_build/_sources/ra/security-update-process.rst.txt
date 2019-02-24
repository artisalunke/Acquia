.. include:: /common/global.rst

Security update process
=======================

Security updates take place in several steps. Both automated and manual
updates use a similar process:

#. `Test updates in an isolated branch <#one>`__
#. `Tag branch and deploy for additional testing <#two>`__
#. `Deploy tested tag to production <#three>`__

.. _one:

Step one: Test updates in an isolated branch
--------------------------------------------

The steps within step one will not affect the operation of production,
stage, or development servers. Acquia's automated security update
process will:

#. Create a branch from the tag or branch deployed to your production
   environment.
#. Deploy this branch to the RA Environment.
#. Live development is enabled on the RA Environment.
#. The production database(s) is copied to the RA environment.
#. Drush or Composer is used to apply all security updates to this
   branch.
#. A ticket is created to inform your team that the security update
   branch is ready for testing and approval.

After you approve the security update branch, Acquia will proceed with
the next step.

.. _two:

Step two: Tag branch and deploy for additional testing
------------------------------------------------------

Once your team has approved the branch provided in the first step, RA
Automation will:

#. Make a tag of the approved security update branch. The only
   difference between this tag and the source from step one should be
   the tested and approved security updates.
#. Backup all databases on your preferred testing environment.
#. Copy the latest databases from production into your preferred test
   environment (this defaults to the Stage environment). This ensures
   that the final test is against the most recent production data.
#. Deploy the tag to the testing environment for final testing.
#. Inform your team that the tag is ready for testing and approval to
   deploy to production. Acquia cannot move updated code to production
   without your explicit approval.

After you approve the tag of the the security update branch, Acquia will
proceed with the next step.

.. _three:

Step three: Deploy tested tag to production
-------------------------------------------

Once your team approves the tag, it will be deployed to production. You
can schedule this for a specific time with a 24-hour notice within
normal business hours. See `Scheduling Production Deploy
Windows </ra/security#scheduling>`__ for details.

.. note:: We cannot move code to production without explicit approval from the 
          customer.

After you have approved the tag for release to production on the ticket,
RA automation will do the following:

#. Back up the production database(s).
#. Deploy the tag.
#. Run any required database updates.
#. Inform you that production has been updated and should be tested.
#. Your RA preference setting will determine who merges the security
   branch into your development branch:

   -  If your RA preference is set to **merge**, RA automation will
      attempt to merge the update into your development branch. If the
      merge into the development branch requires troubleshooting, either
      Acquia or your team can create a new ticket (Premium Only).
   -  If your RA preference is not set to **merge**, you should merge
      the branch/tag into your preferred branch (usually ``master``).
      This ensures that the security updates are included in all future
      work.

.. _alternative:

Alternate procedure: Tag branch and deploy directly to production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you do not want an additional testing period, you may choose to skip
`Tag branch and deploy for additional testing <#two>`__. Acquia ONLY
recommends this if you are certain that testing on the RA environment is
sufficient.

Once your team has approved the branch provided in the first step, RA
Automation will:

#. Make a tag of the approved security update branch. The only
   difference between this tag and the source from step one should be
   the tested and approved security updates.
#. Back up the production database(s).
#. Deploy the tag.
#. Run any required database updates.
#. Inform you that production has been updated and should be tested.
#. Your RA preference setting will determine who merges the security
   branch into your development branch:

   -  If your RA preference is set to **merge**, RA automation will
      attempt to merge the update into your development branch. If the
      merge into the development branch requires troubleshooting, either
      Acquia or your team can create a new ticket (Premium Only).
   -  If your RA preference is not set to **merge**, you should merge
      the branch/tag into your preferred development branch. This
      ensures that the security updates are included in all future work.

For more detailed documentation on using Drush and CloudAPI commands to
apply RA security updates, see `Performing security updates using
CloudAPI and Drush commands </ra/cloudapi-drush>`__.
