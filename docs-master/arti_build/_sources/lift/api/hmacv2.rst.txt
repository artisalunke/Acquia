.. include:: /common/global.rst

|acquia-product:liftapi| and HMAC v2 authorization
==================================================

Based on |acquia-product:alw| account configuration, API calls may
require authentication in the form of a
`HMAC-SHA256 <https://en.wikipedia.org/wiki/Hash-based_message_authentication_code>`__
message hash as a header within the request. HMAC is a keyed-hash
authentication code that calculates a message authentication code (MAC)
involving a cryptographic hash function in combination with a secret
cryptographic key. SHA256 is one type of cryptographic hash function
used in the calculation of an HMAC header; the resulting algorithm is
known as HMAC-SHA256.

The |acquia-product:liftapi| calls authenticate using MHAC v2 to protect
your data and ensure that your secret keys stay secure, while utilizing
the Access Key ID and secret access key associated with your
|acquia-product:cha| subscription. For more information about the HMAC
implementation that is in use, see the `Acquia HMAC
spec <https://github.com/acquia/http-hmac-spec>`__.

.. admonition:: HMAC v1 note

   Although HMAC v1 is still supported, for better security it is recommended 
   that you use HMAC v2. For information about using HMAC v1, see |hmaclink|_.

.. |hmaclink| replace:: \ |acquia-product:liftapi|\  and HMAC authorization
.. _hmaclink: /lift/omni/api/hmac


-  `Setting HMAC authentication as an HTTP request <#setting>`__

   -  `Creating the authorization header <#creating>`__
   -  `Creating the signature <#signature>`__
   -  `Setting HMAC authentication using a GET method <#get>`__
   -  `Setting HMAC authentication using a POST method <#post>`__

-  `Response <#response>`__

   -  `Response header <#response-header>`__
   -  `Response signature <#response-signature>`__
   -  `Response validation <#validation>`__

-  `Managing HMAC authentication in |acquia-product:alw| <#managing>`__
-  `Code examples <#lang>`__


Setting HMAC authentication as an HTTP request
----------------------------------------------

In the |acquia-product:liftapi|, HMAC authentication is set as a header
in an HTTP request. The HTTP client signs the request by adding the
following HTTP headers:

.. code-block:: none

   Authorization : <HMACAuthorization>
   X-Authorization-Timestamp : <Unix Timestamp In Seconds>
   X-Authorization-Content-SHA256 : <HashedContent> (if Content-Length > 0)


Creating the authorization header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create the authorization header, include the following attributes:

-  ``realm`` - The provider — for example, ``Acquia`` or ``MyCompany``
-  ``id`` - The API key's unique identifier, which is an arbitrary
   string
-  ``nonce`` - A hex `version 1 or 4
   UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__
-  ``version`` - The version of HMAC that this request uses
-  ``headers`` - A list of additional request headers that are to be
   included in the signature base string — these are lowercase, and are
   separated with the semicolon ( ``;`` ) character
-  ``signature`` - The
   `Base64-encoded <https://en.wikipedia.org/wiki/Base64>`__ signature
   as described in the `Signature <#signature>`__ section

Each attribute value should be enclosed in double quotes and `percent
encoded <https://en.wikipedia.org/wiki/Percent-encoding>`__.

.. _signature:

Creating the signature
~~~~~~~~~~~~~~~~~~~~~~

The signature is a Base64-encoded binary HMAC-SHA256 digest generated
from the following elements:

-  ``Base64 Hashed SecretKey`` - The API key's shared secret
   The secret key should be a 256- to 512-bit binary value. The secret
   key will normally be stored as a Base64-encoded or hex-encoded string
   representation, but must be decoded to the binary value before use.
