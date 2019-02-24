.. include:: /common/global.rst

Modifying CDF and content with hooks
====================================

If a subscribing website in your |acquia-product:ch| subscription
contains entities with a different data structure than your publishing
website, you may need to customize your shared content as it moves in
and out of your publishing website. |acquia-product:ch| includes hooks
that allow you to customize shared content before publication on a
subscribing website, or to strip out customizations before submitting
content back to the publishing website.

You can use the available hooks to improve content syndication by
modifying either your website's Common Data Format (CDF) or your
entity's data structure to match your subscribing or publishing
website's individual needs.

Modifying the Common Data Format (CDF)
--------------------------------------

Select from the following hooks, based on your installed Drupal version,
to modify your website's CDF in these methods:

-  Modify the CDF before it is sent to the publishing website during the
   normalization process
   This hook's changes affect the publishing website's entity, but the
   subscribing website's Drupal entity will remain unchanged.

   -  *Drupal 8* - ``hook_acquia_contenthub_cdf_from_drupal_alter``
   -  *Drupal 7* - ``hook_content_hub_connector_cdf_from_drupal_alter``

-  Modify the CDF *fetched from the publishing website* before being
   converted to a Drupal entity during the denormalization process
   This hook's changes affect the subscribing website's entity, but the
   publishing website's entity will remain unchanged.

   -  *Drupal 8* - ``hook_acquia_contenthub_cdf_from_hub_alter``
   -  *Drupal 7* - ``hook_content_hub_connector_cdf_from_hub_alter``

Modifying the Drupal entity
---------------------------

Select from the following hooks, based on your installed Drupal version,
to modify your entity's data structure in these available methods:

-  Modify the Drupal entity *after* its conversion from the CDF that is
   fetched from the publishing website during the denormalization
   process
   This hook's changes affect the subscribing website's entity imported
   from the publishing website, but the publishing website's entity will
   remain unchanged.

   -  *Drupal 8* - ``hook_acquia_contenthub_drupal_from_cdf_alter``
   -  *Drupal 7* - ``hook_content_hub_connector_drupal_from_cdf_alter``

-  Add fields to the Drupal entity *before* it is converted to a CDF
   during the export process
   This hook's changes affect the publishing website's entity, but the
   subscribing website's Drupal entity will remain unchanged.

   -  *Drupal 8* - ``hook_acquia_contenthub_drupal_to_cdf_alter``
   -  *Drupal 7* - ``hook_content_hub_connector_drupal_to_cdf_alter``

Examples
--------

Code examples for these hooks can be found in the module's API file,
depending on the version of Drupal in use:

-  *Drupal 8* - ``acquia_contenthub.api.php``
-  *Drupal 7* - ``content_hub_connector.api.php``
