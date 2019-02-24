.. include:: /common/global.rst

Lightning roles
===============

|acquia-product:ld| creates several roles and permissions during
installation for use with content creation and review, and are directly
based on the available content types. These roles are part of the
**Lightning Roles** component.

For experienced developers, these roles may be unnecessary, as having
many additional defined roles can cause the role management on the
website to become unmanageable.

Although this feature is installed by default, it can be disabled during
either of the following situations:

-  `During installation <#disabling-role-creation-at-install>`__
-  `After installation <#disabling-role-creation-after-install>`__

.. note::

   Disabling role creation by |acquia-product:ld| Roles after installation does not remove roles created during the installation process.

Other |acquia-product:ld| components that introduce roles will have
those roles as an optional configuration, which will carry a dependency
on ``lightning_roles``.


Disabling role creation at install
----------------------------------

Because |acquia-product:ld| uses
`sub-profiles </lightning/subprofile>`__ during the installation
process, you can use them to disable the |acquia-product:ld| Roles
component in a sub-profile before installing |acquia-product:ld|.

By default, the |acquia-product:ld| Roles modules is located at
``/docroot/profiles/lightning/modules/lightning_features/lightning_core/modules/lightning_roles``.

For more information on creating and editing installation profiles, see
`How to Write a Drupal 8 Installation
Profile <https://www.drupal.org/docs/8/creating-distributions/how-to-write-a-drupal-8-installation-profile>`__.


Disabling role creation after install
-------------------------------------

If, after installation, you want to prevent |acquia-product:ld| Roles
from creating additional content creation and review roles, complete the
following steps:

#. Sign in to your |acquia-product:ld| website as an administrator.
#. Navigate to **Configuration > Lightning > Roles**.
#. Clear the check boxes for the role types that you do not want to be
   created by the |acquia-product:ld| Roles component.
#. Click **Save configuration.**
