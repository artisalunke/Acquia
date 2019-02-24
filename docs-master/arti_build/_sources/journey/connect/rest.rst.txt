.. include:: /common/global.rst

REST web service connection
===========================

To use a REST web service `adaptor </journey/adaptors>`__ with your
project, you must first configure a *REST Web Service connection*.

For information about creating, configuring, or testing connections, see
|connections|_.

.. |connections| replace:: Managing \ |acquia-product:aj| \ connections
.. _connections: /journey/connect

-  **Endpoint** - The web service endpoint that is the root for all
   queries, typically in the form of ``protocol://resource`` (for
   example, ``https://api.google.com``).
   You can extend this endpoint when the connection is used to create an
   adaptor — no trailing slash or question mark is necessary.
-  **Constant Query Parameters** - Additional query string parameters to
   send with every REST service HTTP request make through this
   connection. Its typical use is for an API key that does not change.
   You can `add adaptor specific query
   parameters </journey/adaptors/rest>`__ in an adaptor.
-  **Constant HTTP Request Headers** - Additional headers to send with
   every REST service HTTP request made with this connection.
