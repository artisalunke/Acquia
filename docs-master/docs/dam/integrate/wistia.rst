.. include:: /common/global.rst

Integration: Wistia
===================

If you have a Wistia subscription, you can use |acquia-product:dam| as
the central repository and distribution website for your media assets,
while leveraging Wistia's advanced video playback features and usage
analytics when displaying your content to your users.

.. important::
  The **Custom field 16** field in |acquia-product:dam| is used for the
  Wistia Hashed IDs, and should not be edited. Acquia recommends leaving
  this metadata field marked as Inactive. (Read more about `configuring
  the metadata schema </dam/admin/metadata>`__.)

.. _enable:

Enabling the integration
------------------------

*The information in this section applies only to users that have
`*Admin* </dam/admin/users#role>`__ role type permissions.*

Complete the following steps to enable the Wistia integration:

#. `Sign in to |acquia-product:dam| </dam/access>`__.
#. Click the **Settings** |Settings| icon, and then click **System
   Preferences**.
#. In the **Cloud Sharing Settings** section, click the **Cloud sharing
   channels** field, and then click **Wistia**.
#. Enter the **Wistia client ID** and **client secret**.
   If you do not know your Wistia client ID and secret, contact your
   Wistia admin.
#. Click **Save**.

.. _publish:

Publishing videos
-----------------

Users with `download permission </dam/admin/users#role>`__ in
|acquia-product:dam| (admins, contributors and regular users) can
publish their videos to Wistia by completing the following steps:

#. `Sign in to |acquia-product:dam| </dam/access>`__.
#. Navigate to and select a video asset.
#. Click the **Share** |Share| icon, and then click Wistia.
#. In the dialog box, click **Add Integration**, and then sign in with
   your Wistia credentials.
#. Authorize the |acquia-product:dam| application.
#. Select the target location in Wistia or create a new project, if
   desired.
#. Click **Send**.

The time needed to upload the video to Wistia and process it may vary
depending on the file size. After uploading and processing are complete,
the Wistia video player will replace the standard |acquia-product:dam|
video player.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Share| image:: https://cdn2.webdamdb.com/100th_sm_UuE2e2Ggqx91.png?1526475526
   :width: 23px
   :height: 20px
