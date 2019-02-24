Using the Search API module
===========================

.. note::

   These instructions are intended for Drupal 7. For Drupal 8 information, see our `Modules for Search </acquia-search/modules>`__ documentation.

As an alternative to using the Apache Solr Search Integration module, |acquia-product:as| supports using the Search API module. For most Drupal 7-based websites, we recommend that you use the Apache Solr Search Integration and related modules instead. Based on our extensive experience helping |acquia-product:as| customers with both the Apache Solr Search Integration module and the Search API module, we have found that using the Apache Solr Search Integration module results in a search solution that is more scalable, better performing, better integrated with Apache Solr, and easier to configure and maintain.

Best practices for using Search API
-----------------------------------

The biggest thing to consider is that, if you choose Search API, is the time that it takes to learn how configure it properly. Because Search API has such extensive configuration options, it is a lot easier to make mistakes. So when you are thinking about scaling a website you need to make conscious choices.

For example:

-  Never do any text processing in Drupal. For example, the Search API processors, such as stopwords and synonyms, can be easily configured in Solr itself.
-  Ensure that you understand the memory footprint of the search page, and that it is consistent with your server resources and configuration. Consider that search is a random result that is based on user input. When you use views and view modes to render your search results, you should either use the Solr fields to theme, or ensure that your cache is large enough and your server is fast enough to quickly render the entities returned on the search page. Entity caching makes a huge difference.
-  Multisite Searching in Search API (not multi-index searching, which is called ``search_api_multi``) is difficult to achieve OOTB due to the architecture of Search API. It was not the main intention to show content that doesn't rely on entities in the current website. Multisite can mean Drupal multisite, or a combination of Drupal websites with a completely different codebase.

Setting up the Search API module with |acquia-product:as|
---------------------------------------------------------

If you desire to use the Search API module with |acquia-product:as|, complete the following steps:

#. Install and enable the following Drupal modules:

   -  `Acquia Search for Search API <https://www.drupal.org/project/search_api_acquia>`__
   -  `Search API Solr search <https://www.drupal.org/project/search_api_solr>`__
   -  `Search API <https://www.drupal.org/project/search_api>`__
   -  `Entity API <https://www.drupal.org/project/entity>`__

#. Connect your website to your |acquia-product:aqs|. For more information, see |anc|_.
#. Run cron manually to have Acquia confirm your search subscription status and allow you to enable the |acquia-product:as| module. |br| 
   To do this, complete the following steps:

   a) In the admin menu, select **Reports**.
   b) Click the **Status report** link.
   c) In the **Cron maintenance tasks** section, click the **run cron manually** link.

   After cron has finished, Acquia provisions |acquia-product:as| for your website. The provisioning process can take a few minutes to complete.
#. In the **Acquia Search** page of the |acquia-product:ui|, click the gear icon to open the **Acquia Search settings** box.
#. Under **ApacheSolr module version**, select the version that corresponds to the version of the Search API Solr module that you are using, and click **Save**.
#. As the Drupal website administrator, configure the Search API Solr search module by completing the following steps:

   a) Navigate to **Configuration > Search API settings > Add**.
   b) When adding a server for the Search API, set the **Service class** to **Acquia Search** — do not select **Solr service**.
   c) Add or configure an existing index to use the new search server that you added.

Unlike the Apache Solr Search module, the Search API module does not add a new option for the existing core search block and form. To search and display results, you will need to enable and configure either the `Views <https://www.drupal.org/project/views>`__ module or the `Search API pages <https://www.drupal.org/project/search_api_page>`__ module.

.. |anc| replace:: \ |acquia-product:anc|\
.. _anc: https://www.drupal.org/project/acquia_connector
