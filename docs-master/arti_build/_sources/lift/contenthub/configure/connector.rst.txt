.. include:: /common/global.rst

|acquia-product:ch| connector settings
======================================

The |acquia-product:chc| has additional settings to help limit data
sent, and to ensure your files are properly placed on your server.

Excluding properties
--------------------

By default, all entities of the types that you selected on the `Entity
Configuration </content-hub/sharing>`__ tab are shared by
|acquia-product:ch|, and are made available to all the other members of
your |acquia-product:ch| network.

You can, however, exclude specific properties or fields of those
entities, causing the properties that you specify as excluded to *not*
be shared and sent to |acquia-product:ch|.

|ch-properties-list.png|

To exclude a property or field, complete the following steps:

#. In the admin menu, go to **Configuration > Content Hub Connector >
   Settings**.
#. In the **Excluded properties** section, in the **Properties List**
   field, enter the properties that you want to exclude, one per line.
   A *property* is the **machine_name** of the field to be excluded.
#. After you have entered all of the properties that you want to
   exclude, click **Save configuration**.

For example, to exclude the Article type's Image and Category
properties, in the **Properties List** field, enter the following
values:

-  ``field_image``
-  ``field_category``

|Setting the excluded properties|

Unmanaged files
---------------

The **Unmanaged files** setting is for storing inline files that are
imported from |acquia-product:ch|. These are files uploaded as inline
files or images in **Long text and summary** fields such as the body
field, using editors such as WYSIWYG or CKEditor. These files are not
linked to database entries in the ``file_managed`` table.

You can set the directory for unmanaged files by using the **Directory
for unmanaged files** field. This is generally a public directory in
your `docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__.

|Unmanaged files directory|

.. |ch-properties-list.png| image:: https://cdn2.webdamdb.com/1280_A8QjryXk6IX0.png?1526475739
   :width: 655px
   :height: 216px
.. |Setting the excluded properties| image:: https://cdn3.webdamdb.com/1280_kAXVJNDddRX3.png?1526475483
   :width: 453px
   :height: 177px
.. |Unmanaged files directory| image:: https://cdn2.webdamdb.com/1280_A9aq9fjLqVS5.png?1526475623
   :width: 493px
   :height: 127px
