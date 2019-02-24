.. include:: /common/global.rst

Attach terms to another entity programmatically
===============================================

| **Fast Track to Drupal 8 Coding** – *`Back to
  Intro </tutorials/fast-track-drupal-8-coding>`__*
| *Previous lesson – `Create terms
  programmatically </tutorials/fast-track-drupal-8-coding/create-terms-programmatically>`__*  |  *Next
  lesson – `Create a custom
  block </tutorials/fast-track-drupal-8-coding/create-custom-block>`__*

Lesson Goal
-----------

Attach existing terms to entities with a taxonomy term reference field.

Implementation Method
---------------------

Drupal Version

Method

Drupal 7

#. Load the node or user object.
#. Assign a term ID to the appropriate field.
#. Save the node or user object.

Drupal 8

`FieldableEntityInterface::set() <https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Entity%21FieldableEntityInterface.php/function/FieldableEntityInterface%3A%3Aset/8.5.x>`__

In Drupal 7 you can only attach term reference fields to Content Types
and Users. In Drupal 8 you can attach term reference fields to any
entity type.

Drupal 7 method
---------------

Place the following code in the ``lotus.module`` file:

``function lotus_attach_term() {   $node = node_load($nid);  // $nid is the node id of the node to update.    // field_example_term_reference: is the field name of a term reference field attached to your content type.   // 4: is the term ID you want to assign to the node.   $node->field_example_term_reference[$node->language][][‘tid’] = 4;   node_save($node); // Save the changes. }``

Drupal 8 method
---------------

Place the following code in the ``lotus.module`` file:

``set('field_example_name', $tid); $node->save(); // End of Example 1 />  // Example 2: attaching multiple terms $node2 = \Drupal\node\Entity\Node::load($nid2);  // To attach multiple terms, the term IDs must be in an array. $multiple_tids = array(1, 2, 3); // Each is Term ID of an existing term. $node2->set('field_example_name', $multiple_tids);  // Note that field_example_name must allow multiple terms. $node2->save(); // End of Example 2 />``

Gist Link
---------

https://gist.github.com/dreambubbler/a89b9ac5ff34facd60fc7d4c8afecc9b

Resources
---------

`FieldableEntityInterface::set() <https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Entity%21FieldableEntityInterface.php/function/FieldableEntityInterface%3A%3Aset/8.5.x>`__
