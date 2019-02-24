.. include:: /common/global.rst

|acquia-product:acm| Promotions
===============================

You can create promotions in your commerce software which can be
synchronized to the |acquia-product:acm| system. You will need to
periodically synchronize your promotion data to ensure that the
promotions are up to date and to see updated prices on SKUs.

To automate synchronization, the ``acq_promotions`` module, included
with `|acquia-product:acm| </commerce/install>`__, enables easy
promotion synchronization through Drush commands. For more information
about creating cron jobs with these Drush commands, see `Using scheduled
jobs to maintain your application </acquia-cloud/manage/cron>`__.

Before you synchronize promotions, perform the following steps:

#. Ensure you have added all necessary content languages in Drupal. See
   `Multilingual configuration <#multi>`__.
#. Ensure you have added all ``store_id`` configurations.

Once your stores and promotions are ready, or whenever you need to make
a change to your promotions, complete these steps:

#. Sync the promotions with the
   ```drush sync-commerce-promotions`` </commerce/drush#sync-commerce-promotions>`__
   command.
#. Sync the products with the
   ```drush sync-commerce-products`` </commerce/drush#sync-commerce-products>`__
   command.

The Drupal website will make a request to the |acquia-product:ccs| to
request the promotion details. The conductor will make a request to the
commerce backend and return all available promotions in a synchronous
request which allows us to run this command locally.

When updating promotions, SKU prices will be updated, based on catalog
promotions, and any promotions that are not applicable will not be
synced. This might include promotions that do not apply to any products
based on the conditional rules in your commerce solution.

Note

To manually synchronize your promotion data, See `Acquia Commerce
Manager configuration settings </commerce/configuration#sync>`__ for
help with synchronization settings.

Multilingual configuration
--------------------------

Magento stores multilingual content as separate stores within a single
Magento website, using one store per language. These stores must be be
mapped directly to the generated ``store_id`` in Drupal. This is a
manual step, as there is no UI to assign ``store_id`` values to language
codes in Drupal.

Configuration per store
~~~~~~~~~~~~~~~~~~~~~~~

To synchronize promotions that match languages installed in Drupal, you
will need to ensure that there is a language specific configuration
override for the ``store_id``.

You can use code similar to the following to assist you in setting
configuration values:

``$conf = \Drupal::languageManager()->getLanguageConfigOverride($langcode, 'acq_commerce.store'); $conf->set('store_id', $store_id); $conf->save();``
