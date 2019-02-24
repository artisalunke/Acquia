.. include:: /common/global.rst

Setting asset download rules
============================

.. container:: message-status

  This feature is available only to |acquia-product:dam| Professional
  subscribers.

**Download Rules** give |acquia-product:dam| admins control over which
assets can be downloaded by configuring rules based on metadata,
download-request form responses, and groups of users. This makes it easy
for approved users to access assets, and keeps restricted assets out of
the hands of unapproved users.

.. _view:

Viewing download rules
----------------------

#. Sign in to |acquia-product:dam|.
#. Click the gear icon |Settings icon| in the top navigation panel, and
   then click **System Preferences**.
#. Click **Download Rules** in the left panel.

.. _create:

Create a Download Rule
----------------------

#. Click the settings icon |Settings| underneath the top navigation
   panel.
#. Create a name for your rule.
#. Select in the rule conditions from the dropdown menus. Be sure to
   select from left to right, as dropdown menu options will change
   depending on what was previously selected.
#. You can create multiple conditions for the rule using the following
   options:

   -  **OR** - Make the rule apply to more criteria
   -  **AND** - Make the rule apply to fewer criteria

#. To remove a condition, point to the condition’s dropdown menus, and
   then click the trashcan icon |Trashcan| to the right of the menus.
#. Select the rule action under **Run this action**.
#. Click **Save**.

.. _edit:

Edit download rules
-------------------

-  Drag and drop rules by the icon to change the hierarchy of rules.
-  Click the icon under **Actions** to edit or delete a rule.

.. _moreinfo:

Additional Information on Download Rules
----------------------------------------

-  Rules are applied in order from top to bottom.
-  Once conditions in a rule are met and the rule is applied, all
   subsequent rules are ignored.
-  If no rules apply, the group and folder download permissions will be
   used.

.. _example:

Example Download Rules
----------------------

Let’s say that you have a folder with images from a photoshoot. All of
these may be downloaded freely except for two images featuring a
particular person. These two images require approval prior to download.

A download rule makes it simple. First, you will need to distinguish
which assets require approval from those that may be freely downloaded.
You may manage this through a metadata field – in this case, we have
created a metadata field called ``Download Rules`` and tagged the two
restricted images with ``Requires Approval`` and the rest of the images
with ``May Be Downloaded``.

Here’s what the download rule could look like:

|Download rules 1|

Let’s change the scenario a bit: Now the two restricted images may be
automatically downloaded and used for editorial purposes only by the
*Superfly Employees* group. If a user from this group needs to download
it for anything other than editorial purposes, they must still get
approval.

You can set up this approval process by asking how the asset will be
used in a Download Request form. After creating a custom field titled
**How will this asset be used**, you may give the user the option to
choose *Editorial*, *Marketing*, or *Other*. See `Creating custom fields
and forms </dam/admin/system/custom>`__ for more information.

Here is what the download rule could look like:

|Download rules 2|

Lastly, using the scenario above, let’s say that the Agency group may
not download the two restricted assets at all, regardless of their
response on the download-request form.

Here is what the download rule could look like:

|Download rules 3|

.. |Settings icon| image:: https://cdn3.webdamdb.com/100th_sm_MgeBHUEa6wa3.png?1527121637
   :width: 25px
   :height: 25px
.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Trashcan| image:: https://cdn3.webdamdb.com/100th_sm_AeVdOw260Ik7.png?1527121637
   :width: 26px
   :height: 26px
.. |Download rules 1| image:: https://cdn2.webdamdb.com/md_EyiJmBNbC428.png?1527121614
   :width: 550px
   :height: 344px
.. |Download rules 2| image:: https://cdn4.webdamdb.com/md_cMPAYDHp0it9.png?1527121623
   :width: 550px
   :height: 466px
.. |Download rules 3| image:: https://cdn3.webdamdb.com/md_UAt560NlFGe1.png?1527121631
   :width: 550px
   :height: 466px
