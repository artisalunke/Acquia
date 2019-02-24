.. include:: /common/global.rst

Restricting metadata field access
=================================

.. container:: message-status

  This feature is available only to |acquia-product:dam| Professional
  subscribers.

Enterprise admins can restrict access to certain metadata fields based
on user groups. Users will only be able to view asset metadata that
their group has permission to view. In addition, only the metadata that
their group has permission to view will be embedded in the asset upon
download.

Example use case: You may have assets that include confidential metadata
like photographer address or contract information. You can restrict
access to these metadata fields to specific user groups such as legal or
account payable.

.. _apply:

Apply metadata permissions
--------------------------

#. Log in to the core application and click the |Settings| **Settings**
   icon in the top navigation panel. Select **Metadata Schema**.
#. Group permission are located in the right column under **Metadata
   Groups**. The default permission setting is **Everyone**.
#. Click inside the field – this opens a drop-down menu of groups.
   Select the ones you want to give access to the metadata field.
   |Metadata groups|
#. Remove permissions for a group by clicking the ``(X)`` on the right
   side of the group.
#. Click the **Save changes** button when you’re finished.

Feature is only available in Enterprise subscription plans.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Metadata groups| image:: https://cdn3.webdamdb.com/1280_wdiUD4V2C591.png?1526475669
   :width: 184px
   :height: 253px
