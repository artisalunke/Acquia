.. include:: /common/global.rst

Managing |acquia-product:ac| servers
====================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/servers/*

Each |acquia-product:ac| environment runs on one or more server
instances. The number and configuration of an environment's servers
depends on the level of the |acquia-product:aqs| the environment is part
of.

- |acquia-product:ace|
   Environments run in a high-availability architecture, with two or more load 
   balancers, web server nodes, and database server nodes for the Production 
   environment.
- |acquia-product:acs|
   All environments run on a single server, which may be dedicated to one 
   subscription, or may be shared with other subscriptions.
- |acquia-product:acfs|
   All environments run on a single server, which is shared with other 
   |acquia-product:acfs| applications.

You can view information about your |acquia-product:ac| server on the
**Applications > [Environment] > Servers** page. For
|acquia-product:acs|, you can also use this page to `reboot, relaunch,
resize, or suspend <#actions>`__ the server. For information about
configuring the environments that run on the |acquia-product:ac|
servers, see `Configuring an
environment </acquia-cloud/manage/configure>`__.

.. _info:

Viewing server information
--------------------------

The **Servers** page displays the following information about your
servers (information may vary based on your subscription):

-  **Name** - the server's name
-  **SSH address** - the address used to `SSH in to the
   server </acquia-cloud/ssh>`__
-  **IP address** - displayed only if it is an `Elastic IP
   address </acquia-cloud/manage/domains/dns#eip>`__
-  **Size** - the current size of the server, including both (**ECU**
   and **RAM**)
-  **Region** - indicates the AWS region in which the server is located
-  **Web** - Indicates whether this is a web server, and if it is
   currently active or passive.
-  **Database** - indicates whether this server contains a database, and
   what the database function (primary or secondary) of this server is
-  **Balancer** - indicates whether or not this server also is a web
   balancer
-  **Dedicated** - Indicates whether or not this is server is dedicated
   to this application, or if it is shared.
-  **Memcache** memory allocation - number of MB of allocated to
   Memcached.

|Server information|

If you have many servers, you may want to limit the ones that are
displayed. You can uncheck **Web**, **Database**, or **Balancer** to
hide servers with those functions.

.. _ssh:

Manage SSH credentials
----------------------

To connect to a server with SSH, you need to register an SSH public key
with your Acquia profile and have the necessary
`permissions </acquia-cloud/ssh/enable/add-key#permissions>`__. Click
**Manage SSH keys** to open the **Credentials** section of your Acquia
profile, and then `add an SSH key </acquia-cloud/ssh/enable/add-key>`__.

.. _graphs:

Server graphs
-------------

|Server graphs icon|\ |acquia-product:acs| customers can view their
server's graphs by clicking the **Server graphs** action icon. This link
directs to the `Stack Metrics </acquia-cloud/monitor/stackmetrics>`__
page. Users can click directly on the **Stack Metrics** in the sidebar
for this information as well.

.. _size:

Server size
-----------

The server size is the processing capacity (measured in ECU) and total
memory (in GB).

Location
--------

The server location is the AWS availability zone in which the server is
located. This is set when you create your |acquia-product:aqs|.

.. _actions:

Reboot, relaunch, resize, or suspend your server
------------------------------------------------

On the **Servers** page, you can reboot, relaunch, resize, or suspend
your server. You may also resize the server disk. This feature is
available only to |acquia-product:acs| customers. Acquia manages any
needed reboots or relaunches for |acquia-product:ace| applications,
while |acquia-product:acfs| applications use shared servers that
customers may not reboot, relaunch, or suspend.

.. admonition:: How |acquia-product:ac| handles non-persistent data with server relaunches or resizing

   -  **Log files** - Historical logs are stored in a location on the
      server that is optimized for fast read/write activity. Although this
      works for actively and simultaneously updating multiple log files,
      the directory will *not* persist after a server is relaunched. Log
      files do persist when a server is rebooted, however. For this reason,
      to ensure that logs are stored permanently, copy your log files to
      permanent storage before relaunching your server. For more
      information, see `Downloading historical logs directly from the
      server </acquia-cloud/manage/logs#cli>`__.
   -  **Host file changes** - Acquia does not support changing a server's
      ``hosts`` file.

|Reboot, relaunch, resize, or suspend a server|

Reboot
~~~~~~

To reboot your server:

#. On the **Servers** page, click **Reboot**.
#. In the confirmation dialog, enter your Acquia password.
#. Click **Reboot server**.

When you reboot your server, all applications on the server will be
unavailable for about 5 minutes while the server reboots.

Relaunch
~~~~~~~~

To relaunch your server:

#. On the **Servers** page, click **Relaunch**.
#. In the confirmation dialog, enter your Acquia password, and then
   click **Relaunch server**.

When you relaunch your server, all applications on the server will be
unavailable for 10 to 30 minutes while a new server is provisioned. You
should not relaunch your server unless you have been instructed to by
Acquia.

Resize
~~~~~~

To resize your server:

#. On the **Servers** page, click **Resize**.
#. On the **Resize server** page, drag the slider to select the new size
   for your server. As you move the slider, the Price change field
   displays the increase or decrease in the monthly cost for the server.

   |Resizing a server|

#. Click **Resize**.

When you resize your server, all applications on the server will be
unavailable for 10 to 30 minutes while a new server is provisioned.

To resize a server disk, see `Managing disk storage
space </acquia-cloud/manage/servers/storage>`__.

Suspend
~~~~~~~

To suspend your server:

#. On the **Servers** page, click the **Suspend server** link.
#. In the confirmation dialog, enter your Acquia password, and then
   click the **Suspend server** button.

All applications on your server will be unavailable until you relaunch
the server.

.. _memcache:

Memcached memory allocation
---------------------------

Memcached memory can be allocated and customized on a per-server basis.
This setting affects all environments on that server.

|cloud-memcache-allocation.png|

To view or change the allocated memory:

#. Click the **Configure** link next to the server.
#. Change the **Memcached memory (MB)** value.
#. Click **Save**.

.. |Server information| image:: https://cdn2.webdamdb.com/1280_UVWc2t9UWl91.png?1527199726
   :width: 943px
   :height: 530px
.. |Server graphs icon| image:: https://cdn4.webdamdb.com/150th_sm_I1DE0w1m112.png?1526475529
   :class: float-right
   :width: 115px
   :height: 76px
.. |Reboot, relaunch, resize, or suspend a server| image:: https://cdn4.webdamdb.com/1280_UhQ4HzWIwj27.png?1526476059
   :width: 748px
   :height: 397px
.. |Resizing a server| image:: https://cdn3.webdamdb.com/1280_gEkYGZjhvZT0.png?1526476156
   :width: 750px
   :height: 379px
.. |cloud-memcache-allocation.png| image:: https://cdn2.webdamdb.com/1280_UfXrYvUIEz13.png?1526475753
   :width: 601px
   :height: 362px
