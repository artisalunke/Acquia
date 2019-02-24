.. include:: /common/global.rst

Mapping multilingual Drupal to Magento store views
==================================================

After you have configured Drupal with your chosen languages, and
configured Magento with the locales and store views that will match up
to those languages, you must map the Drupal languages to Magneto store
views as a pair in the |acquia-product:ccs|, enabling them to
communicate with each other and synchronize product information.

To create a mapped pair, complete the following tasks:

#. Obtain a User ID, key, and secret from your Acquia Administrator,
   such as your Onboarding Success Engineer.
#. `Create authorizations for your systems <#creating-authorizations>`__. Drupal language
   and Magento store views are *systems*.
#. `Add the systems <#add-the-systems>`__ using either your site or user keys and
   link them to the auth details created in the previous step. There
   must be one *system* for each Drupal language and one *system* for
   each Magento store view.
#. `Create a mapping <#map-the-systems-together>`__ that links Magento to Drupal using either
   your site or user key and secret.

.. note::  All endpoints are secured with 
   `HMAC authentication <https://github.com/acquia/http-hmac-spec>`__. You can
   use `Postman <https://www.getpostman.com/>`__ to include a pre-request
   script to perform the HMAC authentication for you. Acquia has an example
   Postman file available for download_. Ask your Acquia Administrator for 
   additional details.

.. _download: https://gist.github.com/acquialibrary/f2c532cdc1a702716ac48dae1aa4a081/archive/a4f9e11e0cb824de5fcca30db1143fcc04e163e7.zip

Each request to the |acquia-product:ccs| must use the following HMAC headers:

.. code-block:: none

   Authorization:{{acqHmacHeader}}
   X-Authorization-Timestamp:{{acqHmacTimestamp}}
   // If the request includes a body then you must also include:
   X-Authorization-Content-SHA256:{{acqHmacContentSha}}

Acquia will provide the ``user ID``, ``hmac_key``, and ``hmac_secret``
for the created user.

Creating authorizations
-----------------------

First, you must create the *site*, and then add *authorizations* for the
Drupal and Magento systems. Use the |use the API|_ to accomplish these tasks.

.. |use the API| replace:: \ |acquia-product:acm|\  API
.. _use the API: /commerce/api

#. **Create a ``site`` using the user keys provided by Acquia.**

   API Endpoint: ``${CONNECTOR_URL}/v2/config/site/create``

   .. list-table::
      :widths: 15 85
      :header-rows: 1 

      * - Request type
        - Request body
      * - ``POST``
        - 
          .. code-block:: none

               {
               "name":"${CUSTOMER_SITE_NAME}",
               "description":"${CUSTOMER_SITE_NAME}",
               "user_id":${CUSTOMER_USER_ID}
               }

   This request returns a ``site_id``, ``hmac_key``, and ``hmac_secret``
   for the site created. The ``site_id`` is used for subsequent API
   calls, and you will need the ``hmac_key`` and ``hmac_secret``
   returned by this request for both Drupal and Magento. The returned
   value set will look similar to this example:

   .. code-block:: none 

      {
         “site_id”:1
         “hmac_key”:”abcdef359d9vs0dxsv89ds9d0f8scd”,
         “hmac_secret”:”gs3dd98dlk349dkwl34kjdf”
      }

#. **Create authorization details for the Magento systems**

   API Endpoint: ``${CONNECTOR_URL}/v2/config/auth_detail/create``

   .. list-table::
      :widths: 15 85
      :header-rows: 1 

      * - Request type
        - Request body
      * - ``POST``
        - 
          .. code-block:: none

               {
               "name":"${BACKEND_AUTH_DETAIL_NAME}", // Your detailed name for Magento
               "description":"BACKEND_AUTH_DETAIL_DESC", // A description for your Magento installation
               "client_id":"${BACKEND_CLIENT_ID}", // The client ID from Magento
               "client_secret":"${BACKEND_CLIENT_SECRET}", // Secret key from Magento
               "token":"${BACKEND_TOKEN}", // The Magento token
               "token_secret":"${BACKEND_TOKEN_SECRET}", // Magento token secret
               "site_id":${SITE_ID} // The site_id created previously
               }

   This request returns an ``auth_ID`` for the Magento authorization
   detail created. You will need this value when creating the Magento
   systems later.

