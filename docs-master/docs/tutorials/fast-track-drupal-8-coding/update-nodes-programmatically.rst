.. include:: /common/global.rst

Update nodes programmatically
=============================

| **Fast Track to Drupal 8 Coding** – *`Back to
  Intro </tutorials/fast-track-drupal-8-coding>`__*
| *Previous lesson – `Unpublish nodes
  programmatically </tutorials/fast-track-drupal-8-coding/unpublish-nodes-programmatically>`__*  |  *Next
  lesson – `Create terms
  programmatically </tutorials/fast-track-drupal-8-coding/create-terms-programmatically>`__*

Lesson Goal
-----------

A website has a user role named *Moderated*, and when this role is added
to a user, all the nodes created by the user should be updated by
appending 'MODERATED USER' to the title of the nodes.

Implementation Method
---------------------

+----------------+---------------------------+
| Drupal Version | Method                    |
+================+===========================+
| Drupal 7       | node_load(), node_save()  |
+----------------+---------------------------+
| Drupal 8       | hook_ENTITY_TYPE_update() |
|                | $node->set()              |
+----------------+---------------------------+

Drupal 7 method
---------------

Add the following code to the ``lotus.module`` file:

``/**  * Implements hook_user_update().  * If a user has a Role named 'moderated',  * append the words 'MODERATED USER' to titles of  * all the nodes authored by the user  */  function lotus_user_update(&$edit, $account, $category){   $uid = $account->uid;   $role = user_has_role('moderated', $account);    if($role){     $query = new EntityFieldQuery();     $query = $query           ->entityCondition('entity_type', 'node')           ->propertyCondition('status', 1)           ->propertyCondition('uid', $uid);     $nodes = $query->execute();      foreach($nodes as $node) {       $node = node_load($node);       $old_title = $node->title;       if(strpos($old_title,'(MODERATED USER)') == FALSE) {         $node->title =  $old_title . " (MODERATED USER)";         $node->save();       }     }     drupal_set_message('All nodes of the user updated');   } }``

Drupal 8 method
---------------

#. Create a role named *Moderated* on your website (machine name:
   ``moderated``).
#. Add a user.
#. Create some nodes and set the Author for the nodes as the newly added
   user.
#. In the ``lotus.module`` file, add the following code:

   ``use Drupal\node\Entity\Node; use Drupal\user\Entity\User;  /**  * Implements hook_ENTITY_TYPE_update().  * If a user has a Role named 'moderated',  * append the words 'MODERATED USER' to titles of  * all the nodes authored by the user  */  function lotus_user_update(\Drupal\Core\Entity\EntityInterface $entity){   $user = User::load($entity->id());   $role = $user->hasRole('moderated');   if($role){     $query = \Drupal::entityQuery('node')       ->condition('uid', $user->id());     $nids = $query->execute();     $nodes = Node::loadMultiple($nids);     foreach($nodes as $node) {       $old_title = $node->title->value;       if(strpos($old_title,'(MODERATED USER)') == FALSE) {         $node->set("title",  $old_title . " (MODERATED USER)");         $node->save();        }     }     drupal_set_message('All nodes of the user updated');   } }``

#. Enable the Lotus module (if its already enabled, do a Cache Rebuild).
#. In the admin menu, click **People**, and then edit the user to add
   the *Moderated* role to the user account.

All of the nodes created by the user should now be appended with the
words ``MODERATED USER``.

Gist Link
---------

https://gist.github.com/prasadshir/656bbc57269a4a24bbd24d6015e55d92

Resources
---------

`hook_ENTITY_TYPE_update() <https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Entity%21entity.api.php/function/hook_ENTITY_TYPE_update/8.5.x%C2%A0>`__
