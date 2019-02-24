.. include:: /common/global.rst

Managing asset approvals
========================

Admins can use the following article to learn how to `create and manage
Approval Paths </dam/workstream/path>`__.

.. _simple:

Initiate Simple Approvals
-------------------------

Simple approvals allow you to send assets for one-off approvals to one
or multiple users or a Team. No approval path is needed, users can
simply enter the email(s) or Team name of the desired approver(s) to
initiate the process.

#. From Workstream, navigate to the **Project** or **Task** details page
   and click the asset in the **Assets** section.
#. From |acquia-product:dam|, navigate to the asset you’d like to send
   for approval.
#. In the asset details page, click the |Approvals icon| **Approvals**
   icon in the actions toolbar or **Send For Approval** in the asset
   details panel.
#. Click **Simple Approval**, if it’s not already selected.
#. For approvers that are |acquia-product:dam| users, type in their name
   or email address and click it once it appears in the dropdown. Add a
   message, if desired.
#. If the approver is not a |acquia-product:dam| user, enter their email
   address.
#. You can also send simple approvals to Workstream Teams (read more
   about `Teams </dam/workstream/getting-started#teams>`__). Type the
   Team name and click it once it appears. An approval will only be
   required from one person on a team, the asset will be marked
   approved/rejected based on the reply of the first approver.

   .. note::
      If you send an asset for approval to a Team and individual, an
      approval will be needed from someone on the Team and the individual.
      If the individual is also on the Team, their approval will count for
      both the team and themselves.

#. Select the desired download/proofing permissions and reminder
   options.

   -  **Allow Downloading**: Allows the approver(s) to download the
      asset. Once enabled, select the desired preset from the dropdown.
      These are the same presets that you have available when
      downloading an asset. (Read more about configuring image and video
      download presets.)
   -  **Allow Proofing**: Allows the approver(s) to access to the
      proofing tool to provide more detailed feedback.
   -  **Remind**: Sends a reminder to the approver(s). Once enabled, set
      the reminder interval and check the box next to **Repeat** to have
      the reminder automatically re-sent after each interval.

#. Click **Send**. An email notification will be sent to each approver.

.. _initiate:

Initiate Approval Paths
-----------------------

Workstream users can initiate an approval path. Once sent, the system
will manage routing the approval through each step, sending
notifications to the appropriate approver(s).

#. From Workstream, navigate to the **Project** or **Task** details page
   and click the asset in the **Assets** section.
#. From |acquia-product:dam|, navigate to the asset you’d like to send
   for approval.
#. On the asset details page, click the |Approvals icon| **Approvals**
   icon in the actions toolbar or **Send For Approval** in the asset
   details panel.
#. Click **Approval Paths** and select an approval path using the drop
   down. Only approval paths that you have permissions to will display.
   |Build an approval path|
#. Enter an optional message and click **Send**.
#. If any step includes prompting the requester for approver(s), you
   must enter the name and/or email address of the appropriate
   approver(s).
#. **If the approver is a |acquia-product:dam| user**, type in their
   name or email address and click it once it appears in the dropdown.
#. **If the approver is not a |acquia-product:dam| user**, enter their
   email address.
#. Click **Send**.

.. _respond:

Respond to Approval Requests
----------------------------

Once an approval is initiated, each approver will receive an email
notification – immediately for simple approvals or as defined in the
approval path.

#. Click **View Request** in your email notification or in the asset
   details panel.
#. Depending on the settings configured by the requester, you can
   **Download** or **Proof** the asset. You can also view any comments
   added during other approvals or reviews.

   -  To download, click the |Download| **Download** icon on the top
      right-hand side of the screen next to the filename.
   -  To proof, click **View Proof**.

#. From the email notification or asset details page, choose which
   action you’d like to take:

   -  |Approve| **Approve**: The asset is approved with no changes
      required.
   -  |Approve with changes| **Approve with Changes**: The asset is
      approved pending the changes requested in the comments or proofing
      section. The requester can make the required changes, upload a new
      version and update the asset status to approved.
   -  |Reject| **Reject**: The asset is not approved.
   -  If you select approve with changes or reject, you must enter a
      comment before your response is recorded.

