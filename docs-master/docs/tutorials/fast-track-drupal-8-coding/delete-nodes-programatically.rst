.. include:: /common/global.rst

Delete nodes programmatically
=============================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Create nodes programmatically
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/create-nodes-programmatically

.. |Next lesson| replace:: Unpublish nodes programmatically
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/unpublish-nodes-programmatically

Lesson Goal
-----------

.. container:: message-status

   Delete all nodes with certain criteria (for example, older than 30 days) 
   during a cron run.

Implementation Method
---------------------

.. list-table::
   :widths: 25 75
   :header-rows: 1 

   * - Drupal Version
     - Method
   * - Drupal 7
     - Use `hook_cron <https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_cron/7.x>`__ with node_delete_multiple_
   * - Drupal 8
     - Use `hook_cron <https://api.drupal.org/api/drupal/core%21core.api.php/function/hook_cron/8.5.x>`__ with |EntityStorageInterface|_


.. _node_delete_multiple: https://api.drupal.org/api/drupal/modules%21node%21node.module/function/node_delete_multiple/7.x


.. |EntityStorageInterface| replace:: EntityStorageInterface::delete
.. _EntityStorageInterface: https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Entity%21EntityStorageInterface.php/function/EntityStorageInterface%3A%3Adelete/8.5.x


Drupal 7 method
---------------

#. Add the following in ``lotus.module`` file:

   .. code-block:: php

      function lotus_cron() {
      $results = db_select('node', 'n')
                  ->fields('n', array('nid'))
                  ->condition('created', strtotime('-30 days'), '<=')
                  ->execute();
      foreach ($results as $result) {
        $nids[] = $result->nid;
      }
      if (!empty($nids)) {
        node_delete_multiple($nids);
      }
    }

#. Run cron.

Drupal 8 method
---------------

#. Add the following in ``lotus.module`` file:

   .. code-block:: php

      function lotus_cron() {
        $result = \Drupal::entityQuery("node")
          ->condition('created', strtotime('-30 days'), '<=')
          ->execute();

        $storage_handler = \Drupal::entityTypeManager()->getStorage("node");
        $entities = $storage_handler->loadMultiple($result);
        $storage_handler->delete($entities);
      }

#. Run cron.

Gist Link
---------

https://gist.github.com/gargsuchi/e2f492b0586900e152f0d86c951f398d

Resources
---------

-  hook_cron() – `Drupal
   8 <https://api.drupal.org/api/drupal/core%21core.api.php/function/hook_cron/8.5.x>`__
   \| `Drupal
   7 <https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_cron/7.x>`__
-  `node_delete_multiple() <https://api.drupal.org/api/drupal/modules%21node%21node.module/function/node_delete_multiple/7.x>`__
-  `EntityStorageInterface::delete <https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Entity%21EntityStorageInterface.php/function/EntityStorageInterface%3A%3Adelete/8.5.x>`__
