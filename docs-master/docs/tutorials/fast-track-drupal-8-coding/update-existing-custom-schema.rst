.. include:: /common/global.rst

Update an existing custom schema
================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Store data in a custom table
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/store-data-custom-table

.. |Next lesson| replace:: Pre-process output provided by other modules
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/pre-process-output-provided-other-modules


Lesson Goal
-----------

.. container:: message-status

   Update a custom module's existing schema.

Implementation Method
---------------------

Both Drupal 7 and 8 use the ``hook_update_N()`` naming of functions
within a ``module.install``.

Drupal 8 does have an additional option called
``hook_post_update_NAME()`` for content updates that need the full suite
of available APIs.

+------------------+--------------------------------------------------+
| Drupal Version   | Method                                           |
+==================+==================================================+
| Drupal 7         | hook\_update\_N()                                |
+------------------+--------------------------------------------------+
| Drupal 8         | hook\_update\_N() and hook\_post\_update\_NAME   |
+------------------+--------------------------------------------------+

Drupal 7 method
---------------

Adding a new column and an index for it to your custom schema:

.. code-block:: php

    function mymodule_update_7100() {
      $table = 'lotus';
      $spec = array(
        'type' => 'varchar',
        'description' => "New Col",
        'length' => 20,
        'not null' => FALSE,
      ); 
      db_add_field($table, 'newcol', $spec);
      db_add_index($table, 'newcol', array('newcol'))
    }

Adding a new database table:

.. code-block:: php

    function mymodule_update_7101() {
      $schema['lotustwo'] = array(
        // table definition left out for brevity
      );
      db_create_table('lotustwo', $schema['lotustwo']);
    }

Drupal 8 method
---------------

Adding a new column and an index for it to your custom schema:

.. code-block:: php

    use Drupal\Core\Database\Database;
    function lotus_update_8001(&amp;$sandbox) {
      $spec = [
        'type' => 'varchar',
        'description' => "New Col",
        'length' => 20,
        'not null' => FALSE,
      ]; 
      $schema = Database::getConnection()->schema();
      $schema->addField('lotus', 'newcol', $spec);
      $schema->addIndex('lotus', ['newcol']);
    }

Adding a new database table:

.. code-block:: php

    function lotus_update_8002(&amp;$sandbox) {
      $spec = array(
        'description' => 'My description',
        'fields' => array(
          'myfield1' => array(
            'description' => 'Myfield1 description.',
            'type' => 'varchar',
            'length' => 255,
            'not null' => TRUE,
            'default' => '',
          ),
          'myfield2' => array(
            'description' => 'Myfield2 description',
            'type' => 'text',
            'not null' => TRUE,
          ),
        ),
        'primary key' => array('myfield1'),
      ); 
    $schema = Database::getConnection()->schema();
    $schema->createTable('lotustwo', $spec);
    }

Changing the title of a specific node after all ``hook_update_N()``
calls are done:

.. code-block:: php

    function lotus_post_update_change_title_of_node() {
      $node = \Drupal::entityManager()->loadEntityByUuid('FC0C01C6-B758-450D-A1BC-93D91D7786CB');
      $node->setTitle('hello world');
      $node->save();
      return t('Node successfully updated.');
    }

Gist Link
---------

https://gist.github.com/codexmas/1709926b89b3461f7692a64ec6f51ebf

Resources
---------

-  *Drupal 7*

   -  https://www.drupal.org/docs/7/api/schema-api/updating-tables-hook_update_n-functions

-  *Drupal 8*

   -  https://www.drupal.org/docs/8/api/update-api/introduction-to-update-api-for-drupal-8
   -  https://www.drupal.org/node/2535384
