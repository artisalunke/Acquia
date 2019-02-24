.. include:: /common/global.rst

Create terms programmatically
=============================

| **Fast Track to Drupal 8 Coding** – *`Back to
  Intro </tutorials/fast-track-drupal-8-coding>`__*
| *Previous lesson – `Update nodes
  programmatically </tutorials/fast-track-drupal-8-coding/update-nodes-programmatically>`__*  |  *Next
  lesson – `Attach terms to another entity
  programmatically </tutorials/fast-track-drupal-8-coding/attach-terms-another-entity-programmatically>`__*

Lesson Goal
-----------

This task demonstrates how to create taxonomy terms in code. Drupal has
a method specifically for this action.

Implementation Method
---------------------

+-----------------------------------+-----------------------------------+
| Drupal Version                    | Method                            |
+===================================+===================================+
| Drupal 7                          | Use                               |
|                                   | `taxonomy_term_save() <https://ap |
|                                   | i.drupal.org/api/drupal/modules!t |
|                                   | axonomy!taxonomy.module/function/ |
|                                   | taxonomy_term_save/7.x>`__        |
|                                   | to create and then save the term  |
|                                   | to the specified vocabulary       |
+-----------------------------------+-----------------------------------+
| Drupal 8                          | Use                               |
|                                   | `\\Drupal\taxonomy\Entity\Term <h |
|                                   | ttps://api.drupal.org/api/drupal/ |
|                                   | core%21modules%21taxonomy%21src%2 |
|                                   | 1Entity%21Term.php/class/Term/8.5 |
|                                   | .x>`__                            |
|                                   | to create and then save the term  |
|                                   | into the specified vocabulary     |
+-----------------------------------+-----------------------------------+

Drupal 7 method
---------------

Add the following code to the ``lotus.module`` file:

``function lotus_term_create() {   $new_term = new stdClass();   $new_term->name = ‘Your term name’;      // Make sure you know the vocabulary ID.   // Look at lotus_get_vocabulary_id_by_name()   // for an example.   $vid = lotus_get_vocabulary_id_by_name(‘Vocab name’);   $new_term->vid = $vid;   taxonomy_term_save(($new_term);  function lotus_get_vocabulary_id_by_name($vocabulary_name) {   $vocabs = taxonomy_get_vocabularies(NULL);   foreach ($vocabs as $vocab_object) {     if ($vocab_object->name == $vocabulary_name) {              $vid = $vocab_object->vid;       return $vid;     }   }   return NULL; }``

Drupal 8 method
---------------

Add the following code inside a function where you want to create new
terms:

``$new_term = \Drupal\taxonomy\Entity\Term::create([           'vid' => 'example_vocabulary_machine_name',           'name' => 'Example term name',     ]);  $new_term->enforceIsNew(); $new_term->save();``

Gist Link
---------

https://gist.github.com/dreambubbler/f671351e102e6c829b13dbcef37fad62

Resources
---------

`\\Drupal\taxonomy\Entity\Term <https://api.drupal.org/api/drupal/core%21modules%21taxonomy%21src%21Entity%21Term.php/class/Term/8.5.x>`__
