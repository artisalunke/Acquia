.. include:: /common/global.rst

Create a custom block
=====================

| **Fast Track to Drupal 8 Coding** – *`Back to
  Intro </tutorials/fast-track-drupal-8-coding>`__*
| *Previous lesson – `Attach terms to another entity
  programmatically </tutorials/fast-track-drupal-8-coding/attach-terms-another-entity-programmatically>`__*  |  *Next
  lesson – `Alter an existing simple
  form </tutorials/fast-track-drupal-8-coding/alter-existing-simple-form>`__*

Lesson Goal
-----------

Create a custom block named ``welcome`` that displays the following
content: 'Welcome to my site'

Implementation Method
---------------------

+-----------------------------------+-----------------------------------+
| Drupal Version                    | Method                            |
+===================================+===================================+
| Drupal 7                          | Use                               |
|                                   | `hook_block_info() <https://api.d |
|                                   | rupal.org/api/drupal/modules%21bl |
|                                   | ock%21block.api.php/function/hook |
|                                   | _block_info/7.x>`__               |
|                                   | to declare a block and            |
|                                   | `hook_block_view() <https://api.d |
|                                   | rupal.org/api/drupal/modules%21bl |
|                                   | ock%21block.api.php/function/hook |
|                                   | _block_view/7.x>`__               |
|                                   | to define block content.          |
+-----------------------------------+-----------------------------------+
| Drupal 8                          | Use Plugins API to declare a      |
|                                   | block and add a class to define   |
|                                   | the content.                      |
+-----------------------------------+-----------------------------------+

Drupal 7 method
---------------

Add the following code to the ``lotus.module`` file:

``/** * Implements hook_block_info() **/  function lotus_block_info() {   $blocks['welcome'] = array(     'info' => t('Welcome'),   );    return $blocks; }   }  /**  * Implements hook_block_view() **/ function lotus_block_view($delta = '') {    $block = array();    switch ($delta) {     case 'welcome':       $block['subject'] = t('Welcome');       $block['content'] = array( $block['content'] = 'Welcome to Lotus website!',       );       break;   }   return $block; }``

Drupal 8 method
---------------

Add the following code to the ``src/Plugin/Block/HelloBlock.php`` file:

``$this->t('Welcome to Lotus website!'),     );   } }``

Gist Link
---------

https://gist.github.com/prasadshir/0bbba050e9f5cd16591822f9d143702c
