.. include:: /common/global.rst

Using environment variables with Node.js applications
=====================================================

One of the most significant |acquia-product:ac| user interface functions
is the handling of environment variables for your Node.js applications.
These variables are set globally, on a per-application basis, and can be
used to define anything your Node.js application may need to work with,
including Drupal APIs and environments.

The |acquia-product:ac| user interface enables you to add, edit, and
delete variables quickly and easily. Because working with variables is
restricted `by permissions </acquia-cloud/teams/permissions>`__, the
|acquia-product:ac| interface will contain appropriate items for working
with variables only if you have adequate permissions.

|Cloud environment variables list|

By default, the value of the variable is hidden for security. Click
**Show** to display the value, or **Hide** to hide it from view again.

Note

Adding, editing, or removing a variable will restart the environment and
update the `task log </acquia-cloud/monitor/tasks>`__.

.. _add:

Adding a variable
-----------------

Using the |acquia-product:ac| interface, complete the following steps to
add an environment variable:

#. Sign in to your |acquia-product:ac| account, and then select your
   Node.js application.
#. Select the environment to which you want to add a variable.
#. Click **Variables**, and then click **Add Environment Variable**.
#. Add the information for your variable:

   -  **Name** - Example: ``Drupal_API_URL``
   -  **Value** - Example: ``http://mydrupalsite.com/api``

#. Click **Add** to add the variable, or click **Cancel** to discard
   your changes.

You should now have a variable in the **Environment Variables** list.

.. _edit:

Editing a variable
------------------

If you have a problem or need to update an existing variable, you can
edit them from the **Variables** page, using the following procedure:

#. Sign in to your |acquia-product:ac| account, and then select your
   Node.js application.
#. In the left menu, click **Variables**.
#. Find the variable that you want to change, and then click its
   **Edit** link.
#. Replace the information in the **Value** text box with your updated
   data.
#. Click **Update**.

|acquia-product:ac| will display your variable's new value in the list.

.. _remove:

Removing a variable
-------------------

To remove an environment variable from use, complete the following
steps:

#. Sign in to your |acquia-product:ac| account, and then select your
   Node.js application.
#. In the left menu, click **Variables**.
#. Find the variable that you want to delete, and then click its
   **Remove** link.
#. Click **Update**.

|acquia-product:ac| will remove your variable from the list.

.. _filter:

Filtering for specific variables
--------------------------------

If you need to find a specific environment variable, you can use the
**Filter Variables** field in the upper-right of the webpage. This will
filter your displayed variables based on your entered text.

.. |Cloud environment variables list| image:: https://cdn3.webdamdb.com/1280_EajN0pMLJew2.png?-62169955200
   :width: 766px
   :height: 171px
