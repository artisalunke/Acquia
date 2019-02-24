.. include:: /common/global.rst

Managing event notifications
============================

.. container:: message-status

  *This feature is available only to |acquia-product:dam| Professional
  subscribers.*

Event notifications can be enabled for Enterprise customers to provide
near real-time alerts about changes made to assets in your DAM.

.. _usecase:

Typical use cases
-----------------

-  You have a PIM system and need to know when new assets are uploaded
   or deleted so the system can be updated.
-  You distribute assets on a third-party website (such as your
   corporate website) and need to know when assets have been updated so
   you can make the required changes.

.. _enable:

Enable Event Notifications
--------------------------

To use event notifications, you will need to enable it in
|acquia-product:dam| and configure your Amazon SNS or SQS account to
relay messages between the |acquia-product:dam| and the desired client.

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings| in the top navigation, and then
   click **System Preferences**.
#. In the left menu, click **Event Notifications**.

   |Event notifications|

#. Complete the **Messaging Service Setup** section with information
   provided from your messaging service. For information about where you
   can find this information and how to set up the relay, see Amazon’s
   `SNS <https://aws.amazon.com/documentation/sns/>`__ and
   `SQS <https://aws.amazon.com/documentation/sqs/>`__ documentation.
#. Click **Save** for the section.
#. In the **Select Event Notifications** section, determine the amount
   of notifications for each of the available events, based on the
   following list values:

   -  **Full** - Includes the asset ID, filename, metadata fields
      (metadata name and value), keywords, the action performed (such as
      Asset upload, Asset deletion, and Metadata updates), who triggered
      the event, and the timestamp
   -  **Minimal** - Includes the asset ID, the action performed, and the
      timestamp
   -  **No notification**

#. Click **Save** for the section.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Event notifications| image:: https://cdn4.webdamdb.com/1280_ELiIShqf8Uy7.png?1526475665
   :width: 291px
   :height: 206px
