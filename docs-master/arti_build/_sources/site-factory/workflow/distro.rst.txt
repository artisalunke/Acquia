.. include:: /common/global.rst

Building your Drupal distribution
=================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/workflow/distro/*

*For Drupal 7 installation and configuration instructions with
|acquia-product:edg|, see `Building your Drupal 7
distribution </site-factory/workflow/distro/drupal7>`__.*

Although Acquia maintains the core platform of |acquia-product:edg|, you
have the freedom to develop your websites to meet your specific needs,
including selecting a Drupal distribution to use for the websites on
your platform.

If you have some websites that need to use Drupal 8, and others that
need to use Drupal 7, you will need to manage them in separate
|acquia-product:edg| *stacks*. A single stack can use either Drupal 8 or
Drupal 7, but not both. For more information, see `Using Site Factory
stacks </site-factory/tiers/stacks>`__.

For Drupal 8, Acquia recommends that you use the
`|acquia-product:ld| </lightning>`__ distribution, which allows you to
create `multiple installation
profiles </site-factory/workflow/profiles>`__ within your custom Drupal
distribution.

To ensure that your websites that use a custom distribution can
communicate with |acquia-product:edg| and the |acquia-product:sfi|, you
must add the `|acquia-product:edg|
Connector <https://www.drupal.org/node/2180241/release?api_version%5B%5D=7234>`__
module to your distribution's code.

.. _security:

Planning for security with your custom Drupal distribution
----------------------------------------------------------

Although |acquia-product:edg| uses Drupal's native multi-site
functionality for governance and resource efficiency, the distribution
of Drupal used by |acquia-product:edg| is ultimately your
responsibility. It is important to remember that your
|acquia-product:edg|-hosted websites will have separate databases,
content, and user account — which means they are all in a single
multi-tenant application. When granting Drupal users elevated *`platform
admin </site-factory/users/admin/platform-admin>`__* or *`site
builder </site-factory/users/admin/site-builder>`__* permissions, these
permissions may include the ability to execute PHP using Drupal's user
interface, based on your configuration.

Acquia recommends the following security practices:

-  Grant elevated permissions only to trusted developers on your team.
-  When developing your distribution, ensure that the standard user
   experience does not require elevated permissions.
-  Never enable Drupal's core PHP module.
-  Follow `Drupal best
   practices <https://www.drupal.org/docs/8/security/writing-secure-code-for-drupal-8>`__
   for writing secure code.
-  Consider installing the
   `Paranoia <https://www.drupal.org/project/paranoia>`__ module, which
   provides additional safeguards against the injection of PHP code
   using Drupal's user interface.
-  Periodically compare your list of installed modules against the
   Paranoia module, and perform additional tests against the modules not
   covered by the Paranoia module. Evaluating your installed modules can
   ensure that it is not possible to inject PHP code using the user
   interface.

.. _steps:

Installing your distribution
----------------------------

To add a Drupal 8 distribution to your |acquia-product:edg| codebase and
prepare it for use, complete the following steps:

#. `Add your SSH key to |acquia-product:ac|, and then clone the code
   repository for the website that you want to use to your local
   computer </site-factory/workflow/git>`__.
#. On your local computer, delete all of the files and subdirectories
   contained in the ``docroot`` directory that you cloned from
   |acquia-product:edg|. When removing its contents, be sure to not
   delete the actual ``docroot`` directory.

   You can run the following Git command from the ``docroot`` directory
   to remove the files:

   ``git rm -r * .htaccess .gitignore``

   Do not run this Git command after you have installed your Drupal
   distribution in the ``docroot`` directory.

#. Move your custom Drupal distribution into the now empty ``docroot``
   directory. For installation instructions for |acquia-product:ld|
   including using `|acquia-product:blt| </devtools/blt>`__, see
   `Installing |acquia-product:ld| </lightning/install>`__.

   After you do this, the ``docroot`` directory should contain the
   distribution's ``index.php`` file, along with all other files and
   subdirectories.

#. Use the following command to add the `|acquia-product:edg|
   Connector <https://www.drupal.org/project/acsf>`__ module to your
   ``composer.json``:

   ``composer require drupal/acsf``

   Notes

   If you prefer to download with
   `Drush <http://docs.drush.org/en/master/>`__, you can download the
   module with the ``drush dl acsf`` command.

   Be sure that you do not install the module in multiple locations in
   your code repository (such as both
   ``docroot/profiles/profilename/modules/contrib`` and
   ``docroot/modules/contrib``). Multiple instances of the module can
   prevent |acquia-product:edg| from discovering and using the module.

   You can run the following Git command in the ``docroot`` directory to
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

After installing your distribution, you must `configure it for
use <#configure>`__.

.. _configure:

Configuring your distribution
-----------------------------

To configure your Drupal 8 distribution for use with your websites, you
can either use `|acquia-product:blt| <#blt>`__, or you can use a `manual
process <#noblt>`__.

Using |acquia-product:blt|
~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure your distribution with |acquia-product:blt|, perform the
following steps as described in the `|acquia-product:blt|
documentation <https://blt.readthedocs.io/en/latest/readme/acsf-setup/#acsf-setup>`__
after setting up |acquia-product:blt|:

#. From the project's ``docroot`` directory, execute ``blt acsf:init``.
#. Create a custom profile `using
   |acquia-product:ld| </lightning/subprofile>`__. If you are not using
   |acquia-product:ld|, you can `create a profile using the Drupal
   Console <https://hechoendrupal.gitbooks.io/drupal-console/content/en/commands/generate-profile.html>`__.
   For more information about installation profiles, see `Installation
   profiles on
   |acquia-product:edg| </site-factory/workflow/profiles>`__.
#. Add ``acsf`` as a dependency for your profile.
#. Edit the ``blt/project.yml`` file. In the ``project`` section, modify
   the ``profile`` key to use the newly created custom profile based on
   the following example, replacing ``mycustomprofile`` with the name of
   your profile:

   ``project:             machine_name: blted8             prefix: BLT             human_name: 'BLTed 8'             profile:                 name: mycustomprofile``

#. Save your changes.
#. Deploy to your Git repository with the ``blt deploy`` command, or
   through your continuous integration configuration.
#. *If you are using continuous integration,* push your build artifact
   to your production or non-production environment.
#. If your custom distribution includes more than one installation
   profile, `enable any installation
   profiles </site-factory/manage/preferences/profiles>`__ that you want
   site builders to be able to select when creating new websites.

Your new custom Drupal distribution is now configured and `available for
use <#next>`__.

.. _noblt:

Manually configuring your distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are *not* using |acquia-product:blt| to manage your distribution,
complete the following steps to configure your new distribution:

#. Configure your installation profiles to require the module using the
   appropriate instruction by adding the following line to your
   profile's installation profile file at
   ``profiles/[profilename]/[profilename].info.yml``, where
   ``[profilename]`` is the name of your profile:

   ``- acsf``

#. Run the following Drush command from the ``docroot`` directory to
   initialize your custom distribution:

   ``drush --include=/path/to/acsf/acsf_init acsf-init``

   Note

   This command does not bootstrap a Drupal website, so you must run it
   with the ``--include`` argument that points to
   ``acsf/acsf_init/acsf_init``.

   The previous Drush command creates several directories, and then
   copies files that |acquia-product:edg| requires for its tasks,
   including locating the correct database credentials.

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

Your new custom Drupal distribution is now configured and `available for
use <#next>`__.

Note

Single sign-on for Drupal 8 websites requires special configuration. For
configuration information, see `Setting up single sign-on for Drupal
8 </site-factory/manage/sso>`__.

.. _next:

Using the Drupal distribution
-----------------------------

Now that your new Drupal distribution is installed and configured, site
builders can select the distribution for their use when create new
websites. For information regarding how to select your custom profile
when creating a new |acquia-product:edg| website, see `Managing
installation profiles in your
Factory </site-factory/manage/preferences/profiles>`__.
