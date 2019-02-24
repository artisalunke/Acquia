.. include:: /common/global.rst

Obtaining relevant search results
=================================

.. toctree::
   :hidden:
   :glob:

   /acquia-search/relevant-results/facets/
   /acquia-search/relevant-results/exact-phrase-searching/
   /acquia-search/relevant-results/bias/

Adjusting your website's search result ordering and matching (often
referred to as *tweaking results*) can be as complicated a topic as you
want to make it. To help you with this process, the `Apache Solr Search
Integration <https://drupal.org/project/apachesolr>`__ module provides
several hooks and user interface options to tweak your website's
results. The combination of hooks and settings that works for you
depends on your architecture, your customers' behavior, and your
real-world user testing.

Use these methods to get the best possible results, make small changes,
and then test and get feedback. Evaluate what the most natural results
would be for searches, and then make modifications.

Here are some of the available options:

-  **Use biasing options to tweak result ordering**

   Use the biasing options in the Drupal user interface either to tweak
   result ordering by newness or by entity type, or to give more
   importance to matches in taxonomy terms, titles, or other fields.

   To view your website's biasing options, sign in as an administrator,
   go to **Configuration > Apache Solr Search > Settings**, and then
   click **Bias** next to the search environment that you want to edit.
   You can also read the |acquia-product:as| documentation on `Using
   bias to tune search results </acquia-search/bias>`__. For example, an
   easy way to bubble up items on search results is if those nodes are
   marked as **sticky at top of lists**. You will also need to work with
   your editors to understand when and how to set this flag.

-  **Use modules to help boost matching terms**

   By using modules such as the `Apachesolr Term
   Proximity <https://drupal.org/project/apachesolr_proximity>`__
   module, you can provide better results when users are searching for
   phrases. For example, a search for ``parking permits`` will boost
   items that have the exact phrase in their contents above items that
   have the words shown separately.

-  **Create custom code that implements hooks**

   Using hooks like
   ```hook_apachesolr_query_alter()`` <http://drupalcontrib.org/api/drupal/contributions%21apachesolr%21apachesolr.api.php/function/hook_apachesolr_query_alter/7>`__
   can change the queries sent to Solr as those queries are being made.
   Hooks can also introduce complex boosting or ordering commands onto
   the Solr query.

-  **Create *hard* overrides of the searching behavior**

   You can create these overrides by editing the following text files in
   your Solr configuration:

   Notes

   -  We recommend that you only change these files if you're
      knowledgeable with Solr — Acquia Support cannot help you debug
      issues relating to changes to these files.
   -  Acquia-hosted Solr instances (|acquia-product:as|) contain limits
      to the files that can be changed. For more information, see
      `Custom Solr configuration </acquia-search/config>`__.

   -  ``synonyms.txt`` - Allows you to swap words

      For example, a search for ``garage`` can only match ``parking``,
      or searches for both ``garage`` and ``parking`` can be equivalent
      and match either ``garage`` or ``parking`` in content.

   -  ``protwords.txt`` - Allows you to force Solr to always take words
      as they are and not cut them down to their root

      This prevents Solr from
      *`stemming <http://en.wikipedia.org/wiki/Stemming>`__* words.
      Normally, a search for ``parking`` will match ``park``, ``parks``,
      and ``parker``, but adding ``parking`` to ``protwords.txt``
      ensures that searches will only match the exact term: ``parking``.

   -  ```elevate.xml`` <http://wiki.apache.org/solr/QueryElevationComponent#elevate.xml>`__
      - Allows you to force certain items to show up among the first
      results for a specific search

      For example, modifying this file allows you to always display
      ``parking`` as the first result when website visitors search for
      phrases like ``parking`` or ``where to park``. The `Solr best
      bets <https://drupal.org/project/solr_best_bets>`__ module can
      help you construct this file. Once you have created and tested a
      version of this file, `contact Acquia
      Support </support#contact>`__ to begin its placement on your
      server.

   -  ``stopwords.txt`` - Allows you to tell Solr which words are not
      meaningful and should be dropped from queries and indexing

For indexing items that are not nodes, the `Apache Solr Not a
Node <https://www.drupal.org/project/apachesolr_nan>`__ module can be
useful.

.. _monitor:

Monitoring website visitors' search experiences
-----------------------------------------------

You can use tools like `Google
Analytics <http://www.google.com/analytics/>`__ to track searches and
see what your visitors are looking for. It might also be worth tracking
low-result and no-result searches, which can help you with an editorial
strategy to get content into the hands of those visitors.

Due to Varnish caching, sometimes Drupal-side logging of searches will
not give you all the data around what's being searched on your website,
while a client-based (JavaScript) option like Google Analytics will. For
example, the `Apache Solr
Statistics <https://www.drupal.org/project/apachesolr_stats>`__ module
will not properly log all searches while working under Varnish.
