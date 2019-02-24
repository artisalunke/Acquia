.. include:: /common/global.rst

|acquia-product:sfi| roles
==========================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/users/admin/*

In order to manage your |acquia-product:edg| environment and websites,
you must sign in with an account that has the appropriate permissions
for the actions that you need to accomplish. |acquia-product:edg|
permissions are gathered in roles, which enable administrators to assign
a collection of permissions to an account, instead of assigning them one
at a time. Your account can be assigned one or more of the following
|acquia-product:edg| roles in the |acquia-product:sfi|:

-  |platform admin|_ -
   Provides overall responsibility for |acquia-product:edg| deployment,
   including management of websites and OpenID accounts
-  |site builder|_ -
   Allows for website and content creation and management
-  |developer|_ - Enables
   updating development and staging environments with new and
   updated code
-  |release engineer|_ - Grants
   access to the PaaS production environment for code pushes and update
   status monitoring

.. |platform admin| replace:: *platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin

.. |site builder| replace:: *site builder*
.. _site builder: /site-factory/users/admin/site-builder

.. |developer| replace:: *developer*
.. _developer: /site-factory/users/admin/developer

.. |release engineer| replace:: *release engineer*
.. _release engineer: /site-factory/users/admin/release-engineer

In addition to the individual roles, you can also 
`assign websites to groups </site-factory/manage/website/manage>`__, and manage access
to the websites in those groups by adding users to a group. For more
information, see 
`Managing site group users </site-factory/manage/website/users>`__.


Video: |acquia-product:sfi| user roles
--------------------------------------

.. raw:: html

   <iframe allowfullscreen="" class="shadow bord" frameborder="0" height="296" src="https://www.youtube.com/embed/fe8M10OL64k?rel=0" width="560"></iframe>

.. _matrix:

Permissions matrix
------------------

+-------------+-------------+-------------+-------------+-------------+
| Website and | *platform   | *site       | *developer* | *release    |
| site        | admin*      | builder*    |             | engineer*   |
| collection  |             |             |             |             |
| management  |             |             |             |             |
+=============+=============+=============+=============+=============+
| View        | |yes|       | |yes|       | |no|        | |no|        |
| websites    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Sign in     | |yes|       | |yes|       | |yes|       | |yes|       |
+-------------+-------------+-------------+-------------+-------------+
| Create,     | |yes|       | |yes|       | |no|        | |no|        |
| `manage </s |             |             |             |             |
| ite-factory |             |             |             |             |
| /manage/web |             |             |             |             |
| site>`__,   |             |             |             |             |
| and delete  |             |             |             |             |
| websites    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Manage      | |yes|       | |yes|       | |no|        | |no|        |
| domains     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Manage      | |yes|       | |no|        | |no|        | |no|        |
| `site       |             |             |             |             |
| groups </si |             |             |             |             |
| te-factory/ |             |             |             |             |
| manage/webs |             |             |             |             |
| ite/manage# |             |             |             |             |
| group>`__   |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Create site | |yes|       | |yes|       | |no|        | |no|        |
| collections |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Remove site | |yes|       | |no|        | |no|        | |no|        |
| collections |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Set the     | |yes|       | |yes|       | |no|        | |no|        |
| primary     |             |             |             |             |
| website in  |             |             |             |             |
| a site      |             |             |             |             |
| collection  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Specify     | |yes|       | |yes|       | |no|        | |no|        |
| login       |             |             |             |             |
| authenticat |             |             |             |             |
| ion         |             |             |             |             |
| mode        |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Specify     | |yes|       | |yes|       | |no|        | |no|        |
| global ToS  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | *platform   | *site       | *developer* | *release    |
| management  | admin*      | builder*    |             | engineer*   |
+-------------+-------------+-------------+-------------+-------------+
| Create user | |yes|       | |no|        | |no|        | |no|        |
| accounts    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Delete,     | |yes|       | |no|        | |no|        | |no|        |
| block, and  |             |             |             |             |
| unblock     |             |             |             |             |
| users       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Assign      | |yes|       | |no|        | |no|        | |no|        |
| roles to    |             |             |             |             |
| users       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Find users  | |yes|       | |no|        | |no|        | |no|        |
+-------------+-------------+-------------+-------------+-------------+
| Workflow    | *platform   | *site       | *developer* | *release    |
| management  | admin*      | builder*    |             | engineer*   |
+-------------+-------------+-------------+-------------+-------------+
| View        | |yes|       | |no|        | |yes|       | |yes|       |
| environment |             |             |             |             |
| 's          |             |             |             |             |
| site update |             |             |             |             |
| status      |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| View        | |yes|       | |no|        | |yes|       | |yes|       |
| environment |             |             |             |             |
| 's          |             |             |             |             |
| staging     |             |             |             |             |
| update      |             |             |             |             |
| status      |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Deploy code | |no|        | |no|        | |yes|       | |yes|       |
| to          |             |             |             |             |
| development |             |             |             |             |
| and staging |             |             |             |             |
| environment |             |             |             |             |
| s           |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Release     | |no|        | |no|        | |no|        | |yes|       |
| code to     |             |             |             |             |
| production  |             |             |             |             |
| environment |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Enable      | |yes|       | |no|        | |no|        | |no|        |
| installatio |             |             |             |             |
| n           |             |             |             |             |
| profiles    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Statistics  | *platform   | *site       | *developer* | *release    |
| and backups | admin*      | builder*    |             | engineer*   |
+-------------+-------------+-------------+-------------+-------------+
| View        | |yes|       | |yes|       | |no|        | |no|        |
| website     |             |             |             |             |
| statistics  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Create      | |yes|       | |yes|       | |no|        | |no|        |
| website     |             |             |             |             |
| backups     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Download    | |yes|       | |yes|       | |no|        | |no|        |
| website     |             |             |             |             |
| backups     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

\* - The *Manage domains* and *Set the primary site in a site
collection* permissions can be configured so that they are limited to
the *platform admin* role. `Learn
more </site-factory/manage/sf-perm>`__.

.. _compare:

Comparing website roles and |acquia-product:sfi| roles
------------------------------------------------------

|acquia-product:edg| and the websites in an |acquia-product:edg|
deployment can have different sets of user roles. For example, a user
might have the *platform admin* role on |acquia-product:edg|, but only
be a standard registered member on one of the |acquia-product:edg|
websites.

A user’s role on the website governs the level of access the user has on
the website. Therefore, a *platform admin* on |acquia-product:edg| would
need administrator privileges on the website itself to maintain a high
level of access.

You can use centralized role management to map |acquia-product:edg|
*platform admin* and *site builder* roles to hosted website roles. For
example, if you have a role on your hosted websites named content
manager, you can specify that all users with the *platform admin* role
also have the content manager role on each hosted website. For more
information, see `Assigning hosted site roles during
sign-in </site-factory/users/centralized>`__.