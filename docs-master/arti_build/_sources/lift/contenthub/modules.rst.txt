.. include:: /common/global.rst

Modules to use with |acquia-product:ch|
=======================================

.. toctree::
   :hidden:
   :glob:

   /lift/contenthub/modules/*

The following contributed modules can be used with |acquia-product:ch|,
either with no modifications or with some additional modules or patches.
Websites with complex or circular content models may experience
unexpected issues and should `contact Support </support#contact>`__ if
these issues occur.

Fully supported modules
-----------------------

The following modules work with |acquia-product:ch| without any
modifications:

-  `ECK (Entity Construction Kit) <https://www.drupal.org/project/eck>`__ versions 7.x-2.0-rc7 and greater
-  `Paragraphs <https://www.drupal.org/project/paragraphs>`__ version
   8.x - Supports both import and export

Modules requiring modifications
-------------------------------

The following modules work with |acquia-product:ch|, but require
additional modules or patches to do so:

-  `ECK (Entity Construction Kit) <https://www.drupal.org/project/eck>`__ version 8.x - Requires
   that you grant anonymous users the **View any [entity_type] entities** permission
-  `Field Collection <https://www.drupal.org/project/field_collection>`__
   versions earlier than 7.x-1.0-beta12 require the
   `patch <https://www.drupal.org/files/issues/1937866-field_collection-metadata-setter-6.patch>`__
   from `this issue <https://www.drupal.org/node/1937866>`__
-  `File Entity (fieldable files) <https://www.drupal.org/project/file_entity>`__ versions 7.x
   and 8.x - Files previously uploaded with this module cannot be
   syndicated until you run cron, which updates the ``bundle`` value for
   uploaded files.
-  Paragraphs_ version
   7.x - Requires `patch <https://www.drupal.org/node/2621866>`__
   Because |acquia-product:ch| supports only entities that have UUID,
   this module also requires the Paragraphs UUID module, which can be
   found in this sandbox_.
-  Shield_ version 8.x -
   Requires *both* a `patch <https://www.drupal.org/node/2822720#comment-12241648>`__ from
   `this issue on Drupal.org <https://www.drupal.org/node/2822720>`__
   and adding the following configuration line to ``settings.php``:

   ``$config['shield.settings']['paths'] = '/acquia-contenthub/*';``

-  `Workbench Moderation <https://www.drupal.org/project/workbench_moderation>`__
   versions 7.x-1.4 and greater - Requires `patch <https://www.drupal.org/node/2757963>`__

.. _Paragraphs: https://www.drupal.org/project/paragraphs
.. _sandbox: https://www.drupal.org/sandbox/tundrainteractive/2369177
.. _Shield: https://www.drupal.org/project/shield

Unsupported modules
-------------------

The following modules are unsupported and may cause problems when used
with |acquia-product:ch|:

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Drupal version
     - Unsupported modules
   * - Drupal 7 
     - 

       * `Brightcove Media <https://www.drupal.org/project/brightcove_media>`__ version 7.x-1.5
      
   * - Drupal 8
     - 

       * Drupal 8 Experimental_ modules |br|
         None of these modules are recommended for use. For example, the Content Moderation experimental module causes errors when used with Content Hub — use `Workbench Moderation <https://www.drupal.org/project/workbench_moderation>`__ instead.
       * `Field Collection <https://www.drupal.org/project/field_collection>`__ - Acquia recommends that you instead use the Paragraphs_ module.
       * `File Entity <https://www.drupal.org/project/file_entity>`__
       * Metatag_
       

.. _Experimental: https://www.drupal.org/core/experimental
.. _Paragraphs: https://www.drupal.org/project/paragraphs
.. _Metatag: https://www.drupal.org/project/metatag
