.. include:: /common/global.rst

Unpublish nodes programmatically
================================

| **Fast Track to Drupal 8 Coding** – *`Back to
  Intro </tutorials/fast-track-drupal-8-coding>`__*
| *Previous lesson – `Delete nodes
  programmatically </tutorials/fast-track-drupal-8-coding/delete-nodes-programatically>`__*  |  *Next
  lesson – `Update nodes
  programmatically </tutorials/fast-track-drupal-8-coding/update-nodes-programmatically>`__*

Lesson Goal
-----------

Unpublish all nodes that match certain criteria (for example, older than
30 days) during a cron run.

Implementation Method
---------------------

+-----------------------------------+-----------------------------------+
| Drupal Version                    | Method                            |
+===================================+===================================+
| Drupal 7                          | Use                               |
|                                   | `hook_cron <https://api.drupal.or |
|                                   | g/api/drupal/modules%21system%21s |
|                                   | ystem.api.php/function/hook_cron/ |
|                                   | 7.x>`__                           |
|                                   | with                              |
|                                   | `node_save <https://api.drupal.or |
|                                   | g/api/drupal/modules%21node%21nod |
|                                   | e.module/function/node_save/7.x>` |
|                                   | __                                |
+-----------------------------------+-----------------------------------+
| Drupal 8                          | Use                               |
|                                   | `hook_cron <https://api.drupal.or |
|                                   | g/api/drupal/core%21core.api.php/ |
|                                   | function/hook_cron/8.5.x>`__      |
|                                   | with Node::save()                 |
+-----------------------------------+-----------------------------------+

Drupal 7 method
---------------

Implement the following functions in ``lotus.module``:

#. Implement a custom function that loads the set of nodes you want to
   unpublish. The following example will load all nodes that are more
   than 30 days old:

   ``function lotus_load_old_nodes() {   $query = new EntityFieldQuery();   $query->entityCondition('entity_type', 'node')     ->propertyCondition('created', strtotime('-30 days'), '<');   $result = $query->execute();   if (!$result) {     // Query failed. @todo implement error handling as needed     return array();   }   return node_load_multiple(array_keys($result['node'])); }``

#. In an implementation of ``hook_cron()``, call the previous function
   and operate on the returned nodes to unpublish them, as follows:

   ``function lotus_cron() {   $old_nodes = lotus_load_old_nodes();   foreach ($old_nodes as $node) {     $node->status = NODE_NOT_PUBLISHED;     node_save($node);   } }``

After this is complete and the Lotus module is enabled, every cron run
will result in the targeted nodes being unpublished.

Drupal 8 method
---------------

The strategy in Drupal 8 is similar to Drupal 7, but with some
differences in the specifics of the code. Drupal 8 introduces the
concept of Service classes, which capture application-wide behaviors
(including database access, sending emails, and translating text) in PHP
classes instead of global functions. Our lookup function is a good
candidate for this kind of implementation.

#. In ``lotus/src/OldNodesService.php``, implement the service class as
   follows:

   ``namespace Drupal\lotus;  use Drupal\Core\Entity\EntityTypeManager;  class OldNodesService {    protected $entityTypeManager;    public function __construct(EntityTypeManager $entity_type_manager) {     $this->entityTypeManager = $entity_type_manager;   }    public function load() {     $storage = $this->entityTypeManager->getStorage('node');     $query = $storage->getQuery()       ->condition('created', strtotime('-30 days'), '<');     $nids = $query->execute();     return $storage->loadMultiple($nids);   }  }``

#. Register your service and describe its dependencies (in this case, an
   instance of the EntityTypeManager service) in
   ``lotus/lotus.services.yml``:

   ``services:   lotus.old_nodes:     class: \Drupal\lotus\OldNodesService     arguments: ["@entity_type.manager"]``

#. Implement ``hook_cron()`` similar to how you did with Drupal 7:

   ``function lotus_cron() {   $old_nodes = \Drupal::service('lotus.old_nodes')->load();   foreach ($old_nodes as $node) {     $node->setPublished(false);     $node->save();   } }``

Gist Links
----------

-  ``OldNodesService.php`` –
   https://gist.github.com/jazzslider/baa52121da0dcbad1ea16a2f7359b8f7
-  ``lotus.services.yml`` –
   https://gist.github.com/jazzslider/0a00f79c17f5f746d5053a2f172bff56
-  ``lotus.module`` –
   https://gist.github.com/jazzslider/e7f2d72ae32b959e245c27fe66016393