#. **Create authorization details for Drupal**

   API Endpoint: ``${CONNECTOR_URL}/v2/config/auth_detail/create``

   .. list-table::
      :widths: 15 85
      :header-rows: 1 

      * - Request type
        - Request body
      * - ``POST``
        - 
          .. code-block:: none

               {
               "name":"${FRONTEND_AUTH_DETAIL_NAME}", // Enter a name for the authorization like "Drupal auth"
               "description":"FRONTEND_AUTH_DETAIL_DESC", // Enter a name for the authorization like "Drupal auth"
               "client_id":"${FRONTEND_CLIENT_ID}", // Your client ID from Drupal allocated when you created the Drupal OAuth user
               "client_secret":"${FRONTEND_CLIENT_SECRET}", // Your secret from Drupal when you created the Drupal OAuth user
               "site_id":${SITE_ID} // The site_id from the site creation.
               }

   This request returns a ``auth_ID`` for the Drupal authorization
   detail created. You will need this value when creating the Drupal
   system later.


Add the systems
---------------

Next, you will add *system* definitions for Magento and Drupal.

#. **Add a Magento store view as a system**

   Repeat this API call for each Magento store view to be configured.

   API Endpoint: ``${CONNECTOR_URL}/v2/config/system/create``

   .. list-table::
      :widths: 15 85
      :header-rows: 1 

      * - Request type
        - Request body
      * - ``POST``
        - 
          .. code-block:: none

               {
               "name":"${BACKEND_SYSTEM_NAME}",  // Magento system name
               "description":"${BACKEND_SYSTEM_DESC}", \ //Magento system description
               "type":"${BACKEND_TYPE}", // System type, in this case "magento"
               "url":"${BACKEND_URL}",  // Full system URL, INCLUDING a trailing slash, such as https://your-magento-host-url.com/rest/store_view_code/V1/"
               "uuid":"${BACKEND_UUID}",  // The language used, such as en_US
               "site_id":${SITE_ID},  // The Magento site_id from before
               "auth_id":${AUTH_ID},  // The auth_id created earlier
               "token_url":"${BACKEND_TOKEN_URL}", 
               "skip_ssl":${SKIP_SSL}
               }


   This request returns a ``system_id`` for the Magento system created.
   You will need the ``system_id`` and the store view when creating the
   mapping.

#. **Add a Drupal system**

   Next, you create a Drupal system for a given language. You must
   repeat this API call for each language you wish to add.

   API Endpoint: ``${CONNECTOR_URL}/v2/config/system/create``

   .. list-table::
      :widths: 15 85
      :header-rows: 1 

      * - Request type
        - Request body
      * - ``POST``
        - 
          .. code-block:: none

               {
               "name":"${FRONTEND_SYSTEM_NAME}", // Drupal system name
               "description":"${FRONTEND_SYSTEM_DESC}", // Drupal System description
               "site_id":${SITE_ID}, // The site_id from previous steps
               "auth_id":${AUTH_ID}, // Your Drupal system auth_id
               "type":"${FRONTEND_TYPE}", // The system type, in this case 'drupal'
               "url":"${FRONTEND_URL}", // URL for your Drupal host, without a trailing slash.
               "uuid":"${FRONTEND_UUID}", // The ACM ID for this language 
               "token_url":"${FRONTEND_TOKEN_URL}", 
               "skip_ssl":${SKIP_SSL}
               }


This request returns a ``system_id`` for the Drupal system created. You
will need the list of all returned ``system_id`` responses, and
languages they correspond to, when creating the mapping.


Map the systems together
------------------------

Finally, configure the |acquia-product:ccs| to map a specific Magento
store view to a specific Drupal language configuration. Repeat this API
call for each Drupal language to Magento store view mapping required.

API Endpoint: ``${CONNECTOR_URL}/v2/config/mapping/create``

.. list-table::
   :widths: 15 85
   :header-rows: 1 

   * - Request type
     - Request body
   * - ``POST``
     - 
         .. code-block:: none

            {
            "name":"${MAPPING_NAME}", // The name of the mapping, such as 'Drupal EN to Magento EN'
            "description":"${MAPPING_DESC}", //  Description of the mapping
            "backend_id":${BACKEND_SYSTEM_ID}, // The Magento system_id
            "frontend_id":${FRONTEND_SYSTEM_ID}, // The Drupal system_id
            "site_id":${SITE_ID} // The site_id
            }

A mapping example
-----------------

If you have a store with three languages, in three locations, your
configuration process would look like this example:

One Drupal installation with three languages:

-  ``EN`` - English
-  ``FR`` - French
-  ``ES`` - Spanish

One Magento installation with three locales:

-  ``en_US`` - US English
-  ``fr_CA`` - French Canadian
-  ``es_MX`` - Mexican Spanish

When the Drupal and Magento installations are mapped appropriately, then
within the |acquia-product:ccs| you will have created the following
setup, which connects your store in all three languages:

-  **One ‘site’**
-  **Two authorizations** - one to connect to Drupal’s OAuth and one to connect to Magento’s OAuth
-  **Three Drupal systems** - one for each language
-  **Three Magento systems** - one for each store view (locale)
-  **Three mappings** - one for each language-locale pair
