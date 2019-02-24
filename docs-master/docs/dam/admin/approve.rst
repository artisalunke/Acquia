.. include:: /common/global.rst

Handling approval requests
==========================

|acquia-product:dam| approvals allow contributors and admins to route
assets to internal and external stakeholders for approval.

.. _start:

Initiate an approval request
----------------------------

#. Sign in to |acquia-product:dam|.
#. Navigate to the detail page of the asset you would like to send for
   approval.
#. Click the |Approval request| **Approval** icon on the actions toolbar
   and select **Approval request**.
   |Request an approval|
#. Enter the email address(es) of the approver(s) and a comment and/or
   instructions (optional). The approvers don’t need to have a
   |acquia-product:dam| account.
#. Click **Request** to send the approval.
   |Request approval|

.. _report:

Approval request report
-----------------------

|acquia-product:dam| admins can view a report of all approval requests,
while other users can view approval requests where they are the
requestor or the approver.

#. Sign in to |acquia-product:dam|.
#. Click **Reports** on the top navigation and select **Approval
   requests**.
#. Click **Pending** in the status column to approve or reject an asset.

.. _respond:

Respond to an approval request
------------------------------

Approvers will receive an email from |acquia-product:dam| asking them to
review and approve the asset. If the approver is an admin, contributor
or regular user, the approval request will also display on the homepage
and in the approval requests report.

#. In the approval request email, click **View Request**.
#. An asset approvals window will also display on the homepage of
   |acquia-product:dam|. Click **View All** to see your approval request
   report, then click **Pending** for the asset you want to approve or
   reject.
   |Review a request|
#. Click the green |Approve| **Approve** icon to approve or the red
   |Reject| **Reject** icon to reject the approval request.
#. You can also add comments (optional).

|Request is approved|

.. _rules:

Approval Rules
--------------

#. Each approver must approve the request in order for the asset to be
   approved.
#. Only one approver needs to reject the request for the asset to be
   rejected.
#. If an approval request has been rejected, users may automatically
   reinitiate the request by adding a new version. (Read more about
   `adding versions </dam/content/asset/version>`__.)

.. _cancel:

Cancel an approval request
--------------------------

The user who initiated the request can cancel it.

#. Sign in to |acquia-product:dam|.
#. Click **Reports** on the top navigation and select **Approval
   requests**.
#. Click **Pending** under the status column. This will take you to the
   asset approval page.
#. Click **Cancel this request**.
#. Click **Yes** to confirm.
   |Cancel a request|

.. _preferences:

Configuring the system preferences
----------------------------------

Admins can configure the system preferences to automatically update the
status of the asset when it is going through the approval process. (Read
here about `updating the asset status </dam/content/asset/status>`__.)

#. Sign in to |acquia-product:dam| as an admin.
#. Click the |Settings| **Settings** icon on the top navigation and
   choose **System preferences**.
#. Under the **Asset approval** section, configure the following
   settings:

   -  **Change status upon request to Inactive**: When checked, the
      asset status will automatically change to (or remain) inactive
      when an approval request is initiated.
   -  **Change status upon approval to Active**: When checked, the asset
      status will automatically change to (or remain) active when an
      asset is approved.
   -  **Change status upon rejection to Inactive**: When checked, the
      asset status will automatically change to (or remain) inactive
      when an asset is rejected.

|Configure approval settings|

.. |Approval request| image:: https://cdn3.webdamdb.com/100th_sm_s0h9U533JwV0.png?1526475654
   :width: 29px
   :height: 22px
.. |Request an approval| image:: https://cdn3.webdamdb.com/1280_YXOSYCOafR07.png?1526475941
   :width: 688px
   :height: 129px
.. |Request approval| image:: https://cdn2.webdamdb.com/1280_Mtm62lYREr01.jpg?1526475748
   :width: 350px
   :height: 275px
.. |Review a request| image:: https://cdn2.webdamdb.com/1280_IcG0Vcd3qa64.jpg?1526475966
   :width: 500px
   :height: 417px
.. |Approve| image:: https://cdn3.webdamdb.com/100th_sm_6HyJs5TpHnx7.png?1526476055
   :width: 28px
   :height: 28px
.. |Reject| image:: https://cdn3.webdamdb.com/100th_sm_gUzsUc9MDi12.png?1526476139
   :width: 29px
   :height: 29px
.. |Request is approved| image:: https://cdn3.webdamdb.com/1280_PHvxbpef6l15.jpg?1526475538
   :width: 480px
   :height: 368px
.. |Cancel a request| image:: https://cdn4.webdamdb.com/1280_QDvOXU3cOjJ1.jpg?1526475586
   :width: 466px
   :height: 272px
.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Configure approval settings| image:: https://cdn3.webdamdb.com/1280_M1OgIcsoch02.jpg?1526476034
   :width: 547px
   :height: 159px
