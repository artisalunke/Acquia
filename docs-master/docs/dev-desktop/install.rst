.. include:: /common/global.rst

Installing Acquia Dev Desktop
=============================

.. toctree::
   :hidden:
   :glob:

   /dev-desktop/install/*

This page describes how to install |acquia-product:add| on your computer.

.. _reqs:

Requirements
------------

Before installing |acquia-product:add|, ensure that you have met the following requirements on your computer:

-  You are using a `supported software </dev-desktop/install/supported>`__ version.
-  Your account has elevated or administrative privileges. |br| 
   |acquia-product:add| starts and stops processes, such as PHP and Apache, which may require higher level system privileges.

Procedures
----------

To install |acquia-product:add| on your local computer, use one of the following methods: `guided installation application <#guided>`__ or the `command line installer <#command>`__:

-  *Installing using the application* |br| 
   |acquia-product:add| includes an application that can guide you through the installation process. To use this installation method, complete the following steps:

   #. `Download <https://dev.acquia.com/downloads>`__ |acquia-product:add| from the Acquia Downloads page. Select the Mac or Windows version of |acquia-product:add|, depending on the operating system of your local computer. |br| 
      For information about supported operating system versions, see the `documentation page </dev-desktop/install/supported>`__ relating to this topic.
   #. Based on the file that you downloaded and your operating system, run the installer using the appropriate instructions:

      -  *macOS* |--| Double-click the installation ``.dmg`` file to mount it, and then open the |acquia-product:add| Installer. Depending on your security settings and OS version, you might need to enter your administrative password or accept other security warnings to continue with the product installation.

         .. note::

             Do not drag the |acquia-product:add| Installer into the Applications folder.

      -  *Windows* |--| Navigate to the folder where you downloaded the file, and then run the |acquia-product:add| installation file.

         .. note::

             Your Windows user home directory must be writable, or the installation will fail.

   #. Select **Yes** to accept the license agreement. |acquia-product:add| optionally tracks diagnostic and usage data. If you want to opt out of sending data to Acquia, clear the related check box. For information about what information is sent if you enable this option, see `Reporting diagnostic and usage information </dev-desktop/sending>`__.
   #. Click **Next**.
   #. *Windows-only:* If you want your website to be able to send email, select **XMail server** on the Select components page, and then click **Next**. The XMail server is a full-featured email server, and it allows websites hosted in |acquia-product:add| to send email.
   #. On the **Choose install locations** page, complete the following steps:

      .. note::

         Avoid using spaces in the |acquia-product:add| website's folder name.

      a. Select the folder in which to install |acquia-product:add|.
      b. Select the folder for the files associated with your websites.
      c. Click **Next**.

   #. On the **Port settings** page, you can define alternate ports to access the Apache web server and MySQL database server if the standard ports conflict with other applications on your web server. In most cases, you can just accept the default settings. |br| 
      After you verify the port settings, click **Next**.
   #. On the **Ready to install** page, click **Next** to complete the installation.

      .. admonition:: Note for Windows users

         Near the end of the |acquia-product:add| installation process, Windows might display Windows security alerts regarding components of |acquia-product:add|. If you want to access websites created on this computer from the Internet or your network, allow access and unblock the Windows Firewall. Alternatively, you can allow the Windows Firewall to continue to block the application if required by your security needs, and you do not need to access your website from outside of your computer.

-  *Installing using the command line installer* |br| 
   As an alternative, for quick, unattended installations that do not prompt the user for any install options (such as the installation path), you can use the `command line installer </dev-desktop/install/commandline>`__.

After the installation completes, you can start |acquia-product:add| by selecting the **Launch** check box, and then clicking **Finish**.

.. admonition:: Note for Windows users

   When you start |acquia-product:add|, Windows may display a User Access Control dialog box that requests a username and password. There are two reasons that Windows requests these items:

   -  Opening the ports for Apache and MySQL
   -  Keeping the computer's ``hosts`` file in sync for local name resolution

For information about the folders and files that are created in your local file system when you install |acquia-product:add| and add one or more Drupal websites, see `Acquia Dev Desktop folders and files </dev-desktop/install/files>`__.

.. _part:

What if you've already installed another xAMP stack or part of it?
------------------------------------------------------------------

|acquia-product:add| installs separate copies of the xAMP stack onto your computer, both to ensure that you have the versions of the software required for Drupal, and to ensure that you do not affect the settings of the applications that you have already installed on your computer.

.. _next:

What's next?
------------

You can now use |acquia-product:add| to create websites on your local computer. For information about the different website creation options available to you, see `Getting started with Acquia Dev Desktop </dev-desktop/start>`__.
