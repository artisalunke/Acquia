.. include:: /common/global.rst

Site collections
================

To help you develop and maintain your production websites, you can
create site collections, which bundle and organize related websites.

A site collection contains a primary website (to which you can associate
a custom domain name) and one or more secondary websites. Site visitors
can view the primary website in a site collection using one of the
following URLs:

-  The website's |acquia-product:edg| URL
-  The site collection's URL
-  One of the custom domain URLs associated with the site collection

For example, you have a production website that describes a product, but
you also have a staging website that contains the theme and content
changes that you're currently developing. Having both of these websites
in a site collection, you can associate the current production website
with a custom domain URL. When the staging website is complete, you can
swap the websites, making the staging website the production website
with the custom domain URL (without having to contact your domain name
registrar regarding the website change).

.. note::  

   -  Only user accounts with the |platformadmin|_ or |sitebuilder|_ role can create
      or manage site collections.
   -  The websites contained by a site collection are completely separate
      from one another and do not have any common workflow capabilities
      (development, staging, production).
   -  You can duplicate a production website to create a secondary
      development website in the site collection, and then later promote it
      to the primary website. (Note that the new primary website doesn't
      contain databases or user-created items created after you duplicated
      the website.)

Video: Using site collections
-----------------------------

.. raw:: html

   <iframe allowfullscreen="" class="shadow bord" frameborder="0" height="296" src="https://www.youtube.com/embed/2lehCHTH_L8?rel=0" width="560"></iframe>

Creating a site collection
--------------------------


.. |sfilink| replace:: \ |acquia-product:sfi|\ 
.. _sfilink: /site-factory/manage/login

To create a new site collection:

#. In the |sfilink|_, select
   the site group that you want to contain the new site collection.

   .. note::  

      You can create site collections only inside of site groups.

#. Click the arrow to the right of **Create a new site** to open its
   menu.

   |Create a new site collection|

#. Click **New site collection**.
#. In the **Site collection name** field, enter a descriptive name for
   the site collection to display in the |acquia-product:sfi| (for
   example, ``Product site``).
#. In the **Internal URL** field, enter the |acquia-product:edg| site
   collection name to use with its URL (for example, ``prodsite``). The
   |acquia-product:edg| base URL is added to this name.
#. Click **Continue**.
#. In the **Site name** field, enter the site name for one of your
   websites. |acquia-product:edg| displays websites that match your
   entry as you type. As you add websites to the site collection, the
   page displays additional site name fields to allow you to add
   multiple websites.
#. If you want to add additional websites to the site collection as
   secondary websites, enter them in the additional site name fields.
#. Click **Finish**.

Using the site collection interface
-----------------------------------

After you create a site collection, the |acquia-product:sfi| displays a
detail page that you can use to manage the collection.

|Site collection detail overview|

#. Site collection URL
#. Number of websites in the site collection
#. Methods to add or remove custom URLs associated with the site
   collection
#. Primary website management
#. Secondary websites in the site collection
#. Groups that contain this site collection

Managing secondary sites
------------------------

After you've created a site collection, you can add or remove secondary
websites to the collection.

Adding sites
~~~~~~~~~~~~

To add a website to a site collection as a secondary website:

#. Go to the site collection detail page.
#. In the **Secondary sites in this collection** section, click **Add**.
#. In an empty **Site name** field, enter the site name for one of your
   websites that you want to add to the collection. |acquia-product:edg|
   displays websites that match your entry as you type.
#. Click **Finish**.

.. note::  
   
   A website can be a secondary website for only a single site collection.

Removing sites
~~~~~~~~~~~~~~

To remove a secondary website from a site collection:

#. Go to the site collection detail page.
#. In the **Secondary sites in this collection** section, find the
   website that you want to remove from the site collection.
#. Click the website's minus button.

   |Secondary site deletion button|

#. To confirm the website's removal from the site collection, click
   **Confirm**.

The website is no longer in the site collection and is moved back to the
group or subgroup that contains the site collection. If the website is
removed from a site collection that is not a member of any group or
subgroup, the website is listed only on the All my sites page.


Setting a new primary site
--------------------------

To make a secondary website the primary website for a site collection
(which associates the site collection's URL and any of its custom domain
names with the new primary website):

#. Go to the site collection detail page.
#. In the **Secondary sites in this collection** section, find the
   website that you want to set as the new primary website.
#. Click the website's **Make primary** button.

Controlling access to this feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, users with the *platform admin* and *site builder* roles can
promote secondary websites to the primary website for a site collection.
If you want to limit the users who can complete this action to only
*platform admins*, use the following steps:

#. Sign in to |acquia-product:edg| as a user with the *platform admin*
   role.
#. In the admin menu, click **Administration**, and then click the
   **Manage permissions** link.
#. Select the roles that you want to be able to promote a secondary
   website.
#. Click **Save**.


Assigning custom domain names
-----------------------------

You can associate one or more custom domain names with each of your site
collections, and each custom domain displays the current primary website
with the associated site collection. This allows you to change your
primary website (for example, you're making a development website the
new production website) without having to contact your domain name
registrar.

.. note::  

   If your primary website uses the `External
   Links <https://drupal.org/project/extlink>`__ module, validate your
   website's external links pattern matching to ensure that it's configured
   to handle new custom domains. For more information, see `External
   links </site-factory/feature/display/external-links>`__.

Associating custom domains
~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about associating custom domain names with your site
collections, see `Custom
domains </site-factory/manage/website/domains>`__.

Removing custom domains
~~~~~~~~~~~~~~~~~~~~~~~

To remove a custom domain from a site collection:

#. Go to the site collection detail page.
#. Click **Manage domains**.
#. In the **Domains belonging to this collection** section, find the
   domain name that you want to remove.
#. Click the domain name's minus icon.

   |Custom domain removal button|

#. To confirm the removal, click **Delete**.

Deleting a site collection
--------------------------

To delete a site collection:

#. `Sign in </site-factory/manage/login>`__ to |acquia-product:edg|  as a
   user account with the |platformadmin|_ role.
#. Find the site collection that you want to delete on the All my sites
   page, the All my groups page, or in a group that contains the site
   collection, and then open its actions menu.

   |Site collection actions menu|

#. Click **Delete collection**.
#. To confirm that you want to delete the site collection, click
   **Delete**.

|acquia-product:edg| deletes the site collection, but not the websites
that it contained. You can find websites from deleted site collections
on the All my sites page, because these websites do not belong to any
group.

.. note::  

   If you delete a site collection, you cannot reuse its name for a site
   collection in the same |acquia-product:edg| subscription.

.. |Create a new site collection| image:: https://cdn4.webdamdb.com/1280_QWA8NJ6VR851.png?1526475543
   :width: 750px
   :height: 177px
.. |Site collection detail overview| image:: https://cdn2.webdamdb.com/1280_AfefrvoN7Bm0.png?1526475574
   :width: 540px
   :height: 386px
.. |Secondary site deletion button| image:: https://cdn2.webdamdb.com/1280_6ueP9AAFyyH6.png?1526475575
   :width: 540px
   :height: 194px
.. |Custom domain removal button| image:: https://cdn4.webdamdb.com/1280_UJq7m36Q9887.png?1526476059
   :width: 540px
   :height: 265px
.. |Site collection actions menu| image:: https://cdn4.webdamdb.com/1280_ggCcffsBQgv1.png?1526475813
   :width: 540px
   :height: 340px

.. |platformadmin| replace:: *platform admin*
.. _platformadmin: /site-factory/users/admin/platform-admin

.. |sitebuilder| replace:: *site builder*
.. _sitebuilder: /site-factory/users/admin/site-builder