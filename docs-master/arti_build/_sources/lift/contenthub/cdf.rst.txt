.. include:: /common/global.rst

|acquia-product:ch| and CDF
===========================

|acquia-product:ch| uses the Common Data Format (CDF) for communication
data between the |acquia-product:ch| storage service and the end-user
client layer comprising all the applications connected to the hub.
|acquia-product:ch| uses the JSON format to serialize CDF. Every piece
of data is typed to ease its indexing for search.


Recommendations
---------------

We recommend that the following items be consistent between non-Drupal
websites and |acquia-product:ch|:

-  When building a connector to publish to |acquia-product:ch|, we
   recommend that you rename the other system's attributes to match what
   Drupal expects. This is more important for attributes that are built
   into Drupal, such as ``Title``. Doing this helps ensure consistent
   naming across all systems, which is important for token usage.
-  Dates should be expressed in the |ISO 8601|_ format — for
   example, ``2016-02-09T23:04:20-05:00``. In PHP, use ``date('c')``
   instead of ``date('Y-m-d H:i:s’)``. Using ``date('Y-m-d H:i:s’)``
   returns ``2016-02-09 23:04:20``, which is incorrect.


Entity structure
----------------

The most important piece of the common data structure is the array of
entities it contains. Each entry is an unrestricted entity, allowing the
transmission of heterogenous collections in a single file.

The following is an example of the ``entities`` object:

.. code::

   {
      "entities": [
         {
               "uuid": "00000000-0000-0000-0000-000000000000",
               "type": "product",
               "created": "2013-04-15T18:56:54-04:00",
               "modified": "2014-02-24T16:13:47-05:00
               "origin": "16074522-f318-4a69-52f5-bb6d740e5a41",
               "attributes": {
                  "title": {
                     "type": "string",
                     "value": {
                           "en": "A",
                           "hu": "B",
                           "und": "C"
                     }
                  },
               },
               "assets": [
                  {
                     "url": "http://mysite.com/sites/default/files/foo.png",
                     "replace-token": "[acquia-logo]"
                  },
                  {
                     "url": "http://mysite.com/sites/default/files/bar.png",
                     "replace-token": "[acquia-thumb]"
                  }
               ]
         }
      ]
   }


The elements of an entity are defined as the following:

-  *uuid* - Each entity is identified by a required UUID. Each client
   application should map its internal storage to such UUID in order to
   allow data synchronization over time.
-  *type* - An arbitrary string which may be used by the client side to
   determine the type of entity and trigger appropriate behavior.
   Examples include articles and products.
-  *created* - The created date in |ISO 8601|_ standard format.
-  *modified* - The modified date in |ISO 8601|_ standard format.
-  *origin* - The UUID of the client application that originally created
   this entity and owns it. This can be useful on the client side to
   know if a client is allowed to perform actions such as editing an
   entity.
-  |attributes-fixed|_ - Localizable collections of values
   keyed by the attribute name. Each attribute is typed so that it can
   be stored in |acquia-product:ch| and indexed properly for search
   purposes.
-  *assets* - A list of resources that are referenced in the attributes
   of the entity in the form of tokens. ``url`` points to the ``Asset``.
   Token strings will be replaced in every attribute that has an
   occurrence in their value.

.. |attributes-fixed| replace:: *attributes*
.. _attributes-fixed: #attributes


Attributes
~~~~~~~~~~

Attributes can be single pieces of information, or can be passed as
nested attributes. Nested attributes follow the |methodology|_.

.. |methodology| replace:: Elasticsearch methodology for mapping
.. _methodology: ttps://www.elastic.co/guide/en/elasticsearch/reference/1.7/mapping-core-types.html

-  *type* - Any primitive data type, such as ``integer``, ``string``,
   ``keyword``, ``boolean``, ``number``, or ``reference``. If the value
   is an array, the type should be wrapped accordingly (for example:
   ``array``).
-  *value* - An associative array, always keyed by language. Unlocalized
   data must contain the ``und`` key, which is the standard for
   undefined language data.


Accessing an entity's CDF
-------------------------

|acquia-product:ch| uses custom paths to both access an entity's CDF and
prevent conflicts with the default system path.

To access an entity's CDF, in your browser's address bar enter a URL
similar to the following, where:

-  ``[site]`` is your website's domain name
-  ``[entity type]`` is the entity type
-  ``[entity id]`` is the entity's ID number

.. code-block:: none

   [site]/acquia-contenthub-cdf/[entity type]/[entity id]?_format=acquia_contenthub_cdf

For example, the following URL example would allow you access to a
paragraph entity's CDF:

.. code-block:: none

   [site]/acquia-contenthub-cdf/paragraph/1?_format=acquia_contenthub_cdf


Modifying entities and the CDF with hooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ch| provides hooks for modifying your website's entities
and CDF, allowing you to improve syndication, and modifying view modes
in your website's CDF to support custom rendering processes:

-  Allow modules to modify the Drupal entity after conversion from CDF
   
   - *Drupal 8* - ``hook_acquia_contenthub_drupal_from_cdf_alter``
   - *Drupal 7* - ``hook_content_hub_connector_drupal_from_cdf_alter``

-  Allow modules to modify the CDF before it is sent to
   |acquia-product:ch|

   - *Drupal 8* - ``hook_acquia_contenthub_cdf_from_drupal_alter``
   - *Drupal 7* - ``hook_content_hub_connector_cdf_from_drupal_alter``

-  Allow modules to modify the CDF before converting to Drupal entity

   - *Drupal 8* - ``acquia_contenthub_cdf_from_hub_alter``
   - *Drupal 7* - ``hook_content_hub_connector_cdf_from_hub_alter``

-  Allow modules to modify the Drupal entity before its normalization to
   CDF

   - *Drupal 8* - ``acquia_contenthub_drupal_to_cdf_alter``
   - *Drupal 7* - ``hook_content_hub_connector_drupal_to_cdf_alter``


.. |ISO 8601| replace:: ISO 8601
.. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601