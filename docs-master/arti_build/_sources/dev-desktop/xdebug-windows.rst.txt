.. include:: /common/global.rst

Using Xdebug on |acquia-product:add| for Windows
================================================

`Xdebug <http://xdebug.org/>`__ is a tool for debugging PHP. With it,
you can do stack or function traces, memory allocation analysis, and
script execution. |acquia-product:add| for Windows comes with
``xdebug.dll`` as a part of its default installation.

Note for PHP 7 users

PHP 7 does not include the required ``xdebug.dll`` file. Download the
correct version for your server
`here <https://xdebug.org/download.php>`__.

To use Xdebug with |acquia-product:add|, complete the following steps:

#. Open the |acquia-product:add| Control Panel, and then click **Stop**
   in the lower right corner of the application. If the stack is already
   stopped, a **Start** button will instead be displayed — do *not*
   click the button to start the stack.
#. From the file menu, select **Acquia Dev Desktop > Preferences**, and
   then click the **Config** tab.
#. In the **Default PHP version** list, click your desired version of
   PHP.
   If you change the version, |acquia-product:add| will briefly display
   a dialog box stating **Applying changes**.
#. In the **Stack configuration files** section, find the **PHP** field
   (which contains a list of ``php.ini`` files). Click the file for your
   selected version of PHP, and then click the **Edit** link to the
   right.
   |acquia-product:add| opens a text editor to edit the file.
#. In the text editor, remove any existing lines in the
   ``[xdebug]``\ section. If this section does not exist, search for the
   ``zend_extension``, which will be the correct place to add the
   information in the following steps.
#. Add code similar to the following to the ``[xdebug]`` section of your
   file:

   ``[xdebug] zend_extension="" xdebug.remote_autostart=off ; Do not run Xdebug on every page request xdebug.remote_enable=1 xdebug.remote_handler=dbgp xdebug.remote_mode=req xdebug.remote_host=localhost xdebug.remote_port=9000``

   where ```` is the location and name of the most recent ``xdebug.dll``
   file to use. For example, the following example could be useful for
   PHP 5.2.17 running on a 64-bit Windows 7, installed
   |acquia-product:add| in the ``C:\Program Files (x86)`` directory:

   ``zend_extension="C:\Program Files (x86)\acquia-drupal\php5_2\ext\php_xdebug-2.2.1-5.2-vc9.dll"``

#. Save the updated ``.ini`` file.
#. Click **OK**.

   Note

   You may receive a pop up window that says **Name is empty**. Go to
   the **Acquia Dev Desktop > Preferences > General** tab and enter
   values into the **Your name:** and **Email:** fields.

.. _confirm:

Confirming that Xdebug is working
---------------------------------

To confirm that Xdebug is loaded and working, complete the following
steps:

#. On the main |acquia-product:add| Control Panel page, click ``Start``
   to start the stack.
#. Click **Settings**, and then click to the **Config** tab. Under the
   **Stack configuration files**, find the **PHP Info**, and then click
   the link for the PHP version that you're using and for which you
   edited the ``php.ini`` file.
#. A web browser opens with the output from ``PHPinfo()``. Search for
   the word **Xdebug**, and if you see something like this, Xdebug is
   enabled:

   ``This program makes use of the Zend Scripting Language Engine: Zend Engine v2.2.0, Copyright (c) 1998-2010 Zend Technologies with Xdebug v2.2.1, Copyright (c) 2002-2012, by Derick Rethans``

   If the preceding output does not appear, you might need to the
   ``php.ini`` file again.

.. _next:

Next steps
----------

After you have completed the procedures on this page, you will need to
configure your IDE to communicate with Xdebug. For information about how
to do this, refer to your IDE's help files or online resources.
