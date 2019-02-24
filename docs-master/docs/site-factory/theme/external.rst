.. include:: /common/global.rst

Adding external themes to your site
===================================

During normal Drupal development, when you're developing your website's
themes, best practices would have you store a theme's files in the
``sites/all/themes`` directory under your docroot. However, what if you
want a design firm to create and maintain your websites' theme files,
but you don't want to provide them with complete access to your
website's code?

|acquia-product:edg| allows you to configure a link to an external Git
repository that contains one or more themes that can be used with a
Drupal website. After you connect your website to a Git repository that
contains one or more themes, the themes will appear when you click
**Appearance** in the admin menu.


Git repository requirements
---------------------------

When you are creating your external Git repository, be sure that it
contains the following items:

-  One or more branches or tags.
-  One or more sets of Drupal theme files to use with your website. Each
   theme's files must be included in a separate directory whose name is
   the name of the theme.


Creating a theme repository whitelist
-------------------------------------

To protect hosted websites from using themes that contain settings or
code that could cause issues with the websites, you can add a whitelist
file of approved theme repositories to |acquia-product:edg|. When
administrative users attempt to add a theme repository,
|acquia-product:edg| compares the repository with the contents of the
``acsf_theme_whitelist.txt`` file.

To create a new whitelist file for your theme repositories, complete the
following steps:

