.. include:: /common/global.rst

|acquia-product:liftapi| and HMAC v1 authorization
==================================================

Based on |acquia-product:alw| account configuration, API calls may
require authentication in the form of a
`HMAC-SHA1 <https://en.wikipedia.org/wiki/Hash-based_message_authentication_code>`__
message hash as a header within the request. HMAC is a keyed-hash
authentication code that calculates a message authentication code (MAC)
involving a cryptographic hash function in combination with a secret
cryptographic key. SHA1 is one type of cryptographic hash function used
in the calculation of an HMAC header; the resulting algorithm is known
as HMAC-SHA1.

This authentication scheme protects your data and ensures your secret
keys stay secure, and utilizes the Access Key ID and secret access key
associated with your |acquia-product:alw| subscription.

Setting HMAC authentication as an HTTP request
----------------------------------------------

In the |acquia-product:liftapi|, HMAC authentication is set as a header
in an HTTP request in the following form:

.. code-block:: none

   AUTHORIZATION:HMAC [key_ID]:[sig]

where ``[key_ID]`` is the access key assigned to your
|acquia-product:alw| account subscription (for example,
``asdf23874hfewahJKHJHa``), and ``[sig]`` is the HMAC-SHA1 hash of
`canonical representation <#generating>`__ using the secret access key
associated with your |acquia-product:alw| account subscription (for
example, ``sdkjfhz[9389PPKJEU``).


Generating the canonical representation of the request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you can `calculate the authorization header <#creating>`__ to
authenticate your API call, you first need to generate the canonical
representation of the request. To do so, start with the empty string
(""), and then use the following guidelines:

-  Add the HTTP verb for the request (for example, ``GET`` or ``POST``)
   in capital letters, followed by a single newline (``U+000A``).
-  Convert specific header names to lowercase. Currently supported
   headers are:

   -  ``accept``
   -  ``host`` (domain name only, no protocol)
   -  ``user-agent``

-  Sort the headers lexicographically by header name.
-  Trim header values by removing any whitespace.
-  Combine lowercase header names and header values using a single colon
   as the separator. Do not include whitespace characters around the
   separator.
-  Combine the specific headers using a single newline character
   (``U+000A``) as the separator and append them to the canonical
   representation, followed by a single newline character (``U+000A``).
-  Append the request URI (the part of this request's URL from the
   protocol name up to the query string) to the canonical
   representation.
-  Sort all parameters lexicographically (alphabetically) by parameter
   name, and then join them using a single ampersand as the separator.
-  Append the parameter string using a single question mark as the
   separator, unless the query string is empty.

Example
^^^^^^^

You are an |acquia-product:alw| and |acquia-product:ldb| customer whose
account ID is EXAMPLEINC, is provisioned in one of the supported
geographic regions, and your |acquia-product:liftapi| requires
authentication. You have an |acquia-product:alw| user who wants to
retrieve a list of defined segments, and has an Access Key of ABCD and a
secret access key of 1234.

The following table describes the process used to handle this example,
along with how it can be executed:


.. list-table::
   :widths: 40 60
   :header-rows: 1 

   * - Step
     - Example
   * - Start with an empty string, and then add the capitalized HTTP verb for the request followed by a single newline.
     - ``GET``
   * - Convert the header names to lowercase, sort them by header name, and then trim any whitespace. Combine the header names and values with a colon separator.
     -
       .. code-block:: none
       
          host:example-liftapi.lift.acquia.com
          user-agent:Apache-HttpClient/4.3.5 (java 1.5)

   * - Combine the specific headers using a single newline character and then append them to the canonical representation, followed by a single newline.
     -  
       .. code-block:: none
       
          GET
          host:example-liftapi.lift.acquia.com
          user-agent: Apache-HttpClient/4.3.5 (java 1.5)

   * - Append the request URI (the part of this request's URL from the protocol name up to the query string) to the canonical representation.
     - 
       .. code-block:: none
       
          GET
          host:example-liftapi.lift.acquia.com
          user-agent:Apache-HttpClient/4.3.5 (java 1.5)
          /dashboard/rest/EXAMPLEINC/segments

   * - Sort all parameters by parameter name, and then join them using a single ampersand as the separator.
     - This example does not require parameters, but if it required parama with a value of 1 and paramb with a value of 2, the sorting and joining result would be: ``parama=1¶mb=2``
   * - Unless the query string is empty, append the parameter string, using a single question mark as the separator.
     - This example does not require parameters, but if it did, the resulting request URI would be: ``/dashboard/rest/EXAMPLEINC/segments?parama=1¶mb=2``

The full canonical representation is:

.. code-block:: none

   GET host:example-liftapi.lift.acquia.com 
   user-agent: Apache-HttpClient/4.3.5 (java 1.5) /dashboard/rest/EXAMPLEINC/segments


Creating the authorization header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you have `generated the canonical request <#generating>`__, you
can create the authorization header. Using the canonical request, you
can calculate the HMAC header value. If your |acquia-product:alw| Access
Key ID is ABCD and the secret access key is 1234, the HMAC header value
is ``cvynYFi7SdCWu6KKt+wImfcY17k=``.

The full HTTP request is:

.. code-block:: none

   GET /dashboard/rest/EXAMPLEINC/segments HTTP/1.1 Host: example-liftapi.lift.acquia.com 
   Connection: Keep-Alive User-Agent: Apache-HttpClient/4.3.5 (java 1.5) 
   Authorization: HMAC ABCD:cvynYFi7SdCWu6KKt+wImfcY17k=

Response validation
^^^^^^^^^^^^^^^^^^^

Requests using the GET method will return a response with a
``Content-MD5`` header. This header is the MD5 hash of the response
content and can be used for response content validation.


Managing HMAC authentication in |acquia-product:alw|
----------------------------------------------------

Although HMAC is enabled by default, it can be disabled for
troubleshooting. To either enable or disable HMAC authentication,
complete the following steps:

#. Click the **Admin** menu.
#. In the **System** menu, click **Manage customers**.
#. In **Account ID**, click your ID.
#. In the **API Authentication** settings, depending on the API call
   that you are using, select or clear the appropriate check boxes to
   either enable or disable your HMAC authentication settings:

   -  **Enable Segment REST Api HMAC Authentication** - Controls HMAC
      authentication for segment calls in the |acquia-product:liftapi|
   -  **Enable Event Import REST Api HMAC Authentication** - Controls
      HMAC authentication for event imports in the
      |acquia-product:liftapi|
   -  **Enable File Export REST Api HMAC Authentication** - Controls
      HMAC authentication for file exports in the
      |acquia-product:liftapi|
   -  **Enable Visitor Query REST Api HMAC Authentication** - Controls
      HMAC authentication for visitor queries in the
      |acquia-product:liftapi|


Code examples
-------------

We have developed several code examines that you can use to help you
understand how to make calls to the |liftapi|_ using different
programming languages:

.. |liftapi| replace:: \ |acquia-product:liftapi|\ 
.. _liftapi: /lift/omni/rest_api

-  `PHP code
   example <https://gist.github.com/acquialibrary/d0d26d68f7e3c5531d22/download>`__
   - Makes a call to the |acquia-product:alw| REST API based on the
   parameters you've provided it. ``getMakeAPICall`` is the entry point
   of the example.
-  `Java code
   example <https://gist.github.com/acquialibrary/22450e13a49fa094542f/download>`__
   - Makes a call to several simple |acquia-product:cha| REST APIs. The
   entry point of the example is the ``main`` method.
