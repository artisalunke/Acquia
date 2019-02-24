.. include:: /common/global.rst

Exact phrase searching
======================

|acquia-product:as| and the `Apache Solr
Search <https://drupal.org/project/apachesolr>`__ module use the
DisMaxRequestHandler, which does not support exact searches with
quotations but instead supports a phrase search. For example, "culture
of service-learning" and "service-learning of culture" would match the
same documents.

This handler has many benefits. It allows the module to search across
multiple fields in the document easily, supports complex weighting of
different search results, and allows you to tune the search results for
your site audience, while requiring no processing of the user's input
keywords.

The advanced configuration option allows you to use full Lucene syntax
using the EDismax parser for all searches. Otherwise, it will be applied
only when the search contains a wildcard ( \*) or question mark ( ?).
For more information about Lucene query syntax, see `Apache Lucene -
Query Parser
Syntax <http://lucene.apache.org/core/3_6_0/queryparsersyntax.html>`__.

These instructions assume you have already installed ApacheSolr.

.. _d7:

Drupal 7
--------

To use Lucene syntax searching in Drupal 7, you must enable it in the
Apache Solr search settings. To do this:

#. In the admin menu, go to **Configuration > Apache Solr search**.
#. Click **Advanced configuration**.
#. In the **Always allow advanced syntax for |acquia-product:as|**
   section, select the **Enabled** option.
#. Click **Save Configuration.**

This is the |acquia-product:as| configuration page for Drupal 7:

|solr-d7-config.png|

.. |solr-d7-config.png| image:: https://cdn2.webdamdb.com/1280_gqb8LqHUzod8.png?-62169955200
   :width: 703px
   :height: 708px
