.. include:: /common/global.rst

SKU attributes, product options, and product categories
=======================================================


.. container:: internal-navigation

  **Products & SKUs**

  * Attributes
  * :doc:`Displays </commerce/categories-products/displays>`

The SKU entity contains a multivalue field for attributes
(``field_attributes``) from your commerce platform. These fields contain
attribute names to attribute values in a ``key:value`` pair arrangement.
The value is typically the untranslated version of an attribute from the
commerce platform.

For example, ``Color`` is an attribute; in Drupal it will appear as
``color: 444``, where ``444`` is the attribute ID for the color value.

.. note::

  - By default, the attributes field is hidden from display by the user interface. To add the ``field_attributes`` field to the form display, edit the configuration for the SKU types.
  - Disabled SKUs are not stored in the system.

**Product Options** and **Product Categories** have special handling applied. Additional fields are added to the SKU that reference Drupal taxonomy terms in **Product Option** and **Product Category** vocabularies.

Special handling for other SKU attributes
-----------------------------------------

If you want to apply similar special handling to attributes, you can do
so.

Although all attributes will be synchronised to Drupal in the
``field_attributes`` field, you may need to expose some attributes
directly as fields. The main reason for doing this is to index actual
values to provide faceted search.

Fields can be added by extending the SKU entity definition in a custom
module by completing the following steps:

#. Add the new schema definitions to the `default configuration of your
   custom module <https://www.drupal.org/docs/8/creating-custom-modules/include-default-configuration-in-your-drupal-8-module>`__.
#. Provide an install hook to attach the definitions to the SKU entity.
#. Provide an entity presave hook to ensure that the fields get
   populated during the import.

Example
~~~~~~~

As an example, refer to the following example to create a color special
attribute.

#. | *Create a base fields configuration file (the schema).*
   | Here is an example that adds a color attribute to the SKU. This
     should be saved as ``my_module.sku_base_fields.yml``. This is how
     we will access the configuration in the next steps).

   .. code-block:: none

     fields:   
       color:    
        parent: 'attributes'    
        label: 'Color'    
        description: 'Color attribute for the product.'    
        cardinality: -1    
        type: 'attribute'    
        configurable: 0    
        visible_view: 0    
        visible_form: 1

   Ensure that base field definitions are correct before adding them.
   All properties are required.

#. | *Create an install hook.*
   | The install hook is required to call the
     ``acq_sku_add_base_fields`` function with the configuration values
     that are stored in the configuration files mentioned in the
     previous step. An example install hook can appear similar to the
     following:

    .. code-block:: php

      function my_module_install() {
        $fields = \Drupal::config('my_module.sku_base_fields')->get('fields');   
        acq_sku_add_base_fields($fields);
       }

#. | *Create a presave hook to update your fields.*
   | If everything has been done correctly, the new fields will be
     displayed when editing a SKU entity, and any new products that are
     synced will update the fields based on their attributes. For simple
     attributes, the base commerce module suite will update any values
     that you have added to the SKU entity.
   | You can define an entity presave hook to handle more complex
     attributes (for example, configurable attributes). This gives you
     complete control of the entity before it is saved, and you will
     have access to the response from the |acquia-product:ccs|. To
     continue with the example, the hook implementation should appear
     similar to the following:

    .. code-block:: php

      function my_module_acq_sku_presave(SKUInterface $sku) {
         $configurable_attributes_data = unserialize($sku->get('field_configurable_attributes')->getString());
            $fields = \Drupal::config('my_modules.sku_base_fields')->get('fields');
            $opts = \Drupal::service('acq_sku.product_options_manager');    foreach ($fields as $field_key => $definition) {     $field_key = "attr_$field_key";
            foreach ($configurable_attributes_data as $attribute_data) {
                  if ($attribute_data['code'] !== $key) {
                      continue;
                   }
                   foreach ($attribute_data['values'] as $index => $value) {
                      $sku->get($field_key)->set($index, $value['value_id']);
                      if ($term = $opts>loadProductOptionByOptionId($key, $value['value_id'],
                          $sku->language()->getId())) {
                            $sku->get($field_key)->set($index, $term->getName());
                            }
                        }
                      }  
                } 
              }

You should now have custom attributes added to the SKU object and be
able to use them when displaying information or creating product
indexes.
