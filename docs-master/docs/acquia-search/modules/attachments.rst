.. include:: /common/global.rst

Configuring the Search API attachments module
=============================================

If you use the `Search API attachments <https://www.drupal.org/project/search_api_attachments>`__ module for indexing and searching file attachments, you need to configure it to work with |acquia-product:as|. To do this, complete the following steps, depending on your version of Drupal:

-  *Drupal 8*

   .. note::

        You must already have a working |acquia-product:as| configuration for your website.

   #. `Install </resource/module-install-d8>`__ the `Search API attachments <https://www.drupal.org/project/search_api_attachments>`__ module, which requires using Composer.
   #. Sign in to your Drupal website as an administrator, and then enable the module.
   #. In the admin menu, go to **Configuration > Search API attachments**.
   #. In the **Extraction method** list, click **Solr extractor**.
   #. In the **Solr server** list, click **Acquia Search API server** (which uses |acquia-product:as| as the backend).
   #. Click **Submit and test extraction** to test.

      .. note::

         As of August 9, 2017, the Solarium library (required by the Search API Solr module) requires a patch to properly extract files using a remote Solr instance (including |acquia-product:as|). If you experience issues when clicking **Submit and test extraction**, attempt to patch Solarium by running the following command in your Drupal docroot (the *vendor* folder may also be at the same level as your docroot):

      .. code-block:: none
      
         cd vendor/solarium/solarium && wget https://patch-diff.githubusercontent.com/raw/solariumphp/solarium/pull/519.patch && patch -p1 <519.patch

   |Search Tika extractor configuration screen|

-  *Drupal 7*

   #. Install and enable both the Search API attachments module and its requirements.
   #. Go to the Search API configuration page, and then click the **Search API attachments** tab.
   #. In the **Solr Extraction Settings** section, in the **Solr extracting servlet path** field, enter ``extract/tika``.

      |Extracting servlet path|

.. |Search Tika extractor configuration screen| image:: https://cdn2.webdamdb.com/1280_1o3M3DQX6Y68.png?1526476115
   :width: 621px
   :height: 460px
.. |Extracting servlet path| image:: https://cdn4.webdamdb.com/1280_q8hw6i9NmD74.png?1526475865

