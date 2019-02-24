.. include:: /common/global.rst

|acquia-product:acm| mappings
=============================

When considering your installation setup for |acquia-product:acm|, there
are many ways to approach it. For assistance in planning your full
website structure, see `Planning your governance
strategy </resources/governance>`__.

|acquia-product:acm| and Magento installations can be mapped to work
together in multiple ways, depending on your store's needs.

-  *One Drupal, one Magento* – One Drupal installation, with one
   language, is mapped to one Magento store view, with direct
   synchronization between the two services. This configuration works
   best for smaller or less complex stores.

   |One Drupal - one Magento|

-  *Multilingual Drupal, and multiple Magento store views in one
   install* – One Drupal installation, with multiple languages
   available, synchronizing with multiple Magento store views in a
   single Magento instance. This configuration enables you to serve
   multiple languages with your Drupal website while maintaining a
   single Magento instance.\ |Multilingual Drupal, multiple Magento|
-  *Multilingual Drupal, and multiple Magneto* – One multilingual Drupal
   installation, with multiple languages available, mapped to store
   views in multiple Magento instances. This configuration enables a
   single, multilingual Drupal installation to handle multiple stores
   that do not have overlap in audience languages. This configuration is
   generally supported, but has not been extensively tested.
   |Multilingual Drupal, multiple Magento installs|

.. |One Drupal - one Magento| image:: https://cdn4.webdamdb.com/1280_AURD8OidiMW7.png?-62169955200
   :class: align-center margin-top-1em no-sb
.. |Multilingual Drupal, multiple Magento| image:: https://cdn4.webdamdb.com/1280_YjdRe5BSSU02.png?1526475757
   :class: align-center margin-top-1em no-sb
.. |Multilingual Drupal, multiple Magento installs| image:: https://cdn2.webdamdb.com/1280_IhOrRUgb0LJ5.png?1526476137
   :class: align-center margin-top-1em no-sb

