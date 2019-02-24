.. include:: /common/global.rst

Using the |acquia-product:ch| API
=================================

.. toctree::
   :hidden:
   :glob:

   /lift/contenthub/api/*

|acquia-product:ch| includes a RESTful API that you can use to create,
read, update, and delete content.

Using the API, you can source content from anywhere and then connect and
use that content with your many websites, native mobile applications, or
other digital experiences — all while maintaining data integrity and
security. You can use the API to also build custom applications that
publish, update, and consume content, and then render that content
natively.

For information about the other APIs available to |acquia-product:cha|
subscribers, see |using|_.

.. |using| replace:: Using the  \ |acquia-product:cha|\  APIs
.. _using: /lift/omni/api


Using the REST API
------------------

Similar to many other APIs, the |acquia-product:ch| API uses standard
HTTP methods to communicate with the service, including GET, PUT, POST,
and DELETE. You can view the list of available |acquia-product:ch| API
calls at the following URL:

**http://api.content-hub.acquia.com/**

.. _sample:

Sample |acquia-product:ch| API methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are some examples of the methods provided in the
|acquia-product:ch| API:

+-----------------------------------+-----------------------------------+
| REST API call                     | Description                       |
+===================================+===================================+
| ``ping``                          | Determine if the API is           |
|                                   | responding                        |
+-----------------------------------+-----------------------------------+
| ``entities``                      | Stores a piece of content,        |
|                                   | prepared for synchronization      |
+-----------------------------------+-----------------------------------+
| ``history``                       | Retrieve history logs that can be |
|                                   | useful for troubleshooting        |
+-----------------------------------+-----------------------------------+
| ``settings``                      | Retrieve subscription             |
|                                   | configuration                     |
+-----------------------------------+-----------------------------------+
| ``register``                      | Register a new client             |
+-----------------------------------+-----------------------------------+
| ``webhooks``                      | Manipulate subscription webhooks  |
+-----------------------------------+-----------------------------------+

For complete documentation, see the |chapi|_.


.. |chapi| replace:: \ |acquia-product:ch|\  API reference
.. _chapi: http://api.content-hub.acquia.com/

Testing your connection
~~~~~~~~~~~~~~~~~~~~~~~

When you first start using the |acquia-product:ch| API, we encourage you
to use the ``ping`` call to test your connection to the API. To do this,
complete the following steps:

#. Open a command prompt window, and then enter the following command:

   ``curl -XGET "http://[example.com]/ping"``

   replacing ``[example.com]`` with the |acquia-product:ch| API URL
   provided by your Acquia technical contact.

#. Verify that the API call returns the following results:

   ``{   "success": true }``

.. _libs:

Using the |acquia-product:ch| client libraries
----------------------------------------------

|acquia-product:ch| also includes a PHP SDK, the |client|_, which you
can `download <https://github.com/acquia/content-hub-php>`__.

|acquia-product:ch| Client for PHP can be installed with
`Composer <https://getcomposer.org/>`__ by adding it as a dependency to
your project's ``composer.json`` file. To do this, complete the
following steps:

#. Create a ``composer.json`` file in the root of your project:
   
   .. code-block:: JSON

      {
          "repositories": [
              {
                  "type": "vcs",
                  "url": "https://github.com/acquia/content-hub-php"
              }
          ],
          "require": {
              "acquia/content-hub-php": "*"
          }
      }

#. Install the package. The following command can be used to do this:

   ``composer install``

Authenticating API calls
------------------------

|acquia-product:ch| API calls are authenticated using HMAC, a
shared-secret cryptography method where signatures are generated on the
client side and validated by the server to authenticate the request.

When receiving a webhook request from |acquia-product:ch|, an
application like Drupal should use HMAC to verify the authenticity of
the request in order to ensure it comes from the same
|acquia-product:ch| server that the application normally communicates
with. This prevents malicious servers sending requests to the
application and modifying data. To verify the request,
|acquia-product:ch| and each application that is registered on
|acquia-product:ch| share a secret key, which is used to verify the
signature of any incoming web request (or webhook). When an application
registers and receives a webhook for the first time, the shared secret
will be missing. In this situation, the application should immediately
contact |acquia-product:ch| to request the shared secret, and store this
in a variable for future use.

.. note::  |acquia-product:ch| relies on HTTPS to encrypt data. To ensure the security of your data, we recommend using HTTPS on your Drupal website.

You can use the |client|_ to register with |acquia-product:ch| and authenticate your API calls.


Registering with |acquia-product:ch|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before using any API calls, you must register with |acquia-product:ch|,
or you will receive an error message in response.

Registering with |acquia-product:ch| requires the following items:

-  |acquia-product:ch| API key - Provided by your Acquia technical contact
-  |acquia-product:ch| Secret key - Provided by your Acquia technical contact
-  |acquia-product:ch| website name - Set by you when you configured_ the |acquia-product:chc|.

.. _configured: /content-hub/configure

To register with |acquia-product:ch|, use the ``register`` 
`API call <http://api.content-hub.acquia.com/#panel_v1_register>`__. Prior to
registration, the origin can be set to any value. When you register for
the first time, you will receive a paired *origin UUID* and *client
name* that you must use in your subsequent requests (any other API
call).

After your client is registered, all other API calls are open to you
using that registered *origin*. You can test registration by doing any
query to any other API function (and using your origin in the requests)
and ensuring that it works.

Here is some example code that uses the |acquia-product:ch| Client for
PHP:

.. code-block:: php

   $api = 'AAAAAAAAAAAAAAAAAAAA';
   $secret = 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB';
   $origin = '11111111-0000-0000-0000-000000000000';

   $client = new ContentHub($api, $secret, $origin, ['base_url' => 'http://localhost:5000']);

   // Register a client
   $client_site = $client->register('myclientsite');

The ``register`` call returns a UUID that you use as the ``origin`` in the following requests:

.. code-block:: php

   $origin = $client_site['uuid'];
   $client = new ContentHub($api, $secret, $origin, ['base_url' => 'http://localhost:5000']);

After you are registered, you can use this as your client ID, which
should not expire. If you use other methods of registration (such as
``getClientByName()``), these may expire, and cause unexpected errors.

When you have a registered origin, the ``getClientByName()`` call can be
used to obtain both the ``site name`` and ``site origin`` pair of a
specific registered website. However, you cannot use that API call to
register a website. For example, if you already registered a website and
execute ``getClientByName()``, you are essentially requesting
|acquia-product:ch| ``/settings/clients/``:

.. code-block:: none

   HTTP REQUEST "/settings/clients/centralstation" [Using a registered ORIGIN UUID]
   
   Array
   (
       [name] => centralstation
       [uuid] => 1231212-1234-1234-1b2e-3a567dfa8d90
   )


API keys and permissions
~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ch| API commands require authentication using both an
API key and a secret key. For information about how to review your
|acquia-product:ch| keys, see |restreference|_.

In addition to your originally provisioned keys, commands may require
particular permissions for an API key. By default, all API keys have
every permission for each method in the |acquia-product:ch| API.
However, you can obtain keys that have only limited permissions if, for
example, you have users who need to be able to create content, but you
do not want them to be able to delete it. If you need API keys with
customized permissions, contact your Acquia technical advisor.

The available permissions are as follows:

-  administer
-  create
-  search
-  register
-  update
-  delete
-  retrieve

.. |restreference| replace:: \ |acquia-product:cha|\  REST API reference
.. _restreference: /lift/omni/rest_api

.. |client| replace:: \ |acquia-product:ch|\  Client for PHP
.. _client: https://github.com/acquia/content-hub-php