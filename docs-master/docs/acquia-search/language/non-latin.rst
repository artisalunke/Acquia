.. include:: /common/global.rst

|acquia-product:as| with non-Latin languages
============================================

Although the |acquia-product:as| default schema is optimized for English
searches, Acquia also provides schemas in `other
languages </acquia-search/language>`__. Because most of these languages
are Latin-based and have many grammatical and vocabulary similarities,
they can be used in a relatively straightforward fashion.

There are other languages however, such as Chinese, Japanese, and Korean
(CJK), that use different stemming and spacing rules than Latin-based
languages, which causes the Solr / Lucene search engine to handle them
differently.

You can add support for these languages by using a `custom
|acquia-product:as| Solr configuration </acquia-search/config>`__.

After you have `developed and tested your configuration
changes </articles/how-test-custom-solr-schema-file-locally>`__,
`contact Acquia Support </support#contact>`__ and we will review and
deploy the changed files to your |acquia-product:as| index.

.. _info:

Additional information
----------------------

For additional background information regarding CJK languages, see the
following resources:

-  https://wiki.apache.org/solr/LanguageAnalysis#Chinese.2C_Japanese.2C_Korean
-  https://lucene.apache.org/core/3_5_0/api/all/org/apache/lucene/analysis/cjk/CJKTokenizer.html
-  http://www.slideshare.net/lucenerevolution/japanese-linguistics-in-lucene-and-solr
