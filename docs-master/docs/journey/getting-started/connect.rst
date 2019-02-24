.. include:: /common/global.rst

Creating connections and adaptors
=================================

|acquia-product:aj| uses Connections to connect to systems and services
outside of the |acquia-product:aj| system. Connections include
databases, web services, social media platforms, message queues and
email systems. An *adaptor* is a particular method on a connection. For
example, a `web service connection </journey/connect/rest>`__ may have a
``GET`` adaptor and a ``POST`` adaptor, each with different query
parameters and input and output data.

A single connection definition can be used to create many adaptors.
Connections can only be created by project administrators. Read more
`About |acquia-product:aj| roles </journey/admin/users/roles>`__.

In this example, we will demonstrate making different web service calls
to `httpbin <https://httpbin.org/>`__, a website that provides open
access for testing many kinds of web service calls you may want to use
in your customer journey.

Creating a web service connection
---------------------------------

`Create a new connection </journey/connect#create>`__ for your project,
and be sure to select the **REST Web Service** connection type.

|journey-add-new-connection.png| |journey-add-new-connection-dialog.png|

Set the end point for the web service to the following value:
``https://httpbin.org/``

|journey-connection-editing.png|

After you save the connector, it is ready to use in a graph.

Creating a web service GET adaptor
----------------------------------

`Create a new web service adaptor </journey/adaptors#add>`__ by choosing
**REST Web Service** from the *Adaptors* section, then use the following
actions to configure the adaptor:

#. In the **Method** list, click one of the following values:

   -  ``GET``
   -  ``POST``
   -  ``PUT``
   -  ``DELETE``

#. Extend the URL with any resource names, query parameters, or
   |acquia-product:aj| parameters. |acquia-product:aj| parameters are
   specified as ``%%paramName%%``.
#. Set the output destination.
#. Update the call and identify new parameters by clicking **Save
   Request & Headers / Update Parameters**.

|journey-web-service-adaptor-options.png|

After |acquia-product:aj| validates the adaptor, it can be used in a
graph.

.. |journey-add-new-connection.png| image:: https://cdn2.webdamdb.com/1280_XFMnthwqL402.png?1527092636
   :width: 834px
   :height: 459px
.. |journey-add-new-connection-dialog.png| image:: https://cdn3.webdamdb.com/1280_wvXy3JMG3A22.png?1527092652
   :width: 300px
   :height: 249px
.. |journey-connection-editing.png| image:: https://cdn2.webdamdb.com/1280_ge8RMUkAUn46.png?1527092644
   :width: 357px
   :height: 255px
.. |journey-web-service-adaptor-options.png| image:: https://cdn2.webdamdb.com/1280_6lRwcDlud579.png?1527092650
   :width: 1010px
   :height: 765px
