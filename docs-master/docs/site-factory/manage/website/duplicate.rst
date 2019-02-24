.. include:: /common/global.rst

Duplicating a site
==================

|acquia-product:edg| enables you to create duplicate websites from an
existing website. These duplicate websites can either contain only the
structure of the original website (*clean copy*), or can be complete and
exact copies of the original website (*full website clone*).

Duplicating your website can be useful in the following situations:

-  You need to create several websites with the same or similar
   configurations.
-  You have a production website that you'd like to experiment with, but
   you want to make changes that external website visitors should not
   encounter.

.. note::  

   If you duplicate a website with a custom domain, |acquia-product:edg| 
   removes any `custom domain redirection </site-factory/manage/redirect>`__ 
   settings from the duplicated website.

What gets duplicated
--------------------

When you duplicate a website, depending on the option that you select,
the new website will contain the following:

Comparison of duplication methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Description           | Clean copy            | Full website clone    |
+=======================+=======================+=======================+
| **Configurations**    | All website           | All website           |
|                       | configurations        | configurations        |
+-----------------------+-----------------------+-----------------------+
| **Content: General**  | Content created by    | All content           |
|                       | anonymous users, and  |                       |
|                       | user accounts with    |                       |
|                       | the *administrator*   |                       |
|                       | or *website           |                       |
|                       | maintainer roles*     |                       |
+-----------------------+-----------------------+-----------------------+
| **Content: Comments** | Not copied            | All content           |
+-----------------------+-----------------------+-----------------------+
| **Database tables**   | All tables are        | All tables            |
|                       | copied, but tables    |                       |
|                       | with ephemeral data,  |                       |
|                       | such as the sessions, |                       |
|                       | accesslog, semaphore, |                       |
|                       | batch, and queue      |                       |
|                       | tables are truncated  |                       |
+-----------------------+-----------------------+-----------------------+
| **Files**             | Files uploaded to the | Files uploaded to the |
|                       | website's Media       | website's Media       |
|                       | Library or attached   | Library or attached   |
|                       | to content using the  | to content using the  |
|                       | File field. Files     | File field            |
|                       | owned by removed      |                       |
|                       | users are reassigned  |                       |
|                       | to the Anonymous      |                       |
|                       | user.                 |                       |
+-----------------------+-----------------------+-----------------------+
| **Modules**           | All modules copied.   | All modules           |
|                       | Some disabled modules |                       |
|                       | may be re-enabled if  |                       |
|                       | they are needed       |                       |
|                       | during the user       |                       |
|                       | scrubbing process.    |                       |
+-----------------------+-----------------------+-----------------------+
| **Structure**         | All structural        | All structural        |
|                       | elements, including   | elements, including   |
|                       | blocks and taxonomies | blocks and taxonomies |
+-----------------------+-----------------------+-----------------------+
| **Themes**            | All themes            | All themes            |
+-----------------------+-----------------------+-----------------------+
| **Users**             | User 1, all user      | All user accounts     |
|                       | accounts with the     |                       |
|                       | *administrator* or    |                       |
|                       | *website maintainer*  |                       |
|                       | roles, all OpenID     |                       |
|                       | administrator users,  |                       |
|                       | and any users listed  |                       |
|                       | in a |hook|_          |                       |
+-----------------------+-----------------------+-----------------------+
| **All other items**   | Not copied            | Copied to the new     |
|                       |                       | website               |
+-----------------------+-----------------------+-----------------------+

.. |hook| replace:: hook that preserves accounts from scrubbing
.. _hook: /site-factory/workflow/scrub


Duplicating a website
---------------------

To duplicate an |acquia-product:edg| website, use one of the following
methods:

-  Using the
   ``/sites/[siteID]/duplicate`` `endpoint <https://www.demo.acquia-cc.com/api/v1#Duplicate-a-site>`__ 
   in the `Acquia Cloud Site Factory API </site-factory/extend/api>`__
-  Using the |acquia-product:sfi|

To duplicate a website through the |acquia-product:sfi| user interface:

#. `Sign in </site-factory/manage/login>`__ to the |acquia-product:sfi|,
   find the website that you want to duplicate, and then open its
   actions menu.

   |Site actions menu|

#. Click **Duplicate site**.
#. In the text field, enter the new |acquia-product:edg| name for your
   website.
#. Select the `duplication option <#duplicating-a-website>`__ that you want to use for
   your website:

   -  **Create a clean copy**
   -  **Full site clone**

#. Click **Duplicate site**.

The duplication process begins and can take several minutes to complete.
When it's finished duplicating, |acquia-product:edg| sends a completion
email to users with the *platform admin* and *site builder* roles.

.. admonition::  Duplicate websites and groups

   Websites duplicated from the **All my sites** page will not be part of
   any group or subgroup.

   If you duplicate a website from within a group, the new website will be
   part of that group. It will not inherit assigned groups and subgroups —
   the duplicate website is assigned only the group or subgroup in which
   you started the duplication process.

Because the website duplication process copies the existing user account
information, members of the original website can sign in on the
duplicate website using their same username and password.

.. |Site actions menu| image:: https://cdn3.webdamdb.com/1280_wq199oFO4a11.png?1526475813
   :width: 750px
   :height: 382px
