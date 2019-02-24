.. include:: /common/global.rst

Acquia Search
=============

.. toctree::
   :hidden:
   :glob:

   /acquia-search/modules/
   /acquia-search/activate/
   /acquia-search/config/
   /acquia-search/language/
   /acquia-search/search-pages/
   /acquia-search/relevant-results/
   /acquia-search/multiple-cores/
   /acquia-search/multidomain/
   /acquia-search/faq/
   /acquia-search/debugging/
   /acquia-search/known-issues/

|image0|

Adding |acquia-product:as| to your website creates a rich index of your website content and adds faceted search refinement, helping users find content faster and stay on your website longer.

|acquia-product:as| provides your website with the following features:

.. container:: message-status

 **QUICK LINKS:**  `Getting started </acquia-search/activate>`__  |  `FAQ </acquia-search/faq>`__  |  `Modules </acquia-search/modules>`__  |  `Indexing </acquia-search/indexing>`__

-  **Search as a service** |br| 
   |acquia-product:as| is a plug-and-play search service that lets you deliver great search functionality in minutes.
-  **Faster searches** |br| 
   Your users can find what they're looking for faster than using Drupal's built-in search. |acquia-product:as| has delivered searches with a 60% to 500% improvement in response time.
-  **High availability** |br| 
   Acquia's search infrastructure of Solr servers, coupled with Ngnix load balancers in a round-robin configuration, ensure consistent availability of your website's search index.
-  **Security** |br| 
   Apache Solr has no native security mechanism; administrators have to implement their own security system on the application or network layer. Acquia has implemented an HMAC authentication mechanism on the Solr servers that only allows access to authorized sites. All data is transmitted over SSL if the client server supports it. |acquia-product:as| also respects node access controls, enabling search content to be limited to authorized users.
-  **Result filtering and weighting** |br| 
   Users can use facets to filter search results, and the content of your choice appears higher in search results, shaping your users' website experience.
-  **Content recommendations** |br| 
   Suggest similar or related content to visitors, which can increase their time on your website.
-  **Multi-entity and attachment searches**
   Enables searching over multiple types of content — not just content nodes, but also users, taxonomy terms, or your own custom entity types. Search also can include the contents of files `attached to your websites. </acquia-search/attachments>`__
-  **Better knowledge of the data structure** |br| 
   |acquia-product:as| automatically understands when content is changed, and updates the index. This means that updating your index requires one small change, instead of waiting for a crawler to check your entire site for changes. This also means that the index can contain metadata that may not be visible to crawlers.

|acquia-product:as| and Drupal 8

In Drupal 8, |acquia-product:as| works best with the `Search API <https://www.drupal.org/project/search_api>`__ module, rather than the `Apache Solr Search <https://www.drupal.org/project/apachesolr>`__ module used with Drupal 7. This change was made for several reasons, including the following:

-  *Avoiding duplication of community effort* |--| It makes sense for the Drupal community to focus its efforts on one primary search module instead of two.
-  *Community momentum* |--| Community support for Search API is stronger than for Apache Solr Search.

For more information about this transition, see the `Battleplan for Search & Solr in Drupal 8 <https://dev.acquia.com/blog/search-strategies-in-drupal-8/battleplan-for-search--solr-in-drupal-8/09/05/2016/10421>`__ log post.

.. _start:

Getting started with |acquia-product:as|
----------------------------------------

For information about how to activate |acquia-product:as| for your website, see `Getting started with Acquia Search </acquia-search/activate>`__.

.. |image0| image:: https://cdn3.webdamdb.com/1280_wapgkyMJ5uW0.png?-62169955200
   :class: float-right
   :width: 61px
