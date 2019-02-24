.. include:: /common/global.rst

Getting started with Acquia Search
==================================

.. toctree::
   :hidden:
   :glob:

   /acquia-search/activate/view-usage/
   /acquia-search/activate/indexing/

.. important::

    Read the entire procedure before installing and starting to use |acquia-product:as|. **Do not** follow this procedure if you are using the Search API. Instead, read `Using the Search API </acquia-search/search-api>`__.

To get started with |acquia-product:as| for your website, complete the following steps:

#. Download and install the |acquia-product:as| module, as well as the
   other required modules on your website. For details, see `Modules for
   </acquia-search/modules>`__ |acquia-product:as|.
#. Obtain your keys and connect to your |acquia-product:aqs|. For more
   information about connecting to an |acquia-product:aqs|, see `Acquia
   Connector </acquia-cloud/insight/install>`__.
#. Run cron manually to have Acquia confirm your search subscription
   status and allow you to enable the |acquia-product:as| module. To do
   this, complete the following steps:

   #. In the admin menu, select **Reports**.
   #. Click the **Status report** link.
   #. In the **Cron maintenance tasks** section, click the **run cron
      manually** link.

   After cron has finished, Acquia provisions |acquia-product:as| for
   your website. The provisioning process can take a few minutes to
   complete.
#. In the admin menu, select **Modules** to open the Modules page.
   In the Acquia Connector section, enable the |acquia-product:as|
   module, and then click **Save configuration**. You do not need to
   enable any other modules at this time.
   Since |acquia-product:as| is dependent on Apache Solr, you will be
   asked if you want to enable the Apache Solr Search and and Apache
   Solr framework modules as well. Approve this request.
   While Acquia provisions your website, you may see the following error
   message on the Status report page. To view the Status report page, in
   the admin menu, select **Reports**, and then click the **Status
   report** link.
#. The |acquia-product:as| index of your website content is built and
   maintained during cron runs. Depending on how much content is on your
   website, the initial indexing process will take some time to
   complete. You can set the indexing rate for your website content
   during each cron run on the **Apache Solr search > Default Index**
   tab, under **Actions**. For more information, read `Indexing your
   website </acquia-search/indexing>`__.
   You and your users can search your website when your website is fully
   indexed. You can check the state of the index on the **Apache Solr
   search > Default Index** tab, under **Search Index Content**. For
   more information, read `Search index reports </acquia-search/activate/indexing/index-reports>`__.

After your website is fully indexed, you can take advantage of the power
of |acquia-product:as|. When visitors enter searches into the search
field or on the search page at ``http://example/?q=search`` (where
*example* is the URL of your server) |acquia-product:as| will provided
the search results.

.. _update:

Updating your version of Apache Solr Search Integration
-------------------------------------------------------

When you update the your search module to a newer version, you must register the update in the |acquia-product:as| page of the |acquia-product:ac| interface. To do this, complete the following steps:

#. Sign in to your Acquia subscription.
#. Select your application, and then click its **Acquia Search** link.
#. In the upper right corner, click **Edit**.
#. In the **Acquia Search configuration set** list, click the new version of the search module.
#. Click **Save**.

What's next
-----------

After you have enabled |acquia-product:as| and indexed your website, you can:

-  `Create alternative search pages </acquia-search/search-pages>`__
-  `Create content recommendation blocks ("More like this") </acquia-search/recommendation>`__
-  `Configure search facets </acquia-search/facets>`__
-  `Use bias to tune search results </acquia-search/bias>`__
-  `Configure multi-site indexing and search </acquia-search/multidomain>`__
-  `Debugging Acquia Search </acquia-search/debugging>`__