#. Click **Submit**.

If you **Approve with Changes** or **Reject**, you can change your
response at a later time. Should you **Approve** an asset, the response
cannot be changed as it may have triggered the next step in an approval
path. In this case, you will need to contact the requester to relay any
comments or request changes.

.. _viewstatus:

View an Approval Status
-----------------------

Administrators and the requester can view the status of an approval
request.

#. From Workstream, navigate to the **Project** or **Task Details** page
   and click the asset in the **Assets** section.
#. From |acquia-product:dam|, navigate to the asset you sent for
   approval.
#. On the asset details page, click **View Request**. You can also click
   the |Approvals icon| **Approvals** icon in the actions toolbar and
   click View.

.. _clearstatus:

Clear “Approve with Changes” Status
-----------------------------------

If a request is marked **Approve with Changes**, the requester should
make the requested changes, upload a new version, and then approve the
request.

#. From Workstream, navigate to the **Project** or **Task Details** page
   and click the asset in the **Assets** section.
#. From |acquia-product:dam|, navigate to the asset that was approved
   with changes.
#. Upload a new version, if necessary.
#. Click the |Approvals icon| **Approvals** icon in the actions toolbar
   and click **Approve** next to the approver who approved with changes.

Based on the settings of the approval path, new versions of an asset my
need to start at the beginning of an approval path, restart at the
current step or simply move forward to the next step.

.. _resubmit:

Resubmit Rejected Approvals
---------------------------

If an approver rejects the approval request, the requester can make any
necessary adjustments, upload a new version, and resubmit for approval.

#. From Workstream, navigate to the **Project** or **Task** Details page
   and click the asset in the **Assets** section.
#. From |acquia-product:dam|, navigate to the asset that was rejected.
#. Upload a new version, if necessary.
#. Click the |Approvals icon| **Approvals** icon in the actions toolbar
   of the asset details page and click **Resubmit** next to the approver
   who rejected the request.

Based on the settings of the approval path, new versions of an asset my
need to start at the beginning of an approval path, restart at the
current step or simply move forward to the next step.

.. _options:

Additional Options
------------------

Administrators and the requester can remove, add or remind an approver
or cancel approval requests.

|Approval examples|

#. From Workstream, navigate to the **Project** or **Task** Details page
   and click the asset in the **Assets** section.
#. From |acquia-product:dam|, navigate to the asset that was sent for
   approval.
#. Click the |Approvals icon| **Approvals** icon in the actions toolbar
   of the asset details page.
#. To remove an approver, hover your mouse over the approver and click
   the ``(X)`` icon.
#. To add an approver, click **Add approvers**. If the approver is a
   |acquia-product:dam| user, type in their name or email address and
   click it once it appears in the dropdown. If the approver is not a
   |acquia-product:dam| user, enter their email address.
#. Add an optional message for the approver(s).
#. To remind an approver, click **Send reminder** and an email reminder
   will be sent to the approver.
#. To cancel an approval, click **Cancel Approval Request**.
#. Click **Ok**.

.. |Approvals icon| image:: https://cdn2.webdamdb.com/100th_sm_E8rLPiUIeLm1.png?1526475551
   :width: 25px
   :height: 22px
.. |Build an approval path| image:: https://cdn4.webdamdb.com/1280_gSD7L1d3F7F6.png?1526475477
   :width: 447px
   :height: 556px
.. |Download| image:: https://cdn3.webdamdb.com/100th_sm_QPtA12JlJNH0.png?1526475594
   :width: 21px
   :height: 22px
.. |Approve| image:: https://cdn3.webdamdb.com/100th_sm_QX52asTIuP53.png?1526475885
   :width: 23px
   :height: 22px
.. |Approve with changes| image:: https://cdn2.webdamdb.com/100th_sm_wai1vBNTinx7.png?1526476133
   :width: 22px
   :height: 22px
.. |Reject| image:: https://cdn2.webdamdb.com/100th_sm_UeD9aAYfw51.png?1526475475
   :width: 24px
   :height: 22px
.. |Approval examples| image:: https://cdn2.webdamdb.com/100th_sm_o5FgvAKJWEX4.png?1526475820
   :width: 550px
   :height: 337px
