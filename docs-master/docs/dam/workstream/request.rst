.. include:: /common/global.rst

Request forms
=============

.. toctree::
   :hidden:
   :glob:

   /dam/workstream/request/*

Request forms are configurable forms that, when completed and submitted,
are used to trigger the creation of a new task in Workstream.

.. _create:

Create Request Forms
--------------------

Request forms can only be created by admins.

#. Log in to Workstream and click **Manage** on the secondary
   navigation.
#. Click **Request Forms**:
   |Request Forms|
#. Click **+New Form** in the upper right-hand corner to create a new
   form template.
#. Enter a name for the form. When users search for and submit the form,
   this will be the name that displays.
#. Drag the desired field(s) from the left panel and drop into the body
   of the form.
   |Build form from components|

.. _fieldtypes:

Field types
~~~~~~~~~~~

**System Fields**: Values added to these fields display in the task
details page. To edit the text in these fields, add a field to a form,
select the text displayed in the field name and enter your desired field
name.

-  Email
-  Assignee
-  Due Date
-  Task Description
-  Keywords - keywords entered by the requester will be automatically
   applied to assets added to the task from your computer.
-  Attachments

**Custom Fields**: These fields can be customized for the specific form.
Once the field is added, enter the desired label:

-  Short Answer
-  Long Answer
-  Dropdown - rows will auto-populate with add an item, enter text for
   the dropdown option on each row.
-  Date
-  Checkboxes - click add an item to enter the checkbox options.
-  Multiple Choice - click add an item to enter the choice options.

**Static Fields**: These fields are fixed in the form. They are
typically added to provide more details about the request form.

-  Title
-  Image - allows images to be attached to the request form.
-  Description

Click **Preview** to show a preview of the form from a requester’s
perspective. Click **Save** to save the form as a draft, which is only
accessible by admins. Click **Publish** to save and publish the form.
Once published, the form will be available to the Workstream groups
listed in the **Settings**.

.. _editfield:

Editing a field
~~~~~~~~~~~~~~~

-  **Move**: Click and hold the grab arrow |Grab icon| to move the field
   to its new location in the form.
-  **Delete**: Click the **Trashcan** |Trashcan| icon.
-  **Require**: Toggle the slider to the right to make a field required.

Settings
--------

Click Settings in the bottom right, below the field options.

#. Who can submit: all Logged In user groups will have access to the
   request form by default.

   -  To add groups, start typing the name of the group that should be
      able to submit this form and click it when it appears in the list.
      Add all groups that should have access to this request form.
   -  To remove groups, hover your mouse over the group name and click
      the ``(X)`` icon.

#. Publish to Brand Portal: To allow non-Workstream users to complete
   request forms, the form must be published to a |acquia-product:bc|
   portal.

   -  Click the toggle next to the |acquia-product:bc| portal that the
      request form should be published, and therefore made available,
      too. Read more about `publishing request forms in
      |acquia-product:bc| </dam/workstream/request/brand-connect>`__.
      |Settings left side|

.. _edit:

Edit Request Forms
------------------

#. Log in to Workstream and click **Manage** on the secondary
   navigation.
#. Click **Request Forms**.
#. Click the request form that you want to edit.

.. _delete:

Unpublish, Duplicate or Delete Request Forms
--------------------------------------------

#. Log in to Workstream and click **Manage** on the secondary
   navigation.
#. Click **Request Forms**.
#. To Unpublish a request form, toggle the slider to the right. To
   publish it again, toggle the slider back to the left.
#. Hover your mouse over the request form that you want to duplicate or
   delete and click the |Options| **Options** icon.
#. Select the following

   -  **Duplicate** - to make a copy of the request form.
   -  **Delete** - to delete the request form.
      |Form options|

.. _submit:

Submit a Request Form from Workstream
-------------------------------------

Workstream users can submit request forms in Workstream. Non-Workstream
users can submit request forms in |acquia-product:bc|. Completed request
forms become tasks in Workstream.

#. Log in to Workstream.
#. Click **+New Task** in the upper right.
#. Click **Get Started** under the request form that you’d like to
   complete. Only request forms that a user has permission to view will
   be displayed.
#. Complete the form.
#. Click **Save for Later** to save a draft, or click **Submit** to
   create a new task.

.. |Request Forms| image:: https://cdn3.webdamdb.com/md_AKD1S14Z9mZ8.png?1526475508
   :width: 350px
   :height: 143px
.. |Build form from components| image:: https://cdn2.webdamdb.com/md_EaU1cFle7mJ4.png?1526476018
   :width: 260px
   :height: 550px
.. |Grab icon| image:: https://cdn4.webdamdb.com/100th_sm_wGgZI6mCq52.png?1526475900
   :width: 25px
   :height: 22px
.. |Trashcan| image:: https://cdn2.webdamdb.com/100th_sm_o7kw8p8iR591.png?1526476134
   :width: 24px
   :height: 24px
.. |Settings left side| image:: https://cdn3.webdamdb.com/md_IsJMw3NJJlJ6.png?1526476049
   :width: 249px
   :height: 500px
.. |Options| image:: https://cdn4.webdamdb.com/100th_sm_MD4MvX7g55x7.png?1526475682
   :width: 18px
   :height: 22px
.. |Form options| image:: https://cdn4.webdamdb.com/md_AeeeN0oIlhJ2.png?1526475546
   :width: 275px
   :height: 234px
