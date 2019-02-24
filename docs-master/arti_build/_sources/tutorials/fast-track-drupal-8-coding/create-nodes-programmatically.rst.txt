.. include:: /common/global.rst

Create nodes programmatically
==========================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Create a custom page with arguments
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/create-custom-page-arguments

.. |Next lesson| replace:: Delete nodes programmatically
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/delete-nodes-programatically


Lesson Goal
-----------

.. container:: message-status

  Create a custom function to create nodes programmatically.

Implementation Method
---------------------

+----------------+-----------------+
| Drupal Version | Method          |
+================+=================+
| Drupal 7       | custom function |
+----------------+-----------------+
| Drupal 8       | custom function |
+----------------+-----------------+

Drupal 7 method
---------------

The following code snippet can be used wherever there is a requirement to add a new node, being sure to replace ``<title>`` and ``<node>`` with their actual values.

.. code-block:: php

  global $user;
    $node = new stdClass();
    $node->title = "<title>";
    $node->type = "<node>";
    node_object_prepare($node); // Sets some defaults. Invokes hook_prepare() and hook_node_prepare().
    $node->language = LANGUAGE_NONE; // Or e.g. 'en' if locale is enabled
    $node->uid = $user->uid; 
    $node->status = 1; //(1 or 0): published or not
    $node->promote = 0; //(1 or 0): promoted to front page
    $node = node_submit($node); // Prepare node for saving
    node_save($node);
    drupal_set_message( "Node with nid " . $node->nid . " saved!\n");

Drupal 8 method
---------------

The following code snippet can be used wherever there is a requirement to add a new node, being sure to replace ``<node_type>``, ``<title>``, ``<body_text>``, and ``<uid>`` with their actual values.

.. code-block:: php

  use Drupal\node\Entity\Node;
  $node = Node::create(['type' => '<node_type>']);
  $node->set('title', '<title>');

  //Body can now be an array with a value and a format.
  //If body field exists.
  $body = [
  'value' => '<body_text>', 
  'format' => 'basic_html',
  ];
  $node->set('body', $body);
  $node->set('uid', <uid>);
  $node->status = 1;
  $node->enforceIsNew();
  $node->save();
  drupal_set_message( "Node with nid " . $node->id() . " saved!\n");

Gist Link
---------

https://gist.github.com/gargsuchi/863a556c732b6fab89c99f0bdaa4d2f1
