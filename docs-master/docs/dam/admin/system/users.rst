.. include:: /common/global.rst

Controlling user registration rules
===================================

.. container:: message-status

  This feature is available only to |acquia-product:dam| Professional
  subscribers.

Admins can automate new user approvals and permissions through the use
of registration rules. You can set rules to automatically add users to
certain groups and/or have them approved based on email domain, IP
address , or a response in a custom field.

.. _create:

Create a registration rule
--------------------------

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings|, and then click **System
   preferences**.
#. Click **Registration Rules** in the left navigation panel.
#. In the actions toolbar, click the ``(+)`` **Plus** sign.

   |Create registration rules|

#. Enter the rule name, which will only be seen by admins.
#. Click the dropdown next to **Add newly registered users to** and
   select the group that you want to add the users to.
#. Set the rule conditions to identify the target group of users based
   on their email domain, IP address, or a custom field. (Read more
   about `creating custom fields and configuring the registration
   form </dam/admin/system/custom>`__.)
#. You can `create multiple conditions </dam/admin/system/custom>`__ by
   clicking **Add a rule**. If the rule is based on email domain, be
   sure to add all subdomains to the rule. For example, a global company
   might include a condition for eu.company.com (for European
   employees), am.company.com (for American employess), and
   ap.company.com (for APAC employees).
#. Check the box next to **Activate new users upon registration** if you
   want the users to gain immediate access to the |acquia-product:dam|
   account.
#. Click **Save**.

   |Registration rules creation|

.. _edit:

Edit or delete a registration rule
----------------------------------

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings|, and then click **System
   Preferences**.
#. Click **Registration Rules** in the left navigation panel.
#. Click the wrench icon |Wrench| under the actions row for the
   registration rule that you want to update.
#. Select **Edit** to change the rule or **Delete** to remove the rule.

   |Registration rules|

.. _update:

Update status
-------------

You can enable or disable registration rules by updating the status. A
green active icon |Active| means that the rule is active and in use
while a red inactive icon |Inactive| means that the rule is inactive and
not in use.

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings| and select **System Preferences**.
#. Click **Registration Rules** in the left navigation panel.
#. Click the green active |Active| or red inactive |Inactive| icon to
   update the status.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Create registration rules| image:: https://cdn2.webdamdb.com/md_o3Is9uRCQN49.png?1527119449
   :width: 550px
   :height: 389px
.. |Registration rules creation| image:: https://cdn2.webdamdb.com/md_QQi0Kg4zqI91.png?1527119460
   :width: 550px
   :height: 390px
.. |Wrench| image:: https://cdn2.webdamdb.com/100th_sm_24n8wRX5SH32.png?1526475691
   :width: 24px
   :height: 21px
.. |Registration rules| image:: https://cdn4.webdamdb.com/md_6lLhp4QPxmj1.png?1527119473
   :width: 550px
   :height: 108px
.. |Active| image:: https://cdn4.webdamdb.com/100th_sm_ohQqGg1alY11.png?1526476063
   :width: 19px
   :height: 17px
.. |Inactive| image:: https://cdn4.webdamdb.com/100th_sm_Uvv89CvMqYN1.png?1526475540
   :width: 20px
   :height: 17px
