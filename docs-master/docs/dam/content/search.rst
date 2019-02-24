.. include:: /common/global.rst

Searching for assets in |acquia-product:dam|
============================================

|acquia-product:dam| offers basic search as well as advanced searching
with filters.

.. _basic:

Basic search
------------

Basic search allows you to perform a quick search across all metadata
fields such as keywords and description.

#. Sign in to |acquia-product:dam|.
#. Enter the search term(s) in the search box and click **Enter/Return**
   on your keyboard. (`Read more about search
   tips. </dam/content/search#tips>`__)
#. Search terms/parameters will display above the asset thumbnails.
   Click the ``(X)`` to remove a search parameter:
   |Basic search|
#. Click **Status filters** to filter your results by asset status.
   Corresponding statuses:

   -  *Setting a folder or asset status* - active, inactive, expired and
      unexpired
   -  *Approval requests* - approved, rejected and pending
   -  *Publishing* - published and unpublished

#. Click each status type that you want returned in your search results.
#. Click the file type again to remove it from the list.
   |Search filter|

.. _advanced:

Advanced Search
---------------

.. _image:

Image filters
~~~~~~~~~~~~~

**Image filters** allow you to filter your results by resolution, size
and orientation. To filter:

#. Click **Advanced option** under the search box.
#. Click **Image filters**.
#. To filter on images by:

   -  Resolution, width and/or height:

      #. Enter the desired resolution or size into the corresponding
         box.
      #. Click the dropdown menu to set the filter by minimum, maximum
         or equal measurements.
      #. Click **Apply**.

   -  To filter on images by orientation:

      #. Click **Vertical**, **Horizontal** or **Square** to filter on
         orientation.
      #. Click **All** to include all asset orientations.
         |Search asset orientations|

.. _keyword:

Keyword filters
~~~~~~~~~~~~~~~

**Keyword filters** allow users to filter results by selecting keywords
from the predefined keyword taxonomy. (Read more about creating a
keyword taxonomy.) To filter:

#. Click **Advanced options** under the search box.
#. Click **Keywords**.
#. Check the box next to the keyword(s) you want to search for.
#. If you select multiple keywords, click **AND** to return assets that
   have all keywords associated or **OR** to return assets that have any
   of the keywords associated.
#. Uncheck the box next to **Auto select parents** if you don’t want
   parent keywords to be selected when choosing a nested keyword.

.. _archival:

Archival filters
~~~~~~~~~~~~~~~~

**Archival filters** allow customers with the archival storage add-on
feature to filter on assets that are archived or not archived. (Read
more about `archival storage </dam/services/archive>`__.)

#. Click **Advanced options** under the search box.
#. By default, assets that aren’t archived will be returned in search
   results. Click **Archived** to filter on assets that have been
   archived or **All** to have all assets returned.

.. _tips:

Additional search tips
----------------------

**Folder search**: You can narrow your search results to a specific
folder (including nested folders) by first selecting the desired folder
in the **Folder tree** and entering your search variables.

**Partial match**: When searching, partial word matches are not
typically returned (with the exception of filenames, see below). For
example, searching ``“brand”`` will not return assets with
``“branding”`` associated. You can use an asterisk ``(*)`` to expand
your search results.

-  *Format*: Add an asterisk before or after the term. Don’t add a space
   between the term and the asterisk.
-  *Example*: ``brand*``
-  *Results*: Returns assets with brand, branding, brands or other terms
   containing “brand.”

**Filenames**: When searching, partial filenames will be returned. For
example, searching for brand will return a filename of “Superfly
Branding.” In addition, you can either search for the entire filename,
including or excluding the file extension.

**In-document searching**: Certain assets, such as Word documents and
PowerPoint presentations, will be returned if the searched term is found
in the text of the file. (Read more about the file types that allow for
in-document searching.)

**Empty field operator**: Find assets that don’t contain any metadata
for a specific metadata field. For example, you may be looking for
assets without any keywords applied.

-  *Format*: Enter the metadata field name into brackets beginning with
   a question mark: ?[metadata field name]
-  *Example*: ``?[keyword]``
-  *Result*: Returns assets that have no keywords associated.

**AND operator**: Returns assets with all searched terms associated. The
terms may be found in any order and any metadata field (see below to
search for phrases).

-  *Format*: Enter the terms separated by a space or an “and”.
-  *Example*:

   -  ``brand guidelines``
   -  ``brand AND guidelines``

-  *Results*: Returns assets that have both “brand” and “guidelines”
   associated.

**OR Operator**: Returns results containing any of your search terms.

-  *Format*: Enter the terms separated by an “or”.
-  *Example*: ``brand OR guidelines``
-  *Results*: Returns assets that that have either “brand” or
   “guidelines” associated.

**Negative Operator**: Exclude a word from the search results.

-  *Format*: Add a minus sign in front of the word. Don't include a
   space between the minus sign and the word.
-  *Example*: ``brand -guidelines``
-  *Results*: Returns assets where the term “brand” is associated but
   not “guidelines”.

**Phrases or exact match**: Returns results where the searched terms are
found together in the metadata or document and in the same order.

-  *Format*: Include quotation marks around the search terms.
-  *Example*: ``“new brand guidelines”``
-  *Results*: Returns assets with the phrase “new brand guidelines”
   associated.

**Searching by filenames**: Filenames are treated differently than other
metadata fields and keywords. When a basic search is conducted, all
metadata fields are queried. For filenames, the search parses filenames
and returns assets with any of the terms or phrases in the filename.
This ensures broader results are retrieved. For example, if you search
``brandguidelines123``, the following filenames could be retrieved:

-  ``BrandGuidelines123.jpg``
-  ``BrandGuidelines456.jpg``
-  ``BrandGuidelinesandLogos.eps``
-  ``123_photoshoot.jpg``

To search an exact match for a filename, surround it with quotes. The
closest match will always be ranked at the top of search results. To
locate an asset with the filename ``brandguidelines123``, search
``“brandguidelines123”``. The file extension is not needed, but may be
included.

.. |Basic search| image:: https://cdn2.webdamdb.com/1280_wu4pccN8ryv2.png?1526476110
   :width: 550px
   :height: 275px
.. |Search filter| image:: https://cdn3.webdamdb.com/1280_MAkABYVEWR14.png?1526475999
   :width: 550px
   :height: 275px
.. |Search asset orientations| image:: https://cdn2.webdamdb.com/1280_ANASta0UWVl4.png?1526475829
   :width: 550px
   :height: 275px
