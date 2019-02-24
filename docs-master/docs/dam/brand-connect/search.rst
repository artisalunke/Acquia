.. include:: /common/global.rst

Searching in |acquia-product:bc|
================================

This page will review:

-  `Basic search <#search>`__
-  `Facets <#facets>`__
-  `Watch assets <#watch>`__
-  `Additional search tips <#tips>`__

.. _search:

Basic search
------------

Basic search allows you to perform a quick search across all metadata
fields, such as keywords and descriptions.

#. Sign in to |acquia-product:bc| and navigate to the asset library.
   This is typically done by clicking **Assets** on the top navigation,
   but this might be different in your DAM.
#. Enter the search term(s) in the search box and click the search icon
   or Enter/Return on your keyboard.
#. Search terms/parameters will display above the asset thumbnails.
   Click the **X** to remove a search parameter.

Facets
------

Facets refer to the metadata search filters that make it easy to search
|acquia-product:bc|. Administrators control which metadata filters
display as facets. (Read more about `activating and deactivating
facets </dam/admin/metadata>`__.)

To search using facets:

#. Sign in to |acquia-product:bc| and navigate to the asset library.
   This is typically done by clicking **Assets** in the top navigation,
   but if you’ve customized your navigation this might be different in
   your DAM.
#. The facets will display on the left-hand side of the screen. The
   number next to the facet value indicates how many assets can be found
   in that category. Click **more** to view all available values for a
   particular facet.
#. Select the check box next to the value that you’d like to filter your
   search results for, which will display assets tagged with this value.
   Continue to select the check box next to other values to further
   narrow your results.
#. Search terms and parameters will display above the asset thumbnails.
   Click the **X** to remove a search parameter.

Additionally, you can select these options:

-  Click the down arrow |Down arrow| next to the facet name to hide the
   values for that particular facet.
-  Click **Hide Facets** to hide all facets.

.. _watch:

Watch assets
------------

You can Watch assets to keep track of things you access regularly and to
receive notifications.

#. Select the lightbox, folder or asset.
#. Click the watch icon |Watch| to watch an item, click it again to stop
   watching.

.. _tips:

Additional search tips
----------------------

Search has several additional features that can help give you better
results.

-  *Folder search* - You can narrow your search results to a specific
   folder (including nested folders) by first selecting the desired
   folder in the folder tree and entering your search variables.
-  *Partial match* - When searching, partial word matches are not
   typically returned (with the exception of filenames.) For example,
   searching ``brand`` will not return assets with ``branding``
   associated. You can use an asterisk (``*``) to expand your search
   results.

   ``brand*``

   returns results for ``brand``, ``branding``, and so on.

-  *Filenames* - When searching, partial filenames will be returned. For
   example, searching for brand will return a filename of “Superfly
   Branding.” In addition, you can either search for the entire
   filename, including or excluding the file extension.
-  *In-document searching* - Certain assets, such as Word documents and
   PowerPoint presentations, will be returned if the searched term is
   found in the text of the file. See `Managing your supported file
   formats </dam/admin/system/files>`__ for additional information.
-  *Empty field operator* - Find assets that don’t contain any metadata
   for a specific metadata field. For example, you may be looking for
   assets without any keywords applied. Enter the metadata field name
   into brackets beginning with a question mark, and it will return
   assets that do not have that metadata. For example:

   ``?[keyword]``

   returns assets that have no keywords attached.

-  *AND operator*- Returns assets with all searched terms associated.
   The terms may be found in any order and any metadata field. Enter the
   terms separated by a space or an *and*.
-  *OR operator* - Returns results containing any of your search terms.
   Enter the terms separated by an *or*
-  *Negative operator* - Excludes a word from the search results. Add a
   minus ``-`` sign in front of the word. Don't include a space between
   the minus sign and the word.
-  *Phrases or exact match* - Returns results where the searched terms
   are found together in the metadata or document and in the same order.
   Include quotation marks around the search terms.

   ``“new brand guidelines”``

-  *Searching by filenames* - Filenames are treated differently than
   other metadata fields and keywords. When a basic search is conducted,
   all metadata fields are queried. For filenames, the search parses
   filenames and returns assets with any of the terms or phrases in the
   filename. This ensures broader results are retrieved. For example, if
   you search ``brandguidelines123``, the following filenames could be
   retrieved:

   -  BrandGuidelines123.jpg
   -  BrandGuidelines456.jpg
   -  BrandGuidelinesandLogos.eps
   -  123_photoshoot.jpg

   To search an exact match for a filename, surround it with quotes. The
   closest match will always be ranked at the top of search results. To
   locate an asset with the filename brandguidelines123, search for
   ``“brandguidelines123”``. The file extension is not needed, but may
   be included.

.. |Down arrow| image:: https://cdn2.webdamdb.com/100th_sm_Aoxb6jHhvGE3.png?1527259214
   :width: 25px
   :height: 16px
.. |Watch| image:: https://cdn4.webdamdb.com/100th_sm_UkwpoZMjwY71.png?1526475553
   :width: 30px
   :height: 26px
