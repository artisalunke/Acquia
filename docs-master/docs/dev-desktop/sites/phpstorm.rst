.. include:: /common/global.rst

Using PhpStorm with |acquia-product:add|
========================================

`PhpStorm <https://www.jetbrains.com/phpstorm/>`__ from JetBrains is an
IDE for PHP and Drupal that can be immensely useful in developing,
testing, and debugging a Drupal website. It includes both a rich code
editor and a visual debugger supporting Xdebug. This topic describes how
to set up PhpStorm to support developing your Drupal website with
|acquia-product:add|. For a summary of some of the benefits of using
PhpStorm, see `Using PhpStorm with
Drupal <%5Bacquia-product:kb%5Darticles/phpstorm-support-drupal>`__.

Before you begin, you should have installed |acquia-product:add| and
have a Drupal website running locally in |acquia-product:add|.

Configuring |acquia-product:add| with Xdebug
--------------------------------------------

The Xdebug PHP extension is included in |acquia-product:add|, but it is
not enabled by default. To use the Xdebug debugger in PhpStorm with
|acquia-product:add|, you will need to edit the ``php.ini`` file in
|acquia-product:add| to enable and configure Xdebug. To do this,
complete the following steps:

#. Open the **Acquia Dev Desktop > Preferences** menu.
#. In the **Config** tab, under **Stack configuration files**, find the
   ``php.ini`` path for the version of PHP that you are using, and then
   click the **Edit** link next to it.

   |Edit your php.ini file|

#. Your ``php.ini`` file will open in a text editor. Search for a line
   that contains ``xdebug.so`` and uncomment it by removing the ``;``
   (semicolon) at the beginning of the line. For example:

   ``zend_extension="/Applications/DevDesktop/php5_5/ext/xdebug.so"``

   For the following PHP versions in *|acquia-product:add| for Windows*,
   enter the following filenames in place of ``xdebug.so``:

   -  PHP 5.3 - ``php_xdebug-2.2.4-5.3-vc9.dll``
   -  PHP 5.4 - ``php_xdebug-2.3.2-5.4-vc9.dll``
   -  PHP 5.5 - ``php_xdebug-2.3.2-5.5-vc11.dll``
   -  PHP 5.6 - ``php_xdebug-2.3.2-5.6-vc11.dll``

      Note

      The PHP 7 version currently included with |acquia-product:add|
      does not currently include Xdebug. You can download an updated
      version of Xdebug `here <https://xdebug.org/download.php>`__.

#. Add the following line to your ``php.ini`` file:

   ``xdebug.remote_enable=1``

   Note

   Although you can add this line anywhere in the file, it is a good
   practice to add any custom configurations to the end of the file.

#. Stop and restart Apache in |acquia-product:add| to ensure that the
   configuration change takes effect.

You can confirm that Xdebug is enabled by visiting the Drupal
``phpinfo()`` page (``/admin/reports/status/php``) and verifying that
the Xdebug extension appears in the list of extensions.

.. _phpstorm:

Installing and configuring PhpStorm
-----------------------------------

#. `Download PhpStorm <http://www.jetbrains.com/phpstorm/download/>`__
   from JetBrains and install it. JetBrains offers a free 30-day trial.
   See the `PhpStorm
   documentation <http://www.jetbrains.com/phpstorm/quickstart/>`__ for
   more information.
#. On the `PhpStorm bookmarklets generator
   page <http://www.jetbrains.com/phpstorm/marklets/>`__, generate
   Xdebug bookmarklets ("start debugger," "stop debugger," and "debug
   this page"), and add them to your browser.

Next, do the following:

-  `Configure PhpStorm to use Xdebug <#enable-xdebug>`__.
-  `Add your |acquia-product:add| website as a project <#project>`__ in
   PhpStorm.
-  `Configure remote debug <#remote-debug>`__.

.. _enable-xdebug:

Configure PhpStorm to use Xdebug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. In PhpStorm, go to the **PhpStorm > Preferences** menu.
#. Under **Project Settings**, expand PHP.
#. Click **Debug**. In the **Xdebug** section, select **Can accept
   external connections**. Confirm that the **Debug port** is set to the
   default value of port 9000.
#. Click **OK** to save your changes.
#. Go to **View** and click **Toolbar**, which has an icon for turning
   listening on and off:

   |The listen icon in the PhpStorm toolbar|

.. _project:

Add your |acquia-product:add| website as a project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use PhpStorm with an |acquia-product:add| website, you need to add
the website's code as a project.

#. In the **File** menu, click **Open**.
#. Select the website's local code directory, and click **Choose**.

.. _remote-debug:

Configure remote debug
~~~~~~~~~~~~~~~~~~~~~~

You need to configure a new remote debug server for each Drupal website
project that you open in PhpStorm. To configure it:

#. In the **Run** menu, select **Edit Configurations**.
#. In the **Run/Debug Configurations** window, click the plus sign **+**
   to add a new configuration, and then select **PHP Remote Debug**.

   |Remote debug configuration|

#. In the **Name** field, provide a meaningful name.
#. Click the box next to the **Server** list to add a new server.

   |Configure a debug server|

#. Provide a meaningful name for the server.
#. Add the hostname and port that your local website uses under
   |acquia-product:add|.
#. Ensure that the Debugger selector is set to **Xdebug**.
#. Click **OK** to save your server configuration.
#. Confirm that your new server is selected in the **Server** list, and
   then click **OK** to save.

.. _xdebug:

Using Xdebug in PhpStorm
------------------------

You can use Xdebug with PhpStorm to debug your |acquia-product:add|
Drupal website. You first set breakpoints in your code, and then run
your code and see the results in PhpStorm.

Set breakpoints
~~~~~~~~~~~~~~~

To set breakpoints in your code, complete the following steps:

#. Load your |acquia-product:add| Drupal website in the browser where
   you created the PhpStorm `debugger bookmarklets <#bookmarklets>`__.
#. Click the **Start Debugger** bookmarklet.
#. In the PhpStorm toolbar, click the Listen icon |PhpStorm listen
   icon|. The icon will change to |PhpStorm listening icon| to indicate
   that PhpStorm is now listening for connections.
#. In PhpStorm, open your project and go to the file that contains the
   code where you want to set a breakpoint.
#. Click in the column to the left of the code to set a breakpoint (or
   enter Command-F8).

   |Setting a breakpoint|

