.. include:: /common/global.rst

Managing site ownership
=======================

Each |acquia-product:edg| website has an authenticated user account that
is listed as its *site owner*. By default, the site owner is the account
that created the website. A website's site owner account (whose
functionality is independent of the
`roles </site-factory/users/admin>`__ available in |acquia-product:edg|)
can perform several `website
actions </site-factory/manage/website/manage#site-action>`__, including
deleting the website.

Site owners can also view all of the websites that they own on the **All
my sites** page in the management interface, even if some or all of the
websites are in groups of which they are not a member.

Transferring site ownership
---------------------------

To change the site owner account for a single website, complete the
following steps:

#. `Sign in </site-factory/manage/login>`__ to |acquia-product:edg|,
   find the website for which you want to transfer ownership, and then
   open its actions menu.

   |Site actions menu|

#. Click **Transfer site ownership**.
#. In the **Username or e-mail** field, enter the username or email
   address for the |acquia-product:edg| account to which you want to
   transfer site ownership.
#. Click **Transfer site**.

|acquia-product:edg| sends confirmation emails to the existing and new
site owners. After each person confirms the change, the website is
associated with the new owner account.

.. _restrict:

Restricting website ownership
-----------------------------

Because website creators are made the site owners by default, this could
provide them greater authority than you may want. To avoid this, you can
configure |acquia-product:edg| to have websites that are created by
users not in the |platform admin|_ role to instead
have a specified *platform admin* user to become their site owner.


.. |platform admin| replace:: *Platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin

To restrict website ownership of newly created websites to a *platform
admin*, complete the following steps:

#. Sign in to the |acquia-product:sfi| with the *platform admin* role.
#. In the admin menu, click **Administration**, and then, under **Site
   Factory management**, click **Site ownership settings**.
#. | In the **Site owner account** field, enter the Site Factory user
     name (email address) for a user with the *platform admin* role:

   |Add site owner email address here|

#. Click **Save**.

Newly-created websites created by any user who does not have the
*platform admin* role will have the user you specified in the **Site
owner account** field designated as the site owner. The site creator in
this case will not have any role with the new website by default; if
they have the *platform admin* or *site builder* role, you can
automatically assign them a role for the website using the `Centralized
role management </site-factory/users/centralized>`__ feature.

To disable this feature, clear the **Site owner account** field, and
then click **Save**. If no user is listed in the **Site owner account**
field, any user who creates a website will be its site owner.

.. admonition::  Permissions Note

   The site transfer process does **not** assign or remove roles from 
   either the previous or the new website owner accounts. The process 
   simply changes the website's owner to a different account.
   
   If you want to associate the new site owner account with an 
   administrative role (such as *Administrator* or *Site maintainer*), you 
   will need to sign in to the website as an administrative account and 
   then manually assign to the new site owner account the required roles.

.. |Site actions menu| image:: https://cdn4.webdamdb.com/1280_MolekfJrnUF5.png?1526475845
   :width: 750px
   :height: 356px
.. |Add site owner email address here| image:: https://cdn4.webdamdb.com/1280_Yvdsr2zSjI51.png?1526476179
   :width: 600px
   :height: 163px
