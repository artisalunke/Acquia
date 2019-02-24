.. include:: /common/global.rst

Managing applications using the command line
============================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/ssh/*

SSH, or secure shell, is a secure network protocol that you can use to
sign in to your |acquia-product:ac| environments and use command-line
tools.

SSH address
-----------

To sign into an environment with SSH, you need its SSH address. You can
find the SSH address for an environment in the |acquia-product:ui|, on
the Servers page of the environment, at the top of the list.

|Finding the SSH address on the Servers page|

The SSH address is in the form ``[application name].[environment name]@[server address]``, where:

-  ``[application name]`` is the name of your application.
-  ``[environment name]`` is the environment name (usually one of ``dev``, ``test``, or ``prod``). When you specify an environment, your PATH and other environment variables are set up in exactly the same way as they are for web processes, cron jobs, and Cloud hooks. In particular, whichever version of PHP you have `configured </acquia-cloud/manage/php>`__ will be the first in the PATH, and thus will be the default in your SSH session.
-  The ``[server address]`` is the URL of the web server, displayed in the |acquia-product:ui|, on the **Servers** page of an environment.

Tasks you can perform from the command line
-------------------------------------------

After you `enable SSH access </acquia-cloud/ssh/enable>`__ in |acquia-product:ac|, you can use SSH/shell access in the |acquia-product:ac| environment to perform the following tasks:

-  `Access your file storage directories from the command line <#access-your-file-storage-directories-from-the-command-line>`__
-  `Import and export databases <#import-and-export-databases>`__
-  `Use the Drush command-line tool <#use-the-drush-command-line-tool>`__

Access your file storage directories from the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You have shell access to all of the web nodes running your application,
using the same username and SSH public key credentials that you use for
rsync, scp, or SFTP on |acquia-product:ac|. To access your file storage
directories, use a command like:

.. code-block:: none

   ssh [SSH address]

For example, this command accesses the Staging environment of an application named ``example`` on the server with the address ``srv-456.devcloud.hosting.acquia.com``:

.. code-block:: none

   ssh example.test@srv-456.devcloud.hosting.acquia.com

Import and export databases
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ac| has unique database requirements that provide the best possible Drupal application performance. With SSH access enabled, you can use the |acquia-product:ac| database import script. For more information, see `Importing your database </acquia-cloud/create/import/manual-db>`__.

Use the Drush command-line tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ac| applications with SSH/shell access have an installed and configured instance of Drush. It enables you to perform many administrative and application maintenance tasks from the command line instead of using the Drupal administrative interface. For more information, see `About Drush on Acquia Cloud </acquia-cloud/drush>`__.

Limitations on shell access
---------------------------

Because of the technical requirements necessary for maintaining a highly available and redundant hosting platform, there are some limits on what you can access and do using shell access on |acquia-product:ac|:

-  **Limited file access**

   You should store files in the persistent network filesystem directory at ``/mnt/files/[application name].[environment name]``.

-  **No root access**

   You do not have root access, even if your application is running on dedicated cloud instances.

-  **Write access to your Drupal docroot**

   Use Git to manage your code on |acquia-product:ac|. By default, you cannot use shell access to install or update modules or to make other changes to your Drupal docroot directory (``/var/www/html``). If you want to make changes to your Drupal docroot directory, enable Live Development. You can use Live Development to modify only your Dev and Stage environments, not your Prod environment. Read more about `Using Live development mode to change code on your server </acquia-cloud/develop/livedev>`__.

.. |Finding the SSH address on the Servers page| image:: https://cdn3.webdamdb.com/1280_wxBwVX1Xaq01.png?-62169955200
   :width: 771px
   :height: 326px
