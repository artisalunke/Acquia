.. include:: /common/global.rst

Managing approval paths
=======================

Approval paths allow admins to build multi-step approval processes that
automatically route assets from one approver (or group of approvers) to
the next.

.. _create:

Create Approval Paths
---------------------

#. `Sign in to Workstream </dam/workstream/getting-started>`__, and then
   click **Manage** in the secondary navigation.
#. Click **Approval Paths**.
#. Click **New Approval Path** in the upper right, and then enter a name
   for your approval path.
#. To create the first step, click **Add one**, and then enter the step
   name.

.. _approver:

Set the Approver(s)
-------------------

#. **Asset’s original uploader** - The approval request will be sent to
   the user who uploaded the asset.

   -  **Prompt Requester for approver** - The requester can enter the
      name and/or email address of the approver or Team (read more
      `about Teams </dam/workstream/getting-started>`__) when the
      request is initiated. This option is often selected if the
      approvers change each time the path is used, such as working with
      different clients or partners, or if the approvers can’t be
      identified until the asset is ready for approval.

#. **Identify approver now** - Enter the desired approver or Team.

   -  **If the approver is a |acquia-product:dam| user or Workstream
      Team**, enter their name, email address, or Team name, and then
      click the name when it appears in the list.
   -  **If the approver is not a |acquia-product:dam| user**, enter
      their email address.

#. **Approver** Style: If you select **Prompt requester for approver**
   or **Identify approver(s) now** (with more than one approver listed),
   you must select the approver style:

   -  **Approval is required from all** - All approvers in this step
      must approve the asset for it to move to the next step.
   -  **First response wins** - Only one approval is needed for the
      asset to move to the next step. If an approver selects **Reject**
      or **Approve** with changes, the asset will not move to the next
      step until it meets the requirements to be approved in the current
      step.

#. Select one or more check boxes to enable the appropriate permissions:

   -  **Approver can view comments** - Allows the approver to view the
      comments made by other users, including comments made in previous
      approval steps.
   -  **Approver can proof** - Allows the approver to access to the
      proofing tool to provide more detailed feedback. (`Read more about
      proofing. </dam/workstream/proofing>`__)
   -  **Approver can download** - Allows the approver(s) to download the
      asset.

#. Toggle the slider to enable the additional settings:

   -  **Remind** - Sends a reminder to the approver after an interval a
      time. Select **Repeat** to send a recurring reminder using the set
      interval of time.
   -  **Escalate** - Escalates the approval to another reviewer if no
      response is given after a set interval of time. If a reminder is
      enabled, the interval of time chosen to escalate an asset must be
      greater than the interval of time selected for the reminder. For
      example, if you send a reminder in two days, the escalation
      interval must be set at three days or longer.
   -  **Auto Decide** - If no response is given after the selected
      interval of time, the asset will automatically be marked as
      approved or denied. The interval selected in this step must be
      longer than the intervals selected in the **Remind** and
      **Escalate** settings, if enabled.

#. Click **Add a step** on the left of the page to add additional steps,
   or click **Continue to the next step** in the approval setup pane.
   The system saves actions as you create new steps.

Settings
--------

To view or modify the available settings, click **Settings** at the
bottom left of the approval path page.

|Settings link|

-  *Who can use this path* - Select which Workstream groups can use this
   approval path. By default, any Workstream user can use a newly
   created approval path. To limit access, toggle the slider to the left
   and select the Workstream group(s) that should have access.
-  *When a new version of an asset is uploaded* - Choose what happens
   when a new version of an asset is uploaded.

   -  **Restart approval process from beginning** if a new approval is
      required from every step of the approval path.
   -  **Restart current step if a new approval is required** starting
      from the current step in the approval path. If selected, the user
      who rejected the asset will receive an email to re-approve.
   -  **Do nothing** if the new version can continue through the
      approval process. The requester can also manually `resubmit the
      approval </dam/workstream/approval>`__.

Be sure to select the **Upon final approval** check box to activate
assets after they have been approved by all steps.

Click **Save** after you’ve configured all steps.

To **Enable an Approval Path**, toggle the slider next to the path name
to the right. By default, newly created approval paths are disabled.

.. _editpaths:

Edit Approval Paths
-------------------

#. `Sign in to Workstream </dam/workstream/getting-started>`__, and then
   click **Manage** on the secondary navigation.
#. Click **Approval Paths**.
#. Use one of the following methods to edit the approval path:

   -  Click the approval path that you want to update, and then click
      **Edit** next to the approval path name.
   -  You can also click the options icon |Options| that appears when
      you point to an approval path name, and then click **Edit**.

      |Edit a path|

.. _deletepath:

Duplicating or deleting approval paths
--------------------------------------

#. `Sign in to Workstream </dam/workstream/getting-started>`__, and then
   click **Manage** on the secondary navigation.
#. Click **Approval Paths**.
#. Click the options icon |Options|.
#. Click **Duplicate** to make a copy of the approval path, or click
   **Delete** to delete the approval path.

.. |Settings link| image:: https://cdn4.webdamdb.com/1280_Yp3UFIXJ6Do7.png?1526475646
   :width: 550px
   :height: 258px
.. |Options| image:: https://cdn4.webdamdb.com/100th_sm_MD4MvX7g55x7.png?1526475682
   :width: 18px
   :height: 22px
.. |Edit a path| image:: https://cdn2.webdamdb.com/1280_2EdpIFM5IU98.png?1526475477
   :width: 297px
   :height: 231px
