.. include:: /common/global.rst

Managing applications with the |acquia-product:ac| interface
============================================================

Click **Develop** in the |acquia-product:ui| toolbar to view the
**Applications** page. The Applications page displays all of the
applications that you have access to that are hosted on
|acquia-product:ac|.

.. _views:

Modifying views of applications
-------------------------------

Click the grid or list icons to switch between:

-  *Grid view* - Displays a tile for each application with its name and
   URL
-  *List view* - Lists each application with its name and URL

|Choose list or grid view of your applications|

You can also use the **Filter Applications** field to the right of the
grid and list icons to limit which applications are displayed. Start
typing in the field, and the Applications page will display only those
applications whose names match the string that you enter. You can also
use 'or' as an operator to use more than one filter.

|acquia-product:ac| will display one or more *badges* for each
application, which indicates the application's type and subscription
level. For more information about badges, see `Working with
environments </acquia-cloud/manage/environments#type>`__.

.. _actions:

Using the Applications page
---------------------------

The **Applications** page provides the following features to help you
manage your applications:

-  Click the application name (or, in grid view, **Manage**) to work
   with the application's
   `environments </acquia-cloud/manage/environments>`__.
-  Click the application's URL to visit the application in a new browser
   window.

.. _add:

Adding applications
-------------------

Click **Add Application** to `add a new
application </acquia-cloud/create>`__ to one of your existing
|acquia-product:ac| subscriptions or purchase an additional
|acquia-product:acs| subscription.

.. _rename:

Renaming applications
---------------------

To change the name of an existing application, complete the following
steps:

#. In the |acquia-product:ui|, select the application.
#. In the upper right of the webpage, click **Rename**.

   |Renaming an application|

#. Enter the new name for the application, and then click **Rename
   application**.

.. _remove:

Deleting applications
---------------------

You cannot delete applications from the |acquia-product:ac| interface.
If there are applications that you want to remove, `contact Acquia
Support </support#contact>`__ to have them remove the applications from
|acquia-product:ac|.

.. _appid:

Obtaining your subscription's application ID
--------------------------------------------

Occasionally, your use of |acquia-product:ac| may require you to provide
your application's unique identifier—this may be referred to as the
``UUID`` for the subscription, or the ``Application_ID``. Use the
following method to locate your application's ID:

#. Sign in to `|acquia-product:ac| <https://cloud.acquia.com>`__.
#. Select the subscription for which you want the ID.
#. Examine the |acquia-product:ac| webpage's URL in your browser's
   address bar, which should appear similar to the following value:

   ``https://cloud.acquia.com/app/develop/applications/[string]``

   The ``[string]`` is your application's ``UUID``.

This ID may be used with methods in the |acquia-product:api|, and with
other development applications that can use it for identifying a
particular application to read or modify.

.. |Choose list or grid view of your applications| https://cdn3.webdamdb.com/1280_2O81FBqRkCS4.png?1526475537
   :width: 1269px
   :height: 263px
.. |Renaming an application| image:: https://cdn4.webdamdb.com/1280_gFtAb3MkAS02.png?1526475756
   :width: 1266px
   :height: 264px
