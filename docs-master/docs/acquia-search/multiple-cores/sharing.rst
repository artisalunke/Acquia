.. include:: /common/global.rst

Sharing Solr cores in read/write mode
=====================================

Multiple |acquia-product:as| cores

-  `Use </acquia-search/multiple-cores>`__
-  `Override </acquia-search/multiple-cores/override>`__
-  Share
-  `Troubleshoot </acquia-search/multiple-cores/troubleshoot>`__

With all of the benefits of allowing multiple websites to write to a
single Solr instance, there are some inherent areas of concern in doing
so. Potential problems can include accidental Solr core pollution (such
as a development website writing to a production index) and accidental
deletion when trying to remove a non-production index.

However, the following methods can help you share Solr cores safely,
which can ensure that your website is able to service users:

-  **Consider using read-only mode**
   Ensure that your application actually needs to write to a Solr core;
   in some cases, reading is sufficient. For example, if your
   development and production websites have the same content, you can
   use the production index in read-only mode for search.
-  **Ensure correct implementation of Solr hashes**
   Solr-related Drupal modules (including `Apache Solr Multisite
   Search <https://www.drupal.org/project/apachesolr_multisitesearch>`__
   and recent versions of `Search API Solr
   Search <https://www.drupal.org/project/search_api_solr>`__) should
   tag all indexed items with a unique string ID called a *hash*. This
   hash value should be unique to each website that writes to the same
   Solr core, allowing you to logically share a single Solr core across
   websites. All queries, indexing, and delete operations are limited to
   items that have this hash value.
   Because of this, problems can occur when moving a Drupal database.
   Hash values are created when the module is installed, and are stored
   as configuration data in Drupal's database. Moving a database to
   another environment can include configuration data (and by extension,
   the hash values). To resolve this, we recommend that you override the
   hash value in code. To review your hash values, examine the following
   items:

   -  `Search API Solr
      Search <https://www.drupal.org/project/search_api_solr>`__ module
      (Drupal 8) - ``search_api_solr.settings:site_hash`` configuration
      setting
   -  `Search API Solr
      Search <https://www.drupal.org/project/search_api_solr>`__ module
      (Drupal 7) - ``search_api_solr_site_hash`` variable
   -  `Apache Solr Search <https://www.drupal.org/project/apachesolr>`__
      module (Drupal 7) - ``apachesolr_site_hash`` variable

-  **Use tools to understand your index**
   Tools such as `Solr
   Devel <https://www.drupal.org/project/solr_devel>`__ (for Drupal 7)
   enable you to both examine outgoing queries and understand the data
   in your index. For information about using Solr Devel, see `Using
   Solr Devel module to debug |acquia-product:as| indexing and
   queries <%5Bacquia-product:kb%5Darticle/using-solr-devel-module-debug-acquia-search-indexing-and-queries>`__.
-  **Be prepared to delete data and reindex**
   If a single Solr core is polluted with data from unintended sources,
   it can be difficult to fix. This is because Drupal keeps tracking
   information about what it thinks it has already indexed in the
   database, separate from the actual Solr data.
   To recover from this issue, and to help prevent future pollution,
   complete the following steps:

   #. Ensure that you close any connections from unwanted websites
      writing to the target Solr core.
   #. Completely wipe data from the target Solr core.
   #. Reindex all of the data that needs to be written to this Solr
      core.
