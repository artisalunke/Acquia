.. include:: /common/global.rst

Search index reports
====================

The Apache Solr search > Configuration > Default Index page provides basic information about your search index, including the following:

- number of items indexed
- number of items that remain to be indexed
- the version name of your search index schema
- the version name of your Solr Core
- delay (the time between when Solr receives the documents and when they are processed)
- number of items pending for deletion

|Search index reports|

For statistics about how your users are using search terms and search facets, and information about your |acquia-product:as| subscription, see `Viewing search usage and statistics </acquia-search/activate/view-usage/>`__.

For a more detailed report on how many document terms and fields have been indexed, click **View more details** on the search index contents link to open the search index report page at **Reports > Apache Solr Search index**.

|Search index report - detail|

The Search Index report displays the following items:

- number of documents in the search index
- number of terms in the search index
- number of fields in the search index

The number of documents in the search index will not necessarily be the same as the number of Drupal nodes in your website. Drupal may create multiple documents in the search index when it processes a single entity (such as a node or a user). For example:

- ``node/1`` has three attached files |br|
  Under certain circumstances, you would end up with four documents in the search index: one for the node and one for each attachment.
- ``node/1`` has field data in three languages |br| 
  Under certain circumstances, you would end up with three documents in the search index, one for each language.

For each field, the Search index report displays:

- field name
- type (such as text, string, or boolean)
- number of distinct terms in that field

Configuration files
-------------------

The **Reports > Configuration Files** tab displays the Solr configuration files. `Contact Acquia Support </support#contact>`__ if you need to modify any of these files.

.. |Search index reports| image:: https://cdn4.webdamdb.com/1280_cARrhRB8iH75.png?1528419496
   :alt: Search index reports
.. |Search index report - detail| image:: https://cdn2.webdamdb.com/1280_Ikwl3LbCS16.png?1527793651
   :alt: Search index report - detail
