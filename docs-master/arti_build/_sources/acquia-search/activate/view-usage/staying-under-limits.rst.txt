.. include:: /common/global.rst

Staying under Acquia Search limits
==================================

Customers with websites using the |acquia-product:as| platform have
limits for some or all of the following resources: total queries,
documents, and disk space. If these limits are consistently met or
exceeded, Acquia reserves the right to restrict the website's use of the
shared search resources or move your website to a dedicated
|acquia-product:as| instance at your expense.

Acquia will not generally block access to your Solr index. However, a
block could occur in an emergency where your or another customer's data
or service could be impacted. `Reviewing service
usage </acquia-search/activate/view-usage>`__ and preventing problems before they
occur ensures the best level of continual service.

.. _below:

If you are still below limits
-----------------------------

If you are not yet at your limit, you can proactively take steps to
prevent your website from ever reaching them. Here are some factors to
consider as you plan for usage:

- What is your `monthly usage </acquia-search/activate/view-usage#usage>`__ like?
- How is your content growing?

-  How much indexable content will your site be generating monthly?
-  If you are indexing files, what is your projected growth? Large
   attachments can `cause problems for your
   index <https://support.acquia.com/hc/en-us/search#stq=issues_large_attachments_and_solr_search>`__.

- What are your traffic patterns like?

  -  Do you expect a growth in visits that trigger search queries?
  -  Are you adding any new functionality like 
     `content recommendation blocks </acquia-search/search-pages/recommendation>`__, 
     auto-complete widgets, or others that increase the number of requests 
     to Solr?

- What is your non-production usage?

  -  Are you using independent Solr indexes for testing environments?
  -  Will there be heavy searching or indexing in non-production
     environments?

If you are concerned you may exceed your limits, you can 
`contact Acquia Support </support#contact>`__, or contact your account manager 
to get help determining the best fit for your website.


If you've exceeded the limits
-----------------------------

If you have exceeded your subscription limits, here are some of the
possible actions Acquia may take:

-  In case of an extended usage spike that may be exceeding your current
   limits, you may be automatically moved into an isolated Search
   cluster; `this may incur extra costs. Acquia may contact you to
   discuss this change </support/guide#shared_resources>`__.
-  Your account manager or Acquia Support may contact you with options
   to change your subscription. We offer multiple |acquia-product:as|
   packages which vary in storage size, query limits, and number of
   documents allowed.
-  You can review your 
   `monthly usage </acquia-search/activate/view-usage#usage>`__, and work to reduce 
   usage.


Reducing index usage
--------------------

|acquia-product:as| uses three metrics for your subscription: disk
storage size, number of Solr requests from Drupal, and the number of
documents in the index. You can use different strategies to reduce usage
in one or more of these areas.


Reduce non-production indexes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All of your Acquia subscription's Solr indexes (production and
non-production) count toward your limits. Reduce usage of some or all
non-production indexes, or remove indexes entirely to stay within your
subscription bounds.

-  `Delete an index and its data </acquia-search/activate/indexing#delete>`__.
-  `Set an index to read-only
   mode <https://support.acquia.com/hc/en-us/search#stq=read-only-apache-solr-search-index>`__.

Reducing requests to Solr
~~~~~~~~~~~~~~~~~~~~~~~~~

Several issues can trigger a high number of requests to your
|acquia-product:as| Solr backend:

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Situation
     - Action
   * - Autocomplete widgets powered by Solr	
     - 
       - Ensure autocomplete AJAX requests leverage Acquia's 
         `Varnish caching. </acquia-cloud/performance/varnish>`__
       - Reduce or eliminate usage of these widgets.

   * - Usage of More Like This 
       `content recommendation </acquia-search/search-pages/recommendation>`__ blocks
     - Cache these blocks or reduce their usage.
   * - Elevated traffic that triggers Solr queries
     - This is often caused by crawlers following links that trigger Solr requests.

       - Add ``nofollow`` directives to facet links to avoid crawlers. 
         `Edit each facet's </acquia-search/relevant-results/facets/configure>`__ 
         **Configure display** settings and enable 
         **Prevent crawlers from following facet links**.
       - Add ``robots.txt`` directives to avoid spiders accessing search results pages or facet links.

   * - The **Index immediately** option is enabled in Search API.
     - This is compounded by mass importing or editing of content.

       - Disable this option in your Search API index settings.

   * - The `Search 404 <https://www.drupal.org/project/search404>`__ module is 
       enabled.
     - Made worse by crawlers and traffic.

       - Disable this module or configure it to avoid triggering on certain requests.

   * - Mass content edits, imports or migrations
     - Disable indexing while doing any mass content handling.
   * - Out of date modules
     - Ensure your modules are up to date.


If you're using Drupal 7, one way to understand what data is being sent
to your Solr index is to use the `Solr
Devel <https://www.drupal.org/project/solr_devel>`__ module, which adds
a **Devel > Solr** tab on each entity. This enables you to see what's
already in your Solr index, as well as what data would be sent if you
were to index an item.


Disk storage size
~~~~~~~~~~~~~~~~~

If you are not careful about what you are indexing, the size of your
Solr index can increase rapidly, consuming excessive disk space. There
are several potential causes:

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Situation
     - Action
   * - Automatic Solr ``optimize`` isn't running
     - The `Optimize Solr operation <https://wiki.apache.org/solr/SolrPerformanceFactors#Optimization_Considerations>`__ is usually invoked weekly by Drupal modules and is responsible for reclaiming disk space after deletes and garbage collection.
     
       - Ensure cron is running on your site and calling the proper modules' cron hook. This may not occur on non-production websites.
       - Ensure the module's automatic weekly optimization runs by checking the timestamp kept here:

         - For Apache Solr, run ``drush solr-variable-get apachesolr_last_optimize``
         - For Search API, run ``drush variable-get search_api_solr_last_optimize``

   * - Indexing too many fields or entity data
     - This often occurs when indexing nodes with many comments.

       - Disable comments, fields, or other data from being indexed.

   * - Indexing large attachments with large amounts of text
     - Large PDF or text files can fill disk space quickly.

       - Avoid indexing files larger than 10MB.
       - Use custom code to truncate amount of data stored.
       - See `Issues with large attachments and Solr search <https://support.acquia.com/hc/en-us/search#stq=issues_large_attachments_and_solr_search>`__.
       

Number of documents indexed
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The relationship between the number of Drupal entities and number of
Solr documents is not always one-to-one; Drupal can process a single
entity such as a node or a user into multiple Solr documents. For
example:

-  ``node/1`` has three attached files. This can create four Solr
   documents - one for the node, and one for each attachment.
-  ``node/1`` has field data in three languages. This may create four
   Solr documents - one for each language.

To reduce the number of documents in your Solr index:

-  Avoid using Solr multilingual modules if your site uses a single
   language.
-  Avoid indexing attachments as separate Solr documents.
-  Index only the content types that must be searchable.
