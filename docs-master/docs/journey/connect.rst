.. include:: /common/global.rst

Managing |acquia-product:aj| connections
========================================

.. toctree::
   :hidden:
   :glob:

   /journey/connect/*

.. container:: message-status

  This feature requires that you have the either the `Admin or
  Developer role </journey/admin/users/roles>`__ for your project.

With |acquia-product:aj|, you can interact with a wide range of external
systems to orchestrate customer journeys. |acquia-product:aj| allows you
to create *connections*, which define how your project communicates with
external systems. After creating a connection for an external resource,
you will add an `adaptor </journey/adaptors>`__ within your graph to
interact with the connected resource by reading, writing, or deleting
data.

Creating a connection
---------------------

To create a connection in a project, complete the following actions:

#. Sign in to |acquia-product:aj|.
#. In the top menu, click **Admin**, and then click **Projects** in the
   left menu.
#. Find your project in the project list, and then click its project
   name.
#. In the project's detail view, click **Connections**.
#. Click **Add New Connection** to display the **Add Connection**
   dialog.
#. In the **Type** list, select your desired connection type from
   following options:

   -  |lift connect|_
   -  `Database </journey/connect/database>`__
   -  `E-mail </journey/connect/email>`__
   -  `File </journey/connect/file>`__
   -  `Queue </journey/connect/message>`__
   -  `Twitter </journey/connect/twitter>`__
   -  `REST Web Service </journey/connect/rest>`__
   -  `SOAP Web Service </journey/connect/soap>`__

.. |lift connect| replace:: \ |acquia-product:cha|\ 
.. _lift connect: /journey/connect/lift

#. In the **Name** field, enter a descriptive name for the connection.

.. note:: When naming your function, base the connection's name on the function
          it performs, rather than the development stage you are creating it
          in, as functional names will make the connection easier to understand
          as it propagates through multiple environments.

#. Click **Save**.

Configuring a connection for an environment
-------------------------------------------

Each connection may have a different configuration for each environment.
(For more information on environments, read `Creating and managing
environments </journey/admin/env>`__.) To add a connection for a
specific environment, complete the following steps:

#. Sign in to |acquia-product:aj|.
#. In the top menu, click **Admin**, and then click **Projects** in the
   left menu.
#. Find your project in the project list, and then click its project
   name.
#. In the project's detail view, click **Connections**.
#. In the **Existing Connections** list, find the connection you want to
   configure for an environment and click the environment name.
#. To the right, the **Connector Editing** pane will appear.
#. Enter the connection details for your chosen connection type.
#. Click **Save** above the *Connector Editing* header to commit your
   changes.
   |connection properties|

Testing a connection
--------------------

You can verify an existing connection to verify it is working normally.
To test a connection, complete the following steps:

-  Sign in to |acquia-product:aj|.
-  In the top menu, click **Admin**, and then click **Projects** in the
   left menu.
-  Find your project in the project list, and then click its project
   name.
-  In the project's detail view, click **Connections**.
-  In the **Existing Connections** list, find the connection you want to
   configure for an environment and click the environment name.
-  In the **Connector Editing** panel, click **Test Connection**.

|Test connection|

If the connection is successful, |acquia-product:aj| will display a
**Connection successful** message.

Deleting a connection
---------------------

You can delete a connection. This will delete the connection for every
environment you have defined in your project. To delete a connection,
complete the following steps:

-  Sign in to |acquia-product:aj|.
-  In the top menu, click **Admin**, and then click **Projects** in the
   left menu.
-  Find your project in the project list, and then click its project
   name.
-  In the project's detail view, click **Connections**.
-  In the **Existing Connections** list, find the connection you want to
   configure for an environment and click the environment name.
-  Find the connection you want to delete and click its name. A
   **trashcan** icon will appear.
-  Click the **trashcan** icon.
-  In the **Delete Connection** dialog, click **Yes, Delete
   Connection**.

.. |connection properties| image:: https://cdn3.webdamdb.com/1280_2nFzcTfee734.png?1526475734
   :width: 550px
.. |Test connection| image:: https://cdn4.webdamdb.com/1280_6PPPfoy8cs02.png?-62169955200
   :width: 550px
   :height: 173px
