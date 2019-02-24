.. include:: /common/global.rst

Store data in a custom table
================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Define a custom config entity
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/define-custom-config-entity

.. |Next lesson| replace:: Update an existing custom schema
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/update-existing-custom-schema


Lesson Goal
-----------

.. container:: message-status

   Create a custom table to store data in the database.

Implementation Method
---------------------

Drupal 8 and Drupal 7 are identical when defining a custom table, the
only difference being the use of the Database service in Drupal 8.

.. note::  

   The ``db_insert``/``delete``/``update``/``query`` functions have been
   deprecated, and are now just wrappers until Drupal 9 is released.

+------------------+------------------------------------------+
| Drupal Version   | Method                                   |
+==================+==========================================+
| Drupal 7         | Use hook\_install() and hook\_schema()   |
+------------------+------------------------------------------+
| Drupal 8         | Use hook\_install() and hook\_schema()   |
+------------------+------------------------------------------+

Drupal 8 method
---------------

As with Drupal 7, the ``module.install`` needs at the minimum the
``hook_schema()`` to create your table. The following example also
implements the ``hook_install()``, which is called after the
``hook_schema()`` to ensure that the table is created in advance.

.. code-block:: php

    /**
    * Implements hook_install().
    *
    * Creates some default entries on this module custom table.
    *
    * @see hook_install()
    *
    * @ingroup lotus
    */
    function lotus_install() {
      $database = \Drupal::database();
      // Add a default entry.
      $fields = array(
        'name' => 'John',
        'surname' => 'Doe',
        'age' => 0,
      );
      $database->insert('lotus')
        ->fields($fields)
        ->execute();
      // Add another entry.
      $fields = array(
        'name' => 'John',
        'surname' => 'Roe',
        'age' => 100,
        'uid' => 1,
      );
      $database->insert('lotus')
        ->fields($fields)
        ->execute();
    }

    /**
    * Implements hook_schema().
    *
    * Defines the database tables used by this module.
    *
    * @see hook_schema()
    *
    * @ingroup lotus
    */
    function lotus_schema() {
      $schema['lotus'] = array(
        'description' => 'Stores example person entries for demonstration purposes.',
        'fields' => array(
          'pid' => array(
            'type' => 'serial',
            'not null' => TRUE,
            'description' => 'Primary Key: Unique person ID.',
          ),
          'uid' => array(
            'type' => 'int',
            'not null' => TRUE,
            'default' => 0,
            'description' => "Creator user's {users}.uid",
          ),
          'name' => array(
            'type' => 'varchar',
            'length' => 255,
            'not null' => TRUE,
            'default' => '',
            'description' => 'Name of the person.',
          ),
          'surname' => array(
            'type' => 'varchar',
            'length' => 255,
            'not null' => TRUE,
            'default' => '',
            'description' => 'Surname of the person.',
          ),
          'age' => array(
            'type' => 'int',
            'not null' => TRUE,
            'default' => 0,
            'size' => 'tiny',
            'description' => 'The age of the person in years.',
          ),
        ),
        'primary key' => array('pid'),
        'indexes' => array(
          'name' => array('name'),
          'surname' => array('surname'),
          'age' => array('age'),
        ),
      );

      return $schema;
    }

Dependency Injection
--------------------

The new method of using the Database system, and others, in Drupal 8:

https://www.drupal.org/docs/8/api/services-and-dependency-injection/services-and-dependency-injection-in-drupal-8

Dependency injection can only be done in a Class, which is why you see
the usage of the service container helper in the hook\_install example
above. The structure of your module should use Classes, Controllers, and
other similar patterns to utilize Dependency Injection to its fullest.

Gist Link
---------

https://gist.github.com/codexmas/733574476cb2e6ac770886e1c3075231

Resources
---------

-  `Drupal 7
   DBTNG <http://cgit.drupalcode.org/examples/tree/dbtng_example?h=7.x-1.x>`__
-  `Drupal 8
   DBTNG <http://cgit.drupalcode.org/examples/tree/dbtng_example>`__
