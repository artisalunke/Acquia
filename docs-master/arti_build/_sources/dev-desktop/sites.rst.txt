.. include:: /common/global.rst

Working with your sites
=======================

.. toctree::
   :hidden:
   :glob:

   /dev-desktop/sites/*

|acquia-product:add| displays all of your websites in the left panel. The following icons distinguish the location of your websites:

.. list-table::
 :widths: 10 90
 :header-rows: 1

 * - Icon
   - Description
 * - |Acquia Cloud site icon|
   - Exists both locally and on |acquia-product:ac|
 * - |Local site icon|
   - Exists only locally in |acquia-product:add|

Viewing local websites
----------------------

|Local website|

When you select a local website in the left panel, the right panel
displays:

-  **Local site** |--| Click the link to view the website in your browser. Select the **Use https** check box to test your website using SSL. For more information, see `Using HTTPS (SSL) with sites <#https>`__.
-  **Local code** |--| Click the link to view your local website's codebase in your local file system, or use this URL in a `Git client <#git-client>`__. Click the terminal icon |Terminal icon| to open a command line, set your Drush path, and go to your website's docroot folder. You can also open the command line by clicking **More > Open Console**.
-  **Local database** |--| Click the link to inspect and manage your website's database in your browser, using `phpMyAdmin <http://docs.phpmyadmin.net/en/latest/>`__. See `Working with your local database <#db>`__.
-  **PHP version** |--| A drop-down list to select the PHP version used for your local website. You can select the PHP version for a website only if your PHP mode is set to the default, Fast CGI (``mod_fcgid``), and not to Apache module (``mod_php``). For more information, see `Configuring Acquia Dev Desktop </dev-desktop/config#config>`__.
-  **Host this site on Acquia Cloud** |--| Click the button to import the website into |acquia-product:ac|. For more information, see `Hosting a site on Acquia Cloud </dev-desktop/cloud>`__.

Working with your local database
--------------------------------

You can work with the database in your local website, using phpMyAdmin (which is included in |acquia-product:add|), the command line, or other database administration tools.

Using phpMyAdmin
~~~~~~~~~~~~~~~~

To access the database with phpMyAdmin, click the **Local database** link to inspect and manage your website's database in your browser, using phpMyAdmin. phpMyAdmin is a full-featured database management tool with which you can examine your database structure, run SQL queries, perform import and export operations, and more. See the `phpMyAdmin <http://docs.phpmyadmin.net/en/latest/>`__ documentation for more information.

Using the command line
~~~~~~~~~~~~~~~~~~~~~~

You can access the database from the command line and use the ``mysql`` command line tool. Click the console icon at the end of the **Local code** line (or click **More > Open Console**). In the console, enter ``mysql``. This gives you access to the ``mysql`` tool, which enables you to execute SQL commands against your database. See the `mysql documentation <http://dev.mysql.com/doc/refman/5.5/en/mysql.html>`__ for more information.

Viewing Acquia Cloud websites
-----------------------------

|Acquia Cloud website|

When you select an |acquia-product:ac| website in the left panel, the right panel displays information about the website. Click the arrow in the left panel to view information about the website's other environments (Dev, Stage, or Prod).

-  **Acquia Cloud workflow** |--| Opens the **Cloud > Workflow** page in the |acquia-product:ac| user interface, so you can drag and drop your website's code between Dev, Stage, and Prod environments, switch deployed code branches or tags, and manage other aspects of your |acquia-product:ac| website.
-  **Cloud site** |--| Click the link to view the website in your browser, served by the |acquia-product:ac| server.
-  **Git** |--| The location of your website's code base in your |acquia-product:ac| version control system. Click the clipboard icon to copy this URL. You can then use it at the command line or in a `client <#git-client>`__ to make changes to your code repository. For more information, see `Managing your code </acquia-cloud/develop/code>`__ and `Sending updates to your code repository </acquia-cloud/develop/update>`__.
-  **Code** |--| The name of the branch or tag that is currently deployed on |acquia-product:ac|. To change the version of code deployed in an environment, click the **Acquia Cloud workflow** button. On the **Cloud > Workflow** page, select the code version you want, using the code selector in the environment's Code block. `Learn more </acquia-cloud/develop/code#deploy>`__.
-  **SSH** |--| The URL of your website's |acquia-product:ac| server.

   -  Click the clipboard icon |Clipboard icon| to copy this URL. You can then use it at the command line to connect to the server.
   -  Click the terminal icon |Terminal icon| to connect to the server.

   For more information, see `Managing your code </acquia-cloud/develop/code>`__ and `Sending updates to your code repository </acquia-cloud/develop/update>`__.

-  **Clone the site locally and use it in Dev Desktop** - Click this button to create a local clone of the |acquia-product:ac| website in your |acquia-product:add| local ``sites`` folder. For more information, see `Working with sites on Acquia Cloud </dev-desktop/cloud/working>`__.

For more information, see `Working with sites on Acquia Cloud </dev-desktop/cloud/working>`__.

.. _git-client:

Using a Git client to work with your code repository
----------------------------------------------------

You can use a local Git client with a GUI to work with your code repository. Some examples are:

-  `SourceTree <https://www.atlassian.com/software/sourcetree/overview>`__
-  `Tower <http://www.git-tower.com/>`__
-  `TortoiseGit <https://tortoisegit.org/>`__
-  `SmartGit <http://www.syntevo.com/smartgit/>`__

You can configure your Git client by pointing it to the location of your local code repository (listed on the **Local code** line in |acquia-product:add|) or |acquia-product:ac| code repository (listed on the **Git** line in |acquia-product:add|).

.. _https:

Using HTTPS (SSL) with local sites
----------------------------------

The **Local site** URL link for local websites provides a **Use https** check box. When you select the **Use https** check box, |acquia-product:add| serves your site using the HTTPS protocol and uses a self-signed SSL certificate to simulate secure traffic. This enables you to develop and test secure websites locally without requiring you to duplicate the SSL certificates you use on your production site.

.. note::

   By default, |acquia-product:add| uses port 8443 for HTTPS traffic rather than the standard port 443, so redirects from HTTP to HTTPS that assume port 443 won't work. You can set |acquia-product:add| to use port 443 in **Acquia Dev Desktop > Preferences > Ports**.

.. _startstop:

Apache and MySQL status indicators
----------------------------------

The Apache and MySQL status indicators at the bottom of the dialog indicate when the Apache server and MySQL server are running (green) or stopped (gray). Click the **Start/Stop** button to start or stop them.

|Status indicators|

.. |Acquia Cloud site icon| image:: https://cdn3.webdamdb.com/1280_AfgIMbKoT4M1.png?-62169955200
   :class: no-sb
   :width: 31px
   :height: 30px
.. |Local site icon| image:: https://cdn2.webdamdb.com/1280_AfwYwIDvMaU6.png?-62169955200
   :class: no-sb
   :width: 33px
   :height: 30px
.. |Local website| image:: https://cdn2.webdamdb.com/1280_w1r2Cw1C4k81.png?-62169955200
   :width: 590px
   :height: 243px
.. |Terminal icon| image:: https://cdn3.webdamdb.com/1280_Qy3QehZDzfA9.png?-62169955200
   :class: no-sb
   :width: 20px
   :height: 16px
.. |Acquia Cloud website| image:: https://cdn4.webdamdb.com/1280_UUMET0qpBet3.png?-62169955200
   :width: 590px
   :height: 255px
.. |Clipboard icon| image:: https://cdn3.webdamdb.com/1280_oUqtbTocXBM8.png?-62169955200
   :width: 22px
   :height: 16px
.. |Status indicators| image:: https://cdn3.webdamdb.com/1280_I9HwQ1NzYy02.png?-62169955200
   :width: 590px
   :height: 300px
