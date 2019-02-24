.. include:: /common/global.rst

Selecting a language
====================

.. toctree::
   :hidden:
   :glob:

   /acquia-search/language/*

|acquia-product:as| can index websites in most languages, but
|acquia-product:as| passes content through a language-specific stemmer
during indexing, depending on the search schema you have set for your
website. |acquia-product:as| offers search schemas for the following
languages:

-  English
-  Dutch
-  French
-  German
-  Spanish

This means languages other than the schema's language are likely to
produce lower-quality search results because partial words, plurals, and
other variations may not be correctly indexed. You can still search in
most languages, but the search results will not be as good as they would
be with a language-specific schema.

To select a language-specific schema, complete the following steps:

#. Sign in to the |cloud-ui|_ with the *Owner* or *Administrator* role.
#. Select the application that you want to work with, and then in the
   left menu, click **Acquia Search**.

   |Select Acquia Search|

#. To edit your settings, click the **Edit** icon in the upper right
   corner.

   |Edit settings|

#. In the **Acquia Search configuration set** list, click the
   version that matches your Drupal version and preferred language. For
   example, for Dutch, click **apachesolr 7.x-1.0+, Optimized for
   Dutch**.

   |Select a language|

#. Click **Save**.

If your website is in a language other than English, Dutch, French,
German, or Spanish, `contact Acquia Support </support#contact>`__ to
determine whether a search schema specific to that language can be made
available for you.

.. |Select Acquia Search| image:: https://cdn2.webdamdb.com/220th_sm_ADQoUIvM7vJ0.png?1527793649
   :alt: Select Acquia Search in the UI
.. |Edit settings| image:: https://cdn4.webdamdb.com/100th_sm_2qD2mc0xMun5.png?1527793651
   :width: 76px
   :height: 86px
   :alt: Edit your settings using the search edit icon
.. |Select a language| image:: https://cdn2.webdamdb.com/md_M8M2N20oXzt2.png?1527793649
   :alt: Select a language


.. |cloud-ui| replace:: \ |acquia-product:ui|\
.. _cloud-ui: https://cloud.acquia.com
