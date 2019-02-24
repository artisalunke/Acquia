.. include:: /common/global.rst

How search facets work
======================

Search facets enable users to refine or sort their search result set.
Users can begin with a general search and narrow down the result set as
they understand better what content is available on your website. This
topic gives some examples about how to use search facets. For more
information, see `Configuring search
facets </acquia-search/facets/configure>`__.

.. note::

    The examples on this page require the Apache Solr Search: Current Search
    block to be enabled and displayed. To display the required search block,
    complete the following steps:

#. In the admin menu, select **Structure**.
#. Click the **Blocks** link.
#. In the list to the right of **Facet API: Apache Solr environment:
   Acquia Search : Current Search**, click **Sidebar first**.
#. Click **Save blocks**.

The Current Search Blocks module is part of the Facets API module. For
more information, see `How do I use the new Current Search Blocks
module? <https://www.drupal.org/node/1375674>`__ on Drupal.org.

Using facets in a search
------------------------

In this example, if you search for "drupal" in the search box of this
example website with Apache Solr search running, you get 9107 results.

|Search_facet_ex_1-3.png|

This is probably too many results to be useful for most purposes.
Filtering with search facets lets users drill down into the results
until they find what they are looking for. You can see that the Apache
Solr search module already tells us how many of each content type there
are in our initial search results.

|Search_facet_ex_3_by-type-2.png|

Clicking on any term in a filter block narrows the search results to
include only content that matches both the original and the newly
selected search criteria. Narrowing the search to include only
"Discussion" nodes reduces the result to 6034 nodes and adds
"Discussion" to the facets list of the Current search block:

|Search_facet_ex_4_by-type-ex-1.png|

Users can add multiple additional search filters until they find what
they are looking for or run out of search results.

If you click the minus sign ( ``-``) link next to any search filter in
a filter block, you remove the filter, which updates the search results
to include all content that matches the current filters.

Filter block results example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This block is configured to display the top ten node authors sorted by
the number of nodes they have created:

|Search_facet_ex_5_by-author-1.png|

Unless you change the default value, the **Show more** link at the
bottom of the block displays 10 additional authors (still in order of
contribution quantity) to the list displayed in the block.

.. |Search_facet_ex_1-3.png| image:: https://cdn3.webdamdb.com/md_w19UTKp1WHq2.png?1527793652
   :alt: Search facet example 1
.. |Search_facet_ex_3_by-type-2.png| image:: https://cdn4.webdamdb.com/md_MAaAULlKAs11.png?1527793651
   :alt: Search facet example by type
.. |Search_facet_ex_4_by-type-ex-1.png| image:: https://cdn3.webdamdb.com/md_st8v7AO0S0V3.png?1527793648
   :alt: Search facet example by type 2
.. |Search_facet_ex_5_by-author-1.png| image:: https://cdn4.webdamdb.com/md_6rN9MAeuxc30.png?1527793650
   :alt: Search facet example by author