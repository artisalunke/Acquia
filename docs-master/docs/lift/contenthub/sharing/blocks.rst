.. include:: /common/global.rst

Using blocks with |acquia-product:ch|
=====================================

Drupal uses blocks for specific layout needs, which |acquia-product:ch|
can take advantage of for syndicating content.


Enabling View mode for custom blocks
------------------------------------

Custom blocks do not, by default, have a View mode available to
|acquia-product:ch|. To enable one, complete the following steps:

#. Sign in to your website as an administrator.
#. In the admin menu, click **Structure**, and then click the **Block
   layout** link.
#. Click the **Custom block library** tab.
#. Find the custom block that you want to share, and in the
   **Operations** column, click **Manage display** from the custom
   block's menu of operations.
#. Click **Custom display settings**, and then select the **Full** check
   box and any other view modes that you may want to use.
#. Click **Save**.

The selected view modes for your block should now be visible on the
**Entity Configuration** page.


Theming a custom block
----------------------

By default, Drupal 8 does not provide a custom theme hook for block
entities. If you want to share content using a custom theme template,
|acquia-product:ch| provides a hook which can be used to style blocks as
they are imported into |acquia-product:ch|.

.. note::  

   Acquia recommends that the |acquia-product:ch| theme template remain
   identical to the block's original theme template to maintain styling
   consistency.

The following steps outline how to apply a custom theme template to
block entities shared using |acquia-product:ch|:

#. Copy the ``/core/modules/block/templates/block.html.twig`` file into
   the ``templates/block/`` folder inside the website's default theme.
#. Rename the copied file to
   ``block-block-content-acquia-contenthub.html.twig``
#. Rebuild the website cache.
#. Use the following Drush command to enable block content view builder
   for block rendering, which allows |acquia-product:ch| to use the new
   theme template that you created:

   .. code-block:: none
   
      drush cset acquia_contenthub.entity_config use_block_content_view_builder true

#. To disable block content view builder and stop |acquia-product:ch|
   from using the theme template, use the following command:

   .. code-block:: none
   
      drush cset acquia_contenthub.entity_config use_block_content_view_builder 0
