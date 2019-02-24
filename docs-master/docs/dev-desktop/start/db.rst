.. include:: /common/global.rst

Importing a database
====================

If you have an existing Drupal website, you can import its database into
a local |acquia-product:add| website. You can choose from two different
methods:

-  `Import a MySQL database dump file <#dump>`__
-  `Import from a MySQL server <#server>`__

.. _dump:

Import a MySQL database dump file
---------------------------------

If you have a MySQL database dump file on your local computer, you can
import it when you install a Drupal distribution or start with an
existing local website. The dump file can either be in ``.sql`` format
or compressed in ``.sql.gz`` format.

#. In the **Install a Drupal distribution (step 2)** or **Import local
   Drupal site** dialog box, in the **Database** list, click **Start
   with MySQL database dump file**.

   |Import a database dump file|

#. In the **Dump file** field, browse for the location where you saved
   the database dump file on your computer.
#. Click **Finish**.

.. _server:

Import from a MySQL server
--------------------------

You can import a database from another MySQL server if you know its
connection information.

#. In the **Install a Drupal distribution (step 2)** dialog box, in the
   **Database** list, click **Start by importing from another MySQL
   server**.

   |Import from another MySQL server|

#. Select the **Protocol** to use when connecting to the MySQL server
   (either **TCP** or **Socket file**).
#. In the **Host** field and the **Port** field, enter the host name
   (URL) and port number of the MySQL server, respectively.
#. Click **Get list** to select an existing database from those
   available on the MySQL server.
#. Enter values for the following fields:

   -  **Username** - The user's username to connect to the MySQL server
   -  **Password** - The user account's password to connect to the MySQL
      server
   -  **New database name** - Your Drupal website's database (in most
      cases, you can accept the default value, which will match the
      local website name that you chose)

#. Click **Finish**.

.. |Import a database dump file| image:: https://cdn2.webdamdb.com/1280_6a6I8sHcUXK7.png?1526475610
   :width: 590px
   :height: 234px
.. |Import from another MySQL server| image:: https://cdn2.webdamdb.com/1280_kn45ULRJGSw6.png?1526476186
   :width: 590px
   :height: 365px
