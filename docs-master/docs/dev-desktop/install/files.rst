.. include:: /common/global.rst

|acquia-product:add| folders and files
======================================

When you install |acquia-product:add| and add one or more Drupal
websites, the following directories and files are created in your local
file system, depending on whether you are using `macOS <#mac>`__ or
`Windows <#windows>`__:

.. _mac:

macOS directories and files
---------------------------

+-----------------------------------+-----------------------------------+
| Directory/File                    | Description                       |
+===================================+===================================+
| ``/Applications/DevDesktop/apache | The virtual hosts file for all    |
| /``                               | websites known to the             |
|    ``conf/vhosts.conf``           | |acquia-product:add| application. |
+-----------------------------------+-----------------------------------+
| ``/Applications/DevDesktop/``     | A package that contains the       |
|    ``Acquia Dev Desktop.app``     | configuration files for           |
|                                   | |acquia-product:add|.             |
+-----------------------------------+-----------------------------------+
| ``~/Sites/devdesktop``            | A directory containing            |
|                                   | |acquia-product:add| websites.    |
+-----------------------------------+-----------------------------------+
| ``~/.acquia/backup``              | When you upgrade to a newer       |
|                                   | version of |acquia-product:add|,  |
|                                   | your existing installation is     |
|                                   | backed up to this directory.      |
+-----------------------------------+-----------------------------------+
| ``~/.acquia/DevDesktop/``         | The website configuration files   |
|    ``DrupalSettings``             | included by ``settings.php``.     |
+-----------------------------------+-----------------------------------+
| ``~/.acquia/DevDesktop/Drush/Alia | Drush aliases for local and       |
| ses/``                            | |acquia-product:ac| websites      |
|    ``aliases.drushrc.php``        | (downloaded from                  |
|                                   | |acquia-product:ac|). These       |
|                                   | aliases include the host,         |
|                                   | docroot, user, site, and          |
|                                   | environment of the                |
|                                   | |acquia-product:ac| website.      |
+-----------------------------------+-----------------------------------+
| ``~/.acquia/DevDesktop/Drush/Alia | Drush aliases for all remote      |
| ses/``                            | |acquia-product:ac|-hosted        |
|    ``cl.[sitename].aliases.drushr | websites known to                 |
| c.php``                           | |acquia-product:add|. These       |
|                                   | aliases include the host,         |
|                                   | docroot, user, site, and          |
|                                   | environment of the website.       |
+-----------------------------------+-----------------------------------+

Any passwords or user names in these files are encrypted to protect your
security.

If you chose something other than the default locations for the
|acquia-product:add| stack location and sites directory when you
installed |acquia-product:add|, these paths will vary, based on the
locations you chose.

Note

In macOS, the ``/.acquia`` directory is hidden. To locate the directory,
complete the following steps:

#. Open Finder.
#. In the menu bar, select **Go > Go to folder**.
#. Enter the path of the directory, and then click **Go**.

.. _windows:

Windows directories and files
-----------------------------

+-----------------------------------+-----------------------------------+
| Directory/File                    | Description                       |
+===================================+===================================+
| ``C:\Program Files (x86)\Dev Desk | The virtual hosts file for all    |
| top\``                            | websites known to the             |
|    ``apache\conf\vhosts.conf``    | |acquia-product:add| application. |
+-----------------------------------+-----------------------------------+
| ``C:\Program Files (x86)\Dev Desk | The executable file for           |
| top\``                            | |acquia-product:add|.             |
|    ``AcquiaDevDesktop\AcquiaDevDe |                                   |
| sktop2.exe``                      |                                   |
+-----------------------------------+-----------------------------------+
| ``C:\Users\[username]\Sites\``    | A directory containing            |
|    ``devdesktop``                 | |acquia-product:add| websites.    |
+-----------------------------------+-----------------------------------+
| ``C:\Users\[username]\.acquia\``  | When you upgrade to a newer       |
|    ``backup``                     | version of |acquia-product:add|,  |
|                                   | your existing installation is     |
|                                   | backed up to this directory.      |
+-----------------------------------+-----------------------------------+
| ``C:\Users\[username]\.acquia\``  | The website configuration files   |
|    ``DevDesktop\DrupalSettings``  | included by ``settings.php``.     |
+-----------------------------------+-----------------------------------+
| ``C:\Users\[username]\.acquia\Dev | Drush aliases for local and       |
| Desktop\``                        | |acquia-product:ac| websites      |
|    ``Drush\Aliases\[sitename].ali | (downloaded from                  |
| ases.drushrc.php``                | |acquia-product:ac|). These       |
|                                   | aliases include the host,         |
|                                   | docroot, user, site, and          |
|                                   | environment of the                |
|                                   | |acquia-product:ac| website.      |
+-----------------------------------+-----------------------------------+
| ``C:\Users\[username]\.acquia\Dev | Drush aliases for all remote      |
| Desktop\``                        | |acquia-product:ac|-hosted        |
|    ``Drush\Aliases\``             | websites known to                 |
|    ``cl.[sitename].aliases.drushr | |acquia-product:add|. These       |
| c.php``                           | aliases include the host,         |
|                                   | docroot, user, site, and          |
|                                   | environment of the website.       |
+-----------------------------------+-----------------------------------+
| ``C:\Documents and settings\[user | Basic configuration settings for  |
| name]\.acquia\DevDesktop\``       | each environment in               |
|    ``DrupalSettings\loc_[sitename | |acquia-product:add|.             |
| ]_dd.inc``                        |                                   |
+-----------------------------------+-----------------------------------+

Any passwords or user names in these files are encrypted to protect your
security.

If you chose something other than the default locations for the
|acquia-product:add| stack location and sites directory when you
installed |acquia-product:add|, these paths will vary, based on the
locations you chose.
