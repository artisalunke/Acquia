.. include:: /common/global.rst

Using Site Factory Stacks
=========================

One of the primary strengths of |acquia-product:edg| is the ability to
centrally manage websites that have the same codebase and are in the
same region—but what if you have some websites that are different from
the rest?

If you have discrete groups of websites that share a set of basic,
fundamental differences between the groups, you can use *stacks* to
manage all of your websites in a single |acquia-product:edg|
subscription. Stacks use the same codebase on the same managed,
dedicated infrastructure for a group of websites. Examples where this
can be helpful include the following:

-  *Different Drupal core* – You may have some websites based on Drupal
   8, while maintaining and developing a different group of websites
   based on Drupal 7.
-  *Different installed modules* – You may have websites that have
   fundamentally different business purposes and therefore use a
   different set of custom and contributed Drupal modules.
-  *Different geographic region* – You may have groups of websites that
   are based in two or more different geographic regions.

With multiple stacks in |acquia-product:edg|, you can develop and
maintain these groups separately, while still managing the websites in
the same subscription and |acquia-product:sfi|. This provides you with
much more flexibility, along with unified governance, assembly, and
delivery.

Getting started with stacks
---------------------------

Each |acquia-product:edg| subscription starts with a single stack—to add
more stacks, contact your Acquia account manager. There is an additional
cost for each stack.

Acquia will provision your additional stack and then let you know when
it is ready for you to begin to develop the new stack's codebase and
websites.

Your first stack will be named **Stack 1**, with any subsequent stacks
being named **Stack 2**, **Stack 3**, and so forth. Although you cannot
rename a stack, you can `contact Acquia Support </support#contact>`__ to
request a description be added to an existing stack.

Websites managed as part of a stack share the same subdomain pattern,
such as ``*.customer.acsitefactory.com``. Each stack that is added in a
different region or to a different pair of load balancers will require a
unique subdomain pattern, such as
``*.us-east.customer.acsitefactory.com`` and
``*.eu-west.customer.acsitefactory.com``.

.. note:: 

   Any additional stacks will share the same |acquia-product:sfi| with your
   first stack. If your stacks need significantly different domain names,
   because domain names cannot be changed after they are provisioned, be
   sure to discuss this need with your Account Manager when requesting
   additional stacks.

Viewing your repository information
-----------------------------------

After provisioning is complete, you can sign in to the
|acquia-product:ac| interface to prepare for developing websites on your
new stack.

#. `Sign in to the Acquia Cloud interface </acquia-cloud/cloud-ui>`__ as a user 
   with |platformadmin|_ permissions.
#. Click the name of your application to select it.
#. Click **Application info** to display code repository information for
   your stack.


Working with stacks
-------------------

After adding additional stacks, you will still manage all of your
|acquia-product:edg| websites using the same |acquia-product:sfi|,
regardless of which stack they are part of. When you perform many
actions in the |acquia-product:sfi|, you will select which stack you
want to work on. For example, you can perform the following actions on a
per-stack basis:

-  `Creating sites and site
   groups </site-factory/manage/website/groups-create>`__
-  `Managing cron tasks using the management
   console </site-factory/manage/tasks/factory>`__
-  `Managing subscription usage </site-factory/manage/usage>`__
-  `Performing a production
   deployment </site-factory/workflow/deployments/steps>`__


Identify the stack for a website
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have more than one Site Factory stack, you can identify what
stack a website belongs to by performing the following steps:

#. Sign in to the |acquia-product:sfi| as a user with the |platformadmin|_ 
   or |sitebuilder|_ role.
#. Click **Sites**.
#. Scroll to or `filter for </site-factory/manage/website/filter>`__ the
   website with the stack that you want to identify.
#. Point to the **Information** icon to display a tooltip that contains
   the stack information.

   |Display a website's stack|

.. |Display a website's stack| image:: https://cdn2.webdamdb.com/1280_wwEW4Fo1wke9.jpg?1526475498
   :width: 289px
   :height: 285px

.. |platformadmin| replace:: *platform admin*
.. _platformadmin: /site-factory/users/admin/platform-admin

.. |sitebuilder| replace:: *site builder*
.. _sitebuilder: /site-factory/users/admin/site-builder