.. include:: /common/global.rst


Using bias to tune search results
=================================

The Apache Solr Search module's bias settings enable you to assign
search bias to certain aspects of indexed items. Configure bias for a
search environment on the **Apache Solr search > Settings** tab, under
**Configuration**.

|Search bias settings|

Search bias influences the importance of those aspects in search
results. Any value except "Omit" or "Ignore" increases that aspect's
score in the results. The higher the score, the more those aspects will
influence the search results. You can assign values from 0.1 to 21.0
when you set a bias. You can assign bias by:

-  `node attributes <#attr>`__
-  `content type <#type>`__
-  `node fields <#fields>`__

Bias by node attributes
-----------------------

|Result biasing|

Using the **Result biasing** section, you can add search bias to favor
nodes that are or have:

-  Sticky at top of lists
-  Promoted to home page
-  More recently created
-  More comments
-  More recent comments

Bias by content type
--------------------

Using the **Type biasing and exclusion** section, you can add search
bias to favor nodes of particular content types. For example, you might
want to favor announcements over blog posts.

Bias by node fields
-------------------

Using the **Field biases** section, you can add search bias based on the
field in a node in which the search term appears. For example, you might
want to give extra weight when the search term appears in a node's title
or H1 headers and less weight when the search term appears in rendered
comments.

Setting a field's value to ``Omit`` means that the field will not be
searched.

|Field biases|

.. |Search bias settings| image:: https://cdn2.webdamdb.com/md_MsvLfyyII7H7.png?1527793648
   :alt: Search bias settings
.. |Result biasing| image:: https://cdn4.webdamdb.com/md_EA5XOb3aVAD9.png?1527793648
   :alt: Result biasing
.. |Field biases| image:: https://cdn3.webdamdb.com/md_8vhXmFBghZ05.png?1527793649
   :alt: Search bias fields