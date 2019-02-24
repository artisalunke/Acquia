.. include:: /common/global.rst

Adding non-Drupal PHP extensions or libraries to your application
=================================================================

The |acquia-product:ac| platform includes a standard set of PHP extensions that are available on all servers. Your application might, however, require additional PHP extensions to support its own desired features. |acquia-product:ace| and |acquia-product:edg| customers can compile and deploy PHP extensions or libraries, and then Acquia can enable them on your |acquia-product:ac| environments.

The Apache servers for your |acquia-product:ac| environments serve everything in the ``/docroot`` directory and ignore files that are not in ``/docroot``. Your repository contains a ``/library`` subdirectory that you can use for PHP code libraries. (This is located in the ``/`` directory of Git repositories.) The ``/library`` subdirectory is part of your default PHP ``include_path`` and is outside of ``/docroot``, so it] will not be served by Apache.

If any PHP library does not work as expected, examine your environment's ``php-error.log``.

.. note::

   Acquia does not guarantee that any PHP extensions used in this manner will function as expected, and we will not assist with troubleshooting extensions that do not function as expected. Also note the limitations under `Unsupported software <#unsupported>`__.

.. _compile:

Compiling PHP libraries
-----------------------

You must compile the PHP extensions (``.so`` files) and libraries that you require and commit them to your code repository. Here is an article that may help you:

-  `How to install PHP Extensions from Source <http://www.sitepoint.com/install-php-extensions-source/>`__

The compiled shared extension (the ``.so`` file) must itself contain any libraries on which it depends. This is called static linking. The goal is that when you run ``ldd`` on the ``.so`` file in the |acquia-product:ac| environment, all of the dependencies are met without manipulating the ``LD_LIBRARY_PATH``. Acquia does not provide support for this process. Here are two articles that may help guide you in understanding the (frequently complex) issues involved:

-  `LD_LIBRARY_PATH Is Not The Answer <http://prefetch.net/articles/linkers.badldlibrary.html>`__
-  `Proper way to link a static library using GCC <http://stackoverflow.com/questions/9952146/proper-way-to-link-a-static-library-using-gcc>`__

You must compile them for the same operating system version that your |acquia-product:ac| environments are running. To determine the operating system version, `connect to your environments with SSH </acquia-cloud/ssh>`__ and run this command:

.. code-block:: none

    lsb_release -c

.. _depend:

Check for dependencies
~~~~~~~~~~~~~~~~~~~~~~

The compiled PHP extension must contain any dependent libraries not already found on your server. To test this, navigate to the PHP extension's folder in your ``/library`` directory on your environment and run ``ldd extension.so``, being sure to replace ``extension.so`` with the name of the actual ``.so`` file you have compiled. When you run ``ldd`` on the ``.so`` file in the Acquia environment, all of the dependencies must be met without manipulating the ``LD_LIBRARY_PATH``.

The following is an example of a compiled extension that does not have the required libraries on the environment or statically linked to the compiled extension:

.. code-block:: none

    sitename@server-1234:/var/www/html/sitename.dev/library$ ldd ssh2.so
    linux-vdso.so.1 =>  (0x00007fff071ff000)
    libssh2.so.1 => not found
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f2ea56b5000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f2ea5c92000)

In this example, one of the requirements was not found.

Deploying PHP extensions
------------------------

You must deploy the version of code that contains this change to whichever environments you need the code to be enabled on. For example, if you commit your code to the ``master`` branch, the extension can be enabled only on environments running ``master`` or a branch or tag pulled from ``master`` after the change was submitted. Otherwise, the files will be missing.

For example, to use a custom PHP library called ``my.php`` with your application, commit it to the ``/library`` directory in your Git repository, and then use the following statement in your Drupal code, in the file where you make a call to the custom library:

.. code-block:: php

    include_once "my.php";

Enabling PHP extensions
-----------------------

Once you have compiled and deployed your PHP extension, you need to get it enabled on your |acquia-product:ac| environments. To do so, file a ticket with Acquia Support. The ticket must specify the location of the compiled extensions, as well as a very brief summary of their intended purpose. Once Acquia has reviewed and approved the request, we will modify the ``php.ini`` files in your environments to point to each compiled extension in your code repository. This typically takes one or two business days.

.. _imap:

Enabling PHP IMAP or xdebug
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PHP ``IMAP`` and ``xdebug`` extensions are present, but disabled by default on |acquia-product:ac|. If you want to use either PHP ``IMAP`` or ``xdebug``, you do not need to compile and deploy it. You need only to file an Acquia Support ticket and request that it be enabled.

Unsupported software
--------------------

|acquia-product:ac| does not support the following software:

-  Moodle (not compatible with high availability)
-  piwik (Acquia has repeatedly seen this cause performance issues)
-  Any non-Drupal CMS
-  CA Single Sign-on (formerly CA SiteMInder)

You cannot install the following software on |acquia-product:ac|:

-  Custom daemons or services, such as Jabber or Microsoft Exchange
-  Custom package installations that require ``apt-get``; you can still install custom executables using your code repository