-  ``StringToSign`` - A concatenated string generated from the following
   parts:

   -  ``HTTP-Verb`` - The uppercase HTTP request method — for example,
      ``GET`` or ``POST``
   -  ``Host`` - The (lowercase) hostname, matching the HTTP Host
      request header field (including any port number)
   -  ``Path`` - The HTTP request path with leading slash — for example,
      ``/resource/11``
   -  ``QueryParameters`` - Any query parameters or empty string, which
      should be the exact string sent by the client, including `percent
      encoding <https://en.wikipedia.org/wiki/Percent-encoding>`__.
   -  ``AuthorizationHeaderParameters`` - Normalized parameters similar
      to `section 9.1.1 of OAuth
      1.0a <https://oauth.net/core/1.0a/#anchor13>`__, which uses the
      following parameters:

      -  id
      -  nonce
      -  realm
      -  version

      Parameters are sorted by name and separated by ``&`` with name and
      value separated by ``=``. They are `percent
      encoded <https://en.wikipedia.org/wiki/Percent-encoding>`__.

   -  ``AdditionalSignedHeaders`` - The normalized header names and
      values specified in the headers parameter of the authorization
      header
      Names should be lowercase, sorted by name, separated from value by
      a colon, and the value followed by a newline (so each extra header
      is on its own line). If there are no added signed headers, an
      empty line should not be added to the signature base string.
   -  ``X-Authorization-Timestamp`` - The value of the
      X-Authorization-Timestamp header, a Unix timestamp (integer
      seconds since Jan 1, 1970 UTC) — required for all requests
      If this value differs by more than 900 seconds (15 minutes) from
      the time of the server, the request will be rejected.
   -  ``Content-Type`` - The lowercase value of the ``Content-type``
      header or an empty string if absent (omit if ``Content-Length`` is
      ``0``)
   -  ``Body-Hash`` - The Base64-encoded SHA-256 digest of the raw body
      of the HTTP request, for POST, PUT, PATCH, DELETE or other
      requests that may have a body (omit this parameter if
      ``Content-Length`` is ``0``)
      This value should be identical to the string sent as the
      X-Authorization-Content-SHA256 header.

X-Authorization-Content-SHA256 header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the Base64-encoded SHA-256 hash value used to generate the
signature base string. This is analogous to the standard ``Content-MD5``
header used with `HMAC v1 </lift/omni/api/hmac>`__. It is required for
any request where ``Content-Length`` is not 0 (for example, a POST
request with a body). This header should be provided by the client, to
ensure that the request body it sent was not tampered with on its way to
the server. After the server receives the request body, it forms the
``Body-Hash``, then compares it to the request body again.

Example
~~~~~~~

In the following example, the HTTP Authorization header and signature
are constructed:

.. code-block:: none

      HMACAuthorization = "acquia-http-hmac" + " " +
      "realm=" + Provider + "," +
      "id=" + AccessKey + "," +
      "nonce=" + HexV4OfRandomUUID + "," +
      "version=" + HMACVersion + "," +
      "headers=" + AdditionalSignedHeaderNames + "," +
      "signature=" + HMACSignature
      AdditionalSignedHeaderNames = "" or
      Lowercase( HTTP-Header-Name ) [ + ";" + Lowercase( HTTP-Header-Name ), for additional headers]

      HMACSignature = Base64( HMAC-SHA256 ( SecretKey, UTF-8-Encoding-Of( StringToSign ) ) )

      StringToSign = HTTP-Verb + "\n" +
      Host + "\n" +
      Path + "\n" +
      QueryParameters + "\n" +
      AuthorizationHeaderParameters + "\n" +
      [ AdditionalSignedHeaders, If the headers attribute is not empty, + "\n" ] + 
      X-Authorization-Timestamp +
      [ "\n" + Content-Type + 
      "\n" + HashedContent, if Content-Length > 0 ]

      AuthorizationHeaderParameters = "id=" + URLEncode( AccessKey ) + "&" + 
      "nonce=" + URLEncode( HexV4OfRandomUUID ) + "&" +
      "realm=" + URLEncode( Provider ) + "&" +
      "version=" + URLEncode( Version )

      AdditionalSignedHeaders = Lowercase( HTTP-Header-Name ) + ":" + HTTP-Header-Value 
      [ + "\n" + Lowercase( HTTP-Header-Name ) + ":" + HTTP-Header-Value, for additional headers]
      (must be sorted by Lowercase( HTTP-Header-Name ) )

      HashedContent = Base64( SHA256 ( Request-Body ) )

``"\n"`` denotes a Unix-style line feed (ASCII code 0x0A).


Setting HMAC authentication using a GET method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the following example, HMAC authentication is set using a HTTP GET
method.

.. code-block:: none

      https://example-liftapi.lift.acquia.com/dashboard/rest/EXAMPLEINC/segments?site_id=10
      X-Authorization-Timestamp: 1432075982

In this example, the authorization header contains the following values:

-  ``realm`` - ``AcquiaLiftWeb``
-  ``id`` - ``Ra9YgrsKAcXDLMexg44N``
-  ``nonce`` - ``d1954337-5319-4821-8427-115542e08d10``
-  ``Base64 Hashed SecretKey`` -
   ``KgFBhwQMC4wZ6Ls9u7UNbX6jV4xEt5Xvetr9zCEQ``

``Signature-Base-String`` is:

.. code-block:: none

      GET
      example-liftapi.lift.acquia.com
      /dashboard/rest/EXAMPLEINC/segments
      site_id=10
      id=Ra9YgrsKAcXDLMexg44N&nonce=d1954337-5319-4821-8427-115542e08d10&realm=AcquiaLiftWeb&version=2.0
      1432075982


.. note::  

   Content type and body hash are omitted for GET methods.

The request signature is ``4wYr5sIgw5C3f6CjO2UGimuCmrwm+PFtZ2CjyW5+7j4=``

This value is created by signing the ``Signature-Base-String`` with the
hashed ``SecretKey``.

The authorization header is:

.. code-block:: none

   acquia-http-hmac realm="AcquiaLiftWeb",id="Ra9YgrsKAcXDLMexg44N",nonce="d1954337-5319-4821-8427-115542e08d10",version="2.0",signature=”4wYr5sIgw5C3f6CjO2UGimuCmrwm+PFtZ2CjyW5+7j4="

The full HTTP request is:

.. code-block:: none

      GET /dashboard/rest/EXAMPLEINC/segments
      Host: example-liftapi.lift.acquia.com
      X-Authorization-Timestamp: 1432075982
      Authorization: acquia-http-hmac realm="AcquiaLiftWeb",id="Ra9YgrsKAcXDLMexg44N",nonce="d1954337-5319-4821-8427-115542e08d10",version="2.0",signature="R6y7kWkBnUdcSNXMxh4Vib6wSSHYKY4srCA1d4unW78="


Setting HMAC authentication using a POST method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the following example, HMAC authentication is set as an HTTP request
using a POST method.

.. code-block:: none

      https://example-liftapi.lift.acquia.com/dashboard/rest/EXAMPLEINC/event_import
      X-Authorization-Timestamp:  1449578521
      Content-Type: application/json

The body of the request contains the following values:

.. code-block:: none

      {"identity":"event_import_eg@example.com","identity_source":"email","event_name":"Content View",
      "event_source":"web","event_date":"2015-11-05 10:22:03.111","engagement_score":"15",
      "identities":{"fb_event_import_eg":"facebook"}};

``X-Authorization-Content-SHA256`` is ``zC4p8Oa+aw6pTdoW1uFN0ngemDjd5QlZXBK5tcUKzCw=``. This value is the
SHA256-encoded request body.

In this example, the authorization header contains the following values:

-  ``realm`` - ``AcquiaLiftWeb``
-  ``id`` - ``Ra9YgrsKAcXDLMexg44N``
-  ``nonce`` - ``64d02132-40bf-4fce-85bf-3f1bb1bfe7dd``
-  Base64 Hashed SecretKey
   -``eox4TsBBPhpi737yMxpdBbr3sgg/DEC4m47VXO0B8qJLsbdMsmN47j/ZF/EFpyUKtAhm0OWXMGaAjRaho7/93Q==``

``Signature-Base-String`` is:

.. code-block:: none

      POST
      example-liftapi.lift.acquia.com
      /dashboard/rest/EXAMPLEINC/event_import
      id=Ra9YgrsKAcXDLMexg44N&nonce=64d02132-40bf-4fce-85bf-3f1bb1bfe7dd&realm=AcquiaLiftWeb&version=2.0
      1449578521
      application/json
      zC4p8Oa+aw6pTdoW1uFN0ngemDjd5QlZXBK5tcUKzCw=

.. note::  

      The preceding code example contains an empty line. This is because there
      are no query parameters being passed in the URL. Omitting this line may
      cause this code example to not work properly.

The request signature is:
``sW4t14rZvcZDEpJwwWWkqCRwTUYiKVAK2aHURtBCIrU=``

The authorization header is:

