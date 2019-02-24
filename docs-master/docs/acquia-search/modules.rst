.. include:: /common/global.rst

Modules for Acquia Search
=========================

.. toctree::
   :hidden:
   :glob:

   /acquia-search/modules/search-api/
   /acquia-search/modules/attachments/

There are several Drupal modules that integrate with |acquia-product:as|, some of which are required, some of which are recommended, and some of which are helpful for different use cases.

Installing the required modules
-------------------------------

To use |acquia-product:as| with your Drupal website, you need to
download, install, and enable the following recommended modules based on
your installed version of Drupal:


.. list-table::
   :widths: 30 20 30 20
   :header-rows: 1

   * - Module
     - Drupal 8
     - Drupal 8 required version
     - Drupal 7
   * - |anc|_
     - |yes|
     - `8.x-1.12 <https://www.drupal.org/project/acquia_connector/releases/8.x-1.12>`__ or greater
     - |yes|
   * - `Search API <https://www.drupal.org/project/search_api>`__
     - |yes|
     - `8.x-1.0 or greater (stable releases only, no 2.x support) <https://www.drupal.org/project/search_api_solr/releases/8.x-1.0>`__ |Stable release|
     - |yes|
   * - `Search API Solr Search <https://www.drupal.org/project/search_api_solr>`__
     - |yes|
     - `8.x-1.3 <https://www.drupal.org/project/search_api/releases/8.x-1.3>`__ or greater
     - |yes|
   * - `Apache Solr Search Integration <https://www.drupal.org/project/apachesolr>`__
     - |no|
     - 
     - |yes|


-  *Drupal 8*

   Before you attempt to install the Drupal modules needed to use 
   |acquia-product:as|, be sure that you meet the following requirements:

   -  Use only the previously specified module versions for Drupal 8
      websites. Other module combinations have not been tested, and may
      not work as intended.
   -  Solr version 4.5 or greater is required. New customers without a
      previous |acquia-product:as| subscription receive this version.
      Previous customers with indexes using Solr 3.5 continue receiving
      this version. `Contact Acquia Support </support#contact>`__ if you
      need the newer version.
   -  Ensure you have compatible Solr configuration files. See `Search
      settings </acquia-search/view-usage>`__ for more information.
   -  This procedure requires that you already have Composer to properly
      manage the autoloader and other files.

.. note::
  |acquia-product:as| is incompatible with 8.x-2.x versions of Search 
  API Solr Search.

After ensuring that you have met the previously described comments,
`install the current release of the Acquia Network Connector
module </acquia-cloud/insight/install>`__, which includes the
|acquia-product:as| module, and then install the specified releases
of the `Search API Solr <https://www.drupal.org/project/search_api_solr>`__ 
and `Search API <https://www.drupal.org/project/search_api>`__ modules.

-  *Drupal 7*

   `Install the current release of the Acquia Network connector
   module </acquia-cloud/insight/install>`__, which includes the
   |acquia-product:as| module. For more information, see `About the
   Acquia Network Connector </acquia-cloud/insight>`__. Although it is
   possible to use the `Search
   API <https://www.drupal.org/project/search_api>`__ and `Search API
   Solr Search <https://www.drupal.org/project/search_api_solr>`__
   modules, they are not recommended for use with Drupal 7.

Configuring the Solr index to match your website’s modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you update the Apache Solr Search Integration module to a later
version, you must register the update in the Acquia Search page of the
Acquia user interface. Click the gear icon, select the new version of
the Apache Solr Search Integration, and then click **Save**.

|Update module version|

Recommended modules
-------------------

The following modules are necessary for important use cases with
|acquia-product:as|:

-  `Facet API <https://www.drupal.org/project/facetapi>`__ - Enables
   faceted search interfaces, so users can filter their search results.
-  `Solr Devel <https://www.drupal.org/project/solr_devel>`__ (Drupal 7
   only) - Enables easier debugging of Solr indexing, searching, and
   ranking.
-  `Apache Solr
   Attachments <https://www.drupal.org/project/apachesolr_attachments>`__
   - Required to include file attachments in your search index.
-  `Apache Solr Multisite
   Search <https://www.drupal.org/project/apachesolr_multisitesearch>`__
   - Required to enable multiple websites to connect to a single search
   index and provide a unified search across all of the websites. This
   also supports searches that span Drupal 7 websites.

Other search modules
--------------------

- *Drupal 8*
   There are several search modules that do not have a stable Drupal 8
   version. The best place to track the development status of these and
   other modules is the `Drupal 8 Contrib
   Tracker <https://www.drupal.org/project/issues/contrib_tracker?status=All&component=Module>`__.
- *Drupal 7*

  -  `Facetapi
     Slider <https://www.drupal.org/project/facetapi_slider>`__ -
     Provides an additional display widget for faceted search.
  -  `Apachesolr
     Commerce <https://www.drupal.org/project/apachesolr_commerce>`__ -
     Supports indexing for commerce entities.
  -  `Apachesolr
     User <https://www.drupal.org/project/apachesolr_user>`__ -
     Supports indexing for user entities.
  -  `Apachesolr
     Term <https://www.drupal.org/project/apachesolr_term>`__ -
     Supports indexing for taxonomy terms.
  -  `Acquia Search Multiple
     Indexes <https://www.drupal.org/project/acquia_search_multi_subs>`__
     - Enables switching between |acquia-product:as| cores, either
     manually or automatically. See `Using multiple search
     cores </acquia-search/multiple-cores>`__.

In addition, see the Drupal project pages for `Apache Solr Search Integration
<https://www.drupal.org/project/apachesolr>`__ and `Facet API 
<https://www.drupal.org/project/facetapi>`__ for links to more  search-related 
modules.


.. |Stable release| image:: https://cdn3.webdamdb.com/100th_sm_2F5h5a71StC1.png?1527793979
   :class: no-sb
   :width: 18px
   :alt: Drupal.org shield for stable release

.. |Update module version| image:: https://cdn3.webdamdb.com/md_MMOlY6FPk112.png?1527793620
   :alt: Update the module version

.. |anc| replace:: \ |acquia-product:anc|\
.. _anc: https://www.drupal.org/project/acquia_connector