PhpStorm indicates the presence of a breakpoint with an icon in the left
margin and highlighting on the code line.

|Breakpoint is set|

Run your code and see the results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once debugging is turned on, and PhpStorm is set up to listen, perform
an action on the website. When the breakpoint is hit, PHP execution will
stop, and a Debug window will appear:

|Using Xdebug|

As you run your code with the debugger, these buttons in the Debugger
tab can be useful for you:

-  |Step over button|  *Step Over* - Step to the next line in the
   current file. See `Stepping Through the
   Program <http://www.jetbrains.com/phpstorm/webhelp/stepping-through-the-program.html>`__.
-  |Step into button|  *Step Into* - Step to the next executed line. See
   `Stepping Through the
   Program <http://www.jetbrains.com/phpstorm/webhelp/stepping-through-the-program.html>`__.
-  |Force Step Into button|  *Force Step Into* - Select the method to
   step in, if the current line contains multiple method call
   expressions. See `Choosing a Method to Step
   Into <http://www.jetbrains.com/phpstorm/webhelp/choosing-a-method-to-step-into.html>`__.
-  |Step Out button|  *Step Out* - Step to a first executed line after
   returning from the current method. See `Stepping Through the
   Program <http://www.jetbrains.com/phpstorm/webhelp/stepping-through-the-program.html>`__.

Related topics
--------------

-  `Using PhpStorm with
   Drupal <%5Bacquia-product:kb%5Darticles/phpstorm-support-drupal>`__
-  `JetBrains PhpStorm
   help <https://www.jetbrains.com/phpstorm/webhelp/phpstorm.html>`__

.. |Edit your php.ini file| image:: https://cdn2.webdamdb.com/1280_cS8IbvYuZWo6.png?1526475653
   :width: 590px
   :height: 419px
.. |The listen icon in the PhpStorm toolbar| image:: https://cdn3.webdamdb.com/1280_ovJ8MGWjroq9.png?1526475446
   :width: 372px
   :height: 54px
.. |Remote debug configuration| image:: https://cdn2.webdamdb.com/1280_EVVqEhwYndt9.png?1526475780
   :width: 222px
   :height: 293px
.. |Configure a debug server| image:: https://cdn3.webdamdb.com/1280_UqSjWxGv2W47.png?1526475558
   :width: 590px
   :height: 133px
.. |PhpStorm listen icon| image:: https://cdn4.webdamdb.com/1280_2Bn6ygPFnZm0.png?1526476101
   :width: 23px
   :height: 21px
.. |PhpStorm listening icon| image:: https://cdn3.webdamdb.com/1280_wlB85KIdRf70.png?1526475673
   :width: 23px
   :height: 22px
.. |Setting a breakpoint| image:: https://cdn4.webdamdb.com/1280_keMkk5HOXge6.png?1526475661
   :width: 253px
   :height: 150px
.. |Breakpoint is set| image:: https://cdn3.webdamdb.com/1280_Q4Pk4LGmlYM3.png?1526475899
   :width: 477px
   :height: 140px
.. |Using Xdebug| image:: https://cdn2.webdamdb.com/1280_UiaS2y0bcrD0.png?1526475439
   :width: 590px
   :height: 186px
.. |Step over button| image:: https://cdn2.webdamdb.com/1280_ABOV6Zk0EJi7.png?1526475679
   :width: 19px
   :height: 18px
.. |Step into button| image:: https://cdn4.webdamdb.com/1280_skiAVRD3331.png?1526476085
   :width: 20px
   :height: 18px
.. |Force Step Into button| image:: https://cdn3.webdamdb.com/1280_svS7m6cZ0S09.png?1526476085
   :width: 21px
   :height: 20px
.. |Step Out button| image:: https://cdn2.webdamdb.com/1280_sPesStez0GP4.png?1526475589
   :width: 20px
   :height: 19px
