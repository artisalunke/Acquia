.. include:: /common/global.rst

Building your Drupal 7 distribution
===================================

*For Drupal 8 installation and configuration instructions with
|acquia-product:edg|, see `Building your Drupal
distribution </site-factory/workflow/distro>`__.*

Although Acquia maintains the core platform of |acquia-product:edg|, you
have the freedom to develop your websites to meet your specific needs,
including selecting a Drupal distribution to use for the websites on
your platform.

If you have some websites that need to use Drupal 8, and others that
need to use Drupal 7, you will need to manage them in separate
|acquia-product:edg| *stacks*. A single stack can use either Drupal 8 or
Drupal 7, but not both. For more information, see `Using Site Factory
stacks </site-factory/tiers/stacks>`__.

Be sure to use the `|acquia-product:edg| Connector for Drupal
7 <https://www.drupal.org/node/2180241/release?api_version%5B%5D=103>`__
version of the `|acquia-product:edg|
Connector <https://www.drupal.org/project/acsf>`__ module.

.. _steps:

Installing and configuring a custom distribution
------------------------------------------------

To use a custom distribution with your |acquia-product:edg| websites,
complete the following steps:

#. `Add your SSH key to |acquia-product:ac|, and then clone the code
   repository for the website that you want to use to your local
   computer </site-factory/workflow/git>`__.
#. | On your local computer, delete all of the files and subdirectories
     contained in the ``docroot`` directory that you cloned from
     |acquia-product:edg|. When removing its contents, be sure to not
     delete the actual ``docroot`` directory.
   | You can run the following Git command from the ``docroot``
     directory to remove the files:

   ``git rm -r * .htaccess .gitignore``

   Do not run this Git command after you have installed your Drupal
   distribution in the ``docroot`` directory.

#. Move your custom Drupal distribution into the now empty ``docroot``
   directory.
   The ``docroot`` directory should contain the distribution's
   ``index.php`` file, along with all other files and subdirectories.
#. | Download the `|acquia-product:edg|
     Connector <https://www.drupal.org/project/acsf>`__ module from
     Drupal.org, and then extract its contents into your distribution.
   | You can use the following
     `Drush <http://docs.drush.org/en/master/>`__ command to do this:

   ``drush dl acsf``

   Note

   Be sure that you do not install the module in multiple locations in
   your code repository (such as both
   ``docroot/profiles/gardens/modules/contrib`` and
   ``docroot/sites/all/modules/contrib``). Multiple instances of the
   module can prevent |acquia-product:edg| from discovering and using
   the module.

   You can run the following command in the ``docroot`` directory to
   determine if your code repository contains more than one version of
   the module:

   ``git ls-files "*acsf.info*"``

#. Ensure that each of the following files can be read, written to, and
   executed by its owner, its group, and by other users:

   -  ``hooks/common/pre-web-activate/000-acquia-deployment.php``
   -  ``hooks/common/post-db-copy/000-acquia_required_scrub.php``

   To do this on Unix-like operating systems, use a command similar to
   the following:

   ``chmod 0755 [file names]``

#. Configure your installation profiles to require the module using the
   appropriate instruction by adding the following line to one of your
   profiles' ``.info`` files:

   ``dependencies[] = acsf``

#. Run the following Drush command from the ``docroot`` directory to
   initialize your custom distribution:

   ``drush --include=/path/to/acsf/acsf_init acsf-init``

   Note

   This command does not bootstrap a Drupal website, so you must run it
   with the ``--include`` argument that points to
   ``acsf/acsf_init/acsf_init``.

   The Drush command creates several directories and then copies files
   that |acquia-product:edg| requires for its tasks, including locating
   the correct database credentials.

#. Run the following Drush command from the ``docroot`` directory to
   ensure that everything is in order before you commit the custom
   distribution to the repository:

   ``drush --include=/path/to/acsf/acsf_init acsf-init-verify``

   The following results should be returned by the ``acsf-init-verify``
   command:

   ``acsf-init required files ok``

#. `Commit and push your custom distribution's files to
   |acquia-product:edg| </site-factory/workflow/deployments/steps>`__.
#. `Update your *Prod* environment with the custom distribution's files
   that you just
   pushed </site-factory/workflow/deployments/steps#deploy>`__.
#. If your custom distribution includes more than one installation
   profile, `enable any installation
   profiles </site-factory/manage/preferences/profiles>`__ that you want
   site builders to be able to select when creating new websites.

Now that your new Drupal distribution is installed and configured, site
builders can select the distribution for their use when create new
websites. For information regarding how to select your custom profile
when creating a new |acquia-product:edg| website, see `Managing
installation profiles in your
Factory </site-factory/manage/preferences/profiles>`__.
