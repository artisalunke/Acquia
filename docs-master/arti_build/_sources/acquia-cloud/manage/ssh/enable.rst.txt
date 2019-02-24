.. include:: /common/global.rst

Enabling SSH access
===================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/ssh/enable/*

|acquia-product:ac| creates a Unix user account for each application called the *site user*. The application's Drupal/PHP code runs as this user, and all of an application's environments (Development, Staging, and Production) use the same Unix user. If there are multiple applications on a single web server, Unix security permissions keep them isolated from each other, because each application runs as a different Unix user.

To use SSH to sign into your web server as the site user, you must register SSH public keys for your Acquia user profile, which provides a more secure way of signing in to a virtual private server with SSH than with a password alone. You can add as many SSH keys as you want, each with its own nickname to help you keep track of them. However, you will sign in to the server as the site user's Unix username. The SSH key nickname is not a Unix username; it is just for your convenience in identifying your SSH keys.

.. note:: 

   If you use Git to manage your Drupal code, you must enable SSH to access your server.

Requirements
------------

To use SSH to access your server, you must meet the following
requirements:

-  Have the appropriate `permissions </acquia-cloud/ssh/enable/add-key#permissions>`__. This means you must be a member of a team assigned to the application, and have a role that includes accessing the server with SSH.
-  Register an SSH public key in your Acquia profile, as described in `Adding a public key </acquia-cloud/ssh/enable/add-key>`__.

It may take a few minutes after you add the key until you can use it to access your server.

Accessing your server using SSH
-------------------------------

When you connect to an environment with SSH, your PATH and other environment variables are set up in exactly the same way as they are for web processes, cron jobs, and Cloud hooks. In particular, whichever version of PHP you have configured will be the first in the PATH, and thus will be the default in your SSH session.

To use SSH to access your servers, use one of the following methods:

-  `Command line <#using-ssh-with-the-command-line>`__
-  `PuTTY (Windows only) <#using-ssh-on-windows-with-putty>`__

Using SSH with the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you enable SSH access, you can access your application's web servers using a command in this form:

.. code-block:: none

   ssh [SSH address]

where ``[SSH address]`` is your environment's server name. To determine your environment's server name, complete the following steps:

#. Sign in to the |cloud-ui|.
#. Select your application and environment.
#. In the menu to the left, click **Servers**.

The following list provides sample host names based on your subscription type:

-  ``srv-1.devcloud.hosting.acquia.com`` (|acquia-product:acs|)
-  ``ded-1.prod.hosting.acquia.com`` (|acquia-product:ace|, single-tier)
-  ``web-1.prod.hosting.acquia.com`` (|acquia-product:ace|, multitier)
-  ``web-1.[realm].hosting.acquia.com`` (|acquia-product:edg|, replacing ``[realm]`` with your realm)

As an example, the following command accesses the Staging environment of a website named ``example`` on the server named ``srv-456.devcloud.hosting.acquia.com``:

.. code-block:: none

   ssh example.test@srv-456.devcloud.hosting.acquia.com

.. note:: 

   You can SSH into multi-tier web servers or single-tier servers. You cannot SSH directly into |acquia-product:ace| database servers. Database servers generally have a server name that starts with ``fsdb`` or ``fsdbmesh``. For |acquia-product:ace| applications, you can check the **Servers** page in the |acquia-product:ui| to verify the server type. If the service for a server is listed as Database, you cannot SSH directly into it.

Using SSH on Windows with PuTTY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows users can use PuTTY, a free Telnet/SSH client for Windows, to open a window that allows command-line access to your files.

When you run PuTTY, enter the connection information for the server (or load a session previously configured to connect to your web server), and then click **Open**.

To install PuTTY on your computer, complete the following steps:

#. Download `PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`__ to your computer.
#. To run the application, double-click the PuTTY icon.
#. In **Category > Session**, in the **Host Name (or IP address)** field, enter the SSH address of the environment. You can find the SSH address for an environment in the |acquia-product:ui|, on the **Servers** page of the environment.
#. In **Category > Connection > SSH > Auth**, in the **Private key file for authentication** field, browse for the private SSH key file you saved on your computer.
#. In **Category > Session**, in the **Saved Sessions** field, enter a name for the server connection, and then click **Save**.

Use the session you created to connect securely to |acquia-product:ac|.

.. note:: 

   If you receive the following warning: *WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!*, it probably just means that your server has been relaunched. Read `SSH and RSA key warnings after a server relaunch </acquia-cloud/ssh/rsa-key-warning>`__ for information about how to handle this warning message.

Related topics
--------------

-  `Generating an SSH public key </acquia-cloud/ssh/generate>`__
-  `Adding a public key </acquia-cloud/ssh/enable/add-key>`__

.. |cloud-ui| replace:: \ |acquia-product:ui|\ 
.. _cloud-ui: https://cloud.acquia.com
