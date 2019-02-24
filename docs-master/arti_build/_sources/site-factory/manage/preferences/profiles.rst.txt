.. include:: /common/global.rst

Managing installation profiles in your Factory
==============================================

After you have added installation profiles to your custom distribution,
you can `enable the installation profiles <#enable>`__ to allow site
builders to select an installation profile when they create new
|acquia-product:edg|-hosted websites.

When site builders create a new website, they will have the choice of
any enabled installation profile. Any installation profiles that are in
your code base, but which have not been enabled, will not be displayed
to site builders on the **Create a new site** page.

|Choosing an installation profile when you create a new website|

Selecting an installation profile is a one-time choice—you cannot change
the installation profile after the website is created.

If you have both added an installation profile to your codebase and
deployed it to your platform, but it does not appear in the
|acquia-product:sfi|, `contact Acquia Support </support#contact>`__ for
assistance.

Enabling installation profiles
------------------------------


.. |platform admin| replace:: *platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin

#. Sign in to the |acquia-product:sfi| with an account that has the
   |platform admin|_ role.
#. In the admin menu, click **Administration**, and then click the
   **Installation profile management** link.

   |Save changes to profiles|

#. In the **Enabled** column, select the check boxes for the
   installation profiles that you want to enable for use by site
   builders.

   .. note::  The installation profile with the **REST API Default** option is the
      default for websites created using the
      `Acquia Cloud Site Factory API </site-factory/extend/api>`__. This does not
      affect the process for creating websites using the
      |acquia-product:sfi|, and means only that if you create a website
      using the |acquia-product:sfa|, the default installation profile will
      be used if you do not designate a different installation profile.

#. Click **Save settings**.

Installation profiles will become available for use after the
``SfVersions`` task completes. To learn more about monitoring task logs,
see 
`Task logs in Acquia Cloud Site Factory </site-factory/monitor/tasklog>`__.

.. |Choosing an installation profile when you create a new website| image:: https://cdn4.webdamdb.com/1280_EYX48ASfbTk0.jpg?-62169955200
   :width: 750px
   :height: 290px
.. |Save changes to profiles| image:: https://cdn4.webdamdb.com/1280_Ier4NauEml11.jpg?-62169955200
   :width: 700px
   :height: 359px
