.. include:: /common/global.rst

Configuring Acquia Dev Desktop
==============================

You can configure |acquia-product:add| using the Settings screen.

To open the Settings screen, select **Acquia Dev Desktop > Preferences**.

|Preferences in the menu|

The Settings screen has five tabs:

-  `General <#general>`__
-  `Ports <#ports>`__
-  `Config <#config>`__
-  `Logs <#logs>`__
-  `Proxy <#proxy>`__

.. _general:

General tab
-----------

On the General tab, you can:

-  Configure how |acquia-product:add| behaves when you start and stop the application.
-  Enable verbose mode for logging and progress monitoring text, which can be useful for debugging.
-  |acquia-product:add| optionally tracks diagnostic and usage data. Uncheck this setting to opt out of sending Acquia data. For more information, see `Reporting diagnostic and usage information </dev-desktop/sending>`__.
-  Remove local sites cloned from |acquia-product:ac|. This deletes all local websites associated with your |acquia-product:ac| account, including the local copies of all code, databases, and files. It does not remove any local websites that are not associated with |acquia-product:ac|, nor does it affect the websites hosted on |acquia-product:ac|. |br| 
   It also removes your |acquia-product:ac| credentials from |acquia-product:add|, so you can click Add |acquia-product:ac| sites and enter credentials for a different |acquia-product:ac| account.
-  Register or generate an SSH key, which is required in order to sync local websites with |acquia-product:ac|. For more information, see `Generating an SSH key </dev-desktop/keygen>`__.

|Settings - General|

.. _ports:

Ports tab
---------

On the Ports tab, you can change the ports used by the |acquia-product:add| Apache server and MySQL server. You can also change the port used for SSH.

|Settings - Configuring ports|

.. _config:

Config tab
----------

On the Config tab, you can:

-  Select the default PHP version for sites you create with |acquia-product:add|.

   .. note::

      Many PHP extensions that are included with PHP 5 versions are not included with PHP 7 because they are not yet available.

-  Select the PHP mode used by PHP on |acquia-product:add|, either Apache module (mod_php) or Fast CGI (mod_fcgid). Generally, you should leave this set to the default, mod_fcgid. If you set the PHP mode to Apache module (mod_php), you can't change the PHP version on a per-site basis, as described in `Working with your sites </dev-desktop/sites>`__.
-  View and edit the configuration files for the Apache server (``apache/conf/httpd.conf``), MySQL server (``mysql/my.conf``), and PHP (``php.ini``).

|Config tab|

.. _logs:

Logs tab
--------

On the Logs tab you can view the Drupal logs for each of your local sites. You can also see the Apache server access and errors logs, and the MySQL error and slow query logs for |acquia-product:add|.

.. _proxy:

Proxy tab
---------

If your local machine is behind a proxy, you can connect from |acquia-product:add| to |acquia-product:ac| by configuring the Proxy tab.

|Settings - Proxy|

#. Select **Enable proxy**.
#. Enter the host name and port number of your proxy.
#. Enter the username and password you use to access your proxy.
#. Click **OK**.

.. |Preferences in the menu| image:: https://cdn4.webdamdb.com/1280_2jOjvdfybC35.png?-62169955200
   :width: 245px
   :height: 210px
.. |Settings - General| image:: https://cdn3.webdamdb.com/1280_E3OT0HU5r02.png?-62169955200
   :width: 590px
   :height: 415px
.. |Settings - Configuring ports| image:: https://cdn2.webdamdb.com/1280_cLYF68MwDo81.png?-62169955200
   :width: 590px
   :height: 419px
.. |Config tab| image:: https://cdn2.webdamdb.com/1280_cUU6swqILUr3.png?-62169955200
   :width: 590px
   :height: 419px
.. |Settings - Proxy| image:: https://cdn2.webdamdb.com/1280_Yp0s39u3Yh22.png?-62169955200
   :width: 590px
   :height: 416px
