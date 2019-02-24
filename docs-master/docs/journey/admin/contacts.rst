.. include:: /common/global.rst

Contacts
========

|acquia-product:aj| supports two kinds of contacts: *organization
contacts* and *per-project* contacts. Contacts added at the
*organization* level will receive notifications for any triggering event
(such as a graph failing to connect) for any project across the entire
organization, while *project* contacts will only receive notifications
for triggering events in the project.

Projects support *emergency contacts*, who are notified by email when
event listeners are unable to connect to their services (for example, a
database listening graph could not connect to its database). The email
will contain the following items:

-  project name
-  graph name
-  version
-  environment
-  error details

.. note:: Upon failure, a graph will remain deployed, and reattempts to connect
          will be made. Multiple notifications for the same graph indicate that
          graph is failing repeatedly.

Viewing organization or project contacts
----------------------------------------

To view existing contacts, perform the following actions:

#. Sign in to |acquia-product:aj|.
#. In the top menu, click **Admin**.
#. In the left menu, click **Projects** to add a per-project contact,
   or click **Organizations** to add an organization-level contact. |br|

   |Organizations|

#. From the list, click to select your organization (if adding an
   organization contact) or your project (if adding a per-project
   contact).
#. Click **Contacts** to view the contacts list.

   |Project contacts|

Adding contacts
---------------

Users who have *Admin* permissions for a project can add contacts to a
project, and Organization *Owners* can add organizational contacts. To
add a contact to a project or an organization, perform the actions
described in `Viewing organization or project contacts <#view>`__ to
view contacts, and then complete the following steps:

#. After |acquia-product:aj| displays the **Add Contacts** drawer, click
   **Add Contact**.
#. To add a new contact, click **Create Contact**.

   .. note::
      When adding a *Project* contact, users already registered to your
      Organization but not yet part of your selected project will appear in
      a list. To add one of these users to your project, click the name of
      the user, and click **Add Selected Contacts**.

   |Select a contact|

#. Provide the email address of the new contact you want to add, and
   then click **Create Contact**.

   |Create contact|

Deleting a contact
------------------

Users who have the *Admin* role for a project can delete the project's
contacts, and Organization *Owners* can delete organizational contacts.
To remove a user from a Project or Organization, complete the following
actions:

#. Sign in to |acquia-product:aj|.
#. In the top menu, click **Admin**.
#. In the left menu, click **Projects** to add a per-project contact, or
   click **Organizations** to add an organization-level contact.

   |Organizations|

#. From the list, click to select your organization (if removing an
   organization contact) or your project (if removing a per-project
   contact).
#. Click **Contacts** to view the contacts list.

   |Project contacts|

#. Click the trashcan icon |Trashcan| next to the contact that you want
   to remove.

The user will be deleted from the contact list, but will not be deleted
from |acquia-product:aj|.

.. |Organizations| image:: https://cdn2.webdamdb.com/1280_orqPTyXA5E71.png?1526475974
   :width: 181px
   :height: 139px
.. |Project contacts| image:: https://cdn4.webdamdb.com/1280_EJkdQOusU1i1.png?1526475683
   :width: 500px
   :height: 388px
.. |Select a contact| image:: https://cdn3.webdamdb.com/1280_2SigNAbJ4391.png?1526476093
   :width: 450px
   :height: 194px
.. |Create contact| image:: https://cdn2.webdamdb.com/1280_NBxDhYR7W18.png?1526475792
   :width: 296px
   :height: 194px
.. |Trashcan| image:: https://cdn4.webdamdb.com/1280_xcGR9zZM6F54.png?1526475804
   :width: 28px
   :height: 27px
