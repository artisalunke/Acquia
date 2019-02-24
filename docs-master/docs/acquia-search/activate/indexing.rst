.. include:: /common/global.rst

Indexing your website
=====================

.. toctree::
   :hidden:
   :glob:

   /acquia-search/activate/indexing/attachments/
   /acquia-search/activate/indexing/index-reports/

|acquia-product:as| indexes your website, making potentially any page or
other entity findable by search. This topic describes what gets indexed
and when.

Which items get indexed
-----------------------

You can configure which entity types (like nodes, taxonomy terms, files,
commerce items, and users) on your website get indexed. By default, all
content type nodes are indexed. To add other entities, you need to add
contributed modules such as `Apache Solr
Attachments <https://www.drupal.org/project/apachesolr_attachments>`__,
`Apachesolr User <https://www.drupal.org/project/apachesolr_user>`__, or
`Apachesolr Term <https://www.drupal.org/project/apachesolr_term>`__.
You can exclude entity types from the search index by unselecting them
on the **Apache Solr search > Configuration > Default Index** page,
under **Configuration**.

|What to index|

When items get indexed
----------------------

|acquia-product:as| indexes your website every time cron runs. In
ordinary operation, you don't need to do anything for new and modified
content to be added to your search index. However, you do have manual
control over search indexing.

Indexing a large number of items at once can have a negative effect on
your website's performance. For that reason, the default behavior for
|acquia-product:as| is to index in increments of 50 items every time
cron runs. You can modify the number of items to index per cron run on
the **Apache Solr Search > Configuration > Settings** page, under
**Advanced Configuration**. Note that the higher you set this number,
the faster your site will be indexed, but the more impact search
indexing will have on your website's server.

Manual control of search indexing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Actions** section on the **Apache Solr Search Configuration >
Default Index** page gives you manual control over search indexing. You
might want to choose one of these options if you have new content that
you want to index immediately:

-  Click **Index queued content (50)** to index as many items as running
   cron would.
-  Click **Index all queued content** to index all items that haven't
   yet been indexed. This can put an increased load on your server and
   potentially have a negative effect on your website's performance.

|Search index actions|

Re-indexing your website
~~~~~~~~~~~~~~~~~~~~~~~~

You can re-index your entire website by clicking **Queue all content for
re-indexing**. Depending on the quantity of content on your site, this
will take some time. In the ordinary course, 50 items will be indexed
every time cron runs. You can re-index faster, at the cost of
potentially slower website performance, by then clicking **Index all
queued content**.

Deleting the search index
~~~~~~~~~~~~~~~~~~~~~~~~~

To delete your search index, click the **Delete the Search & Solr
index** button. Most users will never need to do this. The following
situations may require you to use this option:

-  Your search index has become corrupt.
-  You need to eliminate development data from the site index when you
   launch a site and add production data.
-  You move your Acquia subscription to a different website.
-  You switch from your own Solr server to |acquia-product:as|, or vice
   versa.

Setting environments to read-only
---------------------------------

In many use cases, you will want |acquia-product:as| to index only your
production environment and not your development or testing environments.
You can set your non-production environments to read-only, so that
searching is available on all your environments, but content changes on
non-production environments will not affect your production search
index. For information about how to do this, see `Read-only Apache Solr
search
index <%5Bacquia-product:kb%5Darticles/read-only-apache-solr-search-index>`__.

.. |What to index| image:: https://cdn4.webdamdb.com/md_2gzSFhCd5M82.png?1527793648
   :alt: What to index
.. |Search index actions| image:: https://cdn2.webdamdb.com/md_UTM7kpfpNHX4.png?1527793648
   :alt: Search index actions
