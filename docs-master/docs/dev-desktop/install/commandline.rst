.. include:: /common/global.rst

Installing Dev Desktop from the command line
============================================

The primary way to install |acquia-product:add| is to use the prompted installer, as described in `Installing Acquia Dev Desktop </dev-desktop/install>`__. As an alternative, you can install |acquia-product:add| from a command line on Windows or macOS. To use the command line installer, download |acquia-product:add| from the `Acquia Downloads page <https://dev.acquia.com/downloads>`__, and then follow the instructions for your operating system.

Installing from the command line on Windows
-------------------------------------------

#. Change directories to the directory where you saved the downloaded |acquia-product:add| installer:

   ``cd \Downloads``

#. Run the installer:

   ``AcquiaDevDesktop***.exe  --``

   For example:

   ``AcquiaDevDesktop***.exe --mode unattended --unattendedmodeui minimal``

Installing from the command line on macOS
-----------------------------------------

#. Mount the installation ``.dmg`` with a command like:

   ``hdiutil attach /path/to/acquia dev desktop.dmg``

#. Change directories to the Acquia Dev Desktop installer:

   ``cd /Volumes/"Acquia Dev Desktop Installer" cd "Acquia Dev Desktop Installer.app"/Contents/MacOS``

#. Run the installer:

   ``./installbuilder.sh  --``

   For example:

   ``./installbuilder.sh --mode unattended --unattendedmodeui minimal``

.. _arg:

Installer arguments
-------------------

The installer script takes the following arguments on either Windows or
macOS:

+-----------------------+-----------------------+-----------------------+
| Argument              | Description           | Allowed and default   |
|                       |                       | values                |
+=======================+=======================+=======================+
| ``--mode``            | Installation mode     | ``osx`` (default) —   |
|                       |                       | Use the macOS         |
|                       |                       | interface (macOS      |
|                       |                       | only)                 |
|                       |                       | ``text`` — Use text   |
|                       |                       | prompts on the        |
|                       |                       | command line          |
|                       |                       | ``unattended`` — Use  |
|                       |                       | mode specified with   |
|                       |                       | the                   |
|                       |                       | ``--unattendedmodeui` |
|                       |                       | `                     |
|                       |                       | argument, with input  |
|                       |                       | from a text file      |
|                       |                       | specified with the    |
|                       |                       | ``--optionfile``      |
|                       |                       | argument              |
+-----------------------+-----------------------+-----------------------+
| ``--unattendedmodeui` | UI to use in          | ``none`` (default)    |
| `                     | unattended            | ``minimal``           |
|                       | installation mode     | ``minimalWithDialogs` |
|                       |                       | `                     |
+-----------------------+-----------------------+-----------------------+
| ``--optionfile``      | The path to a text    |                       |
|                       | file that includes    |                       |
|                       | installation options  |                       |
+-----------------------+-----------------------+-----------------------+
| ``--admUsername``     | Username for the      |                       |
|                       | admin account         |                       |
+-----------------------+-----------------------+-----------------------+
| ``--admPass``         | Password for the      |                       |
|                       | admin account         |                       |
+-----------------------+-----------------------+-----------------------+
| ``--admEmail``        | Email address for the |                       |
|                       | admin account         |                       |
+-----------------------+-----------------------+-----------------------+
| ``--debuglevel``      | Debug information     | ``0 1 2`` (default)   |
|                       | level of verbosity    | ``3 4``               |
+-----------------------+-----------------------+-----------------------+
| ``--debugtrace``      | The path of a file    |                       |
|                       | that the installer    |                       |
|                       | should write debug    |                       |
|                       | information to        |                       |
+-----------------------+-----------------------+-----------------------+
| ``--installer-languag | Language to run       | ``en`` (default)      |
| e``                   | installer in          | ``ar bg ca da nl et f |
|                       |                       | r fi``                |
|                       |                       | ``de el es es_AR he h |
|                       |                       | r hu it ja ko pl``    |
|                       |                       | ``pt_BR pt ro ru no s |
|                       |                       | l sk sq sv tr``       |
|                       |                       | ``zh_TW zh_CN va cy c |
|                       |                       | s``                   |
+-----------------------+-----------------------+-----------------------+
| ``--licenseagree``    | Agreement to the      | 1 (default)           |
|                       | license               |                       |
+-----------------------+-----------------------+-----------------------+
| ``--installDir``      | The directory to      | ``/Applications/acqui |
|                       | install Dev Desktop   | a-dev-desktop``       |
|                       | in                    |                       |
+-----------------------+-----------------------+-----------------------+
| ``--siteDir``         | The site directory    | ``/Users//Sites/acqui |
|                       |                       | a-dev-desktop``.      |
|                       |                       | A tilde (~) within    |
|                       |                       | quotes is not         |
|                       |                       | expanded by the       |
|                       |                       | installer to its      |
|                       |                       | value. Therefore, if  |
|                       |                       | the path is           |
|                       |                       | ``~/sites/example``,  |
|                       |                       | use either            |
|                       |                       | -``-siteDir ~/sites/e |
|                       |                       | xample``              |
|                       |                       | or                    |
|                       |                       | ``--siteDir "$HOME/si |
|                       |                       | tes/example"``.       |
+-----------------------+-----------------------+-----------------------+
| ``--apachePort``      | Apache web server     | ``8082``              |
|                       | port number           |                       |
+-----------------------+-----------------------+-----------------------+
| ``--mysqlPort``       | MySQL database port   | ``33066``             |
|                       | number                |                       |
+-----------------------+-----------------------+-----------------------+
| ``--siteName``        | Site name             | ``My [acquia-product: |
|                       |                       | ld] website``         |
+-----------------------+-----------------------+-----------------------+
| ``--help``            | The list of valid     |                       |
|                       | arguments for the     |                       |
|                       | installer script      |                       |
+-----------------------+-----------------------+-----------------------+
| ``--version``         | Product information   |                       |
|                       | for                   |                       |
|                       | |acquia-product:add|  |                       |
+-----------------------+-----------------------+-----------------------+
