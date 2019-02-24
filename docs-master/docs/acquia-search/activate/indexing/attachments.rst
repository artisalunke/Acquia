.. include:: /common/global.rst

Indexing attachments
====================

In addition to Drupal nodes, |acquia-product:as| results presented to your users can include files that contain matches to the search query. File formats that can be indexed include HTML, XML, Microsoft Office documents, OpenDocument, PDF, RTF, ``.zip``, and other compression formats, text formats, audio formats, video formats, and more. For a complete list of supported document formats, see the `Apache Tika documentation <http://tika.apache.org/1.10/formats.html>`__.

Search results for attached files display a direct link to the attached file as well as the node to which it is attached:

|Attachments in search results|

Searching file attachments requires the Apache Solr Attachments module. The Apache Solr Attachments module uses the `Apache Tika Content Analysis Toolkit <http://tika.apache.org>`__ to detect and extract meta data and structured text content from a wide variety of file formats. Once extracted, this information is indexed and available to your users via |acquia-product:as|.

.. note::

    -  Ensure that the most recent versions of your `modules
       </acquia-search/modules>`__ are in use. If you use older
       versions, you may experience problems with extracting attachments.
    -  Drupal 8 requires that you install a patch, available from the
       following `Drupal.org
       posting <https://www.drupal.org/node/2696901#comment-11906929>`__.

Installing the Apache Solr Attachments module
---------------------------------------------

To index attachments, complete the following steps:

#. Install and enable the `Apache Solr
   Attachments <https://www.drupal.org/project/apachesolr_attachments>`__
   module on your website.
#. Go to the **Apache Solr search > Configuration > Default Index**
   page.
#. In the **Configuration** section, select the **File** check box as an
   entity to be indexed.
#. Click **Save**.

|What to index|

The Apache Solr Search configuration page now displays the Attachments
tab. Use the settings on this tab to configure the file attachment
indexing settings.

.. note::

    The Apache Solr Attachments module is compatible only with Apache Solr
    Search. If you are using the Search API module, you can use the `Search
    API attachments
    module <https://www.drupal.org/project/search_api_attachments>`__ instead.
    `Configure it </acquia-search/modules/attachments>`__ to work with
    |acquia-product:as|. Be sure to use version 7.x-1.4 or later; earlier
    versions of the Search API attachments module are not compatible with
    |acquia-product:as|.

Configuring file attachment index settings
------------------------------------------

The Attachments tab of the Apache Solr Search configuration page
contains the following configuration options for indexing attachments in
Apache Solr Search:

|Search - File Attachments configuration tab|

.. list-table::
   :widths: 5 15 80
   :header-rows: 1

   * - 
     - Item
     - Description
   * - 1
     - **Excluded file extensions**
     - A space-separated list of file extensions that are excluded from 
       indexing. Modify this list to suit the needs of your site. Extensions are
       internally mapped to a MIME type, so it is not necessary to include 
       variations that map to the same type. For example, ``tif`` is sufficient 
       to exclude both the ``tif`` and ``tiff`` file extensions.
   * - 2
     - **Extract using**
     - |acquia-product:as| includes Apache Tika for indexing documents. For 
       best performance, select **Solr (remote server)**.
   * - 3
     - **Tika directory**
     - Leave this blank.
   * - 4
     - **Tika jar file**
     - Leave this set to the default value.

Index and cache controls
~~~~~~~~~~~~~~~~~~~~~~~~

File attachments get indexed at the same time as their parent entities.
Under **Actions**, you can:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - **Clear the attachment text extraction cache**
     - Clears all extracted data.
   * - **Delete the attachments from index**
     - Deletes all the attached files on your site from the |acquia-product:as| 
       index. You need to do this if you change what types of files should be 
       indexed, if your search index becomes corrupted, or if you install a 
       new ``schema.xml``.
   * - **Test your tika extraction**
     - Tests if your Tika configuration settings work.

.. |Attachments in search results| image:: https://cdn3.webdamdb.com/md_cnEpXSxh9QQ3.png?1527793736
   :alt: Attachments in search results
.. |What to index| image:: https://cdn3.webdamdb.com/md_2gzSFhCd5M82.png?1527793648
   :alt: Select the data to index
.. |Search - File Attachments configuration tab| image:: https://cdn4.webdamdb.com/md_g4hWxKHA72C7.png?1527793652
   :class: shadow bord
   :alt: Search file attachments configuration tab

