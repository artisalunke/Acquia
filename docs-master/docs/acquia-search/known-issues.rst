.. include:: /common/global.rst

Known issues in |acquia-product:as|
===================================

This page describes the known issues with |acquia-product:as|.

General
-------

-  Solr search has difficulty `handling large
   attachments </articles/issues-large-attachments-and-solr-search>`__.

.. _d7:

Drupal 7
--------

-  The `Workbench
   Moderation <https://drupal.org/project/workbench_moderation>`__
   module can cause problems with ApacheSolr search integration.
-  Search API is `prone to memory errors during
   indexing <https://www.drupal.org/node/1137734>`__.
-  Search API provides fewer configuration options than ApacheSolr
   integration in Drupal 7.

.. _d8:

Drupal 8
--------

-  The |acquia-product:anc| module has a conflict with the
   remote_stream_wrapper module.
   *Workaround* - Apply the `|acquia-product:anc|
   patch <https://www.drupal.org/node/2891977>`__ available on
   Drupal.org.
-  Search API is not currently capable of displaying result snippets —
   the full node output displays as the search result.
   *Workaround* - Create a **Search result** view mode to output
   something smaller than the full node. To employ this workaround,
   complete the following steps:

   #. Go to **Structure > Content types > Article > Manage display**.
   #. In the **Custom display settings** section, select the **Search
      result highlighting input** check box.
   #. Click **Save**.
   #. Go to **Structure > Content types > Article > Manage display >
      Search result highlighting input**. These settings control each
      search result's output.
   #. To display result snippets, edit the appropriate field. For
      example, to make the **Body** field display result snippets,
      complete the following steps:

      a. In **Format**, click **Trimmed**.
      b. Click the gear icon. The webpage displays the **Trimmed limit**
         field.
      c. In the **Trimmed limit** field, enter ``200`` to trim the body
         field to 200 characters.
      d. Click **Update**.

      You have now set the **Body** field to display trimmed output as
      the search result.

-  There is an `issue with attachment
   indexing <https://www.drupal.org/node/2695355>`__, related to Tika,
   being worked on by the community.
-  `Facets <https://www.drupal.org/project/facets>`__ modules currently
   does not have a stable release.
-  Users should be aware of `Views problems with non-SQL query
   plugins <https://www.drupal.org/node/2484565>`__.
