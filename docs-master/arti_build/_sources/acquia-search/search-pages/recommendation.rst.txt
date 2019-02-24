.. include:: /common/global.rst

Creating content recommendation blocks
======================================

A content recommendation block displays a small number of items that are related to the current page in a "More Like This" block. Here are a couple of examples:

|More Like This example| |More Like This example 2|

The Apache Solr Search module comes with a "More Like This" block already configured, with a name of ``More like this``. You can configure this default "More Like This" block, or create additional "More Like This" blocks, using the **Pages/Blocks** Admin page.

To create a new "More Like This" block, click the **Add search block "More Like This"** link.

|Add search block|

To configure an existing "More Like This" block, click the Configure link under Operations.

.. note::

   A "More Like This" block uses data from the search index. If a user is viewing a node that has not yet been added to the search index, any associated content recommendation block will be empty.

Configuring a "More Like This" block
------------------------------------

You can configure the block's title, name (the string displayed to website visitors), and the maximum number of related items to display in the block.

|Configuring block|

Finding related content
-----------------------

You can configure which fields are matched by the search engine in determining whether items are related. Under **Fields for finding related content**, you can select one or more of:

- The full rendered content (the node body)
- Title or label
- Path alias
- Extra rendered content or keywords
- Author name

In most cases, you will get the best results by selecting **Title or label** and **All taxonomy term names**.

Tuning similarity comparisons
-----------------------------

You may find that the items returned in a "More Like This" block are not a good match for the current item. You can experiment with the settings under **Advanced Configuration** (in addition to the settings under **Fields for finding related content**) to get better matches or better performance.

- **Minimum term frequency** |br| 
  A term must appear X number of times in a document before it is considered relevant for comparison.
- **Minimum document frequency** |br| 
  This performance optimization feature sets the number of documents (Drupal content in this case) that have to contain similar content before comparisons can be made. This must be a minimum of two.
- **Minimum word length** |br| 
  This performance optimization feature eliminates short words (such as "the" and "it") from similarity comparisons.
- **Maximum word length** |br| 
  This performance optimization feature eliminates very long words (such as "supercalifragialisticexpialidocious") from similarity comparisons.
- **Maximum number of query terms** |br| 
  If a content recommendation does not return any recommendations, you can either check more settings under Fields for finding related content or increase the maximum number of query terms here. This setting can affect your website performance.

Configuring filters
-------------------

You can filter a "More Like This" block by content types and by additional queries.

Filtering by content types
~~~~~~~~~~~~~~~~~~~~~~~~~~

Under **Content Types**, select the content types that you want to include as related items.

Filtering by additional queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your "More Like This" block can use queries to further filter recommendations. In the **Additional Query** field, enter one or more comma-separated filter queries to apply by default. Query filters use Lucene query syntax. For information about Lucene query syntax, see `Apache Lucene - Query Parser Syntax <http://lucene.apache.org/core/3_6_0/queryparsersyntax.html>`__.

Configuring where to display "More Like This" blocks
----------------------------------------------------

Just like any other Drupal block, you can configure where and how a "More Like This" block should be displayed.

- Use **Region settings** to select the page regions and themes where you want a "More Like This" block to be displayed.
- Use **Visibility settings** to limit the display of a "More Like This" block by page, content type, or role, or enable users to customize in their account settings whether the "More Like This" block is displayed.

Best practices for content recommendation blocks
------------------------------------------------

Note the following best practices and recommendations regarding the use of recommendation blocks on your website.

Multiple recommendation blocks slow page load times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every content recommendation block makes its own separate search query. Having multiple recommendation blocks on a node page can result in a perceivable page loading lag-time as requests are made by each block.

Page and block caching
~~~~~~~~~~~~~~~~~~~~~~

When you use content recommendation blocks, it is advisable to enable page and block caching on your website. To enable block caching, complete the following steps:

#. In the admin menu, select Configuration, and then click the Performance link (``http://example/#overlay=admin/config/development/performance``). The Performance page opens.
#. Under **Caching**, select **Cache blocks**, and then click **Save configuration**.

.. |More Like This example| image:: https://cdn4.webdamdb.com/1280_gsFip8p8YW68.png?1527793650
   :alt: "More Like This" example
.. |More Like This example 2| image:: https://cdn4.webdamdb.com/1280_kSexUheWxn12.png?1527793651
   :alt: "More Like This" example
.. |Add search block| image:: https://cdn3.webdamdb.com/1280_6UJ3RfqRG927.png?1527793650
   :alt: Add search block "More Like This"
.. |Configuring block| image:: https://cdn3.webdamdb.com/1280_6UJ3RfqRG927.png?1527793650
   :alt: Configuring "More like this" block
