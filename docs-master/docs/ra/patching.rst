.. include:: /common/global.rst

Patching and locking modules
============================

Modification of contributed module and core files must implement one of
the following options to ensure that changes are not overwritten by
Remote Administration (RA) updates. RA uses Drush to update both core
and contributed modules, so all modifications will be overwritten during
the update process.

Note

If you're working with a third-party development team who won't be a
part of your ongoing support, ensure that they understand and supply the
information in these guidelines.

.. _locking:

Locking modules
---------------

-  If modified contributed modules should not be updated even when
   insecure, they must contain a ``drush lock`` file to ensure that they
   are not overwritten by drush. For installation instructions, see
   `Using drush lock files with contributed
   modules <%5Bacquia-product:kb%5Darticles/using-drush-lock-files-contributed-modules>`__.
-  This ``lock`` must exist on the production tag, because this is the
   default tag from which all RA Updates begin.
-  Modules that are locked will not receive security updates. Any
   security vulnerability that results is the responsibility of the
   Client’s development team.
-  Modified modules overwritten as a part of the update process can be
   reverted. The RA team can assist with installing lock files to
   prevent further modifications. At this time, update automation does
   not detect differences between the installed module and its official
   release on Drupal.org.

.. _patching:

Patching core and contributed modules
-------------------------------------

Acquia RA supports patches to core and contributed modules at its
discretion. To provide support, patch information and files must be
provided and correctly set up. Update automation will attempt to apply
the provided patches, and all results will be noted in the corresponding
ticket.

Update automation implements a slightly modified version of the `Drush
Patch File <https://bitbucket.org/davereid/drush-patchfile>`__
extension. The following steps detail examples of each different use
case.

#. Create the ``patches.make`` file in the following location:

   ``[reponame]/``

#. Ensure that the ``patches.make`` file contains the following
   information for the patch:

   -  A link to the patch, either on
      `Drupal.org <https://www.drupal.org>`__ (preferred) or in the repo
   -  If the patch exists only in the repo, place it in
      ``[reponame]/patches/my_custom_patch.patch``, as patches placed in
      the directory of the module they modify will be overwritten before
      automation attempts to apply the patch, and the patch will be
      unavailable
   -  A comment linking to the original Drupal.org issue which the patch
      addresses
   -  A comment noting anything special about the applicability of this
      particular patch

#. Repeat the previous step for each discrete patch.

   Note

   It is also possible to combine all patches into a single patch file.
   However, this method makes it more difficult to discern which part of
   the patch is still relevant.

A complete ``patches.make`` file with a Drupal core patch, a remote
patch file from Drupal.org, and a local patch would look similar to
this:

``; Specify the version of Drupal being used. core = 7.x ; Specify the api version of Drush Make. api = 2  ; N/A ; Patching README.txt file. projects[drupal][patch][] = "patches/minor_core_patch.patch"  ; https://www.drupal.org/node/2408217 ; Error when attempting to clear cache that is related to ctools. projects[ctools][patch][] = "https://www.drupal.org/files/issues/ctools-cache-handler.patch"  ; https://www.drupal.org/node/1713076 ; Devel generate fails when generating data for a field. projects[devel][patch][] = "patches/devel_generate_textfield_maxlength-1713076-1.patch"``

Note

Acquia recommends placing local patch files in a directory called
``patches``, which is located above the ``docroot`` directory.

Automated patching is still being tested, and functionality improvements
will be added. It is imperative that all functionality affected by the
patch be thoroughly tested to ensure it behaves as expected. While the
RA team can help troubleshoot such functionality, all customizations are
ultimately the responsibility of the Client’s development team.

Acquia RA recommends moving to stable, unmodified module releases as
soon as possible. We recommend that development teams regularly check to
see if a patched issue was resolved in either a security update or
bug-fix release in order to move from modified code to a clean release.
