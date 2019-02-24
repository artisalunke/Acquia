.. include:: /common/global.rst

Managing product and SKU display
================================

.. container:: internal-navigation

  **Products & SKUs**

  * :doc:`Attributes </commerce/categories-products/sku-attributes>`
  * Displays

The fields displayed by SKUs are controlled by display modes on the SKU
Types. The SKU field is added to the page with a custom display
formatter that will allow you to choose which view mode is used to
render the SKU entity which can be controlled per view mode of the
product content entity.

To update the display for a SKU type, complete the following steps:

#. Sign in to your website as an administrator.
#. Navigate to **Commerce > Configuration > SKU Settings**
   (``[site_URL]/admin/commerce/config/sku``).
#. Find your **SKU type**, and then click its **Edit** link.
#. Click **Manage display**.
#. Update the display as you would a content type, and then click
   **Save**.
#. Navigate to **Structure > Content Types**.
#. Next to **Product**, select **Manage display** from the menu.
#. Ensure that the SKU field is being rendered with the correct **view
   mode**.
#. If you made any changes, click **Save**.

Displaying content
------------------

You can use the following methods to display your content:

-  | *Preprocess functions*
   | The reference SKU entity can be accessed using the first value from
     ``field_sku``. The SKU field has an override for the get method and
     when it is called with ‘entity’ will return the referenced entity.
     Once you have access to the referenced SKU entity you can then call
     entity view builders to render the entity or specific fields. You
     cannot access the SKU entity directly in Twig from ``field_skus``
     so we assign the SKU object directly to a property on the variables
     render array.

    .. code-block:: php

       $product = $variables[‘node’];
       /** @var \Drupal\acq_sku\Entity\SKU $sku */ 
       $sku = $product->get('field_skus')->first()->get('entity')->getValue(); 
       $variables['final_price'] = $sku->get('final_price')->getValue(); 
       $variables['sku'] = $sku;  
       $viewBuilder = \Drupal::entityTypeManager()->getViewBuilder('acq_sku'); 
       $field = $sku->get('attr_color'); $build['color'] = $viewBuilder->viewField($field);

-  | *Twig templates*
   | Twig requires that the template file be preprocessed to provide it
     complete access over the referenced entity. This will need to be
     assigned to a render variable as previously described.

     .. code-block:: none

        {{ sku.final_price.value }} 
        {{ sku.attr_my_custom_attribute.value }}

Price fields
------------

The following price fields are stored in the SKU entity:

- ``Price`` *(was price)* – The initial price of the product
- ``Special price`` *(now price)* – The updated price
- ``Final price`` – The now price with all discounts from catalog rules
   applied

Media fields and files
----------------------

The SKU contains raw data in the Media field. You can process the
field's data by using a custom module to load the images as a Drupal
image, and then display them on product pages. To do this, complete the
following steps:

#. Create a node preprocess function.
   Using a ``hook_preprocess_node`` function, you can create an image
   element for the product node render array.
#. Load the SKU.
   The SKU is stored as a string in a multi-value field, but only the
   first value will be used. The ``SKU:loadFromSku()``\ method can be
   used to load the SKU entity.
#. Load the media information.
   The SKU entity has a ``getMedia()``\ method that will process the raw
   media information, create a file entity if needed with the downloaded
   image, and then return an array of media information. Each element of
   this array has a file key with a file entity.
#. Create a render array element.
   With the file entity, you can create a render array element.
   ``#theme`` with value ``image_style`` is a simple way to do this. You
   will provide a ``#style_name`` that refers to an image style
   configured for the website and the image URI which can be obtained
   with the file entity ``getFileUri()`` method.
#. Configure output with Twig templates.
   You can then handle the new element in node template files. For
   example, you can access a ``$build['image']`` variable in the
   preprocess function as ``{{ elements.image }}`` in a twig template.
#. Create and modify different view modes.
   The preprocess function will include a variable for ``$view_mode``
   and you can use this to format the image differently depending on the
   node view mode. For example, include a thumbnail on a teaser of the
   product.

Refer to the following code for an example of adding media:

.. code-block:: php

   <?php

   use Drupal\acq_sku\Entity\SKU;
   use Drupal\Core\Entity\EntityInterface;
   use Drupal\Core\Entity\Display\EntityViewDisplayInterface;
   use Drupal\file\Entity\File;

   /**
    * Demonstrate adding images to product pages.
    */
   function acq_example_node_view(array &$build, EntityInterface $entity, EntityViewDisplayInterface $display, $view_mode) {
     if ($entity->bundle() == 'acq_product') {
       // The first SKU entry is the only one used at this time.
       $sku_id = $entity->get('field_skus')->first()->getString();
       $sku = SKU::loadFromSku($sku_id);

       // Add the first SKUs first image to the render array.
       if ($sku instanceof SKU) {
         $build['image'] = [];

         // Process the media information and create file entity as needed.
         $sku_media = $sku->getMedia();

         /**
        * There may be multiple images. We are getting just the first here.
          *
          * @var File $sku_image_file
          */
         if (isset($sku_media[1]['file'])) {
           $sku_image_file = $sku_media[1]['file'];
         }

         /**
          * Create a render array.
          *
          * The image will be available as {{ elements.image }} in templates.
          */
         $build['image'] = [
           '#theme' => 'image_style',
           '#style_name' => 'large',
           '#uri' => $sku_image_file->getFileUri(),
         ];
       }
     }
   }
