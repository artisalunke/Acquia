.. include:: /common/global.rst

Block users based on a certain criteria
========================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Update users programmatically
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/update-users-programmatically

.. |Next lesson| replace:: Define a custom config entity
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/define-custom-config-entity

Lesson Goal
-----------

.. container:: message-status

   Block users who have not signed in for the last six months.

Implementation Method
-------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Drupal Version
     - Method
   * - Drupal 7
     - Use hook_cron_ with user_user_operations_block()
   * - Drupal 8
     - Use `hook_cron <https://api.drupal.org/api/drupal/core%21core.api.php/function/hook_cron/8.5.x>`__ with `User::block <https://api.drupal.org/api/drupal/core%21modules%21user%21src%21Entity%21User.php/function/User%3A%3Ablock>`__

.. _hook_cron: https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_cron/7.x


Drupal 7 method
---------------

#. Add the following code to the ``lotus.module`` file:

   .. code-block:: php

      function lotus_cron() {
        $results = db_select('users', 'u')
                    ->fields('u', array('uid'))
                    ->condition('login', strtotime('-6 months'), '<=')
                    ->execute();
        foreach ($results as $result) {
          $uids[] = $result->uid;
        }
        if (!empty($uids)) {
          $users = user_load_multiple($uids);
          user_user_operations_block($users);
        }
    }

#. Run cron.

Drupal 8 method
---------------

#. Add the following code to the ``lotus.module`` file:

   .. code-block:: php

      function lotus_cron() {
        $result = \Drupal::entityQuery("user")
          ->condition('login', strtotime('-6 months'), '<=')
          ->execute();

        $storage_handler = \Drupal::entityTypeManager()->getStorage("user");

        foreach ($result AS $user) {
          $entity = $storage_handler->load($user);
          $entity->block();
          $storage_handler->save($entity);
        }
      }

#. Run cron.

Gist Link
---------

https://gist.github.com/gargsuchi/7c38515d6826532ec9efbde1865d8061

Resources
---------

`User::block <https://api.drupal.org/api/drupal/core%21modules%21user%21src%21Entity%21User.php/function/User%3A%3Ablock>`__
