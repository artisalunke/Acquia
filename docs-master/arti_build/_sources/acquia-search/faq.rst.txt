.. include:: /common/global.rst

|acquia-product:as| FAQ
=======================

* What parts of my website does |acquia-product:as| include in the search index?

  When you configure |acquia-product:as|, you decide what entity types get
  included in the search index and therefore are available to be returned
  to users as search results. This can include things such as nodes like
  articles, pages, and blocks, taxonomy terms, users, and files. In
  addition, you can include file attachments, if you install and configure
  the `Apache Solr Search
  Attachments <https://www.drupal.org/project/apachesolr_attachments>`__
  module.

* Can I search using logical operators?

  Yes, |acquia-product:as| uses the `Apache Lucene Query Parser
  Syntax <http://lucene.apache.org/core/3_6_0/queryparsersyntax.html>`__.

* Can I search using wildcards?

  Yes, you may use "\*" (multiple character) and "?" (single character)
  wildcards. Note that searches may not begin with wildcards or other
  logical operators.

* Does |acquia-product:as| support attachment indexing?

  Yes. This feature requires installing and configuring the `Apache Solr
  Search
  Attachments <https://www.drupal.org/project/apachesolr_attachments>`__
  module. For setup and configuration information, see `Indexing
  attachments </acquia-search/attachments>`__.

* Does |acquia-product:as| support multisite search? Can I combine
  multiple content indexes from multiple hosts in the search results on my
  website?

  Yes. This feature requires installing and configuring the `Apache Solr
  Multisite
  Search <https://www.drupal.org/project/apachesolr_multisitesearch>`__
  module. For setup and configuration information, see `Searching across
  multiple domains </acquia-search/multidomain>`__.

* Does |acquia-product:as| support near-realtime search?

  No, |acquia-product:as| does not support near-realtime search. The
  required configuration would jeopardize the Search-as-a-service platform
  and cause issues with performance and stability. Also, Acquia does not
  allow modifications of the ``solrconfig.xml`` file to increase the
  frequency of auto-commits.

* My website doesn't run in English; what can I expect?

  |acquia-product:as| can index websites in most languages, but
  |acquia-product:as| passes content through a language-specific
  `stemmer <http://en.wikipedia.org/wiki/Stemming>`__ during indexing,
  depending on the search schema you have set for your website.
  |acquia-product:as| offers search schemas for Dutch, French, German, and
  Spanish, as well as English. You can search other languages, but the
  search may produce less relevant search results because partial words,
  plurals and other variations may not be correctly indexed. For more
  information, see `Selecting a language </acquia-search/language>`__.

  If your website is in a language other than Dutch, English, French,
  German, or Spanish, `contact Acquia support </support#contact>`__ to see
  whether a search schema specific to that language can be made available
  for you.


* Does |acquia-product:as| support server-side Solr configuration
  modifications?

  You can select standard configurations on the Search page of the Acquia
  user interface. If you are an Enterprise customer who needs a custom
  configuration (typically a ``schema.xml`` or ``synonyms.txt`` file), you
  should open a support ticket and provide the complete configuration
  file. Note that the frequency and nature of custom search configuration
  changes is limited. See `Configuring
  |acquia-product:as| </acquia-search/config>`__ for details. If you need
  help developing a custom configuration, please contact Acquia sales to
  discuss your needs and implementation possibilities through Acquia's
  professional services division.

* Can I use the Search API module?

  Yes, you can use the Search API module with |acquia-product:as|. This is
  an alternative to using the Apache Solr Search Integration module.
  |acquia-product:as| for Drupal 8 requires Search API, and will not use
  ApacheSolr.

  Do not attempt to use both the Search API module and the Apache Solr
  Search Integration module in the same environment.

  For more information, read `Using the Search API </acquia-search/search-api>`__.

* Can I use Nutch to index my non-Drupal data for search?

  |acquia-product:as| does not support using
  `Nutch <http://nutch.apache.org/>`__ to index external data. For data
  security, the |acquia-product:as| architecture requires authentication,
  which Nutch does not natively support.

  For suggestions for combining non-Drupal data with |acquia-product:as|,
  see the `Bridge the gap between Drupal & Non-Drupal content using
  RDFa/Semantic
  Data <https://dev.acquia.com/blog/bridge-gap-between-drupal-non-drupal-content-using-rdfasemantic-data>`__
  blog post on the Acquia Developer Center.

* What counts as a search query toward my entitlement?

  Acquia counts only ``select`` (searching) and ``update`` (indexing)
  requests that make it to our balancers. These numbers are the same that
  we show on your |acquia-product:anw] Search graphics.

* Drupal modules can index more than one item at a time in a single Solr
  update request.

