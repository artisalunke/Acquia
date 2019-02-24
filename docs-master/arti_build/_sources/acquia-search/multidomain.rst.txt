.. include:: /common/global.rst


Searching across Drupal multisites
==================================

Your users can see search results from the site they are searching from
or from all of the websites included in your |acquia-product:as|
multisite index. To use multisite search, first install and enable the
`Apache Solr Multisite
Search <http://drupal.org/project/apachesolr_multisitesearch>`__ module
on each website that will be included in your |acquia-product:as|
multisite search index.

Enabling search environments for multisite indexing
---------------------------------------------------

To enable a search environment for multisite search indexing:

#. On the **Apache Solr search > Settings** page, click the **Edit**
   link for the search environment.
#. Select **Make this Solr search environment multisite capable**.

   |Enable multisite in this search environment|

.. note::

   When multiple websites are sharing an index, and the Apache Solr Access
   module, they may experience unexpected results. We recommend disabling
   the module on all affected websites and reindexing when possible.

Enabling websites for multisite indexing and searching
------------------------------------------------------

To enable your users to search across the websites in your multisite
index, complete the following steps:

#. Ensure you have installed and enabled the `Apache Solr Multisite
   Search
   module <http://drupal.org/project/apachesolr_multisitesearch>`__ on
   each website that will be included in your Acquia Search multisite
   search index.
#. If you have not yet done so, `connect each site to your
   </acquia-cloud/insight/install>`__ |acquia-product:aqs|. Add your
   subscription identifier and subscription key to the Acquia settings
   page of each site on the **Acquia Network settings** configuration
   page. Each site you wish to include in your Acquia Search multisite
   index must be associated with an
   |aqs|_.
#. Re-index each site that you enable for multisite indexing. For more
   information, read `Indexing your
   website </acquia-search/indexing>`__.
#. In the admin menu, select the **Apache Solr search > Multisite** tab.
   After the other sites' contents start to be indexed in the multisite
   index, they will appear in the Administrative functions section. To
   update the display, click **Refresh metadata now**.

Configure multisite search facets in your search environments
-------------------------------------------------------------

When you enable the Apache Solr Multisite Search module, additional
search facets become available on each search environment's **Settings >
Facets** page.

#. Check **Enabled** for each search facet that you want to make
   available for multisite search.
#. For each facet you enable, you can configure its display,
   dependencies, and filters. For more information, see `Configuring
   search facets </acquia-search/facets/configure>`__.

.. |Enable multisite in this search environment| image:: https://cdn3.webdamdb.com/md_w6ljuBoU8A31.png?1527793648
   :alt: Enable multsite in this search environment


.. |aqs| replace:: \ |acquia-product:aqs|\
.. _aqs: https://www.acquia.com/products-services/acquia-network
