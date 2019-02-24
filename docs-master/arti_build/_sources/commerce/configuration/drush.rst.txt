.. include:: /common/global.rst

Drush commands for Acquia Commerce Manager
==========================================

|acquia-product:acm| includes several
`Drush <https://www.drupal.org/project/drush>`__ commands for both
`normal product use <#cmd>`__ and for more advanced administration. You
can use the commands to manage your products and product categories from
the command line.

.. note::

   For more information about Drush, see the `Introduction to Drush <https://support.acquia.com/hc/en-us/search#stq=drush-intro>`__ Acquia knowledgebase article.

Drush commands
--------------

+-----------------------------------+-----------------------------------+
| Command                           | Description                       |
+===================================+===================================+
| `sync-commerce-cats <#sync-commer | Synchronizes all product          |
| ce-cats>`__                       | categories between                |
|                                   | |acquia-product:acm| and your     |
|                                   | commerce solution                 |
+-----------------------------------+-----------------------------------+
| `sync-commerce-product-options <# | Synchronizes product options      |
| sync-commerce-product-options>`__ | between |acquia-product:acm| and  |
|                                   | your commerce solution            |
+-----------------------------------+-----------------------------------+
| `sync-commerce-products <#sync-co | Synchronizes products             |
| mmerce-products>`__               |                                   |
+-----------------------------------+-----------------------------------+
| `sync-commerce-promotions <#sync- | Synchronize all commerce          |
| commerce-promotions>`__           | promotion records                 |
+-----------------------------------+-----------------------------------+
| `clean-synced-data <#clean-synced | Flush all commerce data from the  |
| -data>`__                         | website                           |
+-----------------------------------+-----------------------------------+

Command details
---------------

-  **``sync-commerce-cats``**
   Run a full synchronization of all commerce product categories.
   +----------+-----------+
   | Alias    | Arguments |
   +==========+===========+
   | ``acsc`` | *none*    |
   +----------+-----------+

-  **``sync-commerce-product-options``**
   Run a full product synchronization of all available product options.
   +-----------+-----------+
   | Alias     | Arguments |
   +===========+===========+
   | ``acspo`` | *none*    |
   +-----------+-----------+

-  **``sync-commerce-products``**
   Run a full product synchronization of all available products.
   +----------+-----------+
   | Alias    | Arguments |
   +==========+===========+
   | ``acsp`` | *none*    |
   +----------+-----------+

-  **``sync-commerce-promotions``**
   Run a full product synchronization of all available products.
   +-----------------------------------+-----------------------------------+
   | Alias                             | Options                           |
   +===================================+===================================+
   | ``acspm``                         | ``--types`` synchronizes a type   |
   |                                   | of promotion; for example,        |
   |                                   | ``drush acspm --types=cart``      |
   |                                   | synchronizes all available cart   |
   |                                   | promotions.                       |
   +-----------------------------------+-----------------------------------+

-  **``clean-synced-data``**
   Flush all commerce data from the website (including products, SKUs
   and product categories).

   Important

   This command removes all of your commerce-related data.

   +----------+-----------+
   | Alias    | Arguments |
   +==========+===========+
   | ``accd`` | *none*    |
   +----------+-----------+