#. Create a new file to contain your whitelist settings, based on the
   following conventions:

   -  Enter each external Git repository on a separate line.
   -  You can add comments to entries by starting lines with the number
      sign ( ``#`` ). The # will not be used for whitelist filtering.
   -  Use the asterisk character ( ``*`` ) for wildcard entry.
   -  If you do not end a repository line with an asterisk, its use is
      implied.

#. Save the file with the name ``acsf_theme_whitelist.txt`` in the root
   directory of your code repository.
#. Commit your code changes with the new whitelist file to your
   codebase.
#. Deploy the code to your production environment.

Example
~~~~~~~

The following whitelist file allows only theme repositories from the
Acquia organization on github.com, the Open Framework repository on
github.com, and the zen.git repository on drupal.org:

.. code:: 

      # Allow any github repos from the Acquia organization
      github.com:acquia/*

      # Allow specific github repo
      github.com:SU-SWS/open_framework

      # Allow the Zen theme from Drupal.org
      git.drupal.org:project/zen.git

If you do not upload a whitelist file, or if the file does not contain
any entries, |acquia-product:edg| will not block any theme repositories
from use.


Connecting to a theme repository
--------------------------------

To connect to an external Git repository that contains one or more
themes, complete the following steps:

#. Sign in to the |acquia-product:sfi| using an account that's been
   assigned either the 
   `Platform admin </site-factory/manage/website/manage/roles/platform-admin>`__
   or 
   `Site builder </site-factory/manage/website/manage/roles/site-builder>`__
   role.
#. Find the website that you want to modify, open its actions menu, and
   then click **Manage theme repository**.
#. Click **Connect site repository** to enter your Git repository's
   information.
#. Click the **Show SSH public key** link to display the SSH public key.
#. Select and copy the contents of the **SSH public key** field to your
   clipboard.
#. Open a new browser tab, and sign in to your Git repository.
#. Add the SSH public key to the theme repository, and configure the key
   to have read access.
#. Return to the page in which you're entering your theme repository
   information, and then enter the following values for the Git
   repository that you want to use:

   -  **Git URL** - The Git SSH URL of the theme repository (for
      example, ``git@github.com:repo.git``)
   -  **Branch or tag** - A valid branch or tag from the theme
      repository

.. note::  

      To ensure that theme changes for one website do not affect other
      websites that may use the same theme, we recommend that you use
      discrete *tags* for production websites. Using *branches* is
      recommended for staged websites, because it can speed your theme
      development process.

#. Click **Save**.

Theme repositories are compared to entries in the 
`whitelist file <#creating-a-theme-repository-whitelist>`__ based on the following parameters:

-  The *user@* preceding the theme repository is ignored.
-  Theme repositories that begin with an exact match of one or more of
   the whitelist file entries are accepted. For example, a whitelist
   entry of ``github.com`` would match ``git@github.com:repo.git``.

If the theme repository is blocked by the whitelist file,
|acquia-product:edg| will display an error message and keep the previous
theme repository settings.

If there are no error messages, your Git repository themes will be
checked out for use by your website. After all of your theme files have
been checked out successfully, you can view the themes by signing in to
the website and clicking **Appearance** in the admin menu.

.. note::  There may be a delay between associating your Git theme repository with
      your website and the availability of its themes on the Appearance page.
      For example, delays can be more noticeable during updates or staging
      processes.

Refreshing your theme
---------------------

Whenever you make changes to your theme files and those changes are
committed to the Git theme repository, you must update your websites'
theme files based on the correct branch or tag. You must update every
website that uses the updated theme.

Use one of the following methods to refresh your theme on a single
website:

-  *Refreshing your theme from the user interface*

   #. If you are refreshing a theme for a Drupal 8 stack, create a
      ``post-theme-deploy`` hook script, as described in `Requirement
      for deploying Drupal 8 themes <#performing-custom-actions-after-theme-deployments>`__. This is needed to clear
      the Twig cache after you deploy the updated theme.
   #. Sign in to the |acquia-product:sfi| using an account that's been
      assigned either the 
      `Platform admin </site-factory/manage/website/manage/roles/platform-admin>`__
      or 
      `Site builder </site-factory/manage/website/manage/roles/site-builder>`__
      role.
   #. Find the website that you want to modify, open its actions menu,
      and then click **Manage theme repository**.
   #. Select the appropriate method based on whether you are using a
      branch (staged websites) or a tag (production websites):

      -  *Branch*
         Click **Refresh themes**.
      -  *Tag*

         a. Click the **Change site theme repository** link.
         b. In the Branch or tag list, click the tag with the new theme
            changes.
         c. Click **Save**.

|acquia-product:edg| obtains your new theme changes from the Git
repository and adds them to your website. After it makes copies of the
theme files, the theme changes will appear in the website's Appearance
page (and if the theme is in use, on the website itself).

.. note::  There may be a delay between associating your Git theme repository 
   with your website and the availability of its themes on the Appearance page.
   For example, delays can be more noticeable during updates or staging
   processes.


Performing custom actions after theme deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the ``post-theme-deploy`` Factory hook to clear Twig caches
or perform other actions after deploying a theme. The
``post-theme-deploy`` Factory hook makes a set of arguments available to
any script that the hook runs:

+----------+-----------------------------------------------------------------+
| Argument | Value                                                           |
+==========+=================================================================+
| 1        | The hosting site group                                          |
+----------+-----------------------------------------------------------------+
| 2        | The hosting environment                                         |
+----------+-----------------------------------------------------------------+
| 3        | The theme scope (currently the only possible value is ``site``) |
+----------+-----------------------------------------------------------------+
| 4        | The theme event (possible values: ``modify``, ``delete``)       |
+----------+-----------------------------------------------------------------+
| 5        | The site domain                                                 |
+----------+-----------------------------------------------------------------+

Using these arguments, you can create a script like the following, which
runs a Drush command to clear the Twig cache on the affected site on
every server. |acquia-product:edg| supplies the needed host,
environment, and domain values:

.. code-block:: none

      #!/bin/bash
      drush8 @$1.$2 --uri=$5 ev '\Drupal\Core\PhpStorage\PhpStorageFactory::get("twig")->deleteAll();'

To deploy or update a Drupal 8 theme from a remote repository:

#. Create a script file with a name like ``ClearTwigCache``, with
   content similar to the previous example. The script must be
   executable.
#. Save and commit the script file in your code repository in the
   ``/factory-hooks/post-theme-deploy`` directory.