.. code-block:: none

      acquia-http-hmac realm="AcquiaLiftWeb",id="f0d16792-cdc9-4585-a5fd-bae3d898d8c5",nonce="64d02132-40bf-4fce-85bf-3f1bb1bfe7dd",version="2.0",signature="sW4t14rZvcZDEpJwwWWkqCRwTUYiKVAK2aHURtBCIrU="

The full HTTP request is:

.. code-block:: none

      POST /dashboard/rest/EXAMPLEINC/event_import
      Host: example-liftapi.lift.acquia.com
      X-Authorization-Timestamp: 1449578521
      Content-Type: application/json
      Request body: {"identity":"event_import_eg@example.com","identity_source":"email","event_name":"Content View","event_source":"web","event_date":"2015-11-05 10:22:03.111","engagement_score":"15","identities":{"fb_event_import_eg":"facebook"}}
      X-Authorization-Content-SHA256: zC4p8Oa+aw6pTdoW1uFN0ngemDjd5QlZXBK5tcUKzCw=
      Authorization: acquia-http-hmac realm="AcquiaLiftWeb",id="efdde334-fe7b-11e4-a322-1697f925ec7b",nonce="d1954337-5319-4821-8427-115542e08d10",version="2.0",signature="R6y7kWkBnUdcSNXMxh4Vib6wSSHYKY4srCA1d4unW78="


Response
--------

The server responds to the client's request by constructing a header and
signature.

Response header
~~~~~~~~~~~~~~~

The following example illustrates construction of the HTTP
X-Server-Authorization-HMAC-SHA256 header and signature for all non-HEAD
requests:

HMACServerAuthorization = Base64( SHA256 ( ResponseStringToSign ) )

.. code-block:: none

      ResponseStringToSign = Nonce + "\n" +
            X-Authorization-Timestamp + "\n" +
            Response-Body

Response signature
~~~~~~~~~~~~~~~~~~

The response signature base string is a concatenated string generated
from the following elements:

-  ``Nonce`` - The nonce that was sent in the Authorization header
-  ``X-Authorization-Timestamp`` -The timestamp that was sent in the
   X-Authorization-Timestamp header
-  ``Response-Body`` - The response body (or empty string)


Example
^^^^^^^

The following is an example of a response signature base string:

.. code-block:: none

      Response body - {"id": 133, "status": "done"}
      Nonce - d1954337-5319-4821-8427-115542e08d10
      X-Authorization-Timestamp - 1432075982
      Base64 encoded secret key - eox4TsBBPhpi737yMxpdBbr3sgg/DEC4m47VXO0B8qJLsbdMsmN47j/ZF/EFpyUKtAhm0OWXMGaAjRaho7/93Q==

``Signature-Base-String`` is:

.. code-block:: none

      d1954337-5319-4821-8427-115542e08d10
      1432075982
      {"id": 133, "status": "done"}

The signed response is: ``M4wYp1MKvDpQtVOnN7LVt9L8or4pKyVLhfUFVJxHemU=``

The full HTTP response is:

.. code-block:: none

      Response body - {"id": 133, "status": "done"}
      X-Server-Authorization-HMAC-SHA256 - M4wYp1MKvDpQtVOnN7LVt9L8or4pKyVLhfUFVJxHemU=


Response validation
~~~~~~~~~~~~~~~~~~~

Requests using the GET method will return a response with a
``X-Server-Authorization-HMAC-SHA256`` header. This header is created
when the response ``Signature-Base-String`` is signed with the client's
``secretKey``.


Managing HMAC authentication in |acquia-product:alw|
----------------------------------------------------

Although HMAC is enabled by default, it can be disabled for
troubleshooting. To either enable or disable HMAC authentication,
complete the following steps:

#. `Sign in to Acquia Lift Web </lift/drupal/web>`__ as an
   administrator, and then click the **Admin** tab.
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

We have developed several code examples that you can use to help you
understand how to make calls to the
`Acquia Lift API </lift/omni/rest_api>`__ using different
programming languages:

-  `PHP code example <https://github.com/acquia/http-hmac-php/>`__ -
   Makes a call to the |acquia-product:liftapi| based on the parameters
   that you have provided. ``getMakeAPICall`` is the entry point of the
   example.
-  `Java code
   example <https://gist.github.com/acquialibrary/37fe146de7ba9e3a3dbb2022759853c9>`__
   - Makes several simple calls to the |acquia-product:liftapi|. The
   entry point of the example is the ``main`` method.
