.. include:: /common/global.rst

Custom Solr configuration
=========================

|acquia-product:as| provides preconfigured Solr search configurations
that work with the most popular search modules and are available for
several languages. You can select one of these configurations using the
**Search** page in the Acquia user interface, as described in `Selecting
a language </acquia-search/language>`__. The principal reason to choose
a different search schema is to support websites whose primary language
is other than English.

Other customizations of the default |acquia-product:as| configuration
files are possible (for example, to support websites in other primary
languages or other content-indexing behavior, like word-splitting rules
or n-gram tokenizing). These kinds of |acquia-product:as| customizations
are available only for |acquia-product:ace| customers or customers with
an Enterprise |acquia-product:aqs|. Those customers can modify their
``schema.xml``, ``elevate.xml``, ``synonyms.txt``, ``stopwords.txt``,
and ``protwords.txt`` files, subject to the following limitations:

.. note::

      Modifications must begin from the stock configuration files that are
      used with |acquia-product:as|. You can retrieve the configuration files
      residing on the Solr server from Drupal, using either of these methods:

      -  `Apache Solr Search
         Integration <https://www.drupal.org/project/apachesolr>`__ module -
         Navigate to **Reports > Apache Solr search index** and select a
         server. Use the **Configuration Files** tab to access the Solr
         configuration files.
      -  `Search API Solr <https://www.drupal.org/project/search_api_solr>`__
         module - Navigate to **Configuration > Search API**, then click on a
         server name. Use the **Files** tab to access the Solr configuration
         files.

-  You can initiate |acquia-product:as| customization by filing a
   support ticket with Acquia.
-  Customer requests to implement |acquia-product:as| customizations are
   processed weekly. Requests submitted by the end of `Acquia business
   hours in the local Acquia support
   region <https://www.acquia.com/drupal-support/coverage-areas-and-hours-operation>`__
   each Monday will be processed on Wednesday of the same week.
-  An |acquia-product:as| customization request ticket has the following
   requirements:

   -  One or more Solr configuration files must be attached to the
      ticket.
   -  The attached files must be UTF-8-encoded without a Byte Order Mark
      (BOM), with LF (Unix-style) line endings.
   -  The ticket can request changes to multiple Solr indexes, but only
      if all files are to be deployed equally to all mentioned indexes
      at the same time.
   -  One or more |acquia-product:as| index IDs or URLs. These can be
      found:

      -  *For Search API* - In the Drupal administrative user interface,
         under **Config > Search API**, and then select the server page.
      -  *For ApacheSolr* - In the Drupal administrative user interface,
         under **Config > Apache Solr Search Integration > Settings**.
      -  *Signed in to Acquia Insight* - Under **Sites**, select a
         Sitename, and then click **Search**.

-  For information about validating your changes before you submit them
   to Acquia, see `How to test a custom Solr schema file
   locally <%5Bacquia-product:kb%5Darticles/how-test-custom-solr-schema-file-locally>`__.
-  When you provide Acquia with modified files, be sure to exclude the
   ``clustering``, ``velocity``, and ``xslt`` folder or any ``*.html``,
   ``*.7z``, ``*.conf`` or ``*.js`` file. Provide *only* the files that
   you have modified and clearly state what you changed.
-  Acquia must validate modifications to the files before they are
   deployed.
-  Consulting on configuration file changes is outside the scope of
   Support.
-  Modifications of the ``solrconfig.xml`` file are not generally not
   permitted. Any additional behavior must be provided using the
   ``solrconfig_extra.xml`` file. If your use case absolutely requires
   ``solrconfig.xml`` modification, `contact Acquia
   Support </support#contact>`__ for a case-by-case evaluation. Acquia
   reserves the right to deny any such changes.
-  Acquia does not support the use of the `Apache Solr
   File <https://www.drupal.org/project/apachesolr_file>`__ module,
   because it requires modifications of the ``solrconfig.xml`` file.
-  Acquia does not permit modifications of the ``solrconfig.xml`` file
   to increase frequency of auto-commits.
-  Acquia reserves the right to deny configuration changes if there is
   evidence that they will cause service disruption, additional server
   load, or potential disruption of service for other customers.
-  Customers are responsible for testing configuration changes before
   submitting them to Acquia. Customizations that do not pass Acquia’s
   automated basic configuration integrity test will be rejected without
   additional investigation. The customer will be notified of the
   failure and is responsible for modifying the custom configuration
   file and testing it locally.
-  Acquia does not perform testing to ensure search configuration
   modifications will perform as intended. It is the responsibility of
   the customer to perform this testing.
-  |acquia-product:as| does not support
   `real-time </acquia-search/realtime>`__ search.

If you require very fine-grained or frequent search configuration
customizations, you may wish to consider a hosted Apache Solr provider,
rather than a software-as-a-service offering like |acquia-product:as|.

.. _download:

Downloading your configuration files
------------------------------------

You can download copies of your current configuration files by
completing the following steps:

#. Sign in to your Drupal website as an administrative user.
#. Complete the following steps based on your installed search module:

   -  `Apache Solr Search <https://www.drupal.org/project/apachesolr>`__ module

      #. In the admin menu, click **Reports**.
      #. Click the **Apache Solr search index** link.
      #. Click the **Configuration Files** tab.

   -  `Search API <https://www.drupal.org/project/search_api>`__
      module

      #. In the admin menu, click **Configuration**.
      #. In the **Search and metadata** section, click the **Search
         API** link.
      #. Click the name of the search server to select it, and then
         click the **Files** tab.

#. Identify the file that you want to download, and then click the
   filename to view it.
#. Copy the text into a text file, and then save it with the same
   filename locally.

.. _best-practice:

Custom configuration best practices
-----------------------------------

-  `EdgeNGrams <https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-edgengram-tokenizer.html>`__
   should be used instead of NGram, and only on short text fields, to
   avoid performance problems and uncontrolled growth of index file
   sizes.
-  Ensure configuration files are encoded in UTF-8.
-  Any and all configuration file changes `should be
   tested </articles/how-test-custom-solr-schema-file-locally>`__ before
   submitting to Acquia, on a non-Acquia-hosted Solr instance. The
   current configuration files can be obtained through Drupal itself by
   either of these methods:

   -  If using the ApacheSolr module: go to **Reports > ApacheSolr** and
      select a server. Then, use the **Configuration Files** tab to
      access the Solr configuration files.
   -  If using the Search API Solr module: go to **Configure > Search >
      Search API** and select a server name. Use the **Files** tab to
      access the Solr configuration files.

-  To generate an ``elevate.xml`` file, we recommend using the `Solr
   Best Bets <http://drupal.org/project/solr_best_bets>`__ module.
-  Be aware that problems in configuration files supplied to Acquia
   might result in |acquia-product:as| Solr instances to fail to restart
   after configuration changes, and search will become unavailable to
   any connected websites or environments.
