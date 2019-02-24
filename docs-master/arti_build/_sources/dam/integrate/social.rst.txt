.. include:: /common/global.rst

Social publishing with Acquia DAM
=================================

Social publishing allows users with appropriate access to publish
digital assets from |acquia-product:dam| to Facebook, Twitter and
YouTube. (Additional options are available with the `Hootsuite
integration </dam/integrate/hootsuite>`__.)

.. _enable:

Enabling the integration
------------------------

*The information in this section applies only to users that have
`*Admin* <#role>`__ role type permissions.*

Use the following instructions to enable social publishing from
|acquia-product:dam|:

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings| in the top menu, and then click
   **System Preferences**.
#. In the **Cloud Sharing Settings** section, click the **Social
   publishing channels** field, and then click the channels that you
   want to enable, from the following list:

   -  **Facebook**
   -  **Twitter**
   -  **YouTube**

#. Click **Save**.

After social publishing is enabled, users with the *Contributor* role,
and other users with the *View and download assets* permission will be
able to publish to social channels. For more information about assigning
roles and permissions, see `Managing users and
groups </dam/admin/users>`__.

.. _publish:

Publishing assets to a social channel
-------------------------------------

To publish one or more assets to a social channel, complete the
following steps:

#. Sign in to |acquia-product:dam|.
#. Click the asset that you want to publish.

   .. note::
      Supported file types include JPG, PNG, GIF, WEBP, MOV, MPEG4, MP4,
      AVI and WMV. The maximum asset size is 5 GB.

#. From the Asset Details page, click the publishing icon |Publishing|
   in the actions toolbar.
#. Select the social channel to which you want to publish.
#. Add an account for the social channel by clicking **Link New
   Account** from the **Select Account** list.

   |Link new accounts|

#. You will be prompted to sign in to the social channel you selected.
   Follow the instructions to grant |acquia-product:dam| access to
   publish to your account.
#. After you have granted authorization, enter any text that you want in
   the post.
#. Click **Send** to post immediately. Click **Change** to schedule your
   post for later.

   |Scheduling posts|

.. _reports:

Viewing social publishing activity reports
------------------------------------------

*The information in this section applies only to users that have
`*Admin* <#role>`__ role type permissions.*

To view a report of social publishing activity, click **Reports**, and
then click **Publish Schedule**. From the report you can edit, cancel or
view posts.

You can also view a specific post on a social channel. To do this, click
the wrench icon |Wrench| in the **Action** column, and then click
**View**.

If you need to edit scheduled posts, click the wrench icon |Wrench|, and
then click **Edit**.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Publishing| image:: https://cdn2.webdamdb.com/100th_sm_27ZhCd5N6wi6.png?1527200784
   :width: 26px
   :height: 24px
.. |Link new accounts| image:: https://cdn2.webdamdb.com/1280_6aNTcto5VDF7.png?1526475531
   :width: 550px
   :height: 418px
.. |Scheduling posts| image:: https://cdn4.webdamdb.com/1280_YKsfmNa1qNQ2.png?1526475563
   :width: 550px
   :height: 417px
.. |Wrench| image:: https://cdn2.webdamdb.com/100th_sm_24n8wRX5SH32.png?1526475691
   :width: 24px
   :height: 21px
