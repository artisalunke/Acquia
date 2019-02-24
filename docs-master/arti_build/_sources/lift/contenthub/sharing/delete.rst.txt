.. include:: /common/global.rst

Deleting content from subscribing sites
=======================================

Whenever content is unpublished or deleted from your publishing website,
you may want to also remove the content from your subscribing websites.
To delete this content, create a small custom Drupal module. For
information about creating custom modules in Drupal 8, see 
`Creating custom modules <https://www.drupal.org/docs/8/creating-custom-modules>`__ on
Drupal.org.

Content deletion code for Drupal 8
----------------------------------

When content is unpublished or deleted from your publishing website, it
is also removed from |acquia-product:ch|. Use the following Drupal
8-based code to instruct your subscribing websites to delete their
copies of the content:

.. code-block:: php

   function my_module_acquia_contenthub_process_webhook_alter($webhook) {
   if($webhook['status'] == 'successful' && $webhook['crud'] == 'delete') {
      $entity_repository = \Drupal::service('entity.repository');
      foreach($webhook['assets'] as $asset) {
         $entity = $entity_repository->loadEntityByUuid($asset['type'], $asset['uuid']);
         if($entity) {
         $entity->delete();
         }
      }
   }
   }

.. important:: 

   The ``DELETE`` webhook affects content in your subscribing websites,
   regardless of whether or not automatic updates are turned on. The
   entities will be deleted from your subscribing websites, even if they
   have been edited or changed.
