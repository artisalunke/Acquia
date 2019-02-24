.. include:: /common/global.rst

Creating and managing tags
==========================

|acquia-product:aj| uses *tags* to make it easier to locate the
`graphs </journey/getting-started/graph>`__, `nodes </journey/node>`__,
or `adaptors </journey/adaptors>`__ that you want to open.

Whenever you create a new graph, node, or adaptor, |acquia-product:aj|
associates one or more `default tags <#default>`__ with the item, with
the tag being related to the object's type. You can also, however,
`create your own custom tags <#create>`__ if required, and then `add
them to your objects <#add-remove>`__.

In the following example, searching with the *api* tag in the **Project
Editor** displays the graphs, nodes, and adaptors related to that tag.

|filter by tag|

Searching for items with tags
-----------------------------

To search for a specific tag to find associated graphs, nodes, or
adaptors, complete the following steps:

#. Sign in to |acquia-product:aj|.
#. On the **Home Screen**, find the project tile for the project that
   you want to customize, and then click its Project Editor icon
   |Project Editor icon|.
#. In the top left of the page, click the action menu icon |Action
   menu|, and then click **Open**.
#. In the search field, enter the name of a tag. As you type, the list
   of available graphs, nodes, and adaptors will update to display only
   items matching your search query.
#. Click the name of the item that you want to open.
#. At the bottom of the page, click **Open**.

Working with custom tags
------------------------

Although |acquia-product:aj| will assign default tags to your objects,
this may not provide you the level of detail you need to effectively
manage your objects, especially if you create a lot of projects with
many graphs, nodes, and adaptors.

You can supplement the default tags assigned by |acquia-product:aj| with
custom tags, based on your specific needs.

Creating a custom tag
~~~~~~~~~~~~~~~~~~~~~

To create a new tag, complete the following steps:

#. Sign in to |acquia-product:aj|.
#. In the top menu, click **Admin**, and then click **Projects** in the
   left menu.
#. Find your project in the project list, and then click its project
   name.
#. In the project's detail view, click **Environments**.
#. In the **Available Project Tags** section, click the plus icon |add
   tag|.
#. In the **Create Tag** dialog, enter a tag name and optionally select
   a color.
#. Click **Create**.

Managing custom tags
~~~~~~~~~~~~~~~~~~~~

Using |acquia-product:aj|, you can edit or delete tags that have been
previously created. Depending on your needs, complete the following
steps:

.. important::
  Deleting a tag immediately removes it from every associated node —
  |acquia-product:aj| does not provide you with a deletion confirmation.

#. Sign in to |acquia-product:aj|.
#. In the top menu, click **Admin**, and then click **Projects** in the
   left menu.
#. Find your project in the project list, and then click its project
   name.
#. In the project's detail view, click **Environments**.
#. In the **Available Project Tags** section, find the tag that you want
   to manage, and then click the icon that corresponds with your desired
   action:

   -  *Edit* - Click the pencil icon.
   -  *Delete* - Click the trash can icon.

#. *If you are editing a tag,* in the **Edit Tag** dialog, make any
   necessary changes, and then click **Save**.

Adding or removing tags
-----------------------

Depending on your needs, use the following procedure to add or remove
tags to (or from) graphs, nodes, or adaptors:

#. `Search for the graph, node, or adaptor <#search>`__ that you want to
   associate with a tag.
#. In the **Tag Editor** panel, scroll to find the tag that you want.
#. Click the icon that corresponds to the action you want to complete:
#. *Add* - Click the link icon |image4|.
#. *Remove* - Click the check mark icon |check icon|.

Default tags
------------

When you create a new node, |acquia-product:aj| assigns related tags as
described in the following table:

