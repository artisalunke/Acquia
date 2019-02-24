.. include:: /common/global.rst

Hooks in |acquia-product:edg|
=============================

.. toctree::
   :hidden:
   :glob:

   /site-factory/extend/hooks/*

.. container:: message-status
    
   **ADVANCED** - Invalid or poorly-tested hook scripts can cause data loss or downtime.

As you develop your |acquia-product:edg| websites, you may have code
that needs to execute during runtime, such as using Drupal core's fast
404 capabilities when your website begins to load. It can also be
beneficial to execute code after certain events, such as deploying a
theme or installing a new website. These actions can all be achieved by
triggering code execution through |acquia-product:edg| hooks.

.. admonition::  Using |acquia-product:ac| hooks

   |acquia-product:edg| hooks differ from 
   `Acquia Cloud hooks </acquia-cloud/api/cloud-hooks>`__. Because 
   |acquia-product:ac| hooks are not designed for use with multisites, even 
   though |acquia-product:ac| hooks exist in |acquia-product:edg|, their use 
   in |acquia-product:edg| is unsupported.

   *Only the hooks described on this documentation page are supported for 
   use with |acquia-product:edg|.*


Available |acquia-product:edg| hooks
------------------------------------

|acquia-product:edg| uses hooks of the following types to help you
complete actions with your websites.


Hooks triggered after website actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following hooks are typically script files that contain Drush
commands, and can be any kind of executable script (including Bash or
Ruby). For instructions on where to place these files, see the
`Executing your commands with a hook <#using>`__ section on this page.

-  ``db-update`` - This hook enables you to execute scripts before and
   after the ``drush updatedb`` command. For more information, see
   `Database update hooks </site-factory/extend/hooks/dbupdate>`__.
-  ``post-install`` - This hook enables you to execute PHP after a new
   website is created in your subscription. Unlike most API-based hooks,
   this hook does not take arguments, but instead executes the PHP code
   it is provided.
-  ``post-staging-update`` - This hook enables you to execute scripts
   after `staging a factory down to a non-production
   environment </site-factory/workflow/staging>`__. For more
   information, see |post-staging-hook|_
-  ``post-theme-deploy`` - This hook enables you to execute code when
   you refresh a theme from an external repository. For more
   information, see 
   `Adding external themes to your site </site-factory/theme/external#refresh>`__.


.. |post-staging-hook| replace:: ``post-staging-update`` hook in \ |acquia-product:edg|\ 
.. _post-staging-hook: /site-factory/extend/hooks/post-staging-update

At this time, no |acquia-product:edg| hooks exist for website
duplication, website staging, or website backups.


Hooks executed on every page load
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you were running your own Drupal website, you would simply modify
your website's ``sites.php`` or ``settings.php`` files. However, because
these files cannot be modified in |acquia-product:edg|, we have created
hooks at the beginning and end of these files to check specified
directories for custom code in files to execute during the website's
bootstrap process:

-  ``sites.php``

   -  ``pre-sites-php`` - At the beginning of the file, before executing
      any instructions in ``sites.php``
   -  ``post-sites-php`` - At the end of the file

-  ``settings.php``

   -  ``pre-settings-php`` - At the beginning of the file, before
      executing any instructions in ``settings.php``
   -  ``post-settings-php`` - At the end of the file

For more information about ``pre-settings-php`` and
``post-settings-php`` hooks, including a script for 
`monitoring website performance with New Relic </acquia-cloud/monitor/apm/multisite#proc>`__, see 
`Altering values in settings.php with hooks </site-factory/extend/hooks/settings-php>`__.

.. important:: 

   -  Files executed by the ``settings.php`` and ``sites.php`` hooks must
      have a ``.php`` extension.
   -  Because commands executed by these hooks are run for every request
      for the web node, commands in the hook files should be lightweight
      (for example, setting variables) and should not read or write to
      either databases or files. Accessing databases or files using the
      hook file can greatly impair your website's performance. If you need
      to access databases or files, you should use modules instead.


Creating good hook scripts
--------------------------

It is extremely important to thoroughly test all hook scripts before
use, as a failed hook script will cause hosting tasks to fail for the
entire environment, not just the individual website the hook script was
executed against. Two important factors to keep in mind when creating
custom hook scripts:

-  **Hook scripts must take responsibility for their own errors** |br|
   Hook scripts must log failures internally and return a ``SUCCESS``
   (exit code 0) status, even if portions of the script fail, unless you
   want the failure of your hook script to trigger failures on all
   hosting tasks, such as website staging and code deployments.
-  **Hook scripts must be multisite-aware** |br|
   Any hook script executed on |acquia-product:edg| must take into
   account the implications of execution in a multisite environment.



Executing your commands with a hook
-----------------------------------

After you have created one or more files with the commands you want to
run, complete the following steps:

#. Ensure that you have created a directory called ``factory-hooks`` at
   the root of your code repository.

   .. note::  

      The ``factory-hooks`` directory and your
      `docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__ are
      separate directories at the same level in your code repository.

#. In the ``factory-hooks`` directory, ensure that you have created a
   directory for the |acquia-product:edg| hook that you want to use (for
   example, ``post-settings-php`` or ``post-install``).
#. | In the directory for the hook that you want to use, add one or more
     of the previously created files which contain the required
     commands.
   | For example, to execute a PHP file named ``action.php`` using the
     ``post-settings-php`` hook, using the following path and filename:

   .. code-block:: php
   
      factory-hooks/post-settings-php/action.php

#. For hooks triggered after website actions, ensure that any scripts
   you create have the executable bit set when you add them to your code
   repository. To set the executable bit for files already in your code
   repository, execute the commands similar to the following from a
   command prompt window (where ``my-hook.sh`` is the file for which you
   want to set the executable bit):

   .. code-block:: php
   
      chmod a+x ./my-hook.sh
      git add ./my-hook.sh
      git commit -m 'Add executable bit to my-hook.sh'
      git push


Directory structure example
---------------------------

**Code repository contents**

   .. code-block:: none

      + docroot
      + factory-hooks
        + db-update
        + pre-sites-php
        + post-sites-php
        + pre-settings-php
        + post-settings-php
          + action.php
        + post-staging-update
        + post-theme-deploy
        + post-install