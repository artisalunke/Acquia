.. include:: /common/global.rst

Acquia Dev Desktop troubleshooting guide
==========================================

Here are some tips for troubleshooting issues you might run into while using |acquia-product:add|. In addition to the tips on this page, be sure to review the following documentation pages:

-  `Getting support </dev-desktop/getting-support>`__
-  `Known issues </dev-desktop/known-issues>`__
-  `Reporting issues, feature requests, and bugs </dev-desktop/reporting>`__

.. _logs:

Examining log files
-------------------

|acquia-product:add| creates two log files in its top-level folder:

-  ``installer.log`` – Records everything done during the most recent installation. This log is useful for diagnosing issues during the |acquia-product:add| install process
-  ``piscript.log`` – Records actions performed with |acquia-product:add|. This log is useful for diagnosing runtime issues.

Both of these logs are packaged and sent to Acquia when you use the **Help > Report an issue** feature.

.. _verbose:

Enabling verbose debug logging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can enable verbose logging and progress monitoring text, which can be useful for debugging issues. Open **Acquia Dev Desktop > Preferences > General**, and select **Verbose logging**. If, before you report an issue to Acquia, you enable verbose logging and then reproduce the issue you encountered, the logs you send will have more information, which makes it easier to diagnose the issue. You can then disable verbose logging to reduce disk space usage and improve |acquia-product:add| performance.

.. _settings-php:

Collisions in settings.php
--------------------------

When you create a local website or sync a website from |acquia-product:ac|, |acquia-product:add| modifies the website's ``settings.php`` file. It adds a block enclosed in comments labeled ``DDSETTINGS`` at the end of the ``settings.php`` file. Some Drupal modules may possibly modify the ``settings.php`` file in a way that conflicts with the |acquia-product:add| settings. If you run into errors, read the documentation for the Drupal module to see if it has special requirements for ``settings.php``, and consider whether the module settings can be moved after the ``DDSETTINGS`` block in the ``settings.php`` file.

.. _sync:

Problems syncing sites with Acquia Cloud
-----------------------------------------------

Permissions
~~~~~~~~~~~

You won't be able to sync websites with |acquia-product:ac| unless your |acquia-product:ac| user profile has the correct permissions. For more information, see `Acquia Cloud credentials and permissions </dev-desktop/cloud/key>`__.

Drush
~~~~~

If Drush isn't working on your |acquia-product:ac| website, you won't be able to sync the website using |acquia-product:add|. To test Drush on your |acquia-product:ac| website:

#. Connect to your |acquia-product:ac| website with SSH.
#. Run a Drush command, such as ``drush status``.

If that doesn't work, either `contact Acquia Support </support#contact>`__ (if you are an Acquia subscriber with support), or use the Feedback button in the |acquia-product:ac| UI to report your issue.

SSH key error
~~~~~~~~~~~~~

If, when you synchronize a website between |acquia-product:add| and |acquia-product:ac|, you experience an SSH key error, you may be able to resolve it by doing the following:

#. In |acquia-product:add|, click **Acquia Dev Desktop > Preferences**.
#. On the **Settings > General** tab, click **Remove local websites cloned from Acquia Cloud**, and then click **OK**.
#. Click the **+** button and select **Add Acquia Cloud websites**.

Workaround: Use the Acquia Cloud import procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're unable to sync your local website to |acquia-product:ac|, as a workaround you can try to use the import procedure described in `Acquia Cloud: Importing manually </acquia-cloud/create/import/manual>`__ and `Importing your codebase using Git </acquia-cloud/create/import/manual-code>`__.

.. _install-prob:

Problems with installation
--------------------------

If you have problems installing |acquia-product:add|, see `Reporting issues, feature requests, and bugs: Problems with installation </dev-desktop/reporting#install>`__.

.. _timeout:

Timeout during stack start
--------------------------

You could get a timeout error (for example, "Process 'MySQL database server' failed to start") while starting |acquia-product:add| if you have unusually large or many databases. If this happens, you can try increasing the ``startTimeout`` setting in the |acquia-product:add| ``dynamic.xml`` configuration file. When you modify the ``startTimeout`` setting, make sure that |acquia-product:add| is not running; otherwise, edits to ``dynamic.xml`` will not persist. The ``dynamic.xml`` configuration file is located:

-  On macOS, in ``/Applications/DevDesktop/common/cfgbox/Acquia Dev Desktop.app/Contents/MacOS/dynamic.xml``
-  On Windows, in ``C:\Program Files (x86)\Dev Desktop\common\cfgbox\AcquiaDevDesktop\dynamic.xml``

The default value of the ``startTimeout`` setting is 30 seconds. You may want to increase this to 240 or 300 (4 or 5 minutes).

.. _issues:

Reporting issues
----------------

If after checking out these troubleshooting tips, you still have problems, see `Reporting issues, feature requests, and bugs </dev-desktop/reporting>`__.
