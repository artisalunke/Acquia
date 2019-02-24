.. include:: /common/global.rst

Connecting to Acquia Cloud with an FTP client
=============================================

You can use a third-party FTP client to connect to your
|acquia-product:ac| environments and work directly with your code,
files, backups, and import folders.

.. _before:

Before you begin
----------------

To successfully connect with and use FTP with your |acquia-product:ac|
based applications, take the following steps:

-  Register your public key with |acquia-product:ac|
    To connect to an |acquia-product:ac| server, you need to both have a
    private/public key pair and register the public key in
    |acquia-product:ac|. For information about how to do this, see
    `Enabling SSH access </acquia-cloud/ssh/enable>`__.
-  Enable Live Development
    You must first enable live development to interact with your
    codebase on |acquia-product:ac| using SFTP. For information about
    how to do this, see `Using Live development mode to change code on
    your server </acquia-cloud/develop/livedev>`__. If you are working
    with files, this step is not necessary.

   .. important:: 

      After you make changes to your codebase using live development, you
      must commit all the changes to your |acquia-product:ac| repository,
      or else the changes will be lost when you exit live development.

.. _choose:

Selecting an FTP client
-----------------------

You can use just about any client that supports SFTP connections to
remote servers. Here are a few possibilities to consider:

-  `Cyberduck <http://cyberduck.ch/>`__ - MacOS
-  `Transmit <http://panic.com/transmit/>`__ - MacOS
-  `WinSCP <http://winscp.net/eng/download.php>`__ - Windows

.. _winscp:

Example
-------

Here is an example that demonstrates how to connect to
|acquia-product:ac| with SFTP, based on WinSCP:

#. Start the WinSCP application.
#. In left pane of the **WinSCP Login** screen, select **Session** and
   enter the following:

   |WinSCP login screen|

   -  Under **File protocol**, select **SFTP**.
   -  In the **Host name** field, enter the full DNS server name of the
      |acquia-product:ac| server you want to connect to. The server name
      is listed on the **Cloud > Servers** page of the Acquia user
      interface. For example: ``ded-1234.devcloud.hosting.acquia.com``.
   -  In the **User name** field, enter ``[site].[env]``, where
      ``[site]`` is the site name, and where ``[env]`` is the
      environment you want to connect to (one of ``prod``, ``test``, or
      ``dev``).
   -  **Password**: Leave this field blank.

#. Click **Advanced**.

   |WinSCP advanced settings|

#. In the left pane of the **Advanced Site Settings** page, select
   **Directories**.
#. Under **Remote directory**, enter the live development folder for
   your application's Development environment,
   ``/mnt/gfs/[sitename].dev/livedev/docroot``.
#. Under **Local directory**, enter the docroot folder in your local
   code repository.
#. In the left pane of the **Advanced Site Settings** page, select
   **Authentication**.
#. In the **Private key file** field, select your private key. You may
   need to convert your SSH key into a format compatible with WinSCP.
   You can use PuTTYgen (which is included in the WinSCP installation
   package) to convert your key into the ``.ppk`` format required by
   WinSCP. For more information, see `Converting SSH keys for
   WinSCP </acquia-cloud/ssh/sftp-key>`__.
#. Click **Ok**.
#. In the **Save session as** dialog, enter ``[site].[env]``, where
   ``[site]`` is the site name, and where ``[env]`` is the environment
   you want to connect to (one of ``prod``, ``test``, or ``dev``).
#. Click **Login** to connect to your |acquia-product:ac| server.

.. |WinSCP login screen| image:: https://cdn3.webdamdb.com/1280_64eA4XIUCp55.png?1526475997
   :class: no-sb
   :width: 590px
   :height: 434px
.. |WinSCP advanced settings| image:: https://cdn3.webdamdb.com/1280_wa8rjcjoQSd4.png?1526475895
   :width: 561px
   :height: 460px
