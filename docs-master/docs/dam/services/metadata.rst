.. include:: /common/global.rst

Metadata mapping in |acquia-product:dam|
========================================

You can add or update metadata to your assets in bulk using our metadata
mapping service, where we map your desired metadata to the assets you
have stored in |acquia-product:dam|.

Metadata mapping is included as part of |acquia-product:dam| standard
onboarding and also available as an add-on service. Contact your Acquia
Account Manager for more information.

.. _process:

Metadata mapping process
------------------------

#. Request a metadata export from your Account Manager — it will include
   a list of all your assets and associated metadata in a ``.csv`` file.
#. Open the file and make the necessary edits. |br|
   Metadata field names are listed at the top of each column. The
   values for fields in Title Case cannot be changed, as they are
   system specific. Fields in CAPS can have their values edited, as
   they are based on the IPTC/XMP metadata standard. |br|
   For example, the values under the metadata field ``CUSTOMFIELD1``
   can be edited; however ``Filename`` and ``Path`` cannot. |br|
   To change the name of a metadata field, insert a new row at the top
   of the sheet and enter the new name in the cell above the field
   name you’d like to replace. For example, you might want to capture
   brand information as a metadata field. To do so, you can rename
   ``CUSTOMFIELD1`` by inserting a new row at the top of the
   spreadsheet and entering ``Brand Name`` above ``CUSTOMFIELD1``.

   |Metadata field names|

#. Add or update metadata in the cells under the metadata field names. |br|
   For example, a group of assets are from the Superfly brand, and you
   want that information reflected in the assets’ metadata. Using the example
   above, under the ``Brand Name/CUSTOMFIELD1`` metadata field on the
   spreadsheet, include ``Superfly`` for each appropriate asset.

   |Asset list by brand name|

#. After your edits are complete, send the file back to your Account
   Manager to map into |acquia-product:dam|. Acquia will provide an ETA
   for completion.

Acquia will provide success/failure logs and an email confirmation after
the process is complete.

.. |Metadata field names| image:: https://cdn3.webdamdb.com/1280_6h2CUCog8eA7.jpg?1527260429
   :width: 614px
   :height: 261px
.. |Asset list by brand name| image:: https://cdn2.webdamdb.com/1280_2sFhttSL2d91.jpg?-62169955200
   :width: 608px
   :height: 332px
