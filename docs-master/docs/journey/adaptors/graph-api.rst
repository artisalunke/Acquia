.. include:: /common/global.rst

Graph API: Listen adaptor
=========================

The |acquia-product:aj| Graph API Listener makes it easy to integrate
business logic into other systems by providing a listener adaptor that
can be added to any graph to make it publicly accessible by a unique
permanent URL.

The |acquia-product:aj| Graph API listener has three modes of operation:

-  *Standard API Listener* - Exposes a web service endpoint that
   responds to a web service ``POST`` request
-  *Web Tracking and Recommendation* - Embeds JavaScript, and is
   available for legacy purposes only. For tracking, use
   |acquia-product:cha| |profile manager|_ instead.
-  *Pixel Tracking* - Embeds a one pixel by one pixel (1x1) transparent
   image — no cookie is set

.. |profile manager| replace:: \ |acquia-product:lpm| \ 
.. _profile manager: /lift/profile-mgr

The Graph API supports several design patterns, including the following:

-  Each graph as its own micro-service, handling one operation
-  A single graph as the entry point for multiple operations, using an
   ``op`` query parameter and then subgraphs for handing each of the
   different operations

When implementing a single graph as an entry point for multiple
operations, you are creating an API endpoint that offers multiple
operations. You can implement this approach using
`JSON-RPC <http://www.jsonrpc.org/specification>`__ for structured JSON
payloads. The operation performed should be determined by the ``op``
query parameter, and each operation should be a function call that,
optionally, returns a value.

You can pass data to your operations by using query string parameters
for ``GET`` requests, or by using the request body for a ``POST``
request. You should use ``POST`` requests when sending sensitive or
identifying information, rather than including the information in the
query string of a ``GET`` request.

For information about other listener types and their functions, see
|adaptors|_.

.. |adaptors| replace:: \ |acquia-product:aj| \ adaptors
.. _adaptors: /journey/adaptors

Adding a Graph API Listener
---------------------------

You can add a new graph API listener by completing the following steps:

#. Sign in to |acquia-product:aj|.
#. On the main project page (accessible by clicking the
   |acquia-product:aj| logo in the top menu), find the project that you
   want to modify, and click its **Project Editor** |Project Editor
   icon| icon.
#. Select the graph to which you want to add a listener, and then click
   **Open** at the bottom of the panel.
#. In the top right of the graph editing canvas, click **Add Listener**.
   |acquia-product:aj| will display the **Listener** dialog box.
#. In the **Listener Type** select list, click **API**.
#. Click **Standard** or **Pixel Tracking** to display configuration
   information for those types of listeners. For more information, see
   `Standard API Listener <#standard>`__ and `Pixel tracking API
   listener <#pixel>`__.

   .. admonition:: Web Tracking and Recommendation API listener

      Acquia recommends that you use the |acquia-product:cha|
      |profile manager|_ for tracking webpage
      activity.

#. Copy the appropriate code for your listener into the application of
   your choice.
#. Click **Save**.

The **Listener ID** is a unique 32-character alphanumeric string that
identifies this listener. The same graph API listener in a different
environment will have a different **Listener ID**.

Standard API Listener
---------------------

The standard listener accepts data sent by either a ``GET`` or ``POST``
request, and returns the value from the `Return
node </journey/node/return>`__ on your graph.

|Create an API listener|

The web service endpoint for the Standard API Listener is displayed in
the example as the **Endpoint**, and is accessible when the graph is
running. Any data provided as part of the ``GET`` or ``POST`` request is
placed into the schema variable location selected in the **Output**
location. The API listener adds the special ``_kw`` key to the
**Output** location with an object containing the following keys:

-  *Headers* - the HTTP headers associated with the HTTP request
-  *Method* - the HTTP method associated with the HTTP request

You can also create micro web services with a standard listener that can
be used by external systems. |acquia-product:aj| Graph API supports
``HTTP GET`` and ``HTTP POST`` methods:

-  ``POST`` - the ``POST`` body, if any, is saved to the **Output**
   location, and any query parameters in the URL will be ignored. The
   ``Content-Type`` may be either ``application/json`` or
   ``application/xml``. The maximum payload size is 100 KB.
-  ``GET`` - the URL parameters, if any, are saved to the **Output**
   location

.. _get:

Making a GET request
~~~~~~~~~~~~~~~~~~~~