+-----------------------+-----------------------+-----------------------+
| Object                | Icon                  | Tags                  |
+=======================+=======================+=======================+
| `2D                   | |2D Table node|       | 2d table              |
| Table </journey/node/ |                       |                       |
| 2d-table>`__          |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Acquia               | |Lift adaptor|        | adaptor, Acquia Lift  |
| Lift </journey/connec |                       |                       |
| t/lift>`__            |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Columnar             | |Columnar Table node| | columnar table        |
| Table </journey/node/ |                       |                       |
| columnar-table>`__    |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Conditional </journe | |Conditional node|    | conditional           |
| y/node/conditional>`_ |                       |                       |
| _                     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Database </journey/c | |Database adaptor|    | adaptor, database     |
| onnect/database>`__   |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Decision             | |Decision Tree node|  | decision tree         |
| Tree </journey/node/d |                       |                       |
| ecision-tree>`__      |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Email </journey/conn | |Email adaptor|       | adaptor, email        |
| ect/email>`__         |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `graph </journey/gett | |graph node|          | graph                 |
| ing-started/graph>`__ |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `JavaScript </journey | |JavaScript node|     | javascript, script    |
| /node/javascript>`__  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Message              | |Message adaptor|     | adaptor, queue        |
| Queue </journey/conne |                       |                       |
| ct/message>`__        |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `R                    | |R Script node|       | r model, script       |
| Script </journey/node |                       |                       |
| /r-model>`__          |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `REST Web             | |REST web service     | adaptor, REST, web    |
| Service </journey/con | adaptor|              | service               |
| nect/rest>`__         |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `SOAP Web             | |SOAP web service     | adaptor, SOAP, web    |
| Service </journey/ada | adaptor|              | service               |
| ptors/soap>`__        |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Split                | |Split Test node|     | split test            |
| Test </journey/node/a |                       |                       |
| b>`__                 |                       |                       |
+-----------------------+-----------------------+-----------------------+
| `Twitter </journey/co | |Twitter adaptor|     | adaptor, twitter      |
| nnect/twitter>`__     |                       |                       |
+-----------------------+-----------------------+-----------------------+

.. |filter by tag| image:: https://cdn3.webdamdb.com/1280_oWjFgsAybec2.jpg?1526476115
   :width: 526px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/1280_Qx24aCvtr211.png?1526475782
   :class: no-sb
   :width: 30px
   :height: 30px
.. |Action menu| image:: https://cdn3.webdamdb.com/1280_ksdoaWdShDr2.png?1526476127
   :class: no-sb
   :width: 30px
   :height: 30px
.. |add tag| image:: https://cdn2.webdamdb.com/1280_QgPYyozN5us9.png?1526475489
   :class: no-sb
   :width: 30px
   :height: 30px
.. |image4| image:: https://cdn4.webdamdb.com/1280_cxWm9DdwJ0L9.png?1526476064
   :class: no-sb
   :width: 30px
.. |check icon| image:: https://cdn2.webdamdb.com/1280_wANZEtT2aW02.png?1526476160
   :class: no-sb
   :width: 30px
.. |2D Table node| image:: https://cdn3.webdamdb.com/1280_AexGBJKU0J65.png?1526475646
   :class: no-sb
   :width: 51px
.. |Lift adaptor| image:: https://cdn2.webdamdb.com/1280_gWT0ClJBKXP4.png?1526475590
   :class: no-sb
   :width: 53px
.. |Columnar Table node| image:: https://cdn2.webdamdb.com/1280_gWT0ClJBKXP4.png?1526475590
   :class: no-sb
   :width: 51px
.. |Conditional node| image:: https://cdn2.webdamdb.com/1280_gWT0ClJBKXP4.png?1526475590
   :class: no-sb
   :width: 51px
.. |Database adaptor| image:: https://cdn2.webdamdb.com/1280_MPQTqoZzw6F6.png?1526475683
   :class: no-sb
   :width: 53px
.. |Decision Tree node| image:: https://cdn4.webdamdb.com/1280_IgAlLvz4LFV9.png?1526475666
   :class: no-sb
   :width: 51px
.. |Email adaptor| image:: https://cdn3.webdamdb.com/1280_woXxAkJDu671.png?1526475625
   :class: no-sb
   :width: 53px
.. |graph node| image:: https://cdn4.webdamdb.com/1280_MaBCqfziZId1.png?1526475487
   :class: no-sb
   :width: 51px
   :height: 51px
.. |JavaScript node| image:: https://cdn2.webdamdb.com/1280_s1lM0x6aVl57.png?1526475692
   :class: no-sb
   :width: 51px
.. |Message adaptor| image:: https://cdn3.webdamdb.com/1280_gOFtcaVv9K59.png?1526475899
   :class: no-sb
   :width: 53px
.. |R Script node| image:: https://cdn2.webdamdb.com/1280_gW4YuksHsEf0.png?1526475452
   :class: no-sb
   :width: 51px
.. |REST web service adaptor| image:: https://cdn4.webdamdb.com/1280_6g6C8mrAZ0E8.png?1526476135
   :class: no-sb
   :width: 53px
.. |SOAP web service adaptor| image:: https://cdn2.webdamdb.com/1280_AyEHsvy16411.png?1526476103
   :class: no-sb
   :width: 53px
.. |Split Test node| image:: https://cdn2.webdamdb.com/1280_6GeJRo74Gkb8.png?1526476026
   :class: no-sb
   :width: 51px
.. |Twitter adaptor| image:: https://cdn2.webdamdb.com/1280_2iWN4x4ZRb54.png?1526476118
   :class: no-sb
   :width: 53px
