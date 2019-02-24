.. include:: /common/global.rst

Known issues in Acquia Dev Desktop
==================================

This page describes known issues in |acquia-product:add|. For more
information, see `Troubleshooting </dev-desktop/troubleshooting>`__. If
you find a problem that isn't listed on this page, see `Reporting
issues, feature requests, and bugs </dev-desktop/reporting>`__ for
information about how to let us know.

-  **Issues with the included versions of PHP 7 and Xdebug** |br| 
   Xdebug may not work properly with the included version of PHP 7. You can download an updated version of Xdebug `here <https://xdebug.org/download.php>`__.
-  **mysqldump errors when syncing websites to Acquia Cloud** |br| 
   |acquia-product:add| may display the following error message for some users when they attempting to push websites from |acquia-product:add| to |acquia-product:ac|:

   .. code-block: none

      mysqldump: Couldn't execute 'SET OPTION SQL_QUOTE_SHOW_CREATE=1': You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'OPTION SQL_QUOTE_SHOW_CREATE=1' at line 1 (1064)

   This error message is displayed due to MySQL 5.6's deprecation of ``OPTION`` in the ``SET`` call. |br| 
   *Workaround* |--| Download and use the |acquia-product:add| - April 13, 2017 version (`macOS <https://www.acquia.com/sites/default/files/downloads/dev-desktop/AcquiaDevDesktop-2-2017-04-13.dmg>`__ / `Windows <https://www.acquia.com/sites/default/files/downloads/dev-desktop/AcquiaDevDesktop-2-2017-04-13.exe>`__).
-  **Timeout during stack start** |br| 
   You could get a timeout error (for example, ``Process 'MySQL database server' failed to start``) while starting |acquia-product:add| if you have unusually large or many databases. If this happens, you can try increasing the ``startTimeout``, as described in `Troubleshooting: Timeout during stack start </dev-desktop/troubleshooting#timeout>`__.
-  **Acquia Dev Desktop cannot make a local clone of an Acquia Cloud website if the website's name is longer than 21 characters** |br| 
   *Workaround* |--| Export your website from |acquia-product:ac| and then import it as a new website that has a name that is 21 characters or less. Then you can make a local clone of the new website in |acquia-product:add|.
-  **Domain Access module requires special configuration** |br| 
   To use the Domain Access module with |acquia-product:add|, you need to add a ``ServerAlias`` entry in the |acquia-product:add| Apache ``vhosts.conf`` configuration file. For details, see `Using Domain Access with Acquia Dev Desktop <%5Bacquia-product:kb%5Darticles/using-domain-access-acquia-dev-desktop>`__.
-  **Acquia Dev Desktop does not support usernames that include non-ASCII characters** |br| 
   This limitation does not apply to the Mac version of |acquia-product:add|. On Windows, use a Windows account with a username that includes only ASCII characters.
-  **On Windows, the path of a file cannot be longer than the Windows maximum path length of 260 characters** |br| 
   This limitation does not apply to the Mac version of |acquia-product:add|. You can experience this issue when trying to clone an |acquia-product:ac| website, or pulling files or code down from |acquia-product:ac|. |br| 
   *Workaround* |--| Either install |acquia-product:add| and the websites directory into a shorter Windows path (for example, ``c:\dd`` or ``c:\sites``, rather than ``c:\program files\dev desktop\...``) or consider renaming long custom file or path names in your |acquia-product:ac| website.
-  **Problems syncing with large websites** |br| 
   Sites hosted on |acquia-product:ac| may not be able to sync locally if they have too many files in one directory or extremely large files. For information about addressing files issues, see `About files </acquia-cloud/manage/files/about>`__, `Proactively organizing files in subfolders <%5Bacquia-product:kb%5Darticles/proactively-organizing-files-subfolders>`__, and `Optimizing file paths: Organizing files in subfolders <%5Bacquia-product:kb%5Darticles/optimizing-file-paths-organizing-files-subfolders>`__.
-  **Acquia Dev Desktop does not support syncing with Acquia Cloud Site Factory** |br| 
   The |acquia-product:add| **Host on Acquia Cloud** or **Clone from Acquia Cloud** buttons work only with |acquia-product:ac| websites, and not with |acquia-product:edg| websites.
-  **Acquia Cloud Site Factory overwrites Acquia Dev Desktop information in settings.php** |br| 
   The ``acsf-init`` command in |acquia-product:edg| removes lines in ``settings.php`` inserted by |acquia-product:add|. |br| 
   *Workaround* |--| Remove |acquia-product:add| changes to your ``settings.php`` file with ``git stash`` before executing the ``acsf-init`` command, unstashing the changes afterward.
-  **Acquia Cloud connection issues when using Acquia Dev Desktop from behind a firewall** |br| 
   Some users may experience connection issues or other seemingly unrelated errors when attempting to sync their |acquia-product:ac| websites locally or report bugs. This may be due to firewalls between your local computer and |acquia-product:ac|. |br| 
   *Workaround* |--| Acquia recommends that you whitelist ``*.acquia.com/`` in your firewall.
-  **Elevated permissions required for Microsoft Windows** |br| 
   |acquia-product:add| requires `elevated permissions </dev-desktop/install#reqs>`__ for both `installation </dev-desktop/install#windows>`__ and operation on computers running Microsoft Windows.
-  **Apache server fails to start on Windows 8 and 10** |br| 
   Some Microsoft Windows version 8 and version 10 users have reported that |acquia-product:add| fails to stop and restart Apache correctly during the website installation process, which prevents installation from completing successfully. |br| 
   *Workaround* |--| While Acquia corrects this issue, use one of the following two potential methods:

   -  On the **Acquia Dev Desktop** menu, click **Preference**, click the **Config** tab, and then click the **Edit** link next to the **Apache** field. This opens the ``httpd.conf`` file in Notepad. Close the file without making changes, which may allow you to create a new website.
   -  Before starting or restarting the application stack in |acquia-product:add|, use the Task Manager to end the Apache process manually.

-  **Trusted Host Settings Not enabled** |br| 
   Some Drupal websites show a ``Trusted Host Settings Not enabled`` message. See `Protecting against HTTP HOST Header attacks (prevent your site from thinking it is someone else) <https://www.drupal.org/node/1992030>`__ for suggestions.
-  **Drupal 8 installation displays a fatal error** |br| 
   When attempting to install Drupal 8, the installation process displays the following fatal error:

   .. code-block:: none

   'The service definition "renderer" does not exist.'

   *Workaround* |--| Do not supply a password when prompted for database credentials. For information about a Drupal core patch that can avoid this issue, see `Exception during installation when auto-creating the MySQL database with special characters <https://www.drupal.org/node/2443839>`__ on Drupal.org.