In the following example, the ``curl`` command is used to make a
``HTTP GET`` request to the API endpoint. The ``key1`` parameter in the
query string is assigned the value ``val``. Replace ``{listenerID}``
with your API Listener endpoint ID.

``curl https://api.journey.acquia.com/api/v1/listener/{listenerID}?key1=val``

Making a POST request
~~~~~~~~~~~~~~~~~~~~~

The following example describes how to make an ``HTTP POST`` request to
the API using the ``curl`` command. The |acquia-product:aj| Graph API
requires the **Content-Type** header field to be set to either
``application/json`` or ``application/xml`` when performing a ``POST``
operation. Replace ``{listenerID}`` with your API Listener endpoint ID.

.. note::
  You must specify the Content-Type when making requests to the API. Most
  HTTP clients do not use ``Content-Type: application/json`` or
  ``Content-Type: application/xml`` as the default. If the Content-Type
  header is omitted, you will receive an error.

``curl -H "Content-Type: application/json" -X POST \   -d '{"body":"this is my body"}' https://api.journey.acquia.com/api/v1/listener/{listenerID}``

If you use ``application/xml``, |acquia-product:aj| performs the
following conversions on your XML document before saving it to your
**Output** location:

-  XML elements become JSON arrays
-  XML attributes become ``$`` objects with fields
-  XML body text becomes ``_`` when there are attributes
-  All element names are converted to lowercase
-  Attribute names remain unchanged

XML conversion examples
~~~~~~~~~~~~~~~~~~~~~~~

The following example shows an empty element produces an object with an
empty field value:

.. list-table::
 :widths: 50 50
 :header-rows: 1

 * - XML document
   - Output
 * - ``<xml/>``
   - ``{``
     ``"xml" : ""``
     ``}``

The following example shows an empty child element is turned into an
array value with a single empty value:

.. list-table::
 :widths: 50 50
 :header-rows: 1

 * - XML document
   - Output
 * - ``<xml>``
     `` <element/>``
     ``</xml>``
   - ``{``
     ``"xml":  {`` 
     ``"element": [ "" ]`` 
     ``}``
     ``}``

The following example shows a collection of child elements with simple
values is transformed into an array of values:

.. list-table::
 :widths: 50 50
 :header-rows: 1

 * - XML document
   - Output
 * - ``<xml>``
     `` <element>a</element>``
     `` <element>b</element>``
     `` <element>c</element>``
     ``</xml>``
   - ``{``
     `` "xml": {``
     `` "element": [ "a", "b", "c" ]``
     `` }``
     ``}``

| The following example shows a collection of child elements with
  attributes and simple or non-existent values transformed to an array
  of objects.
| An element's attributes are held in the special "$" attribute of the
  object they refer to.

.. list-table::
 :widths: 50 50
 :header-rows: 1

 * - XML document
   - Output
 * - ``<xml>``
     `` <element attr1="a" attr2="b">first element</element>``
     `` <element>second element</element>``
     `` <element/>``
     ``</xml>``
   - ``{``
     `` "xml": {``
     `` "element": [``
     `` {``
     `` "$": {``
     `` "attr2": "b",``
     `` "attr1": "a"``
     `` },``
     `` "_": "first element"``
     `` },``
     `` "second element",``
     `` ""``
     `` ]``
     `` }``
     ``}``

In the following example, the attribute names are not converted to lowercase:

.. list-table::
 :widths: 50 50
 :header-rows: 1

 * - XML document
   - Output
 * - ``<xml>``
     `` <element attr1="a" AttributeTwo="b">first element</element>``
     `` <element>second element</element>``
     `` <element/>``
     ``</xml>``
   - ``{``
     `` "xml": {``
     `` "element": [``
     `` {``
     `` "$": {``
     `` "AttributeTwo": "b",``
     `` "attr1": "a"``
     `` },``
     `` "_": "first element"``
     `` },``
     `` "second element",``
     `` ""``
     `` ]``
     `` }``
     ``}``

If the XML is invalid, as in the following example, |acquia-product:aj|
provides the location of the error in the ``message`` property:

.. list-table::
 :widths: 50 50
 :header-rows: 1

 * - XML document
   - Output
 * - ``<xml>``
     `` <element attr1="a" attr2="b">first element</element2>``
     `` <element>second element</element>``
     `` <element/>``
     ``</xml>``
   - ``{``
     `` "message": "Unexpected close tag\nLine: 1\nColumn: 55\nChar: >",``
     `` "error": {}``
     ``}``

The following table describes errors that may be returned as a result of
an invalid HTTP ``POST`` request:

.. list-table::
 :widths: 40 60
 :header-rows: 1

 * - Graph status
   - Error
 * - Deployed graph
   - ``{"message":"undefined is not a function","error":{}}``
 * - Graph being visually tested in the testing console
   - ``{"message":"req.msgBody.hasOwnProperty is not a function","error":{}}``

.. _sample:

Sample Web Service Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example is an approach for implementing a basic CRUD
(create, read, update, and delete) endpoint using the
|acquia-product:aj| Graph API:

+-----------------+-----------------+-----------------+-----------------+
| Operation       | HTTP Method     | URL             | Description     |
+=================+=================+=================+=================+
| Create          | ``POST``        | ``?op=create``  | Receives the    |
|                 |                 |                 | ``HTTP POST``   |
|                 |                 |                 | content body    |
|                 |                 |                 | and returns an  |
|                 |                 |                 | ID referring    |
|                 |                 |                 | the data.       |
+-----------------+-----------------+-----------------+-----------------+
| Read            | ``GET``         | ``?op=read&id=1 | Returns the     |
|                 |                 | 0``             | data for ID 10. |
+-----------------+-----------------+-----------------+-----------------+
| Update          | ``POST``        | ``?op=update&id | Updates the     |
|                 |                 | =1234``         | data associated |
|                 |                 |                 | with ID 10.     |
+-----------------+-----------------+-----------------+-----------------+
| Delete          | ``GET``         | ``?op=delete&id | Deletes the     |
|                 |                 | =10``           | data associated |
|                 |                 |                 | with ID 10.     |
+-----------------+-----------------+-----------------+-----------------+

A `decision tree node </journey/node/decision-tree>`__ can be used to
check the correct operation and method combination. The following image
displays a decision tree that implements the CRUD configuration in the
previous table.

|journey-graph-decision-tree-editor.png|

In this example, the graph uses the decision tree node defined
previously to execute the correct embedded graph based on the value of
the ``op`` parameter in the |acquia-product:aj| Graph API endpoint of
the following graph.

|journey-graph-with-decision-branching.png|

Web Tracking and Recommendation API listener
--------------------------------------------

Acquia recommends that you use the |acquia-product:cha| |profile manager|_ for
tracking webpage activity.

Pixel tracking API listener
---------------------------

Pixel tracking options allow you to use a graph with an API listener in
situations where you can load an image but cannot otherwise run code,
such as emails or web pages whose source you cannot control. The
|acquia-product:aj| API single-pixel image tag can be placed in emails,
web pages, and anything else that supports HTML to track HTTP headers
and any additional information (such as campaign ID or customer ID) that
is passed by the query string.

|Pixel tracking screenshot|

Email pixel tracking
~~~~~~~~~~~~~~~~~~~~

Pixel tracking passes data from the HTTP request, and an optional URL
query string, to your graph. In this example, the previous ``img`` tag
sends a packet of data into your graph that includes all HTTP headers,
and the query parameter ``name`` with the value ``User2``:

``<img src="https://api.journey.acquia.com/api/v1/listener/{listenerID}/epixel.gif?name=User2" />``

Website pixel tracking
~~~~~~~~~~~~~~~~~~~~~~

Acquia recommends you use the |acquia-product:cha|
|profile manager|_ for tracking activity on
websites.

.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Create an API listener| image:: https://cdn2.webdamdb.com/1280_61pu839aE9O8.png?1526475745
   :width: 550px
   :height: 334px
.. |journey-graph-decision-tree-editor.png| image:: https://cdn3.webdamdb.com/1280_YAFD79vyT6L2.png?1526475497
   :width: 1118px
   :height: 551px
.. |journey-graph-with-decision-branching.png| image:: https://cdn2.webdamdb.com/1280_MbNAX0ppTty5.png?1526475496
   :width: 842px
   :height: 527px
.. |Pixel tracking screenshot| image:: https://cdn4.webdamdb.com/1280_ktAd0ScXvj37.png?1526475824
   :width: 550px
   :height: 100px
