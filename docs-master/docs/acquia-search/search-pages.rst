.. include:: /common/global.rst

Creating search pages
=====================

.. toctree::
   :hidden:
   :glob:

   /acquia-search/search-pages/*

A search page displays search results to your site visitors. The Apache
Solr Search module comes with a search page already configured, with a
path of ``/search/site``. You can configure this default search page, or
create additional search pages or blocks, using the **Apache Solr search
> Pages/Blocks** configuration page. You can use different search pages
and search blocks, each of which can be designed and configured to
present the right search results with the right style for the context.
For example, you might want different search pages for these situations:

-  You have multiple search environments and in some cases you want a
   multi-site search and in others you want to present results from just
   one search environment.
-  You want to exclude some content types in some contexts, but include
   them in other contexts.
-  You want to show only content from a specific bundle (for example,
   blogs or webinars).
-  You want to have separate sections in your site with separate search
   behavior or themes.

To create a new search page, click the **Add a search page** link, or
copy an existing search page by clicking the **Clone** link under
**Operations**.

To configure an existing search page, click the **Edit** link.

Configuring a search page
-------------------------

Every search page, like every other Drupal page, needs a label that
identifies it in the Drupal content administration pages. In addition,
you can add a description. This can be helpful to identify the context
the search page should be used in.

Under Search Page Information, you can configure:

|Configuring a search page|

-  **Search environment** - If you don't specify a search environment,
   this search page will be disabled. If you only have one search
   environment, specify Acquia Search. For more information, read `Using
   multiple search environments </acquia-search/environments>`__.
-  **Title** - This is the HTML title that the browser displays. You can
   use the variable ``%value`` to include the search term in the title.
   For example, if you set the search term title to
   ``Search results for %value`` and the user searches for ``Gold``, the
   search page will display the title **Search results for Gold**.
-  **Search type** - If you are filtering on a value from the search
   path, you can specify the search type.
-  **Path** - The path for the search page. Search keywords will appear
   as query arguments at the end of the path.

Configuring custom filters
--------------------------

Your search page can use custom filters to apply to all searches. Select
**Custom filter**, then enter one or more comma-separated filter queries
to apply by default. For example, you could filter your search pages to
return only blog content with this custom filter:

`` bundle:blog``

Custom filters use Lucene query syntax. For information about Lucene
query syntax, read `Apache Lucene - Query Parser
Syntax <http://lucene.apache.org/core/3_6_0/queryparsersyntax.html>`__.

Configuring Advanced Search Page Options
----------------------------------------

Under **Advanced Search Page Options**, you can configure:

-  **Results per page** - The number of search results to display on
   each page of the search results.
-  **Enable spell check** - Offer spelling suggestions in a "Did you
   mean...?" message displayed above the search results.
-  **Enable the search box on the page** - Display the search box on the
   page.
-  **Allow user input using the URL** - You can allow users to manually
   facet the search results using query parameters in the URL (for
   example, ``example.com?q=test&fq=userinput``). This works for users only
   after they have executed a search using a search term. We recommend
   that you do not enable this.

Configuring behavior on empty search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under **Advanced Search Page Options**, you can configure how the search
page behaves when a search does not return any results. If you have
enabled the Facets API, you can select one of:

-  Show search box.
-  Show enabled facets' blocks under the search box. This is the default
   behavior, if you have enabled the Facets API.
-  Show enabled facets' blocks in their configured regions.
-  Show enabled facets' blocks in their configured regions and first
   page of all available results.

For more information, read `Filtering search
results </acquia-search/facets>`__.

.. |Configuring a search page| image:: https://cdn4.webdamdb.com/md_cTnO8tnK5VT2.png?1527793649
   :alt: Configuring a search page
