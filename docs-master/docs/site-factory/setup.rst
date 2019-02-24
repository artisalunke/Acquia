.. include:: /common/global.rst

Setting up your Factory
=======================

.. container:: internal-navigation

   **Configuring and using Site Factory**

   * Setup
   * :doc:`Migrate </site-factory/migrate>`
   * :doc:`Manage </site-factory/manage>`
   * :doc:`Workflow </site-factory/workflow>`
   * :doc:`Extend </site-factory/extend>`
   * :doc:`Monitor </site-factory/monitor>`


When preparing to develop your new |acquia-product:edg|-hosted websites, your development plan should incorporate all of the following actions to ensure a smooth and successful launch:

.. note::  The |checklist|_ documentation page provides a list of specific, actionable tasks that correspond with these topics to help ensure a smooth, successful launch.


.. |checklist| replace:: Checklist for migrating your sites to \ |acquia-product:edg|\ 
.. _checklist: /site-factory/migrate/plan

1) Perform governance assessment
--------------------------------

Your success with |acquia-product:edg| depends on a strong governance strategy, which ensures that your websites are architected and built in a sustainable manner. Review our product-agnostic `governance strategy documentation </resources/governance>`__ and |govpage|_ to prepare for creating the infrastructure upon which your websites will be built.

.. |govpage| replace:: Governance on  \ |acquia-product:edg|\ 
.. _govpage: /site-factory/governance

2) Create your distributions and installation profiles
------------------------------------------------------

After creating a development plan, you should `select a base distribution </site-factory/workflow/distro>`__ on which to base your
websites' creation. Acquia recommends that you use the |ldlink|_ distribution in conjunction with |bltlink|_,  which allows you to create and manage `multiple installation profiles </site-factory/workflow/profiles>`__. Profile inheritance enables you to create distinct sub-profiles for groups of websites that share baseline global functionality, but may differ in information architecture or features.

.. |ldlink| replace:: \ |acquia-product:ld|\ 
.. _ldlink: /lightning

.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt

.. important::  Develop your base distribution and installation profiles before you begin website development.


3) Create and manage theming
----------------------------

As part of your governance policy, your `distribution of Drupal </site-factory/workflow/distro>`__ and `installation profiles </site-factory/workflow/profiles>`__ should provide base themes that provide the majority of layout and design. Each website in your
platform should leverage an `external theme repository </site-factory/theme/external>`__ to provide per-website branding and styling within the guidelines set by your platform’s base theme.


4) Familiarize yourself with the |acquia-product:sfi|
-----------------------------------------------------

See |manage|_ to familiarize yourself with the |acquia-product:sfi|, which helps you manage the configuration of your platform.

.. |manage| replace:: Managing your  \ |acquia-product:edg|\ 
.. _manage: /site-factory/manage


5) Configure users, teams, and roles
------------------------------------

Your governance strategy should focus on defining roles that can be applied globally to all of your |acquia-product:edg|-hosted websites, instead of providing website-by-website permissions. The |acquia-product:sfi| `provides predefined roles </site-factory/users/admin>`__ to help you manage your shared infrastructure and websites. As part of your initial setup, you should perform the following tasks:

-  Configure your `Acquia Cloud teams and permissions </site-factory/manage/cloud-perm>`__
-  Configure `single sign-on </site-factory/manage/sso>`__ (Drupal 8 only)
-  Configure `login authentication mode </site-factory/manage/login-mode>`__ (Drupal 7 only)
-  Set up and require `two-factor authentication </site-factory/users/tfa>`__ for your users


6) Create websites, and the groups and site collections to manage them
----------------------------------------------------------------------

Best practices would have you `create groups </site-factory/manage/website/groups-create>`__ in the |acquia-product:sfi| before creating individual websites. |acquia-product:edg| `groups </site-factory/manage/website#group>`__ allow you to separate your websites into logical sets, and `control user access </site-factory/manage/website/users>`__ to the websites in the |acquia-product:sfi|. For more information about managing your groups after creating them, see `Managing site groups </site-factory/manage/website/groups-manage>`__.

As you create websites, you can also `create site collections </site-factory/manage/website/site-coll>`__, which bundle and organize related websites together for easier management. A site collection contains a primary website (usually the production website) and one or more secondary websites. By having these related websites in a site collection, you can associate the current production website with a custom domain URL. When the staging website is complete, you can promote the staging website to be the primary website in the collection, which will then be available at the custom domain URL you created for the site collection without needing to perform a DNS change.

.. important::  Review the naming conventions in `Organizing your websites, collections, and groups </site-factory/manage/website/organize>`__ to ensure that your groups, site collections, and websites receive names that remain helpful as your platform expands.


7) Connect your platform to other Acquia services
-------------------------------------------------

As you develop on |acquia-product:edg|, review the steps necessary to integrate your websites with other Acquia products and services, such as |searchlink|_ and `Remote Administration </site-factory/manage/ra>`__.

.. |searchlink| replace:: \ |acquia-product:as|\ 
.. _searchlink: /site-factory/manage/search

8) Optimize performance
-----------------------

When developing multi-tenant websites in a platform architecture, it is important to ensure each website uses `both Drupal and Varnish caching </site-factory/manage/website/cache>`__ to improve performance. You can improve performance by `modifying caching
settings </site-factory/manage/website/cache/modify>`__ or by incorporating additional performance improvements, such as a `content delivery network </site-factory/manage/cdn>`__ (such as |edgelink|_).

.. |edgelink| replace:: \ |acquia-product:cf|\ 
.. _edgelink: /edge

9) Add and manage domains
-------------------------

You will need to create a Unified Communications Certificate (UCC) and `provide the certificate to Acquia </site-factory/manage/ssl>`__ as you `add custom domain names </site-factory/manage/website/domains>`__ for your websites. `Path-based domain names </site-factory/manage/website/domains/path>`__ are also available.


10) Familiarize yourself with extended features
-----------------------------------------------

|acquia-product:edg| offers `extended features </site-factory/extend>`__, such as the |apilink|_ and |hooks|_, which can help to simplify and automate your development process. Several `monitoring and logging services </site-factory/monitor>`__ are also available to help you troubleshoot and monitor your |acquia-product:edg| infrastructure and websites.


.. |apilink| replace:: \ |acquia-product:sfi|\ 
.. _apilink: /site-factory/extend/api

.. |hooks| replace:: \ |acquia-product:edg|\  hooks
.. _hooks: /site-factory/extend/hooks