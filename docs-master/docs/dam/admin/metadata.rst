.. include:: /common/global.rst

Configuring the metadata schema
===============================

.. toctree::
   :hidden:
   :glob:

   /dam/admin/metadata/*

Metadata is the information used to describe an asset and the primary
driver of search. It not only enhances searchability, but can also track
key pieces of information such as copyright, location, image source, and
more.

It’s important that your metadata is consistent. There are several tools
to assist with this, including creating picklists and a keyword
taxonomy. (Read more about `best practices for building a metadata
strategy </dam/admin/metadata/best>`__.)

.. _configure:

Configure the metadata schema
-----------------------------

Admins can configure the metadata schema.

#. Sign in to |acquia-product:dam|.
#. Click the **Settings** icon |Settings| in the top navigation, and
   then click **Metadata Schema**.
#. Click one of the four metadata schema tabs: **XMP**, **EXIF**,
   **Keywords**, or **Facets**.

XMP
---

`XMP <https://en.wikipedia.org/wiki/Extensible_Metadata_Platform>`__
(eXtensible Metadata Platform) is metadata that can be edited by admins
and contributors. Some examples include:

-  Photographer
-  Copyright information
-  Caption and description
-  Configurable custom fields

|acquia-product:dam| supports XMP and
`IPTC <https://en.wikipedia.org/wiki/IPTC_Information_Interchange_Model>`__
(International Press Telecommunications Council) Core metadata
standards, so information that is added to an asset in a program like
Bridge or Photoshop will be available in |acquia-product:dam|.

The following section outlines configuring the XMP:

**Status**: Metadata fields must be *active* to display in the asset
details panel, and allow admins and contributors with asset-editing
permissions to apply values to the active metadata fields. (Read more
about `editing metadata </dam/content/mobile/manage>`__.) The active
metadata will display in the center window of the XMP tab. Inactive
metadata will be listed in the **Inactive XMP Fields** dropdown at the
top right-hand corner of the screen. To activate or deactivate a
metadata field:

-  *To activate* - Click **Add a field** in the **Inactive Metadata**
   dropdown at the top right-hand corner of the screen. Search or
   navigate the list, and then click the field that you want to
   activate.
-  *To deactivate* - Click the **Deactivate** icon |Deactivate| next to
   the **Field ID** in the active metadata panel.
-  Click **Save changes**.

**Order**: Refers to the order of the active metadata fields in the
asset details panel. Usually, the most important or most commonly used
metadata fields appear at the top of the asset details panel. To
reorder:

#. Point to the order number.
#. When the hand pointer |Pointer| appears, click and hold.
#. Drag and drop the row to the desired location.
#. Click **Save changes**.

   |Configure metadata|

**Field ID**: Refers to the metadata field name displayed in programs
like Adobe Bridge or Photoshop.

**Field Name**: Refers to the name that displays in the asset details
panel. Typically, the Field ID and the Field Name will be the same, but
you might want to rename a field name for clarification purposes or to
use internal verbiage. In addition, you can rename custom fields to
track custom information like product, event name, campaign, etc.

To rename a field, complete the following steps:

#. Click the **Field name** field.
#. Enter the new field name.
#. Click **Save changes**.

**|acquia-product:bc|**: Allows the metadata field to display in the
asset details section of |acquia-product:bc|. You can disable this
option if there are any fields that should not be viewable or searchable
by users in |acquia-product:bc|.

**Searchable**: Allows the metadata fields to be returned in search
results. Typically the metadata should be searchable; however, there
might be certain use cases where you do not want a specific field to be
searchable.

Example: Your copyright notice probably includes your company name.
Since your company name is a term that users will often search for, you
might want to make the copyright metadata field unsearchable so that
assets with the copyright notice won’t be returned every time a user
searches for the company name.

To allow assets to be searchable, check the box under the **Searchable**
column, then click **Save changes**.

**Field Type**: Refers to whether users will be able to add metadata to
a field by typing in information or choosing from a picklist or
multi-select. Metadata fields are text fields by default, but admins can
create a picklist or multi-select. To create a picklist or multi-select:

#. Click the wrench icon |Configure icon| in the **Field Type** column.
#. Enter or paste the picklist values — one value per line.
#. Select the **Allow multi-select** check box if you want to allow
   users to select more than one value in the list.
#. Click **Save**.

**Metadata Groups**: Enterprise admins can restrict access to certain
metadata fields based on user groups. (Read more about `metadata
permissions </dam/admin/metadata/perms>`__.)

**Required** (Enterprise and Professional Editions only): Makes an entry
for the metadata field mandatory, it cannot be left blank. Any fields
set as required will be viewable to all users, although who can edit
metadata options will still be controlled through Group Permissions.

To make a field required:

#. In the **Required** column, select the check box for the field.
#. Click **Yes** when you see the confirmation prompt.
#. Click **Save changes** to apply your changes.

Enabling required metadata adds a new status, **Holding**, to newly
uploaded assets. You will also need to manage the **Purge** settings
related to this status.

**Holding**: If a user uploads assets to the DAM without completing the
required metadata field(s), the asset(s) will be placed on hold. Assets
on hold are only viewable by the uploader and admins. When the required
metadata is added requirements are fulfilled, the asset will be removed
from holding and become available to other users as defined in the
permissions. To view the assets currently on hold:

#. Sign in to |acquia-product:dam|.
#. Run an empty/blank search to view all assets in your library - you
   can do so by leaving the search box blank and clicking the |Search|
   **Search** icon.
#. Click the **Status** filters in the left-hand navigation and select
   **Holding**. Assets in **Holding** will display a warning icon
   |Warning| next to their file name.

If you change a required metadata field to no longer be required, assets
that were missing that required metadata field value will be removed
from holding and will therefore be released to their intended
destination folders. If an asset is still missing other required fields,
it will remain on hold.

This does not happen in converse situation. If you add a field to the
required list, assets that already exist in your DAM and are not
currently in a holding state will not be changed to on hold. However, if
you attempt to edit the metadata for an asset and new required metadata
fields have been added, the asset will be put on hold if values are not
added to those required fields.

**Delete assets still in holding:** You have the option to purge assets
that are on hold. Any assets that don’t have input for the required
fields will be removed from the DAM.

To configure purge settings:

#. Navigate to your System Preferences.
#. In the Assets section, click the dropdown next to Automatically
   delete asset still in “Holding state” after to select the desired
   action.

   |Purge durations|

Exif
----

`Exif <https://en.wikipedia.org/wiki/Exif>`__ (Exchangeable image file
format) is metadata generated from the camera and cannot be edited.
Examples include f-stop, exposure and flash.

The following section outlines configuring the EXIF:

**Status**: Metadata fields must be active to display in the asset
details panel. The active metadata displays in the center window of the
EXIF tab. Inactive metadata is listed in the Inactive EXIF Field
dropdown at the top right-hand corner of the screen.

To activate or deactivate a metadata field, complete the following
steps:

-  *Activate* - Click **Add a field** in the **Inactive Metadata**
   dropdown at the top right-hand corner of the screen. Search or
   navigate the list and then click the field that you want to activate.
-  *Deactivate* - Click the deactivate icon |Deactivate| next to the
   field name in the active metadata panel.

Be sure to click **Save Changes** after you make your selection.

**Order**: Refers to the order of the active metadata fields in the
asset details panel. To reorder:

#. Point to the order number.
#. When the pointer appears, click and hold.
#. Drag and drop the row to the desired location.
#. Click **Save changes**.

Keywords
--------

Keywords are a subset of metadata, which display in |acquia-product:dam|
as clickable links. Admins can create a keyword taxonomy, or keyword
list, to ensure that keywords are being added in a consistent manner. To
create the taxonomy, you can either `upload a tab-separated TXT file or
build the keyword taxonomy in
|acquia-product:dam| </dam/admin/metadata>`__.

The following section outlines creating a keyword taxonomy:

.. _addkeyword:

Add a keyword
~~~~~~~~~~~~~

#. Click **Add a main keyword** to add a top-level (parent) keyword.
#. Right-click a keyword, and then click **Add** to add a nested (child)
   keyword.
#. Enter the keyword, and then click anywhere on the screen to save. |br|
   Keywords automatically rearrange into alphabetical order.

   |Keywords rearrange|

.. _renamekeyword:

Rename a keyword
~~~~~~~~~~~~~~~~

#. Right-click the keyword, and then click **Rename**.
   You can also double-click the keyword to edit.
#. Rename the keyword, then click anywhere on the screen to save.
   |Rename keywords|

.. _deletekeyword:

Delete a keyword
~~~~~~~~~~~~~~~~

#. Right-click the keyword, and then click **Delete**.
#. Click **Delete** to confirm. If you delete a keyword with child
   keywords, the nested keywords will also be deleted.
   |Delete keyword|

.. _movekeyword:

Move a keyword
~~~~~~~~~~~~~~

#. Click and hold the keyword.
#. Drag and drop the keyword to the desired location in the taxonomy.
   |Move a keyword|

.. _upload:

Upload a keyword taxonomy
~~~~~~~~~~~~~~~~~~~~~~~~~

You can also build a hierarchical keyword taxonomy in Word or Excel,
then import it into |acquia-product:dam|.

#. Create a new Microsoft Excel sheet.
#. Enter your desired keywords.

   -  To create main (parent) keywords, press Enter or Return after each
      entry
   -  To create nested (child) keywords, press Tab after each entry

#. Save the spreadsheet as a tab delimited text (.txt) file. When
   prompted, click **Continue**.
#. Open the file in Microsoft Word. Select **Mac OS (Default)**, then
   click **OK**.
#. When the document opens, click **File > Save As** and select **Plain
   Text (.txt)**.
#. In the pop up, check the box next to "Insert line breaks" and choose
   **CR/LF** in the "End lines with" dropdown.
#. From the keywords tab of |acquia-product:dam|, click **Select a
   File** to locate and select the file created on your computer.
#. Set the toggle to **Append** to add onto an existing keyword taxonomy
   or **Replace** to overwrite an existing keyword taxonomy.
#. Click **Import**.

.. _export:

Export keywords
~~~~~~~~~~~~~~~

You can export your keyword taxonomy to a TXT file for auditing purposes
or if you plan to make changes to your taxonomy to re-import.

.. _settings:

Keyword taxonomy settings
~~~~~~~~~~~~~~~~~~~~~~~~~

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings|, and then click **System
   preferences**.
#. In the **Assets** section, there are two keyword taxonomy settings:

   -  **Enable keyword taxonomy** - Select this check box to make the
      keyword taxonomy available for use by admins and contributors.
   -  **Enforce keyword taxonomy** - Select this check box to require
      admins and contributors to only add keywords from the keyword
      taxonomy. This will prevent them from typing in new keywords.

#. (Read more about `applying metadata to
   assets </dam/content/asset/metadata>`__.)
#. Click Save.

Facets
------

Facets refer to the metadata search filters that make your assets easy
to search in |acquia-product:bc|.

The default facets include file type, keywords, date captured, file size
and your `active XMP metadata fields </dam/admin/metadata>`__. In
addition to these facets, users will also be able to search by date
(including date created, date captured, date expired, and date modified)
and by size (including width, height, resolution, and file size). These
search options are default and cannot be deactivated.

The following section outlines configuring the facets:

**Status**: Facets must be active to display in |acquia-product:bc|. The
active facets will display in the center window of the Facets tab.
Inactive facets will be listed in the Inactive facets dropdown at the
top right-hand corner of the screen. Inactive facets will still be
searchable using the basic search in |acquia-product:bc|, and the
facet’s metadata will still display on the asset details page. Newly
added XMP metadata fields will display in the inactive facets dropdown.

To activate or deactivate a facet:

#. **Activate**: Click **Add a field** in the **inactive facet**
   dropdown at the top right-hand corner of the screen. Search or
   navigate the list and then click the field that you want to activate.
#. **Deactivate**: Click the deactivate icon |Deactivate| next to the
   field name in the active metadata panel. Deactivated XMP metadata
   fields will be automatically deleted.
#. Click **Save** changes.

**Order**: Refers to the order of the facets in |acquia-product:bc|. To
reorder:

-  Point to the order number.
-  When the |Hand| pointer appears, click and hold.
-  Drag and drop the row to the desired location.
-  Click **Save** changes.

.. _tips:

Helpful Information
-------------------

|acquia-product:dam| does not delete or strip any metadata.

Metadata applied to assets in |acquia-product:dam| is embedded upon
download.

If a keyword is renamed or deleted from the keyword taxonomy, the change
will not update at the asset level. If assets need to be updated by
deleting or changing to a new keyword, we recommend batch editing the
assets. (Read more about `editing
metadata </dam/content/mobile/manage>`__.)

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 31px
.. |Deactivate| image:: https://cdn4.webdamdb.com/100th_sm_gUmFYCc6cec8.png?1527118348
   :width: 23px
   :height: 23px
.. |Pointer| image:: https://cdn2.webdamdb.com/100th_sm_6jQJotZamyN1.png?1527118349
   :width: 23px
   :height: 24px
.. |Configure metadata| image:: https://cdn2.webdamdb.com/md_s26Eunaod8u9.jpg?1527118347
   :width: 550px
   :height: 196px
.. |Configure icon| image:: https://cdn2.webdamdb.com/100th_sm_24n8wRX5SH32.png?1526475691
   :width: 24px
   :height: 21px
.. |Search| image:: https://cdn2.webdamdb.com/100th_sm_swpRfK2DUf66.png?1527118353
   :width: 23px
   :height: 25px
.. |Warning| image:: https://cdn3.webdamdb.com/100th_sm_Aq9NM2Ut7Qq8.png?1526476101
   :width: 25px
   :height: 22px
.. |Purge durations| image:: https://cdn3.webdamdb.com/md_3kUvblZO3m21.png?1527118354
   :width: 550px
   :height: 300px
.. |Keywords rearrange| image:: https://cdn2.webdamdb.com/md_k04hp6zpGar0.png?1527118349
   :width: 550px
   :height: 275px
.. |Rename keywords| image:: https://cdn2.webdamdb.com/md_UGK9TrRhxxk6.png?1527118345
   :width: 550px
   :height: 275px
.. |Delete keyword| image:: https://cdn3.webdamdb.com/md_6107ub5mwT31.png?1527118347
   :width: 550px
   :height: 275px
.. |Move a keyword| image:: https://cdn4.webdamdb.com/md_6PyCrOcmb1Z1.png?1527118348
   :width: 550px
   :height: 275px
.. |Hand| image:: https://cdn3.webdamdb.com/100th_sm_6jQJotZamyN1.png?1527118349
   :width: 23px
   :height: 24px
